"""多轮会话历史累积的单元测试.

用 mock 替换 iot_agent.stream, 模拟一轮带工具调用的对话, 验证:
1. 本轮产生的完整消息(AIMessage 含 tool_calls + ToolMessage + 最终 AIMessage)被写回历史;
2. 下一轮发起时, 传入 agent 的 payload 携带了上一轮的工具调用历史.
旧实现只存最终文本, 工具返回的原始数据会丢失, 这是多轮会话"失忆"的根因.
"""

from unittest.mock import patch

from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import (
    AIMessage,
    AIMessageChunk,
    HumanMessage,
    ToolMessage,
)

import agent_server


def _round1(_payload):
    """模拟工具调用: AIMessage(tool_calls) -> ToolMessage -> 最终 AIMessage(文本)."""
    yield (
        AIMessageChunk(
            id="m1",
            content="",
            tool_call_chunks=[
                {"name": "deviceList", "args": "", "id": "c1", "index": 0, "type": "tool_call_chunk"},
            ],
        ),
        {"langgraph_node": "agent"},
    )
    yield (
        AIMessageChunk(
            id="m1",
            content="",
            tool_call_chunks=[
                {"name": None, "args": "{}", "id": "c1", "index": 0, "type": "tool_call_chunk"},
            ],
        ),
        {"langgraph_node": "agent"},
    )
    yield (
        ToolMessage(
            content='[{"iotId": "dev1", "name": "小车"}]',
            tool_call_id="c1",
            name="deviceList",
        ),
        {"langgraph_node": "tools"},
    )
    yield (AIMessageChunk(id="m2", content="当前有1台设备: 小车"), {"langgraph_node": "agent"})


def _round2(_payload):
    """第二轮不调工具, 仅返回文本."""
    yield (AIMessageChunk(id="m3", content="小车状态正常"), {"langgraph_node": "agent"})


def _make_stream(responder, captured):
    def _stream(payload, config=None, stream_mode="messages"):
        captured.append(payload)
        return responder(payload)

    return _stream


def test_multi_turn_history_preserves_tool_calls():
    sid = "test-multi-turn"
    agent_server.sessions[sid] = []
    captured = []

    # ---- 第一轮: 带工具调用 ----
    with patch.object(agent_server.iot_agent, "stream", _make_stream(_round1, captured)):
        events = list(agent_server.stream_agent(sid, "查看在线设备"))

    # SSE 事件: 有 delta 和 message_end
    assert any(e["type"] == "delta" for e in events)
    assert any(e["type"] == "message_end" for e in events)
    # 工具调用拆成两段事件: 入参先到(tool_call), 输出后到(tool_result)
    call_ev = next(e for e in events if e["type"] == "tool_call")
    assert call_ev["name"] == "deviceList"
    assert call_ev["id"] == "c1"
    result_ev = next(e for e in events if e["type"] == "tool_result")
    assert result_ev["name"] == "deviceList"
    assert result_ev["id"] == "c1"
    # tool_call 必须早于 tool_result: 不必等工具执行完即可看到这次调用
    assert events.index(call_ev) < events.index(result_ev)
    # 输出只随 tool_result 给出, tool_call 不带 content
    assert "content" in result_ev
    assert "content" not in call_ev

    history = agent_server.sessions[sid]
    kinds = [type(m).__name__ for m in history]
    # 期望: 用户消息 -> AI(含 tool_calls) -> Tool -> AI(最终文本)
    assert kinds == ["HumanMessage", "AIMessage", "ToolMessage", "AIMessage"], kinds

    # 第一条 AIMessage 必须保留 tool_calls, 否则下一轮 OpenAI 兼容接口会因
    # 缺少配对的 assistant tool_calls 而报错, 且模型拿不到工具调用上下文.
    ai_with_tc = history[1]
    assert ai_with_tc.tool_calls, "AIMessage 丢失了 tool_calls"
    assert ai_with_tc.tool_calls[0]["name"] == "deviceList"
    assert ai_with_tc.tool_calls[0]["id"] == "c1"

    # ToolMessage 保留 tool_call_id 与上一条 AI 配对
    assert history[2].tool_call_id == "c1"
    # 最终 AI 文本
    assert history[3].content == "当前有1台设备: 小车"

    # ---- 第二轮: 验证上一轮的工具调用历史被带上 ----
    with patch.object(agent_server.iot_agent, "stream", _make_stream(_round2, captured)):
        list(agent_server.stream_agent(sid, "小车信号如何"))

    # 第二次调用 agent 时传入的 messages
    second_payload = captured[-1]
    msgs = second_payload["messages"]

    # 上一轮的 4 条历史 + 本轮 user = 5 条
    assert len(msgs) == 5, [type(m).__name__ for m in msgs]
    # 关键: 工具调用消息仍在历史中(旧实现这里只剩纯文本 user/assistant)
    assert any(isinstance(m, ToolMessage) for m in msgs), "工具历史未带入第二轮"
    assert any(
        isinstance(m, AIMessage) and m.tool_calls for m in msgs
    ), "tool_calls 未带入第二轮"
    # 最后一条是本轮 user
    assert isinstance(msgs[-1], HumanMessage)
    assert msgs[-1].content == "小车信号如何"


if __name__ == "__main__":
    test_multi_turn_history_preserves_tool_calls()
    print("PASS: 多轮会话历史累积正确")
