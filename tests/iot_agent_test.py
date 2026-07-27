from services.iot_agent import iot_agent


def test_iot_agent():
    print("test_iot_agent start")
    from langchain_core.messages import AIMessageChunk, ToolMessage

    for chunk in iot_agent.stream(
            {"messages": [{"role": "user", "content": "有哪些设备在线"}]},
            stream_mode=["messages", "updates"],  # 多模式组合
    ):
        mode, data = chunk  # 解包：(模式名, 数据)

        if mode == "messages":
            # data 是 (AIMessageChunk, metadata) 元组
            msg_chunk, metadata = data
            if isinstance(msg_chunk, AIMessageChunk):
                if msg_chunk.content:
                    print(f"[TOKEN] {msg_chunk.content}")
                if msg_chunk.tool_call_chunks:
                    print(f"[TOOL_CALL] {msg_chunk.tool_call_chunks}")
            elif isinstance(msg_chunk, ToolMessage):
                print(f"[TOOL_CALL] {msg_chunk.name} {msg_chunk.content}")
            else:
                print(f"[OTHER] {msg_chunk}")

        elif mode == "updates":
            # data 是 {节点名: {状态增量}} 字典
            for node_name, node_output in data.items():
                print(f"\n[STEP] 节点: {node_name}")
                if "messages" in node_output:
                    for msg in node_output["messages"]:
                        print(f"  → {msg.content[:100]}")
    print("end\n")


def test_iot_agent_async():
    print("test_iot_agent_async start")
    import asyncio

    async def run():
        from langchain_core.messages import AIMessageChunk, ToolMessage

        # 使用 astream_events(version="v2") 直接订阅 LLM 的 token 级事件,
        # 绕开 create_agent 异步路径不透传 streaming chunk 的问题.
        async for event in iot_agent.astream_events(
                {"messages": [{"role": "user", "content": "有哪些设备在线"}]},
                version="v3",
        ):
            print(event)
            kind = event["event"]
            data = event["data"]

            if kind == "on_chat_model_stream":
                chunk = data["chunk"]
                if isinstance(chunk, AIMessageChunk):
                    if chunk.content:
                        print(f"[TOKEN] {chunk.content}")
                    if chunk.tool_call_chunks:
                        print(f"[TOOL_CALL] {chunk.tool_call_chunks}")
            elif kind == "on_chat_model_end":
                output = data["output"]
                print(f"[STEP] 节点: model\n  → {output.content[:100] if output.content else output}")
            elif kind == "on_tool_end":
                print(f"[STEP] 节点: tools\n  → {data['output']}")
        print("end")

    asyncio.run(run())


if __name__ == "__main__":
    # test_iot_agent()
    test_iot_agent_async()
