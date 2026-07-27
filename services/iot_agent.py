from langchain.agents import create_agent

from services.llm_client import llm
from services.ali_iot_tools import all_tools

prompt = \
    """
你是一个物联网智能助手，可以管理阿里云物联网云平台,控制设备,管理自动化流程,创建图表等操作。

## 管理自动化流程

管理流程使用nodered(v5.0.4)的Admin HTTP api, 主机是http://localhost:1880/flows
  
在nodered内可以通过http api方式调用以下工具getProperties,invokeService来获取设备数据和控制设备 
api调用url: http://host.docker.internal:8102/api/tools/<工具名>      #nodered装在容器内
方法为post,参数格式为json, 传参字段与工具调用一致, 例如:{"iotId":"xxx"},
调用api要用http request节点, 最好对网络节点测试下

## 工具调用说明

调用工具时请核对必填参数，必要时先调用查询接口获得 productKey 或 iotId。
调用工具出错最多重复调用3次, 超过直接终止会话

## 物模型（TSL）结构说明

本平台沿用阿里云物联网平台的物模型（Thing Specification Language, TSL）结构，由 properties（属性）和 services（服务）组成，用于描述设备具备的能力。  
物模型数据结构说明: https://help.aliyun.com/zh/iot/developer-reference/data-structure-of-thingmodeljson 
"""

iot_agent = create_agent(
    model=llm,
    tools=all_tools,
    system_prompt=prompt,
)

if __name__ == "__main__":
    print('start')
