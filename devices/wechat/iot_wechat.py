import os, sys, json, time, asyncio, threading, logging

# 切到脚本目录,确保 wechat 模块的 load_dotenv 能找到 .env,且同级模块可导入
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(CUR_DIR)
sys.path.insert(0, CUR_DIR)

from linkkit import linkkit
import contacts
import notify
import wechat as wx

# 日志:同时写文件与控制台,每条带时间
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(CUR_DIR, 'iot_wechat.log'), encoding='utf-8'),
        logging.StreamHandler(),
    ],
)
log = logging.getLogger('iot_wechat')

_lock = threading.Lock()
last_props = {}


def read_props():
    """读取属性 contact(联系人):get_contacts 返回 {id:name},序列化为 TEXT(<=100)"""
    try:
        data = contacts.get_contacts() or {}
    except Exception as e:
        log.error("读取联系人失败: %s", e)
        return {}
    s = json.dumps(data, ensure_ascii=False)
    if len(s) > 100:
        s = s[:97] + '...'
    return {'contact': s}


def service_add_contact(params):
    """添加联系人:输入 userId、name"""
    uid = params.get('userId', '')
    name = params.get('name', '')
    old = contacts.add_contact(uid, name)
    log.info("添加联系人 userId=%s name=%s 覆盖旧名称=%s", uid, name, old)
    return 200, {}


def service_send_notification(params):
    """发送通知:输入 message、userId,经 notify 写入中转文件由 wechat 服务推送"""
    message = params.get('message', '')
    uid = params.get('userId', '')
    notify.notify(message, uid)
    log.info("发送通知 userId=%s message=%s", uid, message)
    return 200, {}


def on_thing_call_service(identifier, request_id, params, userdata):
    res = {}
    try:
        if identifier == 'add_contact':
            code, res = service_add_contact(params)
        elif identifier == 'send_notification':
            code, res = service_send_notification(params)
        else:
            code = 400
            log.warning("未知服务: %s", identifier)
    except Exception as e:
        code = 500
        log.exception("服务 %s 处理异常: %s", identifier, e)
    lk.thing_answer_service(identifier, request_id, code, res)


def on_connect(session_present, rc, userdata):
    if rc == 0:
        log.info("物联网平台连接成功 rc=%s", rc)
    else:
        log.error("物联网平台连接失败 rc=%s", rc)


def on_disconnect(rc, userdata):
    log.warning("物联网平台断开连接 rc=%s", rc)


def on_thing_enable(userdata):
    log.info("物模型已启用,可接收服务调用并上报属性")


def report_loop():
    """每 10s 检测一次,仅上报发生变化的属性"""
    while True:
        time.sleep(10)
        cur = read_props()
        with _lock:
            changed = {k: v for k, v in cur.items() if last_props.get(k) != v}
            if changed:
                lk.thing_post_property(changed)
                last_props.update(changed)
                log.info("上报变化属性: %s", changed)


def run_wechat():
    """独立线程运行企业微信服务(WebSocket 接收 + 主动推送轮询)"""
    try:
        asyncio.run(wx.main())
    except Exception as e:
        log.exception("企业微信服务异常: %s", e)


# 1. 连接云平台前先启动企业微信服务
log.info("启动企业微信服务...")
threading.Thread(target=run_wechat, daemon=True).start()
time.sleep(3)

# 2. 连接物联网云平台
lk = linkkit.LinkKit(
    host_name="cn-shanghai",
    product_key="a1td1VNnCDp",
    device_name="wxbotai",
    device_secret="63223925c1ac3dce46c92084335e85c1",
)
lk.on_connect = on_connect
lk.on_disconnect = on_disconnect
lk.on_thing_enable = on_thing_enable
lk.on_thing_call_service = on_thing_call_service
lk.thing_setup(os.path.join(CUR_DIR, "tsl.json"))
lk.connect_async()

threading.Thread(target=report_loop, daemon=True).start()
log.info("iot_wechat 启动完成,进入后台运行")

while True:
    time.sleep(1)
