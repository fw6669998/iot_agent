"""阿里云物联网平台(IoT Platform)工具集.

仿照 iot_tools.py, 使用 langchain-core 的 @tool 装饰器定义供 agent 调用的工具,
统一通过 alibabacloud_iot20180120 SDK 访问阿里云物联网平台.

直接使用 SDK 的 Client 对象调用接口, 响应均为对象(body), 便于按属性访问;
仅在返回给 agent 前将失败响应整理为统一 dict.

配置通过 .env 加载:
    ALI_IOT_ACCESS_KEY_ID      AccessKey ID
    ALI_IOT_ACCESS_KEY_SECRET  AccessKey Secret
    ALI_IOT_REGION_ID          地域, 如 cn-shanghai
    ALI_IOT_INSTANCE_ID        企业版实例ID; 旧版公共实例留空
    ALI_IOT_ENDPOINT           可选, 自定义接入域名, 默认 iot.${REGION_ID}.aliyuncs.com
    ALI_IOT_SECURE_MODE        MQTT 安全模式, 默认 3(TCP直连 1883); 2 为 TLS 直连(8883)

说明:
- 阿里云设备由 (productKey, deviceName) 唯一标识, 同时平台颁发 iotId. 本工具集沿用
  iot_tools 的约定, 设备操作工具以 iotId 为主键; 仅 SetDevicesProperty 不支持 iotId,
  内部会先 QueryDeviceDetail 解析出 productKey/deviceName 再调用.
- CreateThingModel 的 ThingModelJson 只接受 properties/services/events 三段 JSON, 不可
  传入完整 TSL(含 _ppk). QueryThingModel 返回的则是带 _ppk 的完整物模型.
"""

import hashlib
import hmac
import json
import os
import subprocess
import sys
import time
import uuid
from typing import Any, Optional

from alibabacloud_iot20180120 import models as iot_models
from alibabacloud_iot20180120.client import Client
from alibabacloud_tea_openapi import models as openapi_models
from langchain_core.messages import HumanMessage
from langchain_core.tools import tool

from services import common_tool, llm_client

deploy_host = os.getenv('DEPLOY_HOST', 'localhost')


def _is_success(body) -> bool:
    """阿里云响应成功标志: success 为 True(部分版本可能是字符串 'true')."""
    ok = getattr(body, "success", False)
    return ok is True or ok == "true" or ok == "True"


def _failed(body) -> bool:
    """body 是否为失败响应(对象 success 不为 True)."""
    return not _is_success(body)


def _failed_result(body) -> dict:
    """由失败 body 构造返回给 agent 的统一失败 dict."""
    return {
        "status": "failed",
        "code": getattr(body, "code", None),
        "errorMessage": getattr(body, "error_message", None),
    }


def _inject_product_key(feature: dict, product_key: str) -> dict:
    """为单个物模型功能补全 productKey 字段.

    CreateThingModel 要求 ThingModelJson 中每个 property/service 都内含 productKey,
    缺失时平台会报 "productKey must not be empty!".
    """
    feature.setdefault("productKey", product_key)
    return feature


def _normalize_service(service: dict, product_key: str) -> dict:
    """将服务归一化为阿里云 CreateThingModel 接受的内部格式(原地修改).

    - name -> serviceName        (服务用 serviceName, 属性用 name)
    - callType 统一大写          (async -> ASYNC, sync -> SYNC)
    - inputData/outputData -> inputParams/outputParams
    - 入参/出参补全 direction(PARAM_INPUT/PARAM_OUTPUT) 与 paraOrder(序号)
    - 注入 productKey
    """
    if "name" in service and "serviceName" not in service:
        service["serviceName"] = service.pop("name")
    if isinstance(service.get("callType"), str):
        service["callType"] = service["callType"].upper()
    if "inputData" in service and "inputParams" not in service:
        service["inputParams"] = service.pop("inputData")
    if "outputData" in service and "outputParams" not in service:
        service["outputParams"] = service.pop("outputData")
    service.setdefault("productKey", product_key)
    service.setdefault("inputParams", [])
    service.setdefault("outputParams", [])
    for i, p in enumerate(service["inputParams"]):
        p.setdefault("direction", "PARAM_INPUT")
        p.setdefault("paraOrder", i)
    for i, p in enumerate(service["outputParams"]):
        p.setdefault("direction", "PARAM_OUTPUT")
        p.setdefault("paraOrder", i)
    return service


