import time, threading, os, sys
from linkkit import linkkit

CUR_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CUR_DIR)
import computer


def read_props():
    return {
        'system_name': computer.get_system_name(),
        'host_name': computer.get_host_name(),
        'lock_status': 1 if computer.check_lock_screen() else 0,
    }


def service_lock_screen(params):
    computer.lock_screen_win32()
    return 200, {}


def service_start_remote_software(params):
    computer.start_remote_control()
    return 200, {}


def on_thing_call_service(identifier, request_id, params, userdata):
    res = {}
    try:
        if identifier == 'lock_screen':
            code, res = service_lock_screen(params)
        elif identifier == 'start_remote_software':
            code, res = service_start_remote_software(params)
        else:
            code = 400
    except Exception as e:
        print('service error:', e)
        code = 500
    lk.thing_answer_service(identifier, request_id, code, res)


def report_loop():
    while True:
        time.sleep(10)
        cur = read_props()
        with _lock:
            changed = {k: v for k, v in cur.items() if last_props.get(k) != v}
            if changed:
                print('上报变化属性:', changed)
                lk.thing_post_property(changed)
                last_props.update(changed)


last_props = {}
_lock = threading.Lock()

lk = linkkit.LinkKit(
    host_name="cn-shanghai",
    product_key="a1XKV83f73J",
    device_name="homelaptop01",
    device_secret="a836ee46f23827d26df0e4e14685e42f",
)
lk.thing_setup(os.path.join(CUR_DIR, "tsl.json"))
lk.connect_async()
lk.on_thing_call_service = on_thing_call_service

threading.Thread(target=report_loop, daemon=True).start()

while True:
    time.sleep(1)
