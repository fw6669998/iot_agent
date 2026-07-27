import asyncio
import json
import os
from datetime import datetime
import aiohttp
from aibot import WSClient, WSClientOptions, generate_req_id
from dotenv import load_dotenv

load_dotenv()

WECHAT_BOT_ID = os.getenv('WECHAT_BOT_ID')
WECHAT_BOT_SECRET = os.getenv('WECHAT_BOT_SECRET')
NOTIFIER_USER_ID = os.getenv('NOTIFIER_USER_ID')

# agent_server 聊天接口(同机默认 8100 端口): 收到文本消息后调用其获取回复
CHAT_API_URL = os.getenv('CHAT_API_URL', 'http://localhost:8100/api/chat')

# 主动消息中转文件(与 notify.py 共享同一路径)
# 其他程序通过 notify.py 写入,本程序轮询读取后经 WebSocket 主动推送
TRANSFER_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'msg_transfer.txt')
TRANSFER_POLL_INTERVAL = 1  # 轮询间隔(秒)


class FileObj:
    recent_file_path = ''


# 1. 创建客户端实例
ws_client = WSClient(
    WSClientOptions(
        bot_id=WECHAT_BOT_ID,  # 企业微信后台获取的机器人 ID
        secret=WECHAT_BOT_SECRET,  # 企业微信后台获取的机器人 Secret
    )
)


# 2. 监听认证成功
@ws_client.on('authenticated')
def on_authenticated():
    print('🔐 认证成功')


# 3. 监听文本消息: 调用 agent_server 聊天接口获取回复并流式返回
async def _chat_reply(content: str) -> str:
    """调用 /api/chat 接口获取回复, 消费 SSE 流并返回最终文本.

    /api/chat 以 Server-Sent Events 流式返回, 主要事件:
      delta        增量文本片段
      message_end  完整最终文本(命中即直接返回)
      error        服务端出错
      done         流结束
    出错或无内容时返回带 ⚠️ 前缀的提示, 便于在微信端直接展示.
    """
    parts: list[str] = []
    try:
        timeout = aiohttp.ClientTimeout(total=120)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            async with session.post(CHAT_API_URL, json={'content': content}) as resp:
                resp.raise_for_status()
                # SSE 事件之间以空行(\n\n)分隔, 按块累积解析
                buffer = ''
                async for chunk in resp.content.iter_any():
                    buffer += chunk.decode('utf-8', errors='replace')
                    while '\n\n' in buffer:
                        block, buffer = buffer.split('\n\n', 1)
                        event_type, data_str = '', ''
                        for line in block.split('\n'):
                            if line.startswith('event: '):
                                event_type = line[len('event: '):].strip()
                            elif line.startswith('data: '):
                                data_str = line[len('data: '):]
                        if event_type == 'done' or not data_str:
                            continue
                        try:
                            evt = json.loads(data_str)
                        except json.JSONDecodeError:
                            continue
                        etype = evt.get('type', event_type)
                        if etype == 'delta':
                            parts.append(evt.get('content', ''))
                        elif etype == 'message_end':
                            final = evt.get('content')
                            if final:
                                return final
                        elif etype == 'error':
                            return f'⚠️ {evt.get("content", "服务异常")}'
    except Exception as e:
        return f'⚠️ 调用聊天服务失败: {e}'

    return ''.join(parts).strip() or '⚠️ 未收到回复'


@ws_client.on('message.text')
async def on_text(frame):
    content = frame.get('body', {}).get('text', {}).get('content', '')
    if FileObj.recent_file_path:
        content = f'{content}\n\n文件路径: {FileObj.recent_file_path}'
        FileObj.recent_file_path = None
    print(f'收到消息: {content}')

    stream_id = generate_req_id('stream')

    # 先回复"正在思考", 给用户即时反馈
    await ws_client.reply_stream(frame, stream_id, '正在思考中...', False)

    # 调用 agent 聊天接口获取回复
    reply = await _chat_reply(content)

    # 发送最终结果
    await ws_client.reply_stream(frame, stream_id, reply, True)


# 4. 监听文件消息并下载到本地
@ws_client.on('message.file')
async def on_file(frame):
    body = frame.get('body', {})
    file_info = body.get('file', {})
    # 下载链接字段名可能是 file_url 或 url，兼容处理
    file_url = file_info.get('file_url') or file_info.get('url')
    aes_key = file_info.get('aeskey')

    if not file_url:
        print('⚠️ 文件消息缺少下载链接，跳过下载')
        return

    print(f'收到文件: {file_info.get("filename") or "未知文件名"}，开始下载...')

    try:
        # 内部完成 HTTP 下载 + AES-256-CBC 解密，返回 (数据, 文件名)
        data, filename = await ws_client.download_file(file_url, aes_key)
    except Exception as e:
        print(f'❌ 文件下载失败: {e}')
        return

    # 文件名优先取消息体，其次取下载响应头，最后使用默认名
    save_name = file_info.get('filename') or filename or '未命名文件'

    # 文件名前加秒级时间戳，避免同名文件覆盖
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    save_name = f'{timestamp}_{os.path.basename(save_name)}'

    # 保存到脚本同级的 downloads 目录
    download_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'downloads')
    os.makedirs(download_dir, exist_ok=True)
    save_path = os.path.join(download_dir, save_name)

    FileObj.recent_file_path = save_path

    with open(save_path, 'wb') as f:
        f.write(data)

    print(f'✅ 文件已保存: {save_path}（{len(data)} bytes）')

    # 回复发送者下载结果
    stream_id = generate_req_id('stream')
    await ws_client.reply_stream(
        frame, stream_id,
        f'✅ 已收到文件：{os.path.basename(save_path)}（{len(data)} bytes）',
        True,
    )


# 5. 监听进入会话事件（发送欢迎语）
@ws_client.on('event.enter_chat')
async def on_enter_chat(frame):
    await ws_client.reply_welcome(frame, {
        'msgtype': 'text',
        'text': {'content': '您好！我是智能助手，有什么可以帮您的吗？'},
    })


# 6. 后台轮询中转文件，主动推送消息
async def transfer_file_loop():
    """轮询 msg_transfer.txt，将其中的消息主动推送到企业微信。

    其他程序（如打印机 IoT）通过 notify.py 把消息写入该文件，
    本任务读取后调用 send_message 发送；发送失败的写回文件下一轮重试。
    """
    while True:
        await asyncio.sleep(TRANSFER_POLL_INTERVAL)
        try:
            with open(TRANSFER_FILE, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except FileNotFoundError:
            continue

        lines = [ln.strip() for ln in lines if ln.strip()]
        if not lines:
            continue

        # 先清空文件，避免下一轮重复发送；清空后新写入的消息会在下一轮处理
        try:
            open(TRANSFER_FILE, 'w', encoding='utf-8').close()
        except OSError:
            pass

        failed = []
        for ln in lines:
            try:
                msg = json.loads(ln)
                await ws_client.send_message(msg['chatid'], msg['body'])
                print(f'✅ 已主动推送 -> {msg.get("chatid")}')
            except Exception as e:
                print(f'❌ 推送失败，稍后重试: {e}')
                failed.append(ln)

        # 发送失败的消息写回，下一轮重试
        if failed:
            with open(TRANSFER_FILE, 'a', encoding='utf-8') as f:
                f.write('\n'.join(failed) + '\n')


async def main():
    await ws_client.connect()
    asyncio.create_task(transfer_file_loop())
    await asyncio.Event().wait()  # 保持运行


if __name__ == '__main__':
    # 7. 启动：建立连接 + 后台轮询主动推送
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        ws_client.disconnect()
