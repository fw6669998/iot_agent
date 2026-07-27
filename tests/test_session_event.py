"""回归测试: session SSE 事件的 data 必须含 type='session'.

前端 handleEvent 用 switch(data.type) 分发, 若 session 事件 data 缺少 type 字段,
currentSession 永远不会更新, 导致每轮都新建 session、历史永远为空.
"""
import json
from unittest.mock import patch

from dotenv import load_dotenv

load_dotenv()

from langchain_core.messages import AIMessageChunk

import agent_server


def test_session_event_carries_type():
    def fake_stream(payload, config=None, stream_mode="messages"):
        yield (AIMessageChunk(id="m1", content="ok"), {})

    client = agent_server.app.test_client()
    with patch.object(agent_server.iot_agent, "stream", fake_stream):
        resp = client.post(
            "/api/chat",
            json={"content": "hi", "session_id": None},
            buffered=False,
        )

    text = resp.get_data(as_text=True)
    session_data = None
    for part in text.split("\n\n"):
        etype = ""
        data = ""
        for line in part.split("\n"):
            if line.startswith("event: "):
                etype = line[7:]
            elif line.startswith("data: "):
                data = line[6:]
        if etype == "session":
            session_data = json.loads(data)
            break

    assert session_data is not None, "未收到 session 事件"
    assert session_data.get("type") == "session", f"session 事件缺 type 字段: {session_data}"
    assert session_data.get("session_id"), "session 事件缺 session_id"


if __name__ == "__main__":
    test_session_event_carries_type()
    print("PASS: session 事件携带 type 字段")
