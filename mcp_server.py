from langchain_mcp_adapters.tools import to_fastmcp
from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv

load_dotenv()
from services.ali_iot_tools import all_tools

iot_tools = [to_fastmcp(t) for t in all_tools]
# stateless_http=True: 每个请求独立处理, 不维护会话状态.
# Dify 等客户端在 streamable-http 有态模式下不一定正确携带 Mcp-Session-Id,
# 会导致服务端返回 404 "Session not found"(客户端表现为 "Session terminated by server").
# 无态模式下无需会话, 彻底规避该问题.
mcp = FastMCP("iot", tools=iot_tools, host="0.0.0.0", port=8101, stateless_http=True)

if __name__ == "__main__":
    mcp.run(transport="streamable-http")
