import time
import pytest

from services.ali_iot_tools import (
    productAddPropertiesServices,
    getThingModel,
    productList,
    createProduct,
    deviceList,
    createDevice,
    invokeService,
    setProperty,
    getProperties,
    all_tools,
    all_tool_map,
    TOOL_NAME_CN, productDelFun,
)


def test_all_tools_count():
    assert len(all_tools) == 10
    assert len(all_tool_map) == 10


def test_tool_name_cn_mapping():
    for cn_name, tool_fn in all_tool_map.items():
        assert tool_fn.name in TOOL_NAME_CN
        assert TOOL_NAME_CN[tool_fn.name] == cn_name



def test_get_thing_model():
    thingModelJson = getThingModel.invoke({"productKey": "SmokeDetector"})
    print(thingModelJson)
    assert isinstance(thingModelJson, dict)


def test_product_list():
    result = productList.invoke({})
    assert isinstance(result, list)


def test_product_list_with_filter():
    result = productList.invoke({"product_name": "test"})
    assert isinstance(result, list)


def test_device_list():
    result = deviceList.invoke({})
    print(result)
    assert isinstance(result, list)


def test_create_device():
    products = productList.invoke({})
    assert len(products) > 0, "need at least one product"
    pk = products[0]["productKey"]
    ts = int(time.time())
    result = createDevice.invoke({
        "productKey": pk,
        "deviceName": f"ut_test_device_{ts}",
    })
    print(result)
    assert isinstance(result, dict)
    assert "iotId" in result


def test_get_properties():
    devices = deviceList.invoke({})
    assert len(devices) > 0, "need at least one device"
    iot_id = 'YIZbpStJRuvLh5dcj9fZ'
    result = getProperties.invoke({"iot_id": iot_id})
    assert isinstance(result, dict)


def test_product_add_fun():
    ts = int(time.time())
    result = productAddPropertiesServices.invoke({
        "productKey": 'hGgDzuu5zwW',
        "funType": "properties",
        "funDetail": {
            "identifier": f"ut_test_prop_{ts}",
            "name": "UT测试属性",
            "accessMode": "r",
            "required": False,
            "dataType": {"type": "int", "specs": {"min": "0", "max": "100", "step": "1"}},
        },
    })
    assert isinstance(result, dict)


def test_product_add_service():
    ts = int(time.time())
    result = productAddPropertiesServices.invoke({
        "productKey": "J2XUEhMQULw",
        "funType": "services",
        "funDetail": {
            "name": "打印",
            "identifier": "print",
            "callType": "async",
            "required": False,
            "inputData": [
                {
                    "name": "文件名",
                    "identifier": "fileName",
                    "required": True,
                    "dataType": {
                        "type": "text",
                        "specs": {
                            "length": 256
                        }
                    }
                },
                {
                    "name": "打印份数",
                    "identifier": "copies",
                    "required": False,
                    "dataType": {
                        "type": "int",
                        "specs": {
                            "min": "1",
                            "max": "999",
                            "unit": "份",
                            "unitName": "份",
                            "step": "1"
                        }
                    }
                }
            ]
        }
    })
    print(result)


def test_productDelFun():
    ts = int(time.time())
    result = productDelFun.invoke({
        "productKey": 'f4idT4ms38l',
        "funType": "properties",
        "identifier": f"aaa",
    })
    print(result)


def test_device_list_with_invalid_product_key():
    with pytest.raises(RuntimeError):
        deviceList.invoke({"product_key": "invalid_key_xyz"})


def test_create_product():
    ts = int(time.time())
    res = createProduct.invoke({
        "product_name": f"unit_test_{ts}",
        "description": "这是一个测试产品",
    })
    print(res)


def test_set_property():
    devices = deviceList.invoke({})
    res = setProperty.invoke({
        "iotId": devices[0]["iotId"],
        "data": {"Temperature": 25},
    })
    print(res)
    pass


def test_invoke_service_offline_device():
    devices = deviceList.invoke({})
    if len(devices) == 0:
        pytest.skip("no devices available")
    iot_id = devices[0]["iotId"]
    res = invokeService.invoke({
        "iotId": iot_id,
        "identifier": "nonexistent_service",
        "arg": {},
    })
    assert isinstance(res, dict)


def test_some():
    a = {"categoryKey", "categoryName"}
    b = {"categoryKey": 123, "categoryName": 3232}
    print(a, b)

