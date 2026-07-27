import json
import re
import uuid
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterator
from flask import (
    Flask,
    Response,
    jsonify,
    render_template_string,
    request,
    send_file,
    stream_with_context,
)
from flask_cors import CORS
from langchain_core.messages import (
    AIMessage,
    AIMessageChunk,
    HumanMessage,
    HumanMessageChunk,
    ToolMessage,
    message_chunk_to_message,
    messages_to_dict,
)
from dotenv import load_dotenv

load_dotenv()
from services.iot_agent import iot_agent
from services.ali_iot_tools import TOOL_NAME_CN

app = Flask(__name__, static_folder="static", static_url_path="/static")
CORS(app)

sessions: dict[str, Any] = defaultdict(list)

# 会话内容落盘目录: 每个会话一个 JSON 文件, 路径 data/chat/<sid>.json
CHAT_DIR = Path(__file__).parent / "data" / "chat"
# 仪表盘 HTML 文件目录: 每个文件是一个独立仪表盘, /dashboard 页面列出它们
DASHBOARD_DIR = Path(__file__).parent / "static" / "dashboard"
_SAFE_SID = re.compile(r"^[A-Za-z0-9_-]{1,64}$")


def _content_to_str(content: Any) -> str:
    """把 LangChain 消息 content(str 或 list[dict]) 统一成可读字符串."""
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(
            p.get("text", "") if isinstance(p, dict) else str(p) for p in content
        )
    return str(content)


def _message_to_record(msg: Any) -> dict[str, Any]:
    """把单条消息转成可读字典, 保留工具调用的关键信息(name/args/id)."""
    if isinstance(msg, HumanMessage):
        return {"role": "user", "content": _content_to_str(msg.content)}
    if isinstance(msg, AIMessage):
        rec: dict[str, Any] = {
            "role": "assistant",
            "content": _content_to_str(msg.content),
        }
        if getattr(msg, "tool_calls", None):
            rec["tool_calls"] = [
                {"name": tc.get("name"), "args": tc.get("args"), "id": tc.get("id")}
                for tc in msg.tool_calls
            ]
        return rec
    if isinstance(msg, ToolMessage):
        return {
            "role": "tool",
            "name": getattr(msg, "name", None),
            "tool_call_id": getattr(msg, "tool_call_id", None),
            "content": _content_to_str(msg.content),
        }
    return {
        "role": type(msg).__name__,
        "content": _content_to_str(getattr(msg, "content", "")),
    }


