"""物联网工具 REST API 服务.

将 services/iot_tools.py 中的 langchain @tool 工具逐一暴露为 HTTP 接口,
供非 MCP 客户端直接以 JSON 调用. 与 mcp_server.py(MCP 协议)、
agent_server.py(对话流式)并列, 三者共享同一套工具实现.

启动: python api_server.py  (默认 0.0.0.0:8102)

接口:
    GET  /api/health            健康检查
    GET  /api/tools             列出全部工具及元数据(名称/中文名/描述/参数 schema)
    POST /api/tools/<name>      按名调用工具, 请求体 JSON 作为入参
"""

from dotenv import load_dotenv

load_dotenv()
from flask import Flask, jsonify, request
from flask_cors import CORS

from services.ali_iot_tools import all_tools, TOOL_NAME_CN, all_tool_map
from services import ali_iot_tools

app = Flask(__name__)
# jsonify 默认 ensure_ascii=True, 会把中文转成 \uXXXX 转义导致无法直读;
# 关闭后以 UTF-8 原文返回(Content-Type 仍带 charset=utf-8).
app.json.ensure_ascii = False
CORS(app)

# 工具名 -> StructuredTool, 用于按名路由调用
TOOL_MAP = {t.name: t for t in all_tools}


@app.get("/api/health")
def health():
    """健康检查, 顺带返回可用工具数量."""
    return jsonify(status="ok", tools=len(TOOL_MAP))


@app.get("/api/tools")
def list_tools():
    """列出全部工具及其元数据, 供客户端发现工具并据此拼装入参."""
    args = request.get_json(silent=True) or {}
    level = args.get("level", "control")  # 查询操作设备=control,  操作平台+control=platform.
    control_tools = [
        ali_iot_tools.productList,
        ali_iot_tools.deviceList,
        ali_iot_tools.getThingModel,
        ali_iot_tools.getProperties,
        ali_iot_tools.setProperty,
        ali_iot_tools.invokeService,
    ]
    if level == "platform":
        tools = all_tools
    else:
        tools = control_tools
    return jsonify(tools=[
        {
            "name": t.name,
            # "name_cn": TOOL_NAME_CN.get(t.name, t.name),
            "description": t.description,
            "args": t.args,
        }
        for t in tools
    ])


@app.post("/api/tools/<name>")
def invoke_tool(name):
    """按名调用工具. 请求体 JSON 作为工具入参, 缺省参数走工具默认值.

    成功: {"ok": true, "result": <工具返回>}
    失败: {"ok": false, "error": "..."} (404 未知工具 / 400 调用异常)
    """
    tool = TOOL_MAP.get(name)
    if tool is None:
        return jsonify(ok=False, error=f"未知工具: {name}"), 404

    args = request.get_json(silent=True) or {}
    token = request.headers.get("Authorization")
    # if token != "Bearer " + "123456":
    #     return jsonify(ok=False, error="无效的授权"), 401
    try:
        result = tool.invoke(args)
    except Exception as e:
        return jsonify(ok=False, error=str(e)), 400
    return jsonify(result)


if __name__ == "__main__":
    # threaded=True: connectDeviceToPlatform 等工具会阻塞数分钟,
    # 多线程避免单个长调用挤占其它请求
    app.run(host="0.0.0.0", port=8102, threaded=True)
