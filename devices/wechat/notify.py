"""
notify.py - 企业微信主动通知接口(供其他程序调用)

其他程序调用本模块的函数,把消息写入 msg_transfer.txt;
wechat.py 的后台任务会轮询该文件,通过 WebSocket 主动推送到企业微信。
跨进程通信,无需共享内存或事件循环。

用法:
    from wechat.notify import notify, send_markdown, send_message
    notify('打印完成: report.pdf')
    send_markdown('zhangsan', '## 提醒\n下午3点开会')
"""

import json
import os

# 通信中转文件(与 wechat.py 共享同一路径)
TRANSFER_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "msg_transfer.txt"
)

# 默认通知目标:单聊填用户 userid,群聊填群 chatid
DEFAULT_CHATID = "wr3o6IOgAA-Ht8y_sgCsCiEzJiO4DHWA"  # TODO: 改成你的企业微信 userid(注意通常不是手机号)


def _append(message: dict) -> None:
    """追加一条消息到中转文件(JSON Lines 格式,每行一条 JSON)。"""
    with open(TRANSFER_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(message, ensure_ascii=False) + "\n")


def send_message(chatid: str, body: dict) -> None:
    """底层接口:发送任意格式的企业微信消息(经文件中转,由 wechat.py 异步发出)。

    :param chatid: 单聊填用户 userid,群聊填群 chatid
    :param body:   企业微信消息体,例如
                    {'msgtype': 'markdown', 'markdown': {'content': '...'}}
    """
    _append({"chatid": chatid, "body": body})


def send_markdown(chatid: str, content: str) -> None:
    """发送 markdown 消息。"""
    send_message(chatid, {"msgtype": "markdown", "markdown": {"content": content}})


def notify(content: str, chatid: str = DEFAULT_CHATID) -> None:
    """快捷方法:向默认接收人发送一条 markdown 通知。"""
    send_markdown(chatid, content)


if __name__ == "__main__":
    notify("哈哈哈哈")  # 个人
    # notify('哈哈哈哈__', contacts.get_groups()['AI部门群'])  # 群
    pass