def _save_session(sid: str, messages: list[Any]) -> None:
    """把会话完整历史写入 data/chat/<sid>.json, 一会话一文件.

    每轮对话结束后整体覆写, 文件始终反映会话最新状态; 先写临时文件再原子重命名,
    避免写一半崩溃产生损坏文件. sid 仅作文件名, 校验为安全字符以防路径穿越.
    """
    if not _SAFE_SID.match(sid):
        return
    CHAT_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "session_id": sid,
        "updated_at": datetime.now().isoformat(timespec="seconds"),
        "messages": [_message_to_record(m) for m in messages],
    }
    target = CHAT_DIR / f"{sid}.json"
    tmp = target.with_name(target.name + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(target)


def _delete_session_file(sid: str) -> None:
    """删除会话对应的落盘文件, 与内存会话生命周期保持一致."""
    if not _SAFE_SID.match(sid):
        return
    (CHAT_DIR / f"{sid}.json").unlink(missing_ok=True)


def _record_to_message(rec: Any) -> Any:
    """把落盘的可读记录还原成 LangChain 消息, 保留工具调用配对关系."""
    if not isinstance(rec, dict):
        return HumanMessage(content=str(rec))
    role = rec.get("role")
    content = rec.get("content", "")
    if role == "assistant":
        return AIMessage(content=content, tool_calls=rec.get("tool_calls") or [])
    if role == "tool":
        return ToolMessage(
            content=content,
            name=rec.get("name"),
            tool_call_id=rec.get("tool_call_id"),
        )
    # user 及未知类型一律按用户消息兜底
    return HumanMessage(content=content)


def _load_session(sid: str) -> list[Any]:
    """从 data/chat/<sid>.json 读取并还原会话历史.

    文件不存在或解析失败时返回空列表, 调用方据此把(可能为空的)会话放入内存.
    """
    if not _SAFE_SID.match(sid):
        return []
    f = CHAT_DIR / f"{sid}.json"
    if not f.exists():
        return []
    try:
        data = json.loads(f.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []
    if not isinstance(data, dict):
        return []
    return [_record_to_message(r) for r in data.get("messages", [])]


@app.get("/api/health")
def health():
    return jsonify(status="ok")


@app.get("/api/sessions")
def list_sessions():
    return jsonify(sessions=list(sessions.keys()))


@app.post("/api/sessions")
def create_session():
    sid = uuid.uuid4().hex[:10]
    sessions[sid] = []
    return jsonify(session_id=sid)


@app.delete("/api/sessions/<sid>")
def delete_session(sid):
    sessions.pop(sid, None)
    _delete_session_file(sid)
    return jsonify(ok=True)


@app.get("/api/sessions/<sid>/messages")
def get_messages(sid):
    return jsonify(messages=messages_to_dict(sessions.get(sid, [])))


@app.delete("/api/sessions/<sid>/messages")
def reset_messages(sid):
    if sid in sessions:
        sessions[sid] = []
        _save_session(sid, sessions[sid])
    return jsonify(ok=True)


def _lookup_tool_args(
        ai_chunks: dict[str, AIMessageChunk], tool_call_id: str | None
) -> Any:
    """根据 tool_call_id 在已累积的 AIMessageChunk 中查找工具调用的输入参数.

    流式 AIMessageChunk 的 tool_call_chunks 是分片到达的, 累积合并后才能得到
    完整的 tool_calls, 再按 tool_call_id 与 ToolMessage 的输出对应起来.
    """
    if not tool_call_id:
        return None
    for chunk in ai_chunks.values():
        for tc in getattr(chunk, "tool_calls", None) or []:
            if isinstance(tc, dict) and tc.get("id") == tool_call_id:
                return tc.get("args")
    return None


def _ready_tool_calls(message: Any) -> list[dict[str, Any]]:
    """从累积的 AIMessageChunk 中提取"参数已流式完整"的工具调用, 供尽早播报.

    流式工具调用的 args 是分片到达的, 在拼成合法 JSON 之前 ``tool_calls`` 会把
    args 误报成空 ``{}``, 不能据此判断完成. 这里按 index 拼接原始 args 字符串,
    以"能解析为合法 JSON"作为完成信号(无参工具的 ``"{}"`` 同样命中), 返回
    ``[{"id", "name", "input"}]``, ``input`` 为解析后的参数 dict.
    """
    ready: list[dict[str, Any]] = []
    by_idx: dict[Any, dict[str, Any]] = {}
    for tc in getattr(message, "tool_call_chunks", None) or []:
        idx = tc.get("index", 0) if isinstance(tc, dict) else getattr(tc, "index", 0)
        name = tc.get("name") if isinstance(tc, dict) else getattr(tc, "name", None)
        cid = tc.get("id") if isinstance(tc, dict) else getattr(tc, "id", None)
        frag = (tc.get("args") if isinstance(tc, dict) else getattr(tc, "args", None)) or ""
        entry = by_idx.setdefault(idx, {"id": None, "name": None, "raw": ""})
        if name:
            entry["name"] = name
        if cid:
            entry["id"] = cid
        entry["raw"] += frag
    if by_idx:
        for entry in by_idx.values():
            cid = entry["id"]
            if not cid or not entry["raw"].strip():
                continue
            try:
                parsed = json.loads(entry["raw"])
            except (ValueError, TypeError):
                continue  # args 仍在流式, 尚未拼成合法 JSON
            ready.append({"id": cid, "name": entry["name"] or "工具", "input": parsed})
        return ready
    # 兜底: 非流式模型 tool_call_chunks 为空, tool_calls 已是完整解析结果
    for tc in getattr(message, "tool_calls", None) or []:
        cid = tc.get("id") if isinstance(tc, dict) else None
        if not cid:
            continue
        ready.append({
            "id": cid,
            "name": (tc.get("name") if isinstance(tc, dict) else None) or "工具",
            "input": tc.get("args") if isinstance(tc, dict) else None,
        })
    return ready


def stream_agent(sid: str, content: str) -> Iterator[dict[str, Any]]:
    history = sessions.get(sid, [])
    user_msg = HumanMessage(content=content)
    payload = {"messages": history + [user_msg]}
    final_parts: list[str] = []
    ai_chunks: dict[str, AIMessageChunk] = {}
    # 按到达顺序记录本轮消息, 用于把完整的工具调用过程写回多轮历史
    seq: list[tuple[str, Any]] = []
    seen_ai: set[str] = set()
    emitted_tool_calls: set[str] = set()  # 已向前端播报过"调用入参"的工具调用 id

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
                # 累积分片还原完整 AIMessage(含 tool_calls): 既用于回查工具入参,
                # 也用于把工具调用过程写回历史, 否则下一轮拿不到工具返回的数据
                mid = getattr(msg, "id", None) or "_anon"
                if isinstance(msg, AIMessageChunk):
                    ai_chunks[mid] = (ai_chunks[mid] + msg) if mid in ai_chunks else msg
                else:
                    ai_chunks[mid] = msg
                if mid not in seen_ai:
                    seen_ai.add(mid)
                    seq.append(("ai", mid))
                # 工具调用参数一旦流式完整, 立即把"调用入参"推给前端,
                # 不必等工具执行完才看到这次工具调用
                for tc in _ready_tool_calls(ai_chunks[mid]):
                    if tc["id"] in emitted_tool_calls:
                        continue
                    emitted_tool_calls.add(tc["id"])
                    yield {
                        "type": "tool_call",
                        "id": tc["id"],
                        "name": tc["name"],
                        "name_cn": TOOL_NAME_CN.get(tc["name"], tc["name"]),
                        "input": tc["input"],
                    }

            elif isinstance(msg, ToolMessage):
                name = getattr(msg, "name", "tool") or "工具调用"
                tc = getattr(msg, "content", "")
                try:
                    parsed = json.loads(tc) if isinstance(tc, str) else tc
                    summary = parsed if isinstance(parsed, (list, dict)) else tc
                except Exception:
                    summary = tc
                seq.append(("tool", msg))
                call_id = getattr(msg, "tool_call_id", None)
                yield {
                    "type": "tool_result",
                    "id": call_id,
                    "name": name,
                    "name_cn": TOOL_NAME_CN.get(name, name),
                    "input": _lookup_tool_args(ai_chunks, call_id),
                    "content": summary,
                }

            elif isinstance(msg, (HumanMessage, HumanMessageChunk)):
                continue
    except Exception as e:
        yield {"type": "error", "content": f"调用失败: {e}"}
        return

    # 还原本轮完整消息序列(AIMessage 含 tool_calls + ToolMessage)写入历史.
    # 旧实现只存最终文本, 工具返回的原始数据全部丢失, 导致多轮会话失忆.
    new_messages: list[Any] = []
    for kind, key in seq:
        if kind == "ai":
            m = ai_chunks[key]
            new_messages.append(
                message_chunk_to_message(m) if isinstance(m, AIMessageChunk) else m
            )
        else:
            new_messages.append(key)

    final_text = "".join(final_parts)
    history.append(user_msg)
    history.extend(new_messages)
    sessions[sid] = history
    _save_session(sid, history)

    yield {"type": "message_end", "content": final_text}


def _sse(event: str, data: Any) -> str:
    """格式化一条 SSE 事件: event: xxx\\ndata: json\\n\\n"""
    payload = json.dumps(data, ensure_ascii=False) if not isinstance(data, str) else data
    return f"event: {event}\ndata: {payload}\n\n"


@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    content = (data.get("content") or "").strip()
    if not content:
        def empty() -> Iterator[str]:
            yield _sse("error", {"content": "内容不能为空"})
            yield _sse("done", "")

        return Response(
            stream_with_context(empty()),
            content_type="text/event-stream",
            headers={"Cache-Control": "no-cache", "X-Accel-Buffering": "no"},
        )

    sid = data.get("session_id")
    if not sid:
        sid = uuid.uuid4().hex[:10]
    if sid not in sessions:
        # 内存中没有则尝试从落盘文件恢复, 找不到文件时 _load_session 返回空列表
        sessions[sid] = _load_session(sid)

    def event_stream() -> Iterator[str]:
        yield _sse("session", {"type": "session", "session_id": sid})
        for evt in stream_agent(sid, content):
            yield _sse(evt["type"], evt)
        yield _sse("done", "")

    return Response(
        stream_with_context(event_stream()),
        content_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "X-Accel-Buffering": "no",
            "Connection": "keep-alive",
        },
    )


@app.route("/")
def index():
    return send_file(Path(__file__).parent / "static" / "index.html")


# 仪表盘页面: 列出 static/dashboard 下的 HTML 仪表盘, 按创建时间倒序, 显示文件名(无后缀)与创建时间
DASHBOARD_HTML = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>会话仪表盘</title>
  <style>
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: -apple-system, "Segoe UI", "Microsoft YaHei", sans-serif;
      background: #f5f7fa;
      color: #333;
    }
    .container { max-width: 820px; margin: 40px auto; padding: 0 20px; }
    h1 { font-size: 24px; margin: 0 0 8px; }
    .sub { color: #888; margin-bottom: 24px; font-size: 14px; }
    table {
      width: 100%;
      border-collapse: collapse;
      background: #fff;
      border-radius: 8px;
      overflow: hidden;
      box-shadow: 0 1px 3px rgba(0, 0, 0, .08);
    }
    th, td { padding: 12px 16px; text-align: left; border-bottom: 1px solid #eee; }
    th { background: #fafbfc; font-weight: 600; color: #555; font-size: 14px; }
    td { font-size: 14px; }
    tbody tr:last-child td { border-bottom: none; }
    tbody tr:hover { background: #f9f9fb; }
    td.idx { color: #aaa; width: 48px; }
    td.time { color: #666; white-space: nowrap; }
    .empty { text-align: center; color: #aaa; padding: 48px; background: #fff; border-radius: 8px; }
    td.name a { color: #2563eb; text-decoration: none; }
    td.name a:hover { text-decoration: underline; }
  </style>
</head>
<body>
  <div class="container">
    <h1>仪表盘列表</h1>
    <div class="sub">共 {{ items|length }} 个仪表盘, 按创建时间倒序</div>
    {% if items %}
    <table>
      <thead>
        <tr><th>#</th><th>文件名</th><th>创建时间</th></tr>
      </thead>
      <tbody>
        {% for item in items %}
        <tr>
          <td class="idx">{{ loop.index }}</td>
          <td class="name"><a href="{{ url_for('static', filename='dashboard/' ~ item.file) }}" target="_blank">{{ item.name }}</a></td>
          <td class="time">{{ item.ctime_str }}</td>
        </tr>
        {% endfor %}
      </tbody>
    </table>
    {% else %}
      <div class="empty">暂无仪表盘</div>
    {% endif %}
  </div>
</body>
</html>
"""


@app.get("/dashboard")
def dashboard():
    """仪表盘索引: 扫描 static/dashboard/*.html, 显示文件名(无后缀)与创建时间, 按创建时间倒序.

    每个 HTML 文件是一个独立仪表盘, 文件名链接到该仪表盘页面.
    """
    DASHBOARD_DIR.mkdir(parents=True, exist_ok=True)
    items: list[dict[str, Any]] = []
    for f in DASHBOARD_DIR.glob("*.html"):
        try:
            ctime = f.stat().st_ctime
        except OSError:
            continue
        items.append({
            "name": f.stem,
            "file": f.name,
            "ctime": ctime,
            "ctime_str": datetime.fromtimestamp(ctime).strftime("%Y-%m-%d %H:%M:%S"),
        })
    items.sort(key=lambda x: x["ctime"], reverse=True)
    return render_template_string(DASHBOARD_HTML, items=items)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8100)