def _publish_thing_model(product_key: str) -> bool:
    """发布物模型草稿, 使新增/删除的功能在物联网平台生效并可见.

    CreateThingModel/DeleteThingModel 只修改草稿, 平台控制台默认展示已发布版本,
    故变更后需调用 PublishThingModel 发布, 否则功能在控制台不可见.
    """
    req = iot_models.PublishThingModelRequest(
        product_key=product_key, iot_instance_id=instance_id
    )
    try:
        body = client.publish_thing_model(req).body
    except Exception:  # noqa: BLE001 - 发布失败不阻断主操作, 仅告警
        return False
    return _is_success(body)


def _build_client() -> Client:
    """根据 .env 配置构造阿里云物联网平台 SDK 客户端."""
    ak = os.getenv("ALI_IOT_ACCESS_KEY_ID", "")
    sk = os.getenv("ALI_IOT_ACCESS_KEY_SECRET", "")
    if not ak or not sk:
        raise ValueError(
            "ALI_IOT_ACCESS_KEY_ID / ALI_IOT_ACCESS_KEY_SECRET 未配置, 请检查 .env"
        )
    region_id = os.getenv("ALI_IOT_REGION_ID", "cn-shanghai")
    endpoint = os.getenv("ALI_IOT_ENDPOINT") or f"iot.{region_id}.aliyuncs.com"
    config = openapi_models.Config(
        access_key_id=ak,
        access_key_secret=sk,
        region_id=region_id,
        endpoint=endpoint,
    )
    return Client(config)


# 模块级客户端: 直接使用 Client 对象调用接口, 响应均为对象, 便于按属性访问
client: Client = _build_client()
instance_id: Optional[str] = os.getenv("ALI_IOT_INSTANCE_ID") or None
secure_mode: str = os.getenv("ALI_IOT_SECURE_MODE", "3")


@tool
def getThingModel(productKey: str = None) -> Any:
    """物模型_获取.

    获取指定产品的物模型 (properties / services / events), 返回 thingModelJson 字符串.
    返回内容为带 _ppk 的完整物模型 JSON.

    Args:
        productKey: 产品 key.
    """
    req = iot_models.QueryThingModelRequest(
        product_key=productKey, iot_instance_id=instance_id
    )
    try:
        body = client.query_thing_model(req).body
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(body):
        return _failed_result(body)
    thing_model_json = getattr(getattr(body, "data", None), "thing_model_json", None)
    return {"thingModelJson": thing_model_json}


@tool
def productAddPropertiesServices(
        productKey: str,
        properties: str = None,
        services: str = None,
) -> Any:
    """为产品添加属性和服务(物模型新增功能).单次最多新增 10 个功能

    Args:
        productKey: 产品 key.
        properties: 属性列表, 示例:
            [
              {
                "identifier": "lock_status",
                "name": "锁屏状态",
                "dataType": "BOOL",
                "rwFlag": "READ_ONLY",
                "required": false,
                "dataSpecsList": [
                  {
                    "identifier": "lock_status",
                    "name": "未锁屏",
                    "dataType": "BOOL",
                    "custom": true,
                    "value": 0
                  },
                  {
                    "identifier": "lock_status",
                    "name": "已锁屏",
                    "dataType": "BOOL",
                    "custom": true,
                    "value": 1
                  }
                ]
              },
              {
                "identifier": "system_name",
                "name": "系统名",
                "dataType": "TEXT",
                "rwFlag": "READ_ONLY",
                "required": false,
                "dataSpecs": {
                  "length": 100,
                  "dataType": "TEXT"
                }
              }
            ]
        services: 服务列表, 示例:
            [
              {
                "identifier": "lock_screen",
                "name": "锁屏",
                "callType": "async",
                "required": false,
                "inputData": []
              }
            ]

    """
    if properties:
        properties = (
            properties if isinstance(properties, list) else json.loads(properties)
        )
    else:
        properties = []
    if services:
        services = services if isinstance(services, list) else json.loads(services)
    else:
        services = []

    # 归一化为阿里云 CreateThingModel 接受的内部格式(注入 productKey、服务字段名等)
    properties = [_inject_product_key(p, productKey) for p in properties]
    services = [_normalize_service(s, productKey) for s in services]

    thing_model_json = json.dumps(
        {"properties": properties, "services": services, "events": []},
        ensure_ascii=False,
    )
    req = iot_models.CreateThingModelRequest(
        product_key=productKey,
        thing_model_json=thing_model_json,
        iot_instance_id=instance_id,
    )
    try:
        body = client.create_thing_model(req).body
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(body):
        return _failed_result(body)
    success_add = [p.get("name") for p in properties if p.get("name")]
    success_add += [s.get("serviceName") for s in services if s.get("serviceName")]
    msg = "成功添加功能: " + ", ".join(success_add)
    if not _publish_thing_model(productKey):
        msg += "; 注意: 物模型发布失败, 新功能可能在平台不可见, 请手动发布"
    return {"result": msg}


