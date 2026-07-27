"""contacts.py - 企业微信通讯录管理

contacts.json 采用扁平结构 {id: name}:
    - 群聊 chatid 以 "wr" 开头, 例如 "wr3o6IOgAA-Ht8y_sgCsCiEzJiO4DHWA"
    - 用户 userid 为其余条目, 例如 "17320394612"

用法:
    from wechat import contacts
    contacts.add_contact('17320394612', '付伟')
    name = contacts.get_name('17320394612')
    chatid = contacts.get_groups()['AI部门群']
"""

import json
import os

# 通讯录文件(与本模块同级)
CONTACTS_FILE = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'contacts.json'
)

# 企业微信群聊 chatid 固定以 "wr" 开头,据此区分群聊与用户
_GROUP_PREFIX = 'wr'


def _load() -> dict:
    """读取通讯录;文件不存在或为空时返回空字典。"""
    try:
        with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    if not isinstance(data, dict):
        return {}
    return data


def _save(contacts: dict) -> None:
    """写回通讯录(覆盖式)。"""
    with open(CONTACTS_FILE, 'w', encoding='utf-8') as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)


def get_contacts() -> str:
    """返回全部通讯录 {id: name}。"""
    with open(CONTACTS_FILE, 'r', encoding='utf-8') as f:
                data = json.load(f)
    return data


def get_name(userid: str) -> str | None:
    """按 id 查询名称,找不到返回 None。"""
    return _load().get(userid)


def get_id(name: str) -> str | None:
    """按名称查询 id(首个匹配),找不到返回 None。"""
    for uid, nm in _load().items():
        if nm == name:
            return uid
    return None


def get_groups() -> dict:
    """返回全部群聊 {name: chatid}。"""
    return {
        name: chatid
        for chatid, name in _load().items()
        if chatid.startswith(_GROUP_PREFIX)
    }


def get_users() -> dict:
    """返回全部用户 {name: userid}。"""
    return {
        name: userid
        for userid, name in _load().items()
        if not userid.startswith(_GROUP_PREFIX)
    }


def add_contact(userid: str, name: str) -> str | None:
    """添加或更新联系人;返回被覆盖的旧名称(新增时为 None)。"""
    contacts = _load()
    old_name = contacts.get(userid)
    contacts[userid] = name
    _save(contacts)
    return old_name


def remove_contact(userid: str) -> str | None:
    """删除联系人;返回被删除的名称(不存在时为 None)。"""
    contacts = _load()
    name = contacts.pop(userid, None)
    if name is not None:
        _save(contacts)
    return name


if __name__ == '__main__':
    # 演示:打印当前通讯录与分组
    print('全部通讯录:', get_contacts())
    print('群聊:', get_groups())
    print('用户:', get_users())
