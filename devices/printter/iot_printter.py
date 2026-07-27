import time, threading, os, sys, logging

from linkkit import linkkit

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CUR_DIR)
from printer import print_file

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(os.path.join(CUR_DIR, "iot_printter.log"), encoding="utf-8"),
    ],
)
log = logging.getLogger("iot_printter")

last_props = {}
_lock = threading.Lock()


def read_props():
    # 打印机无上报属性, 返回空
    return {}


def service_print(params):
    filename = params.get("filename", "")
    if not filename:
        return 400, {"error": "filename为空"}
    # 相对路径基于脚本目录解析
    if not os.path.isabs(filename):
        filename = os.path.join(CUR_DIR, filename)
    log.info("开始打印文件: %s", filename)
    print_file(filename)
    log.info("打印完成: %s", filename)
    return 200, {}


def on_thing_call_service(identifier, request_id, params, userdata):
    res = {}
    try:
        log.info("收到服务调用: %s, params=%s", identifier, params)
        if identifier == "print":
            code, res = service_print(params)
        else:
            code = 400
            res = {"error": "未知服务: %s" % identifier}
    except FileNotFoundError as e:
        code, res = 404, {"error": str(e)}
        log.warning("文件不存在: %s", e)
    except Exception as e:
        code, res = 500, {"error": str(e)}
        log.exception("服务处理异常: %s", e)
    lk.thing_answer_service(identifier, request_id, code, res)


def on_connect(session_present, rc, userdata):
    if rc == 0:
        log.info("设备上线成功 (rc=%s)", rc)
    else:
        log.error("设备上线失败 (rc=%s)", rc)


def on_disconnect(rc, userdata):
    log.warning("设备断开连接 (rc=%s)", rc)


def report_loop():
    while True:
        time.sleep(10)
        cur = read_props()
        with _lock:
            changed = {k: v for k, v in cur.items() if last_props.get(k) != v}
            if changed:
                log.info("上报变化属性: %s", changed)
                lk.thing_post_property(changed)
                last_props.update(changed)


lk = linkkit.LinkKit(
    host_name="cn-shanghai",
    product_key="a1OAJSvGyYP",
    device_name="printer1",
    device_secret="7808236bcd18f63d870da7fe0e2ebe9b",
)
lk.thing_setup(os.path.join(CUR_DIR, "tsl.json"))
lk.on_connect = on_connect
lk.on_disconnect = on_disconnect
lk.on_thing_call_service = on_thing_call_service

threading.Thread(target=report_loop, daemon=True).start()
lk.connect_async()

log.info("打印机接入程序启动")
while True:
    time.sleep(1)