@tool
def productDelFun(
        productKey: str,
        funType: str,
        identifiers: list[str] | str,
) -> Any:
    """产品删除功能, 更新功能先删除后新建.

    Args:
        productKey: 产品 key.
        funType: 功能类型, 取值: properties=属性, services=服务, events=事件.
        identifiers: 功能标识列表 (可传 list 或 JSON 字符串).
    """
    identifiers = (
        identifiers if isinstance(identifiers, list) else json.loads(identifiers)
    )
    req = iot_models.DeleteThingModelRequest(
        product_key=productKey,
        iot_instance_id=instance_id,
    )
    # 标识符需以列表传入, SDK 会序列化为 PropertyIdentifier.1 / .2 ... 形式的重复参数
    if funType == "properties":
        req.property_identifier = identifiers
    elif funType == "services":
        req.service_identifier = identifiers
    elif funType == "events":
        req.event_identifier = identifiers
    else:
        return {"status": "failed", "errorMessage": f"不支持的功能类型: {funType}"}
    try:
        body = client.delete_thing_model(req).body
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(body):
        return _failed_result(body)
    msg = "成功删除功能: " + ", ".join(identifiers)
    if not _publish_thing_model(productKey):
        msg += "; 注意: 物模型发布失败, 变更可能在平台不可见, 请手动发布"
    return {"result": msg}


@tool
def productList() -> Any:
    """产品列表, 包含所有产品."""
    items: list[dict] = []
    current_page = 1
    page_size = 200
    while True:
        req = iot_models.QueryProductListRequest(
            current_page=current_page,
            page_size=page_size,
            iot_instance_id=instance_id,
        )
        try:
            body = client.query_product_list(req).body
        except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
            return {"status": "failed", "errorMessage": str(e)}
        if _failed(body):
            return _failed_result(body)
        pdata = getattr(body, "data", None)
        # data.list 是 QueryProductListResponseBodyDataList 包装对象, 真正列表在其 product_info
        rows = getattr(getattr(pdata, "list", None), "product_info", None) or []
        for p in rows:
            items.append(
                {
                    "productKey": getattr(p, "product_key", None),
                    "productName": getattr(p, "product_name", None),
                    "deviceCnt": getattr(p, "device_count", None),
                    "description": getattr(p, "description", None),
                }
            )
        page_count = getattr(pdata, "page_count", 0) or 0
        if current_page >= page_count or not rows or current_page >= 50:
            break
        current_page += 1
    return items


@tool
def createProduct(
        product_name: str,
        description: str = None,
) -> Any:
    """新建产品. 创建前请检查是否已有同名产品.

    Args:
        product_name: 产品名.
        description: 备注; 可选.
    """
    req = iot_models.CreateProductRequest(
        product_name=product_name,
        description=description,
        net_type='WIFI',
        node_type=0,
        data_format=1,
        auth_type='secret',
        aliyun_commodity_code="iothub_senior",
        publish_auto=False,
        iot_instance_id=instance_id,
    )
    try:
        body = client.create_product(req).body
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(body):
        return _failed_result(body)
    return {"productKey": getattr(body, "product_key", None)}


