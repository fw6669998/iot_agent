import uvicorn
from langchain_mcp_adapters.tools import to_fastmcp
from mcp.server.fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.routing import Mount

from services.iot_tools import all_tools

iot_tools = [to_fastmcp(t) for t in all_tools]
iot_app = FastMCP("iot", tools=iot_tools).streamable_http_app()

gateway = Starlette(
    routes=[
        Mount("/iot", app=iot_app),  # http://host:8080/iot/mcp
    ]
)

if __name__ == "__main__":
    uvicorn.run(gateway, host="0.0.0.0", port=8100)
