"""物联网平台工具集.

使用 langchain-core 的 @tool 装饰器定义 10 个供 agent 调用的工具,
统一通过 IoTClient 访问 http://iot.iuvtech.com 平台.

配置通过 .env 加载:
    IOT_HOST          平台地址
    IOT_TOKEN         全局 header token
    IOT_API_PREFIX    api 统一前缀
    IOT_PROJECT_ID    默认项目 id
"""

import json
import os
from typing import Any, Optional

import requests
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()


class IoTClient:
    """物联网平台 HTTP 客户端单例."""

    _instance: Optional["IoTClient"] = None

    def __new__(cls) -> "IoTClient":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self) -> None:
        host = os.getenv("IOT_HOST", "").rstrip("/")
        if not host:
            raise ValueError("IOT_HOST 未配置, 请检查 .env")
        self.base_url: str = f"{host}/api"
        self.project_id: Any = os.getenv("IOT_PROJECT_ID", "")
        self.session: requests.Session = requests.Session()
        token = os.getenv("IOT_TOKEN", "")
        if token:
            self.session.headers["token"] = token

    def _check(self, resp: dict) -> Any:
        """统一校验响应, 成功返回 data, 失败抛出 sysMsg."""
        status = resp.get("status")
        if status != "S":
            raise RuntimeError(f"物联网平台调用失败: {resp.get('sysMsg', resp)}")
        return resp.get("data")

    def _get(self, path: str, params: Optional[dict] = None) -> Any:
        url = f"{self.base_url}/{path}"
        resp = self.session.get(url, params=params, timeout=30)
        resp.raise_for_status()
        return self._check(resp.json())

    def _post_form(self, path: str, data: Optional[dict] = None) -> Any:
        """form-data / urlencoded POST (无文件上传)."""
        url = f"{self.base_url}/{path}"
        resp = self.session.post(url, data=data or {}, timeout=30)
        resp.raise_for_status()
        return self._check(resp.json())

    _post_urlencoded = _post_form


_client = IoTClient()


@tool
def insert_thing_fun(
        product_key: str,
        fun_type: str,
        fun_detail: dict,
) -> Any:
    """物模型_插入功能 (iotThing/insertThingFun).

    为指定产品的物模型新增一个属性/服务/事件.

    Args:
        product_key: 产品 key.
        fun_type: 功能类型, 取值: properties=属性, services=服务, events=事件.
        fun_detail: 功能详情, dict 会被序列化成 json 字符串提交.
            属性示例: {"identifier": "cpu_usage", "name": "CPU使用率", "accessMode": "rw", "required": false, "dataType": {"type": "float", "specs": {"min": "0", "max": "100", "unit": "%", "unitName": "百分比", "step": "0.1"}}}
            服务/事件示例详见 doc/物模型TSL.json.
    """
    return _client._post_form(
        "iotThing/insertThingFun",
        {
            "productKey": product_key,
            "funType": fun_type,
            "funDetail": json.dumps(fun_detail, ensure_ascii=False),
        },
    )


@tool
def thing_list_search(page: int = 0, size: int = 100) -> Any:
    """物模型模板列表 (iotThing/thingListSearch).

    获取平台预置物模型分类 (3 层级数据), 基本不变, 建议缓存.

    Args:
        page: 分页页码, 从 0 开始.
        size: 每页元素个数.
    """
    return _client._get("iotThing/thingListSearch", {"page": page, "size": size})


@tool
def get_thing_model(product_key: str) -> Any:
    """物模型_获取 (iotThing/getThingModel).

    获取指定产品的物模型 (properties / services / events).

    Args:
        product_key: 产品 key.
    """
    return _client._get("iotThing/getThingModel", {"productKey": product_key})


@tool
def product_list_search(
        page: int = 0,
        size: int = 10,
        sort: str = "createTime,desc",
        node_type: Optional[int] = None,
        product_name: Optional[str] = None,
        project_id: Optional[int] = None,
) -> Any:
    """设备模型(产品)列表和搜索 (iotProduct/listSearch).

    Args:
        page: 页码, 从 0 开始.
        size: 每页元素个数.
        sort: 排序, 默认 "createTime,desc".
        node_type: 设备类型: 0=直连设备, 1=网关设备, 2=非直连子设备; None 不过滤.
        product_name: 产品名模糊搜索; None 不过滤.
        project_id: 项目 id, 默认使用 .env 的 IOT_PROJECT_ID.
    """
    params = {
        "projectId": project_id if project_id is not None else _client.project_id,
        "page": page,
        "size": size,
        "sort": sort,
    }
    if node_type is not None:
        params["nodeType"] = node_type
    if product_name:
        params["productName"] = product_name
    return _client._get("iotProduct/listSearch", params)