# --------------------------------------------------------------------------- #
# 设备
# --------------------------------------------------------------------------- #
def _query_devices(product_key: str):
    """查询单个产品的全部设备(分页), 返回设备列表; 失败返回 failed dict."""
    items: list[dict] = []
    current_page = 1
    page_size = 200
    while True:
        req = iot_models.QueryDeviceRequest(
            current_page=current_page,
            page_size=page_size,
            product_key=product_key,
            iot_instance_id=instance_id,
        )
        try:
            body = client.query_device(req).body
        except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
            return {"status": "failed", "errorMessage": str(e)}
        if _failed(body):
            return _failed_result(body)
        rows = getattr(getattr(body, "data", None), "device_info", None) or []
        for d in rows:
            items.append(
                {
                    "iotId": getattr(d, "iot_id", None),
                    "productKey": getattr(d, "product_key", None),
                    "deviceName": getattr(d, "device_name", None),
                    "nickname": getattr(d, "nickname", None),
                    "status": getattr(d, "device_status", None),
                    "gmtCreate": getattr(d, "gmt_create", None),
                    "gmtModified": getattr(d, "gmt_modified", None),
                }
            )
        page_count = getattr(body, "page_count", 0) or 0
        if current_page >= page_count or not rows or current_page >= 50:
            break
        current_page += 1
    return items


@tool
def deviceList(productKey: str = None) -> Any:
    """设备实例列表, 包含所有设备实例.

    Args:
        productKey: 产品key, 不传全部设备.
    """
    if productKey:
        return _query_devices(productKey)
    # 未指定产品: 先取所有产品, 再逐产品汇总设备; 单产品查询失败则跳过继续
    products = productList.invoke({})
    if isinstance(products, dict):  # 获取产品失败, 直接返回错误
        return products
    all_devices: list[dict] = []
    for p in products:
        pk = p.get("productKey")
        if not pk:
            continue
        devices = _query_devices(pk)
        if isinstance(devices, dict):  # 该产品查询失败, 跳过
            continue
        all_devices.extend(devices)
    return all_devices


@tool
def createDevice(
        productKey: str,
        deviceName: str,
        nickname: str,
) -> Any:
    """设备实例创建.

    Args:
        productKey: 归属产品的 key.
        deviceName: 设备名(产品内唯一),纯英文或数字,不要有符号
        nickname: 昵称,中文名
    """
    req = iot_models.RegisterDeviceRequest(
        product_key=productKey,
        device_name=deviceName,
        nickname=nickname,
        iot_instance_id=instance_id,
    )
    try:
        body = client.register_device(req).body
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(body):
        return _failed_result(body)
    info = getattr(body, "data", None)
    return {"iotId": getattr(info, "iot_id", None)}


@tool
def invokeService(
        iotId: str,
        identifier: str,
        arg: dict,
) -> Any:
    """设备服务调用 (InvokeThingService).

    Args:
        iotId: 设备全局 id.
        identifier: 服务标识符 (物模型 services[].identifier).
        arg: 服务调用参数, 例: {"light": 1}.
    """
    req = iot_models.InvokeThingServiceRequest(
        iot_id=iotId,
        identifier=identifier,
        args=json.dumps(arg, ensure_ascii=False),
        iot_instance_id=instance_id,
    )
    try:
        body = client.invoke_thing_service(req).body
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(body):
        return _failed_result(body)
    info = getattr(body, "data", None)
    return {
        "messageId": getattr(info, "message_id", None),
        "result": getattr(info, "result", None),
    }


@tool
def setProperty(
        iotId: str,
        data: dict,
) -> Any:
    """设置属性 (SetDevicesProperty).

    SetDevicesProperty 不支持 iotId, 内部先 QueryDeviceDetail 解析 productKey/deviceName.

    Args:
        productKey: 设备全局 id.
        data: 属性键值对, 例: {"Humidity": 66, "Temperature": 60}.
    """
    req = iot_models.SetDevicePropertyRequest(
        iot_id=iotId,
        items=json.dumps(data, ensure_ascii=False),
        iot_instance_id=instance_id,
    )
    try:
        body = client.set_devices_property(req).body
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(body):
        return _failed_result(body)
    return {"result": "成功设置属性"}


