import time, threading, os, sys

from linkkit import linkkit     # aliyun-iot-linkkit


def read_props():
    return {}


def service_xxx(params):
    res = {}
    return 200, res


def on_thing_call_service(identifier, request_id, params, userdata):
    res = {}
    try:
        if identifier == 'xxx':
            code, res = service_xxx(params)
        else:
            code = 400
    except Exception as e:
        code = 500
    lk.thing_answer_service(identifier, request_id, code, res)


def report_loop():
    while True:
        time.sleep(10)
        print("上报变化属性")
        cur = read_props()
        with _lock:
            changed = {k: v for k, v in cur.items() if last_props.get(k) != v}
            if changed:
                lk.thing_post_property(changed)
                last_props.update(changed)


last_props = {}
CUR_DIR = os.path.dirname(os.path.abspath(__file__))

lk = linkkit.LinkKit(
    host_name="cn-shanghai",
    product_key="${productKey}",
    device_name="${deviceName}",
    device_secret="${secret}",
)
lk.thing_setup(os.path.join(CUR_DIR, "tsl.json"))
lk.connect_async()
lk.on_thing_call_service = on_thing_call_service

thing_enabled = threading.Event()
_lock = threading.Lock()

threading.Thread(target=report_loop, daemon=True).start()

while True:
    time.sleep(1)
