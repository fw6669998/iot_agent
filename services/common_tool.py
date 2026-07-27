import json
import time
from typing import Optional

import requests
from langchain_core.tools import tool


@tool
def delay(second: float = 5):
    """ 延时
    :param second:延时多少秒
    """
    time.sleep(second)
    return "已延时" + str(second) + "秒"


@tool
def webRequest(
    url: str,
    method: str = "get",
    params: Optional[dict | str] = None,
    headers: Optional[dict | str] = None,
    body: Optional[dict | str] = None,
    timeout: float = 30,
) -> dict:
    """发送 HTTP 网络请求, 支持 GET/POST/PUT/DELETE/PATCH/HEAD/OPTIONS 等全部方法.

    可用于调用 REST API、获取网页内容、与第三方服务交互等. 请求或响应出错时不抛异常,
    而是在返回 dict 的 error 字段中说明原因, 供调用方判断处理.

    Args:
        url: 请求地址, 需包含协议(http:// 或 https://).
        method: HTTP 方法, 不区分大小写, 默认 get.
        params: URL 查询参数, 例 {"page": 1, "q": "iot"} (可传 dict 或 JSON 字符串).
        headers: 请求头, 例 {"Authorization": "Bearer xxx"} (可传 dict 或 JSON 字符串).
            发送表单时设置 Content-Type: application/x-www-form-urlencoded,
            并把 body 传为 "a=1&b=2" 形式的字符串.
        body: 请求体. 传 dict(或 JSON 字符串) 时自动按 JSON 发送并设置
            Content-Type: application/json; 传非合法 JSON 的字符串时按原始文本发送.
            GET/HEAD 一般不带 body. (可传 dict 或 JSON 字符串)
        timeout: 超时秒数, 默认 30.

    Returns:
        成功: {"status_code": 200, "headers": {...}, "body": "..."}; 响应体超过
        8000 字符会截断并附带 truncated=true 与 body_length;
        失败: {"status_code": 0, "error": "..."}
    """
    method = (method or "get").strip().lower()

    def _as_dict(value):
        """dict 直返; 字符串尝试 JSON 解析, 失败抛 ValueError; None 直返."""
        if value is None or isinstance(value, dict):
            return value
        if isinstance(value, str):
            try:
                return json.loads(value)
            except (TypeError, ValueError) as e:
                raise ValueError(f"无法解析为 JSON: {value[:200]}") from e
        raise ValueError(f"不支持的参数类型: {type(value).__name__}")

    # params / headers 支持 dict 或 JSON 字符串, 统一转 dict
    try:
        params = _as_dict(params)
        headers = _as_dict(headers)
    except ValueError as e:
        return {"status_code": 0, "error": f"参数解析失败: {e}"}

    # 构造请求体: dict / 合法JSON字符串 -> json=; 非JSON字符串 -> data=(原始文本/表单)
    json_body = None
    data_body = None
    if body is not None:
        if isinstance(body, dict):
            json_body = body
        elif isinstance(body, str):
            try:
                json_body = json.loads(body)
            except (TypeError, ValueError):
                data_body = body
        else:
            data_body = body

    try:
        resp = requests.request(
            method=method,
            url=url,
            params=params,
            headers=headers,
            json=json_body,
            data=data_body,
            timeout=timeout,
        )
    except requests.Timeout:
        return {"status_code": 0, "error": f"请求超时({timeout}s)"}
    except requests.ConnectionError as e:
        return {"status_code": 0, "error": f"连接失败: {e}"}
    except requests.RequestException as e:
        return {"status_code": 0, "error": f"请求异常: {e}"}

    # 响应体过长则截断, 避免大响应(如整页 HTML)撑爆 agent 上下文
    text = resp.text
    max_len = 8000
    result: dict = {
        "status_code": resp.status_code,
        "headers": dict(resp.headers),
        "body": text if len(text) <= max_len else text[:max_len],
    }
    if len(text) > max_len:
        result["truncated"] = True
        result["body_length"] = len(text)
    return result


@tool
def get_time():
    """ 获取当前时间
    """
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