@tool
def getProperties(iotId: str) -> Any:
    """获取设备属性 (QueryDevicePropertyStatus).

    Args:
        iotId: 设备全局 id.

    Return:
        响应示例: {"Humidity": 66, "Temperature": 60}
    """
    req = iot_models.QueryDevicePropertyStatusRequest(
        iot_id=iotId, iot_instance_id=instance_id
    )
    try:
        body = client.query_device_property_status(req).body
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(body):
        return _failed_result(body)
    list_obj = getattr(getattr(body, "data", None), "list", None)
    if list_obj is not None and hasattr(list_obj, "property_status_info"):
        infos = getattr(list_obj, "property_status_info", None) or []
    elif isinstance(list_obj, list):
        infos = list_obj
    else:
        infos = []
    infos2 = {}
    for p in infos:
        infos2[getattr(p, "identifier", '')] = getattr(p, "value", '')
    return infos2


# --------------------------------------------------------------------------- #
# 设备接入
# --------------------------------------------------------------------------- #
def _device_detail(iot_id: str):
    """通过 iotId 查询设备详情, 返回响应 body 对象(异常向上抛出由调用方处理)."""
    req = iot_models.QueryDeviceDetailRequest(
        iot_id=iot_id, iot_instance_id=instance_id
    )
    return client.query_device_detail(req).body


@tool
def connectDeviceToPlatform(iotId: str, prompt: str):
    """接入设备到物联网云平台, 耗时较长

    Args:
        iotId: 设备全局 id.
        prompt: 用户提示词, 包含接入设备相关信息, 调用子 agent 使用.
    """
    result: dict = {}
    try:
        detail_body = _device_detail(iotId)
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(detail_body):
        return _failed_result(detail_body)
    detail = getattr(detail_body, "data")
    product_key = getattr(detail, "product_key")
    device_name = getattr(detail, "device_name")
    device_secret = getattr(detail, "device_secret")
    if not all([product_key, device_name, device_secret]):
        return {"status": "failed", "errorMessage": "设备缺少三元组信息"}

    # 获取物模型
    thing_model = getThingModel.invoke({"productKey": product_key})
    model_text = (
        thing_model.get("thingModelJson", "")
        if isinstance(thing_model, dict)
        else str(thing_model)
    )
    try:
        model_text = json.dumps(json.loads(model_text), ensure_ascii=False, indent=2)
    except (TypeError, ValueError):
        pass

    with open('doc/template_iot_connect.py', 'r', encoding='utf-8') as f:
        code = f.read()  # 读取全部内容
    code = code.replace('${productKey}', product_key)
    code = code.replace('${deviceName}', device_name)
    code = code.replace('${secret}', device_secret)
    task_prompt = (
        "你是物联网设备接入专家。请根据用户需求完成任务\n"
        "一般是让你帮忙将设备接入阿里云物联网平台, 也有可能让你帮忙解决bug\n"
        "设备接入要求:\n"
        "- 如果目标设备工作目录下存在iot.txt请优先根据该说明完成任务\n"
        "- 依据物模型 properties 实现属性上报, 依据 services 实现服务调用处理与回复\n"
        "- 属性10s一检测,变化才上报且只上报变化的属性\n"
        "- 接入成功后让接入程序在后台运行,但不要设置开机运行\n"
        "- 接入程序加上日志,每条日志有时间\n"
        "- 使用python语言编写代码,代码尽量简洁\n"
        f"- 非远程环境, 默认使用{sys.prefix}目录的python环境运行\n"
        "- 在工作目录生成tsl.json\n"
        "- 文件名用iot_{当前目录名}.py\n"
        "- 使用python库: aliyun-iot-linkkit==1.2.13, paho-mqtt==1.6.1\n\n"
        f"【用户需求】\n{prompt}\n\n"
        f"【tsl.json】\n{model_text}\n\n"
        f"【模版代码】\n{code}\n\n"

    )

    # 调用本地 claude code cli, --dangerously-skip-permissions 使其可自主读写文件与执行命令
    random_dir_name = str(uuid.uuid4())
    workspace = "D:/data/ai_empty_workspace/" + random_dir_name
    os.makedirs(workspace, exist_ok=True)
    try:
        proc = subprocess.run(
            ["claude", "-p", "--dangerously-skip-permissions", "--output-format", "text"],
            input=task_prompt,
            capture_output=True,
            text=True,
            encoding="utf-8",
            timeout=1800,
            cwd=workspace,
        )
    except FileNotFoundError:
        result["error"] = "未找到 claude 命令, 请确认已安装 Claude Code CLI 并加入 PATH"
        return result
    except subprocess.TimeoutExpired:
        result["error"] = "claude code cli 执行超时"
        return result

    output = (proc.stdout or "").strip()
    if proc.returncode != 0:
        result["error"] = (
            f"claude code cli 执行失败(returncode={proc.returncode}): "
            f"{output}\n{(proc.stderr or '').strip()}"
        )
    else:
        result["output"] = output

    return result