@tool
def create_product(
        product_name: str,
        node_type: int,
        auth_type: str,
        link_obj: str,
        belong: str,
        data_parse_rule: str,
        net_type: Optional[str] = None,
        category_key: Optional[str] = None,
        data_format: Optional[int] = None,
        description: Optional[str] = None,
        product_type: Optional[str] = None,
        project_id: Optional[int] = None,
) -> Any:
    """设备模型(产品)新建 (iotProduct/create).

    Args:
        product_name: 产品名.
        node_type: 设备类型: 0=直连设备, 1=网关设备, 2=非直连子设备.
        auth_type: 认证方式: secret=设备秘钥, x509=x509证书.
        link_obj: 映射对象: virtual=虚拟设备, real=硬件设备, virtualReal=虚实联动设备.
        belong: 模型归属: public=租户共用, private=工程私有.
        data_parse_rule: 数据解析规则.
        net_type: 联网方式: WiFi/BlueTooth/Cellular/Ethernet/LoRaWAN; 可选.
        category_key: 物模型模板模型标识, 自定义传空; 可选.
        data_format: 数据格式: 0=自定义, 1=json; 可选.
        description: 备注; 可选.
        product_type: 接入协议: Modbus/OPCUA/ZigBee/BLE/Custom; 可选.
        project_id: 项目 id, 默认使用 .env 的 IOT_PROJECT_ID.
    """
    data = {
        "productName": product_name,
        "nodeType": node_type,
        "authType": auth_type,
        "linkObj": link_obj,
        "belong": belong,
        "dataParseRule": data_parse_rule,
        "projectId": project_id if project_id is not None else _client.project_id,
    }
    if net_type is not None:
        data["netType"] = net_type
    if category_key is not None:
        data["categoryKey"] = category_key
    if data_format is not None:
        data["dataFormat"] = data_format
    if description is not None:
        data["description"] = description
    if product_type is not None:
        data["productType"] = product_type
    return _client._post_form("iotProduct/create", data)


@tool
def device_list_search(
        page: int = 0,
        size: int = 10,
        sort: Optional[str] = None,
        product_key: Optional[str] = None,
        node_type: Optional[int] = None,
        device_name: Optional[str] = None,
        project_id: Optional[int] = None,
) -> Any:
    """设备实例列表和搜索 (iotDevice/listSearch).

    Args:
        page: 分页页码, 从 0 开始.
        size: 每页元素个数.
        sort: 排序; None 不过滤.
        product_key: 按产品 key 过滤; 可选.
        node_type: 设备类型: 0=直连设备, 1=网关设备, 2=非直连子设备; 可选.
        device_name: 设备名称或 uuid; 可选.
        project_id: 项目 id, 默认使用 .env 的 IOT_PROJECT_ID.
    """
    params = {
        "projectId": project_id if project_id is not None else _client.project_id,
        "page": page,
        "size": size,
    }
    if sort:
        params["sort"] = sort
    if product_key:
        params["productKey"] = product_key
    if node_type is not None:
        params["nodeType"] = node_type
    if device_name:
        params["deviceName"] = device_name
    return _client._get("iotDevice/listSearch", params)


@tool
def create_device(
        product_key: str,
        nickname: str,
        labels: Optional[str] = None,
        description: Optional[str] = None,
        gw_device: Optional[str] = None,
        hardware_id: Optional[str] = None,
        scene_id: Optional[str] = None,
        scene_device_id: Optional[str] = None,
) -> Any:
    """设备实例创建 (iotDevice/create).

    Args:
        product_key: 归属产品的 key.
        nickname: 设备名.
        labels: 标签, 用逗号分割, 前后都加上逗号, 例: ",aaa,bbb,"; 可选.
        description: 描述; 可选.
        gw_device: 网关设备的 iotId; 可选.
        hardware_id: 硬件 UUID; 可选.
        scene_id: 关联场景 id; 可选.
        scene_device_id: 关联场景设备 id; 可选.
    """
    data = {
        "productKey": product_key,
        "nickname": nickname,
    }
    if labels is not None:
        data["labels"] = labels
    if description is not None:
        data["description"] = description
    if gw_device is not None:
        data["GWDevice"] = gw_device
    if hardware_id is not None:
        data["hardwareId"] = hardware_id
    if scene_id is not None:
        data["sceneId"] = scene_id
    if scene_device_id is not None:
        data["sceneDeviceId"] = scene_device_id
    return _client._post_form("iotDevice/create", data)


@tool
def invoke_service(
        iot_id: str,
        identifier: str,
        arg: dict,
) -> Any:
    """设备服务调用 (iotDevice/invokeService).

    Args:
        iot_id: 设备全局 id.
        identifier: 服务标识符 (物模型 services[].identifier).
        arg: 服务调用参数, dict 会被序列化成 json 字符串提交, 例: {"type": "temp5"}.
    """
    return _client._post_urlencoded(
        "iotDevice/invokeService",
        {
            "iotId": iot_id,
            "identifier": identifier,
            "arg": json.dumps(arg, ensure_ascii=False),
        },
    )


@tool
def set_property(
        iot_id: str,
        data: dict,
) -> Any:
    """设置属性 (iotDevice/setProperty).

    Args:
        iot_id: 设备全局 id.
        data: 属性键值对, dict 会被序列化成 json 字符串提交, 例: {"Humidity": 66, "Temperature": 60}.
    """
    return _client._post_form(
        "iotDevice/setProperty",
        {
            "iotId": iot_id,
            "data": json.dumps(data, ensure_ascii=False),
        },
    )


@tool
def get_properties(iot_id: str) -> Any:
    """获取设备属性 (iotDevice/getProperties).

    Args:
        iot_id: 设备全局 id.
    """
    return _client._get("iotDevice/getProperties", {"iotId": iot_id})


all_tools = [
    insert_thing_fun,
    thing_list_search,
    get_thing_model,
    product_list_search,
    create_product,
    device_list_search,
    create_device,
    invoke_service,
    set_property,
    get_properties,
]

if __name__ == "__main__":
    print(f"已定义 {len(all_tools)} 个工具:")
    for t in all_tools:
        print(f"  - {t.name}")
