import time
import threading

from linkkit import linkkit


def read_props():
    return {}


def on_thing_call_service(identifier, request_id, params, userdata):
    code = 200
    lk.thing_answer_service(identifier, request_id, code, {})


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


lk = linkkit.LinkKit(
    host_name="cn-shanghai",
    product_key="{{PRODUCT_KEY}}",
    device_name="{{DEVICE_NAME}}",
    device_secret="{{DEVICE_SECRET}}",
)
lk.thing_setup()
lk.connect_async()
lk.on_thing_call_service = on_thing_call_service

thing_enabled = threading.Event()
last_props = {}
_lock = threading.Lock()

threading.Thread(target=report_loop, daemon=True).start()

while True:
    time.sleep(1)