@tool
def connectDeviceToPlatformCode(iotId: str, prompt: str):
    """生成接入设备到物联网云平台代码

    Args:
        iotId: 设备全局 id.
        prompt: 用户提示词, 包含接入设备相关信息, 调用子 agent 使用.
    """
    result: dict = {}
    try:
        detail_body = _device_detail(iotId)
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": str(e)}
    if _failed(detail_body):
        return _failed_result(detail_body)
    detail = getattr(detail_body, "data")
    product_key = getattr(detail, "product_key")
    device_name = getattr(detail, "device_name")
    device_secret = getattr(detail, "device_secret")
    if not all([product_key, device_name, device_secret]):
        return {"status": "failed", "errorMessage": "设备缺少三元组信息"}

    # 获取物模型
    thing_model = getThingModel.invoke({"productKey": product_key})
    model_text = (
        thing_model.get("thingModelJson", "")
        if isinstance(thing_model, dict)
        else str(thing_model)
    )
    try:
        model_text = json.dumps(json.loads(model_text), ensure_ascii=False, indent=2)
    except (TypeError, ValueError):
        pass

    with open('doc/template_iot_connect.py', 'r', encoding='utf-8') as f:
        code = f.read()  # 读取全部内容
    code = code.replace('${productKey}', product_key)
    code = code.replace('${deviceName}', device_name)
    code = code.replace('${secret}', device_secret)
    task_prompt = (
        "你是物联网设备接入专家。请根据用户需求生成代码\n"
        "一般是让你帮忙将设备接入阿里云物联网平台, 也有可能让你帮忙解决bug\n"
        "设备接入代码要求:\n"
        "- 依据物模型 properties 实现属性上报, 依据 services 实现服务调用处理与回复\n"
        "- 使用python语言编写代码,代码尽量简洁\n"
        f"【用户需求】\n{prompt}\n\n"
        f"【tsl.json】\n{model_text}\n\n"
        f"【模版代码】\n{code}\n\n"
    )
    print(f"[connectDeviceToPlatformCode] 开始调用 LLM(流式), prompt 长度={len(task_prompt)} 字符", flush=True)
    t0 = time.time()
    try:
        messages = [
            HumanMessage(content=task_prompt)
        ]
        chunks = []
        llm2 = llm_client.get_llm(model='qwen3.7-plus', streaming=True, enable_thinking=False)
        for chunk in llm2.stream(messages):
            # 流式 chunk 偶有空片段(开头 role delta / 末尾 usage chunk), 过滤后实时回显并拼接为完整文本
            if chunk.content:
                print(chunk.content, end="", flush=True)
                chunks.append(chunk.content)
        result_text = "".join(chunks)
    except Exception as e:  # noqa: BLE001 - 透传错误供 agent 处理
        return {"status": "failed", "errorMessage": f"LLM 调用失败: {e}"}
    print(f"\n[connectDeviceToPlatformCode] LLM 返回, 耗时={time.time() - t0:.1f}s", flush=True)
    return result_text


