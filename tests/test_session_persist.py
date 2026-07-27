"""会话内容落盘测试: 每轮对话结束后把完整历史写入 data/chat/<sid>.json, 一会话一文件.

CHAT_DIR 已由 conftest 的 _isolate_chat_dir 重定向到 tmp_path, 故此处直接用 tmp_path.
"""
import json
from unittest.mock import patch

from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import AIMessage, AIMessageChunk, HumanMessage, ToolMessage

import agent_server


def _fake_stream(_payload, config=None, stream_mode="messages"):
    yield (AIMessageChunk(id="m1", content="hello"), {})


def test_session_saved_to_file(tmp_path):
    sid = "test-persist"
    agent_server.sessions[sid] = []

    with patch.object(agent_server.iot_agent, "stream", _fake_stream):
        list(agent_server.stream_agent(sid, "你好"))

    f = tmp_path / f"{sid}.json"
    assert f.exists(), "会话文件未生成"
    data = json.loads(f.read_text(encoding="utf-8"))
    assert data["session_id"] == sid
    assert data["updated_at"], "缺少 updated_at"
    roles = [m["role"] for m in data["messages"]]
    assert roles == ["user", "assistant"], roles
    assert data["messages"][0]["content"] == "你好"
    assert data["messages"][1]["content"] == "hello"


def test_load_session_reconstructs_tool_calls(tmp_path):
    """_load_session 应还原工具调用配对: AIMessage(tool_calls) -> ToolMessage -> AIMessage."""
    sid = "test-load"
    (tmp_path / f"{sid}.json").write_text(
        json.dumps(
            {
                "session_id": sid,
                "updated_at": "2026-08-02T00:00:00",
                "messages": [
                    {"role": "user", "content": "查看在线设备"},
                    {
                        "role": "assistant",
                        "content": "",
                        "tool_calls": [{"name": "deviceList", "args": {}, "id": "c1"}],
                    },
                    {
                        "role": "tool",
                        "name": "deviceList",
                        "tool_call_id": "c1",
                        "content": '[{"iotId":"dev1"}]',
                    },
                    {"role": "assistant", "content": "当前有1台设备"},
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    msgs = agent_server._load_session(sid)
    assert len(msgs) == 4
    assert isinstance(msgs[0], HumanMessage)
    assert isinstance(msgs[1], AIMessage)
    assert msgs[1].tool_calls[0]["name"] == "deviceList"
    assert msgs[1].tool_calls[0]["id"] == "c1"
    assert isinstance(msgs[2], ToolMessage)
    assert msgs[2].tool_call_id == "c1"
    assert msgs[2].name == "deviceList"
    assert isinstance(msgs[3], AIMessage)
    assert msgs[3].content == "当前有1台设备"


def test_load_session_missing_file_returns_empty(tmp_path):
    """文件不存在时 _load_session 返回空列表, 不抛异常."""
    assert agent_server._load_session("no-such-sid") == []


def test_chat_loads_missing_session_from_file(tmp_path):
    """聊天时 sid 不在内存则从文件加载历史, 并连同本轮一起传给 agent."""
    sid = "test-chat-load"
    (tmp_path / f"{sid}.json").write_text(
        json.dumps(
            {
                "session_id": sid,
                "updated_at": "2026-08-02T00:00:00",
                "messages": [
                    {"role": "user", "content": "之前的问题"},
                    {"role": "assistant", "content": "之前的回答"},
                ],
            },
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    agent_server.sessions.pop(sid, None)

    captured = []

    def fake_stream(payload, config=None, stream_mode="messages"):
        captured.append(payload)
        yield (AIMessageChunk(id="m1", content="ok"), {})

    client = agent_server.app.test_client()
    with patch.object(agent_server.iot_agent, "stream", fake_stream):
        resp = client.post(
            "/api/chat",
            json={"content": "继续", "session_id": sid},
            buffered=False,
        )
        resp.get_data()  # 消费 SSE 流, 触发 stream_agent 执行

    msgs = captured[0]["messages"]
    # 文件里 2 条历史 + 本轮 user = 3 条
    assert len(msgs) == 3, [type(m).__name__ for m in msgs]
    assert isinstance(msgs[0], HumanMessage) and msgs[0].content == "之前的问题"
    assert isinstance(msgs[1], AIMessage) and msgs[1].content == "之前的回答"
    assert isinstance(msgs[2], HumanMessage) and msgs[2].content == "继续"


if __name__ == "__main__":
    import tempfile
    from pathlib import Path

    with tempfile.TemporaryDirectory() as d:
        orig = agent_server.CHAT_DIR
        agent_server.CHAT_DIR = Path(d)
        try:
            test_session_saved_to_file(Path(d))
        finally:
            agent_server.CHAT_DIR = orig
    print("PASS: 会话内容已落盘")
