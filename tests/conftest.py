import sys

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(autouse=True)
def _isolate_chat_dir(tmp_path, monkeypatch):
    """把 agent_server 的会话落盘目录重定向到临时目录, 避免测试污染 data/chat.

    仅当 agent_server 已被当前测试套件导入时生效, 不影响不依赖它的测试.
    """
    if "agent_server" in sys.modules:
        monkeypatch.setattr(sys.modules["agent_server"], "CHAT_DIR", tmp_path)