@tool
def createFlow(flowJson: str):
    """创建流程, 适用于nodered v5.0.4版本.
可以通过api的方式调用getProperties,setProperty,invokeService工具,传参与工具调用一致
调用api使用http request节点
api的url格式: post http://host.docker.internal:8102/api/tools/<工具名>
Content-Type: application/json

    Args:
        :param flowJson: 流程内容json,适用于nodered的flows.json,包含tab节点
    """
    try:
        new_nodes = json.loads(flowJson)
    except (TypeError, ValueError) as e:
        return f"流程json解析失败: {e}"
    if isinstance(new_nodes, dict):
        new_nodes = [new_nodes]
    if not isinstance(new_nodes, list) or not new_nodes:
        return "流程json格式不正确, 应为非空节点数组"

    # 定位 docker/nodered/flows.json (相对项目根目录, 不依赖运行时cwd)
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    flows_path = os.path.join(project_root, "docker", "nodered", "flows.json")

    # 读取原有 flows.json, 用于合并以及避免id冲突
    existing: list = []
    if os.path.exists(flows_path):
        try:
            with open(flows_path, "r", encoding="utf-8") as f:
                loaded = json.load(f)
            if isinstance(loaded, list):
                existing = loaded
        except (TypeError, ValueError, OSError):
            existing = []
    existing_ids = {n.get("id") for n in existing if isinstance(n, dict)}

    # 为每个节点生成新的16位hex id(与nodered默认风格一致), 避免与已有id重复
    id_map: dict = {}
    for node in new_nodes:
        if not isinstance(node, dict) or "id" not in node:
            continue
        new_id = uuid.uuid4().hex[:16]
        while new_id in existing_ids or new_id in id_map.values():
            new_id = uuid.uuid4().hex[:16]
        id_map[node["id"]] = new_id

    def _remap_ref(ref):
        """替换引用: 字符串id 或 含id的对象(如wires中的连线目标)."""
        if isinstance(ref, str):
            return id_map.get(ref, ref)
        if isinstance(ref, dict) and ref.get("id") in id_map:
            ref["id"] = id_map[ref["id"]]
        return ref

    # 重写每个节点的 id / z(所属tab引用) / wires(连线引用), 保持拓扑一致
    for node in new_nodes:
        if not isinstance(node, dict):
            continue
        if node.get("id") in id_map:
            node["id"] = id_map[node["id"]]
        if node.get("z") in id_map:
            node["z"] = id_map[node["z"]]
        if isinstance(node.get("wires"), list):
            node["wires"] = [
                [_remap_ref(target) for target in port]
                for port in node["wires"]
            ]

    # 合并到原flows.json并落盘
    existing.extend(new_nodes)
    try:
        with open(flows_path, "w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=4)
    except OSError as e:
        return f"流程写入失败: {e}"

    # 重启nodered容器使其重新加载flows.json
    try:
        subprocess.run(
            ["docker", "restart", "nodered"],
            capture_output=True, text=True, timeout=60, check=False,
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as e:
        return f"流程已写入, 但nodered重启失败: {e}"

    return "流程创建成功"


@tool
def createDashboard(name: str, html: str):
    """创建仪表盘, 尽量减少页面代码,不要注释,科技风
可以使用bootcdn源的jquery,bootstrap库
可以通过api的方式调用getProperties,setProperty,invokeService,deviceList等工具,传参与工具调用一致
api的url格式: post http://106.53.211.236:8102/api/tools/<工具名>
Content-Type: application/json

    Args:
        name: 仪表盘名称,英文
        html: 仪表盘html
    """

    fileName = name + ".html"
    with open(f'static/dashboard/{fileName}', 'w', encoding='utf-8') as f:
        f.write(html)
    return f"创建仪表盘成功,地址: http://{deploy_host}:8100/static/dashboard/{fileName}"


all_tool_map = {
    "物模型获取": getThingModel,
    "产品列表": productList,
    "产品添加功能": productAddPropertiesServices,
    "产品删除功能": productDelFun,
    "产品新建": createProduct,
    "设备列表": deviceList,
    "设备创建": createDevice,
    "设备服务调用": invokeService,
    "设置设备属性": setProperty,
    "获取设备属性": getProperties,
    "连接设备到物联网云平台": connectDeviceToPlatform,
    # "连接设备到物联网云平台代码": connectDeviceToPlatformCode,
    # "创建流程": createFlow,
    # "设置仪表盘": setDashboard,
    "创建仪表盘": createDashboard,
    "延时": common_tool.delay,
    "发送网络请求": common_tool.webRequest,
}

TOOL_NAME_CN = {fun.name: key for key, fun in all_tool_map.items()}
all_tools = list(all_tool_map.values())
