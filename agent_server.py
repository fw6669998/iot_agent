import asyncio
import json
import uuid
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterator

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, StreamingResponse
from fastapi.staticfiles import StaticFiles
from langchain_core.messages import AIMessage, AIMessageChunk, HumanMessage, HumanMessageChunk, ToolMessage
from pydantic import BaseModel

from services.iot_agent import iot_agent

app = FastAPI(title="IoT Agent Chat")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

sessions: dict[str, Any] = defaultdict(list)


@app.get("/api/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/api/sessions")
async def list_sessions() -> dict[str, list[str]]:
    return {"sessions": list(sessions.keys())}


@app.post("/api/sessions")
async def create_session() -> dict[str, str]:
    sid = uuid.uuid4().hex[:10]
    sessions[sid] = []
    return {"session_id": sid}


@app.delete("/api/sessions/{sid}")
async def delete_session(sid: str) -> dict[str, bool]:
    sessions.pop(sid, None)
    return {"ok": True}


@app.get("/api/sessions/{sid}/messages")
async def get_messages(sid: str) -> dict[str, Any]:
    return {"messages": sessions.get(sid, [])}


@app.delete("/api/sessions/{sid}/messages")
async def reset_messages(sid: str) -> dict[str, bool]:
    if sid in sessions:
        sessions[sid] = []
    return {"ok": True}


class ChatRequest(BaseModel):
    content: str
    session_id: str | None = None


def stream_agent(sid: str, content: str) -> Iterator[dict[str, Any]]:
    history = sessions.get(sid, [])
    payload = {"messages": history + [{"role": "user", "content": content}]}
    final_parts: list[str] = []

    try:
        for msg, _meta in iot_agent.stream(
                payload, {"configurable": {}}, stream_mode="messages"
        ):
            if isinstance(msg, (AIMessage, AIMessageChunk)):
                chunk = getattr(msg, "content", "")
                if isinstance(chunk, list):
                    chunk = "".join(
                        p.get("text", "") if isinstance(p, dict) else str(p)
                        for p in chunk
                    )
                if isinstance(chunk, str) and chunk:
                    final_parts.append(chunk)
                    yield {"type": "delta", "content": chunk}

            elif isinstance(msg, ToolMessage):
                name = getattr(msg, "name", "tool") or "工具调用"
                tc = getattr(msg, "content", "")
                try:
                    parsed = json.loads(tc) if isinstance(tc, str) else tc
                    summary = parsed if isinstance(parsed, (list, dict)) else tc
                except Exception:
                    summary = tc
                yield {"type": "tool", "name": name, "content": summary}

            elif isinstance(msg, (HumanMessage, HumanMessageChunk)):
                continue
    except Exception as e:
        yield {"type": "error", "content": f"调用模型失败: {e}"}
        return

    final_text = "".join(final_parts)
    history.append({"role": "user", "content": content})
    history.append({"role": "assistant", "content": final_text})
    sessions[sid] = history

    yield {"type": "message_end", "content": final_text}


@app.post("/api/chat")
async def chat(req: ChatRequest) -> StreamingResponse:
    content = req.content.strip()
    if not content:
        def empty() -> Iterator[str]:
            yield _ndjson({"type": "error", "content": "内容不能为空"})
            yield _ndjson({"type": "done"})

        return StreamingResponse(
            empty(),
            media_type="application/x-ndjson",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    sid = req.session_id
    if not sid:
        sid = uuid.uuid4().hex[:10]
    if sid not in sessions:
        sessions[sid] = []

    def event_stream() -> Iterator[str]:
        yield _ndjson({"type": "session", "session_id": sid})
        for evt in stream_agent(sid, content):
            yield _ndjson(evt)
        yield _ndjson({"type": "done"})

    return StreamingResponse(
        event_stream(),
        media_type="application/x-ndjson",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Connection": "keep-alive",
        },
    )


def _ndjson(obj: dict[str, Any]) -> str:
    return json.dumps(obj, ensure_ascii=False) + "\r\n"


app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent / "static"),
    name="static",
)


@app.get("/")
async def index() -> FileResponse:
    return FileResponse(Path(__file__).parent / "static" / "index.html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
