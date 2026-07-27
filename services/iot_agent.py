from langchain.agents import create_agent

from services.llm_client import llm
from services.iot_tools import all_tools

iot_agent = create_agent(
    model=llm,
    tools=all_tools,
    system_prompt=(
        "你是一个物联网平台的智能助手，可以查询和管理设备产品、物模型和设备实例。"
        "支持创建产品、新增物模型功能、创建设备、查询设备列表、读写设备属性、调用设备服务等操作。"
        "调用工具时请核对必填参数，必要时先调用查询接口获得 productKey 或 iotId。"
    ),
)

if __name__ == "__main__":
    print('start')
