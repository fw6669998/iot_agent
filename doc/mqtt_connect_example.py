import json, sys, time, uuid, threading
import paho.mqtt.client as mqtt

MQTT_HOST = "iot.iuvtech.com"
MQTT_PORT = 1883
PRODUCT_KEY = "${productKey}"
DEVICE_NAME = "${deviceName}"
CLIENT_ID = f"{PRODUCT_KEY}.{DEVICE_NAME}"
USERNAME = f"{PRODUCT_KEY}.{DEVICE_NAME}"
PASSWORD = "${password}"

TOPIC_PROPERTY_POST = f"/sys/{PRODUCT_KEY}/{DEVICE_NAME}/thing/event/property/post"
TOPIC_SERVICE_INVOKE = f"/sys/{PRODUCT_KEY}/{DEVICE_NAME}/thing/service/+"

REPORT_INTERVAL = 10


def collect_properties():
    return {}


def execute_service(service_name, params):
    if service_name == "xxx":
        # 处理服务
        return execute_service_xxx(params)
    else:
        # 忽略
        return None


def execute_service_xxx(params):
    # 处理服务
    return {}


def report_loop(client):
    while True:
        time.sleep(REPORT_INTERVAL)
        try:
            props = collect_properties()
            payload = {
                "id": str(uuid.uuid4()),
                "version": "1.0",
                "sys": {"ack": 0},
                "params": props,
                "method": "thing.event.property.post",
            }
            client.publish(TOPIC_PROPERTY_POST, json.dumps(payload, ensure_ascii=False), qos=1)
        except Exception:
            pass


def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode("utf-8")
    except Exception:
        payload = msg.payload.decode("utf-8", errors="replace")
    try:
        data = json.loads(payload)
    except json.JSONDecodeError:
        return

    service_name = msg.topic.rstrip("/").split("/")[-1]
    params = data.get("params", {})
    execute_service(service_name, params)


def on_connect(client, userdata, flags, reason_code, properties):
    if reason_code == 0:
        client.subscribe(TOPIC_SERVICE_INVOKE, qos=1)


def main():
    client = mqtt.Client(
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
        client_id=CLIENT_ID,
        protocol=mqtt.MQTTv311,
    )
    client.username_pw_set(USERNAME, PASSWORD)
    client.reconnect_delay_set(min_delay=3, max_delay=120)
    client.on_connect = on_connect
    client.on_message = on_message
    try:
        client.connect(MQTT_HOST, MQTT_PORT, keepalive=60)
    except Exception:
        sys.exit(1)

    threading.Thread(target=report_loop, args=(client,), daemon=True).start()
    client.loop_forever(retry_first_connection=True)


if __name__ == "__main__":
    main()
