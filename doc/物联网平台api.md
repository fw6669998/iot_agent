# 全局公共参数

**全局Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | {{token}} | string | 是 | 调用登陆接口后自动设置token变量, 使用: {{token}} |

**全局Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**全局Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**全局认证方式**

> 无需认证

# 状态码说明

| 状态码 | 中文描述 |
| --- | ---- |
| 暂无参数 |

# 物模型

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 13:38:13

> 更新时间: 2022-06-15 16:43:53

**属性, 事件, 服务, topic 信息**

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 物模型模板列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-07 10:22:59

> 更新时间: 2026-07-24 16:34:38

**3层级数据**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/thingListSearch?size=100&page=0

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| size | 100 | Text | 否 | - |
| page | 0 | Text | 否 | 分页页码，数字类型 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"modelId": 1,
				"superId": 0,
				"categoryKey": "SmartCity",
				"categoryName": "智能城市"
			},
			{
				"modelId": 2,
				"superId": 1,
				"categoryKey": "PublicService",
				"categoryName": "公共服务"
			},
		],
		"last": false,
		"totalPages": 40,
		"totalElements": 399,
		"number": 0,
		"size": 10,
		"sort": null,
		"numberOfElements": 10,
		"first": true
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content.modelId | 1 | number | 模型id |
| data.content.superId | 0 | number | 父模型id |
| data.content.categoryKey | SmartCity | string | 产品物模型id |
| data.content.categoryName | 智能城市 | string | 产品物模型描述 |
| data.last | true | string | 最后一页 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 399 | number | 总元素数 |
| data.number | 0 | number | 当前页数 |
| data.size | 500 | number | 每页元素数 |
| data.sort | - | object | 排序信息 |
| data.numberOfElements | 399 | number | 总元素个数 |
| data.first | true | string | 是否是第一页 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## topic_新建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-15 17:10:01

> 更新时间: 2023-03-22 10:31:52

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/createTopic

**请求方式**

> POST

**Content-Type**

> urlencoded

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | h7s72qjeGaM | Text | 是 | 产品key |
| topicKeyShort | sysinfo3 | Text | 是 | topic主题 |
| operation | 2 | Text | 是 | 操作权限:0=发布,1=订阅,2=发布订阅 |
| topicName | 测试2 | Text | 否 | topic功能 |
| topicDesc | 大发大2 | Text | 否 | topic描述信息 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"topicId": 5,
		"productKey": "h7s7PwecpHX",
		"topicKey": "sysinfo",
		"topicName": "测试",
		"topicDesc": "大发大",
		"operation": 0,
		"updateTime": "2022-06-20 06:25:53",
		"topicIdIot": "23082644"
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.topicId | 5 | number | - |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.topicKey | sysinfo | string | topic主题 |
| data.topicName | 测试 | string | topic功能 |
| data.topicDesc | 大发大 | string | topic描述信息 |
| data.operation | 0 | number | 操作权限:0=订阅,1= |
| data.updateTime | 2022-06-20 06:25:53 | string | 更新时间 |
| data.topicIdIot | 23082644 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## topic_列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-15 17:20:36

> 更新时间: 2022-10-24 11:38:59

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/topicList?productKey=iy4uY75WdQj

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 产品key |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": [
		{
			"topicId": 2,
			"productKey": "h7s7PwecpHX",
			"topicKey": "h7s7PwecpHX/${deviceName}/user/qweq",
			"topicName": "测试",
			"topicDesc": "大发大",
			"operation": 0,
			"updateTime": "2022-06-16 01:54:12",
			"topicIdIot": "22916965"
		},
		{
			"topicId": 3,
			"productKey": "h7s7PwecpHX",
			"topicKey": "h7s7PwecpHX/${deviceName}/user/qweq2",
			"topicName": "测试",
			"topicDesc": "大发大",
			"operation": 8,
			"updateTime": "2022-06-16 01:56:37",
			"topicIdIot": "22916966"
		},
		{
			"topicId": 4,
			"productKey": "h7s7PwecpHX",
			"topicKey": "h7s7PwecpHX/${deviceName}/user/qweq3",
			"topicName": "测试",
			"topicDesc": "大发大",
			"operation": 0,
			"updateTime": "2022-06-16 01:58:50",
			"topicIdIot": "22917096"
		},
		{
			"topicId": 5,
			"productKey": "h7s7PwecpHX",
			"topicKey": "h7s7PwecpHX/${deviceName}/user/sysinfo",
			"topicName": "测试",
			"topicDesc": "大发大",
			"operation": 0,
			"updateTime": "2022-06-20 06:25:53",
			"topicIdIot": "23082644"
		}
	],
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.topicId | 2 | number | - |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.topicKey | h7s7PwecpHX/${deviceName}/user/qweq | string | topic主题 |
| data.topicName | 测试 | string | topic功能 |
| data.topicDesc | 大发大 | string | topic描述信息 |
| data.operation | 0 | number | 操作权限:0=发布,1=订阅,2=发布订阅 |
| data.updateTime | 2022-06-16 01:54:12 | string | 更新时间 |
| data.topicIdIot | 22916965 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## topic_更新

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-15 17:34:02

> 更新时间: 2022-11-07 10:51:01

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/updateTopic

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| topicKeyShort | sysinfo | Text | 否 | topic主题 |
| topicName | 测试23322 | Text | 否 | topic功能 |
| operation | 0 | Text | 否 | 操作权限:0=发布,1=订阅,2=发布订阅 |
| topicDesc | 大发大1231323 | Text | 否 | topic描述信息 |
| topicId | 11 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"topicId": 5,
		"productKey": "h7s7PwecpHX",
		"topicKey": "sysinfo",
		"topicName": "测试23322",
		"topicDesc": "大发大123",
		"operation": 0,
		"updateTime": "2022-06-20 06:34:29",
		"topicIdIot": "23082644"
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.topicId | 5 | number | - |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.topicKey | sysinfo | string | topic主题 |
| data.topicName | 测试23322 | string | topic功能 |
| data.topicDesc | 大发大123 | string | topic描述信息 |
| data.operation | 0 | number | 操作权限:0=订阅,1= |
| data.updateTime | 2022-06-20 06:34:29 | string | 更新时间 |
| data.topicIdIot | 23082644 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## topic_删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-16 11:29:52

> 更新时间: 2022-10-24 11:45:37

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/deleteTopic

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| topicId | 11 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": null,
	"status": "S",
	"sysMsg": "操作成功"
}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## topic_列表_基础(基本不变,建议缓存,所有产品通用)

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-24 17:20:23

> 更新时间: 2023-04-25 11:16:29

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/baseTopicList

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": [
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/event/property/post",
			"topicName": "属性上报",
			"topicDesc": "设备属性上报",
			"operation": 0,
			"topicType": 1,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/event/property/post_reply",
			"topicName": "属性上报",
			"topicDesc": "云端响应属性上报",
			"operation": 1,
			"topicType": 1,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/service/property/set",
			"topicName": "属性设置",
			"topicDesc": "设备属性设置",
			"operation": 1,
			"topicType": 1,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/event/${tsl.event.identifier}/post",
			"topicName": "事件上报",
			"topicDesc": "设备事件上报",
			"operation": 0,
			"topicType": 1,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/event/${tsl.event.identifier}/post_reply",
			"topicName": "事件上报",
			"topicDesc": "云端响应事件上报",
			"operation": 1,
			"topicType": 1,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/service/${tsl.service.identifier}",
			"topicName": "服务调用",
			"topicDesc": "设备服务调用",
			"operation": 1,
			"topicType": 1,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/service/${tsl.service.identifier}_reply",
			"topicName": "服务调用",
			"topicDesc": "设备端响应服务调用",
			"operation": 0,
			"topicType": 1,
			"status": 1
		},
		{
			"topicKey": "/ota/device/inform/${productKey}/${deviceName}",
			"topicName": "OTA 升级",
			"topicDesc": "设备上报固件升级信息",
			"operation": 0,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/ota/device/upgrade/${productKey}/${deviceName}",
			"topicName": "OTA 升级",
			"topicDesc": "固件升级信息下行",
			"operation": 1,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/ota/device/progress/${productKey}/${deviceName}",
			"topicName": "OTA 升级",
			"topicDesc": "设备上报固件升级进度",
			"operation": 0,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/ota/firmware/get",
			"topicName": "OTA 升级",
			"topicDesc": "设备主动拉取固件升级信息",
			"operation": 0,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/deviceinfo/update",
			"topicName": "设备标签",
			"topicDesc": "设备上报标签数据",
			"operation": 0,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/deviceinfo/update_reply",
			"topicName": "设备标签",
			"topicDesc": "云端响应标签上报",
			"operation": 1,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/deviceinfo/delete",
			"topicName": "设备标签",
			"topicDesc": "设备删除标签信息",
			"operation": 1,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/deviceinfo/delete_reply",
			"topicName": "设备标签",
			"topicDesc": "云端响应标签删除",
			"operation": 0,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/ext/ntp/${productKey}/${deviceName}/request",
			"topicName": "时钟同步",
			"topicDesc": "NTP 时钟同步请求",
			"operation": 0,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/ext/ntp/${productKey}/${deviceName}/response",
			"topicName": "时钟同步",
			"topicDesc": "NTP 时钟同步响应",
			"operation": 1,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/config/push",
			"topicName": "配置更新",
			"topicDesc": "云端主动下推配置信息",
			"operation": 1,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/config/get",
			"topicName": "配置更新",
			"topicDesc": "设备端查询配置信息",
			"operation": 0,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/sys/${productKey}/${deviceName}/thing/config/get_reply",
			"topicName": "配置更新",
			"topicDesc": "云端响应配置信息",
			"operation": 1,
			"topicType": 0,
			"status": 1
		},
		{
			"topicKey": "/broadcast/${productKey}/${identifier}",
			"topicName": "广播",
			"topicDesc": "广播 Topic，identifier 为用户自定义字符串",
			"operation": 1,
			"topicType": 0,
			"status": 1
		}
	],
	"errCode": null,
	"requestId": "fb06153632e64610a0b551584a98e8f5",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.topicKey | /sys/${productKey}/${deviceName}/thing/event/property/post | string | topic主题 |
| data.topicName | 属性上报 | string | topic功能 |
| data.topicDesc | 设备属性上报 | string | topic描述信息 |
| data.operation | 0 | number | 操作权限:0=发布,1=订阅,2=发布订阅 |
| data.topicType | 1 | number | topic类型:0=基础通信,1=物模型通信 |
| data.status | 1 | number | 状态:0=未使用,1=使用中 |
| errCode | - | object | - |
| requestId | fb06153632e64610a0b551584a98e8f5 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 物模型_获取

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-21 17:05:31

> 更新时间: 2022-10-28 10:06:29

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/getThingModel?productKey=h7s72qjeGaM

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | h7s72qjeGaM | string | 是 | 产品key |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"modelId": 331,
		"thingModelJson": "{\n  \"schema\": \"https://iotx-tsl.oss-ap-southeast-1.aliyuncs.com/schema.json\",\n  \"profile\": {\n    \"version\": \"1.5\",\n    \"productKey\": \"h7s72qjeGaM\"\n  },\n  \"properties\": [\n    {\n      \"identifier\": \"cpu_usage\",\n      \"name\": \"CPU使用率\",\n      \"accessMode\": \"rw\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"float\",\n        \"specs\": {\n          \"min\": \"0\",\n          \"max\": \"100\",\n          \"unit\": \"%\",\n          \"unitName\": \"百分比\",\n          \"step\": \"0.1\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"PowerLed\",\n      \"name\": \"power_LED\",\n      \"accessMode\": \"rw\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"bool\",\n        \"specs\": {\n          \"0\": \"关\",\n          \"1\": \"开\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"Temperature\",\n      \"name\": \"温度\",\n      \"accessMode\": \"rw\",\n      \"desc\": \"温度\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"float\",\n        \"specs\": {\n          \"min\": \"0\",\n          \"max\": \"100\",\n          \"unit\": \"°C\",\n          \"unitName\": \"摄氏度\",\n          \"step\": \"0.1\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"Humidity\",\n      \"name\": \"湿度\",\n      \"accessMode\": \"rw\",\n      \"desc\": \"湿度\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"float\",\n        \"specs\": {\n          \"min\": \"0\",\n          \"max\": \"100\",\n          \"unit\": \"%RH\",\n          \"unitName\": \"相对湿度\",\n          \"step\": \"0.1\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"DISK_used_percentage\",\n      \"name\": \"磁盘空间\",\n      \"accessMode\": \"rw\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"float\",\n        \"specs\": {\n          \"min\": \"0\",\n          \"max\": \"100\",\n          \"unit\": \"%\",\n          \"unitName\": \"百分比\",\n          \"step\": \"0.1\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"cpu_temperature\",\n      \"name\": \"cpu温度\",\n      \"accessMode\": \"rw\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"float\",\n        \"specs\": {\n          \"min\": \"-1.4E-45\",\n          \"max\": \"3.4028235E38\",\n          \"unit\": \"°C\",\n          \"unitName\": \"摄氏度\",\n          \"step\": \"0.1\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"DH11status\",\n      \"name\": \"温度计运行状态\",\n      \"accessMode\": \"rw\",\n      \"desc\": \"内容推荐。0：未知状态，1：熄屏，2：亮屏\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"bool\",\n        \"specs\": {\n          \"0\": \"异常\",\n          \"1\": \"正常\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"tempSpace\",\n      \"name\": \"临时文件空间\",\n      \"accessMode\": \"rw\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"text\",\n        \"specs\": {\n          \"length\": \"1024\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"other\",\n      \"name\": \"其他\",\n      \"accessMode\": \"rw\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"int\",\n        \"specs\": {\n          \"min\": \"0\",\n          \"max\": \"200\",\n          \"step\": \"1\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"ChildLockSwitch2\",\n      \"name\": \"童锁开关2\",\n      \"accessMode\": \"rw\",\n      \"required\": true,\n      \"dataType\": {\n        \"type\": \"bool\",\n        \"specs\": {\n          \"0\": \"关\",\n          \"1\": \"开\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"ChildLockSwitch22\",\n      \"name\": \"童锁开关22\",\n      \"accessMode\": \"rw\",\n      \"required\": true,\n      \"dataType\": {\n        \"type\": \"bool\",\n        \"specs\": {\n          \"0\": \"关\",\n          \"1\": \"开\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"other3\",\n      \"name\": \"other3\",\n      \"accessMode\": \"rw\",\n      \"required\": true,\n      \"dataType\": {\n        \"type\": \"double\",\n        \"specs\": {\n          \"min\": \"16\",\n          \"max\": \"55\",\n          \"unit\": \"°C\",\n          \"unitName\": \"摄氏度\",\n          \"step\": \"1\"\n        }\n      }\n    },\n    {\n      \"identifier\": \"jiaodu\",\n      \"name\": \"角度\",\n      \"accessMode\": \"rw\",\n      \"required\": false,\n      \"dataType\": {\n        \"type\": \"int\",\n        \"specs\": {\n          \"min\": \"0\",\n          \"max\": \"180\",\n          \"step\": \"1\"\n        }\n      }\n    }\n  ],\n  \"events\": [\n    {\n      \"identifier\": \"post\",\n      \"name\": \"post\",\n      \"type\": \"info\",\n      \"required\": true,\n      \"desc\": \"属性上报\",\n      \"method\": \"thing.event.property.post\",\n      \"outputData\": [\n        {\n          \"identifier\": \"cpu_usage\",\n          \"name\": \"CPU使用率\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%\",\n              \"unitName\": \"百分比\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"PowerLed\",\n          \"name\": \"power_LED\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"Temperature\",\n          \"name\": \"温度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"Humidity\",\n          \"name\": \"湿度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%RH\",\n              \"unitName\": \"相对湿度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"DISK_used_percentage\",\n          \"name\": \"磁盘空间\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%\",\n              \"unitName\": \"百分比\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"cpu_temperature\",\n          \"name\": \"cpu温度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"-1.4E-45\",\n              \"max\": \"3.4028235E38\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"DH11status\",\n          \"name\": \"温度计运行状态\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"异常\",\n              \"1\": \"正常\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"tempSpace\",\n          \"name\": \"临时文件空间\",\n          \"dataType\": {\n            \"type\": \"text\",\n            \"specs\": {\n              \"length\": \"1024\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"other\",\n          \"name\": \"其他\",\n          \"dataType\": {\n            \"type\": \"int\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"200\",\n              \"step\": \"1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"ChildLockSwitch2\",\n          \"name\": \"童锁开关2\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"ChildLockSwitch22\",\n          \"name\": \"童锁开关22\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"other3\",\n          \"name\": \"other3\",\n          \"dataType\": {\n            \"type\": \"double\",\n            \"specs\": {\n              \"min\": \"16\",\n              \"max\": \"55\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"jiaodu\",\n          \"name\": \"角度\",\n          \"dataType\": {\n            \"type\": \"int\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"180\",\n              \"step\": \"1\"\n            }\n          }\n        }\n      ]\n    },\n    {\n      \"identifier\": \"TemperatureSensorExceptional\",\n      \"name\": \"环境温度传感器异常2\",\n      \"type\": \"error\",\n      \"required\": false,\n      \"method\": \"thing.event.TemperatureSensorExceptional.post\",\n      \"outputData\": [\n        {\n          \"identifier\": \"Error\",\n          \"name\": \"环境温度传感器异常\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"正常\",\n              \"1\": \"环境温度传感器异常\"\n            }\n          }\n        }\n      ]\n    }\n  ],\n  \"services\": [\n    {\n      \"identifier\": \"set\",\n      \"name\": \"set\",\n      \"required\": true,\n      \"callType\": \"async\",\n      \"desc\": \"属性设置\",\n      \"method\": \"thing.service.property.set\",\n      \"inputData\": [\n        {\n          \"identifier\": \"cpu_usage\",\n          \"name\": \"CPU使用率\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%\",\n              \"unitName\": \"百分比\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"PowerLed\",\n          \"name\": \"power_LED\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"Temperature\",\n          \"name\": \"温度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"Humidity\",\n          \"name\": \"湿度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%RH\",\n              \"unitName\": \"相对湿度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"DISK_used_percentage\",\n          \"name\": \"磁盘空间\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%\",\n              \"unitName\": \"百分比\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"cpu_temperature\",\n          \"name\": \"cpu温度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"-1.4E-45\",\n              \"max\": \"3.4028235E38\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"DH11status\",\n          \"name\": \"温度计运行状态\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"异常\",\n              \"1\": \"正常\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"tempSpace\",\n          \"name\": \"临时文件空间\",\n          \"dataType\": {\n            \"type\": \"text\",\n            \"specs\": {\n              \"length\": \"1024\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"other\",\n          \"name\": \"其他\",\n          \"dataType\": {\n            \"type\": \"int\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"200\",\n              \"step\": \"1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"ChildLockSwitch2\",\n          \"name\": \"童锁开关2\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"ChildLockSwitch22\",\n          \"name\": \"童锁开关22\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"other3\",\n          \"name\": \"other3\",\n          \"dataType\": {\n            \"type\": \"double\",\n            \"specs\": {\n              \"min\": \"16\",\n              \"max\": \"55\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"jiaodu\",\n          \"name\": \"角度\",\n          \"dataType\": {\n            \"type\": \"int\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"180\",\n              \"step\": \"1\"\n            }\n          }\n        }\n      ],\n      \"outputData\": []\n    },\n    {\n      \"identifier\": \"get\",\n      \"name\": \"get\",\n      \"required\": true,\n      \"callType\": \"async\",\n      \"desc\": \"属性获取\",\n      \"method\": \"thing.service.property.get\",\n      \"inputData\": [\n        \"cpu_usage\",\n        \"PowerLed\",\n        \"Temperature\",\n        \"Humidity\",\n        \"DISK_used_percentage\",\n        \"cpu_temperature\",\n        \"DH11status\",\n        \"tempSpace\",\n        \"other\",\n        \"ChildLockSwitch2\",\n        \"ChildLockSwitch22\",\n        \"other3\",\n        \"jiaodu\"\n      ],\n      \"outputData\": [\n        {\n          \"identifier\": \"cpu_usage\",\n          \"name\": \"CPU使用率\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%\",\n              \"unitName\": \"百分比\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"PowerLed\",\n          \"name\": \"power_LED\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"Temperature\",\n          \"name\": \"温度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"Humidity\",\n          \"name\": \"湿度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%RH\",\n              \"unitName\": \"相对湿度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"DISK_used_percentage\",\n          \"name\": \"磁盘空间\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"100\",\n              \"unit\": \"%\",\n              \"unitName\": \"百分比\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"cpu_temperature\",\n          \"name\": \"cpu温度\",\n          \"dataType\": {\n            \"type\": \"float\",\n            \"specs\": {\n              \"min\": \"-1.4E-45\",\n              \"max\": \"3.4028235E38\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"0.1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"DH11status\",\n          \"name\": \"温度计运行状态\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"异常\",\n              \"1\": \"正常\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"tempSpace\",\n          \"name\": \"临时文件空间\",\n          \"dataType\": {\n            \"type\": \"text\",\n            \"specs\": {\n              \"length\": \"1024\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"other\",\n          \"name\": \"其他\",\n          \"dataType\": {\n            \"type\": \"int\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"200\",\n              \"step\": \"1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"ChildLockSwitch2\",\n          \"name\": \"童锁开关2\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"ChildLockSwitch22\",\n          \"name\": \"童锁开关22\",\n          \"dataType\": {\n            \"type\": \"bool\",\n            \"specs\": {\n              \"0\": \"关\",\n              \"1\": \"开\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"other3\",\n          \"name\": \"other3\",\n          \"dataType\": {\n            \"type\": \"double\",\n            \"specs\": {\n              \"min\": \"16\",\n              \"max\": \"55\",\n              \"unit\": \"°C\",\n              \"unitName\": \"摄氏度\",\n              \"step\": \"1\"\n            }\n          }\n        },\n        {\n          \"identifier\": \"jiaodu\",\n          \"name\": \"角度\",\n          \"dataType\": {\n            \"type\": \"int\",\n            \"specs\": {\n              \"min\": \"0\",\n              \"max\": \"180\",\n              \"step\": \"1\"\n            }\n          }\n        }\n      ]\n    },\n    {\n      \"identifier\": \"clear\",\n      \"name\": \"清理垃圾\",\n      \"required\": false,\n      \"callType\": \"async\",\n      \"desc\": \"12321\",\n      \"method\": \"thing.service.clear\",\n      \"inputData\": [\n        {\n          \"identifier\": \"type\",\n          \"name\": \"类型\",\n          \"dataType\": {\n            \"type\": \"text\",\n            \"specs\": {\n              \"length\": \"50\"\n            }\n          }\n        }\n      ],\n      \"outputData\": []\n    },\n    {\n      \"identifier\": \"UpdateModel2\",\n      \"name\": \"12312\",\n      \"required\": false,\n      \"callType\": \"sync\",\n      \"desc\": \"12313\",\n      \"method\": \"thing.service.UpdateModel2\",\n      \"inputData\": [],\n      \"outputData\": []\n    },\n    {\n      \"identifier\": \"switchbling\",\n      \"name\": \"调整灯开关\",\n      \"required\": false,\n      \"callType\": \"async\",\n      \"method\": \"thing.service.switchbling\",\n      \"inputData\": [\n        {\n          \"identifier\": \"switch\",\n          \"name\": \"调整颜色\",\n          \"dataType\": {\n            \"type\": \"text\",\n            \"specs\": {\n              \"length\": \"10240\"\n            }\n          }\n        }\n      ],\n      \"outputData\": []\n    }\n  ],\n  \"functionBlocks\": [\n    {\n      \"functionBlockId\": \"add\",\n      \"functionBlockName\": \"add\",\n      \"gmtCreated\": 1666669166493,\n      \"productKey\": \"h7s72qjeGaM\"\n    },\n    {\n      \"functionBlockId\": \"add2\",\n      \"functionBlockName\": \"add2\",\n      \"gmtCreated\": 1666677006065,\n      \"productKey\": \"h7s72qjeGaM\"\n    }\n  ]\n}",
		"productKey": "h7s72qjeGaM",
		"createTime": "2022-10-24 11:21:09",
		"updateTime": "2022-10-25 01:57:10",
		"categoryKey": null,
		"isStandard": null
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.modelId | 331 | number | - |
| data.thingModelJson | {  "schema": "https://iotx-tsl.oss-ap-southeast-1.aliyuncs.com/schema.json",  "profile": {    "version": "1.5",    "productKey": "h7s72qjeGaM"  },  "properties": [    {      "identifier": "cpu_usage",      "name": "CPU使用率",      "accessMode": "rw",      "required": false,      "dataType": {        "type": "float",        "specs": {          "min": "0",          "max": "100",          "unit": "%",          "unitName": "百分比",          "step": "0.1"        }      }    },    {      "identifier": "PowerLed",      "name": "power_LED",      "accessMode": "rw",      "required": false,      "dataType": {        "type": "bool",        "specs": {          "0": "关",          "1": "开"        }      }    },    {      "identifier": "Temperature",      "name": "温度",      "accessMode": "rw",      "desc": "温度",      "required": false,      "dataType": {        "type": "float",        "specs": {          "min": "0",          "max": "100",          "unit": "°C",          "unitName": "摄氏度",          "step": "0.1"        }      }    },    {      "identifier": "Humidity",      "name": "湿度",      "accessMode": "rw",      "desc": "湿度",      "required": false,      "dataType": {        "type": "float",        "specs": {          "min": "0",          "max": "100",          "unit": "%RH",          "unitName": "相对湿度",          "step": "0.1"        }      }    },    {      "identifier": "DISK_used_percentage",      "name": "磁盘空间",      "accessMode": "rw",      "required": false,      "dataType": {        "type": "float",        "specs": {          "min": "0",          "max": "100",          "unit": "%",          "unitName": "百分比",          "step": "0.1"        }      }    },    {      "identifier": "cpu_temperature",      "name": "cpu温度",      "accessMode": "rw",      "required": false,      "dataType": {        "type": "float",        "specs": {          "min": "-1.4E-45",          "max": "3.4028235E38",          "unit": "°C",          "unitName": "摄氏度",          "step": "0.1"        }      }    },    {      "identifier": "DH11status",      "name": "温度计运行状态",      "accessMode": "rw",      "desc": "内容推荐。0：未知状态，1：熄屏，2：亮屏",      "required": false,      "dataType": {        "type": "bool",        "specs": {          "0": "异常",          "1": "正常"        }      }    },    {      "identifier": "tempSpace",      "name": "临时文件空间",      "accessMode": "rw",      "required": false,      "dataType": {        "type": "text",        "specs": {          "length": "1024"        }      }    },    {      "identifier": "other",      "name": "其他",      "accessMode": "rw",      "required": false,      "dataType": {        "type": "int",        "specs": {          "min": "0",          "max": "200",          "step": "1"        }      }    },    {      "identifier": "ChildLockSwitch2",      "name": "童锁开关2",      "accessMode": "rw",      "required": true,      "dataType": {        "type": "bool",        "specs": {          "0": "关",          "1": "开"        }      }    },    {      "identifier": "ChildLockSwitch22",      "name": "童锁开关22",      "accessMode": "rw",      "required": true,      "dataType": {        "type": "bool",        "specs": {          "0": "关",          "1": "开"        }      }    },    {      "identifier": "other3",      "name": "other3",      "accessMode": "rw",      "required": true,      "dataType": {        "type": "double",        "specs": {          "min": "16",          "max": "55",          "unit": "°C",          "unitName": "摄氏度",          "step": "1"        }      }    },    {      "identifier": "jiaodu",      "name": "角度",      "accessMode": "rw",      "required": false,      "dataType": {        "type": "int",        "specs": {          "min": "0",          "max": "180",          "step": "1"        }      }    }  ],  "events": [    {      "identifier": "post",      "name": "post",      "type": "info",      "required": true,      "desc": "属性上报",      "method": "thing.event.property.post",      "outputData": [        {          "identifier": "cpu_usage",          "name": "CPU使用率",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%",              "unitName": "百分比",              "step": "0.1"            }          }        },        {          "identifier": "PowerLed",          "name": "power_LED",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "Temperature",          "name": "温度",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "°C",              "unitName": "摄氏度",              "step": "0.1"            }          }        },        {          "identifier": "Humidity",          "name": "湿度",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%RH",              "unitName": "相对湿度",              "step": "0.1"            }          }        },        {          "identifier": "DISK_used_percentage",          "name": "磁盘空间",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%",              "unitName": "百分比",              "step": "0.1"            }          }        },        {          "identifier": "cpu_temperature",          "name": "cpu温度",          "dataType": {            "type": "float",            "specs": {              "min": "-1.4E-45",              "max": "3.4028235E38",              "unit": "°C",              "unitName": "摄氏度",              "step": "0.1"            }          }        },        {          "identifier": "DH11status",          "name": "温度计运行状态",          "dataType": {            "type": "bool",            "specs": {              "0": "异常",              "1": "正常"            }          }        },        {          "identifier": "tempSpace",          "name": "临时文件空间",          "dataType": {            "type": "text",            "specs": {              "length": "1024"            }          }        },        {          "identifier": "other",          "name": "其他",          "dataType": {            "type": "int",            "specs": {              "min": "0",              "max": "200",              "step": "1"            }          }        },        {          "identifier": "ChildLockSwitch2",          "name": "童锁开关2",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "ChildLockSwitch22",          "name": "童锁开关22",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "other3",          "name": "other3",          "dataType": {            "type": "double",            "specs": {              "min": "16",              "max": "55",              "unit": "°C",              "unitName": "摄氏度",              "step": "1"            }          }        },        {          "identifier": "jiaodu",          "name": "角度",          "dataType": {            "type": "int",            "specs": {              "min": "0",              "max": "180",              "step": "1"            }          }        }      ]    },    {      "identifier": "TemperatureSensorExceptional",      "name": "环境温度传感器异常2",      "type": "error",      "required": false,      "method": "thing.event.TemperatureSensorExceptional.post",      "outputData": [        {          "identifier": "Error",          "name": "环境温度传感器异常",          "dataType": {            "type": "bool",            "specs": {              "0": "正常",              "1": "环境温度传感器异常"            }          }        }      ]    }  ],  "services": [    {      "identifier": "set",      "name": "set",      "required": true,      "callType": "async",      "desc": "属性设置",      "method": "thing.service.property.set",      "inputData": [        {          "identifier": "cpu_usage",          "name": "CPU使用率",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%",              "unitName": "百分比",              "step": "0.1"            }          }        },        {          "identifier": "PowerLed",          "name": "power_LED",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "Temperature",          "name": "温度",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "°C",              "unitName": "摄氏度",              "step": "0.1"            }          }        },        {          "identifier": "Humidity",          "name": "湿度",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%RH",              "unitName": "相对湿度",              "step": "0.1"            }          }        },        {          "identifier": "DISK_used_percentage",          "name": "磁盘空间",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%",              "unitName": "百分比",              "step": "0.1"            }          }        },        {          "identifier": "cpu_temperature",          "name": "cpu温度",          "dataType": {            "type": "float",            "specs": {              "min": "-1.4E-45",              "max": "3.4028235E38",              "unit": "°C",              "unitName": "摄氏度",              "step": "0.1"            }          }        },        {          "identifier": "DH11status",          "name": "温度计运行状态",          "dataType": {            "type": "bool",            "specs": {              "0": "异常",              "1": "正常"            }          }        },        {          "identifier": "tempSpace",          "name": "临时文件空间",          "dataType": {            "type": "text",            "specs": {              "length": "1024"            }          }        },        {          "identifier": "other",          "name": "其他",          "dataType": {            "type": "int",            "specs": {              "min": "0",              "max": "200",              "step": "1"            }          }        },        {          "identifier": "ChildLockSwitch2",          "name": "童锁开关2",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "ChildLockSwitch22",          "name": "童锁开关22",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "other3",          "name": "other3",          "dataType": {            "type": "double",            "specs": {              "min": "16",              "max": "55",              "unit": "°C",              "unitName": "摄氏度",              "step": "1"            }          }        },        {          "identifier": "jiaodu",          "name": "角度",          "dataType": {            "type": "int",            "specs": {              "min": "0",              "max": "180",              "step": "1"            }          }        }      ],      "outputData": []    },    {      "identifier": "get",      "name": "get",      "required": true,      "callType": "async",      "desc": "属性获取",      "method": "thing.service.property.get",      "inputData": [        "cpu_usage",        "PowerLed",        "Temperature",        "Humidity",        "DISK_used_percentage",        "cpu_temperature",        "DH11status",        "tempSpace",        "other",        "ChildLockSwitch2",        "ChildLockSwitch22",        "other3",        "jiaodu"      ],      "outputData": [        {          "identifier": "cpu_usage",          "name": "CPU使用率",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%",              "unitName": "百分比",              "step": "0.1"            }          }        },        {          "identifier": "PowerLed",          "name": "power_LED",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "Temperature",          "name": "温度",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "°C",              "unitName": "摄氏度",              "step": "0.1"            }          }        },        {          "identifier": "Humidity",          "name": "湿度",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%RH",              "unitName": "相对湿度",              "step": "0.1"            }          }        },        {          "identifier": "DISK_used_percentage",          "name": "磁盘空间",          "dataType": {            "type": "float",            "specs": {              "min": "0",              "max": "100",              "unit": "%",              "unitName": "百分比",              "step": "0.1"            }          }        },        {          "identifier": "cpu_temperature",          "name": "cpu温度",          "dataType": {            "type": "float",            "specs": {              "min": "-1.4E-45",              "max": "3.4028235E38",              "unit": "°C",              "unitName": "摄氏度",              "step": "0.1"            }          }        },        {          "identifier": "DH11status",          "name": "温度计运行状态",          "dataType": {            "type": "bool",            "specs": {              "0": "异常",              "1": "正常"            }          }        },        {          "identifier": "tempSpace",          "name": "临时文件空间",          "dataType": {            "type": "text",            "specs": {              "length": "1024"            }          }        },        {          "identifier": "other",          "name": "其他",          "dataType": {            "type": "int",            "specs": {              "min": "0",              "max": "200",              "step": "1"            }          }        },        {          "identifier": "ChildLockSwitch2",          "name": "童锁开关2",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "ChildLockSwitch22",          "name": "童锁开关22",          "dataType": {            "type": "bool",            "specs": {              "0": "关",              "1": "开"            }          }        },        {          "identifier": "other3",          "name": "other3",          "dataType": {            "type": "double",            "specs": {              "min": "16",              "max": "55",              "unit": "°C",              "unitName": "摄氏度",              "step": "1"            }          }        },        {          "identifier": "jiaodu",          "name": "角度",          "dataType": {            "type": "int",            "specs": {              "min": "0",              "max": "180",              "step": "1"            }          }        }      ]    },    {      "identifier": "clear",      "name": "清理垃圾",      "required": false,      "callType": "async",      "desc": "12321",      "method": "thing.service.clear",      "inputData": [        {          "identifier": "type",          "name": "类型",          "dataType": {            "type": "text",            "specs": {              "length": "50"            }          }        }      ],      "outputData": []    },    {      "identifier": "UpdateModel2",      "name": "12312",      "required": false,      "callType": "sync",      "desc": "12313",      "method": "thing.service.UpdateModel2",      "inputData": [],      "outputData": []    },    {      "identifier": "switchbling",      "name": "调整灯开关",      "required": false,      "callType": "async",      "method": "thing.service.switchbling",      "inputData": [        {          "identifier": "switch",          "name": "调整颜色",          "dataType": {            "type": "text",            "specs": {              "length": "10240"            }          }        }      ],      "outputData": []    }  ],  "functionBlocks": [    {      "functionBlockId": "add",      "functionBlockName": "add",      "gmtCreated": 1666669166493,      "productKey": "h7s72qjeGaM"    },    {      "functionBlockId": "add2",      "functionBlockName": "add2",      "gmtCreated": 1666677006065,      "productKey": "h7s72qjeGaM"    }  ]} | string | 物模型json, 格式参考: https://help.aliyun.com/document_detail/213902.html |
| data.productKey | h7s72qjeGaM | string | 产品key |
| data.createTime | 2022-10-24 11:21:09 | string | 创建时间 |
| data.updateTime | 2022-10-25 01:57:10 | string | 更新时间 |
| data.categoryKey | - | object | 设备模型识别码 |
| data.isStandard | - | object | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 物模型_获取单位

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-22 08:59:28

> 更新时间: 2022-10-24 11:34:36

**基本不变, 建议缓存**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/getThingUnit

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": [
		{
			"Symbol": "mg/kg",
			"Name": "毫克每千克"
		},
		{
			"Symbol": "NTU",
			"Name": "浊度"
		},
		{
			"Symbol": "pH",
			"Name": "PH值"
		},
		{
			"Symbol": "dS/m",
			"Name": "土壤EC值"
		},
		{
			"Symbol": "W/㎡",
			"Name": "太阳总辐射"
		},
		{
			"Symbol": "mm/hour",
			"Name": "降雨量"
		},
		{
			"Symbol": "var",
			"Name": "乏"
		},
		{
			"Symbol": "cP",
			"Name": "厘泊"
		},
		{
			"Symbol": "aw",
			"Name": "饱和度"
		},
		{
			"Symbol": "pcs",
			"Name": "个"
		},
		{
			"Symbol": "cst",
			"Name": "厘斯"
		},
		{
			"Symbol": "bar",
			"Name": "巴"
		},
		{
			"Symbol": "ppt",
			"Name": "纳克每升"
		},
		{
			"Symbol": "ppb",
			"Name": "微克每升"
		},
		{
			"Symbol": "uS/cm",
			"Name": "微西每厘米"
		},
		{
			"Symbol": "N/C",
			"Name": "牛顿每库仑"
		},
		{
			"Symbol": "V/m",
			"Name": "伏特每米"
		},
		{
			"Symbol": "ml/min",
			"Name": "滴速"
		},
		{
			"Symbol": "mmHg",
			"Name": "血压"
		},
		{
			"Symbol": "mmol/L",
			"Name": "血糖"
		},
		{
			"Symbol": "mm/s",
			"Name": "毫米每秒"
		},
		{
			"Symbol": "turn/m",
			"Name": "转每分钟"
		},
		{
			"Symbol": "count",
			"Name": "次"
		},
		{
			"Symbol": "gear",
			"Name": "档"
		},
		{
			"Symbol": "stepCount",
			"Name": "步"
		},
		{
			"Symbol": "Nm3/h",
			"Name": "标准立方米每小时"
		},
		{
			"Symbol": "kV",
			"Name": "千伏"
		},
		{
			"Symbol": "kVA",
			"Name": "千伏安"
		},
		{
			"Symbol": "kVar",
			"Name": "千乏"
		},
		{
			"Symbol": "uw/cm2",
			"Name": "微瓦每平方厘米"
		},
		{
			"Symbol": "只",
			"Name": "只"
		},
		{
			"Symbol": "%RH",
			"Name": "相对湿度"
		},
		{
			"Symbol": "m³/s",
			"Name": "立方米每秒"
		},
		{
			"Symbol": "kg/s",
			"Name": "公斤每秒"
		},
		{
			"Symbol": "r/min",
			"Name": "转每分钟"
		},
		{
			"Symbol": "t/h",
			"Name": "吨每小时"
		},
		{
			"Symbol": "KCL/h",
			"Name": "千卡每小时"
		},
		{
			"Symbol": "L/s",
			"Name": "升每秒"
		},
		{
			"Symbol": "Mpa",
			"Name": "兆帕"
		},
		{
			"Symbol": "m³/h",
			"Name": "立方米每小时"
		},
		{
			"Symbol": "kvarh",
			"Name": "千乏时"
		},
		{
			"Symbol": "μg/L",
			"Name": "微克每升"
		},
		{
			"Symbol": "kcal",
			"Name": "千卡路里"
		},
		{
			"Symbol": "GB",
			"Name": "吉字节"
		},
		{
			"Symbol": "MB",
			"Name": "兆字节"
		},
		{
			"Symbol": "KB",
			"Name": "千字节"
		},
		{
			"Symbol": "B",
			"Name": "字节"
		},
		{
			"Symbol": "μg/(d㎡·d)",
			"Name": "微克每平方分米每天"
		},
		{
			"Symbol": "",
			"Name": "无"
		},
		{
			"Symbol": "ppm",
			"Name": "百万分率"
		},
		{
			"Symbol": "pixel",
			"Name": "像素"
		},
		{
			"Symbol": "Lux",
			"Name": "照度"
		},
		{
			"Symbol": "grav",
			"Name": "重力加速度"
		},
		{
			"Symbol": "dB",
			"Name": "分贝"
		},
		{
			"Symbol": "%",
			"Name": "百分比"
		},
		{
			"Symbol": "lm",
			"Name": "流明"
		},
		{
			"Symbol": "bit",
			"Name": "比特"
		},
		{
			"Symbol": "g/mL",
			"Name": "克每毫升"
		},
		{
			"Symbol": "g/L",
			"Name": "克每升"
		},
		{
			"Symbol": "mg/L",
			"Name": "毫克每升"
		},
		{
			"Symbol": "μg/m³",
			"Name": "微克每立方米"
		},
		{
			"Symbol": "mg/m³",
			"Name": "毫克每立方米"
		},
		{
			"Symbol": "g/m³",
			"Name": "克每立方米"
		},
		{
			"Symbol": "kg/m³",
			"Name": "千克每立方米"
		},
		{
			"Symbol": "nF",
			"Name": "纳法"
		},
		{
			"Symbol": "pF",
			"Name": "皮法"
		},
		{
			"Symbol": "μF",
			"Name": "微法"
		},
		{
			"Symbol": "F",
			"Name": "法拉"
		},
		{
			"Symbol": "Ω",
			"Name": "欧姆"
		},
		{
			"Symbol": "μA",
			"Name": "微安"
		},
		{
			"Symbol": "mA",
			"Name": "毫安"
		},
		{
			"Symbol": "kA",
			"Name": "千安"
		},
		{
			"Symbol": "A",
			"Name": "安培"
		},
		{
			"Symbol": "mV",
			"Name": "毫伏"
		},
		{
			"Symbol": "V",
			"Name": "伏特"
		},
		{
			"Symbol": "ms",
			"Name": "毫秒"
		},
		{
			"Symbol": "s",
			"Name": "秒"
		},
		{
			"Symbol": "min",
			"Name": "分钟"
		},
		{
			"Symbol": "h",
			"Name": "小时"
		},
		{
			"Symbol": "day",
			"Name": "日"
		},
		{
			"Symbol": "week",
			"Name": "周"
		},
		{
			"Symbol": "month",
			"Name": "月"
		},
		{
			"Symbol": "year",
			"Name": "年"
		},
		{
			"Symbol": "kn",
			"Name": "节"
		},
		{
			"Symbol": "km/h",
			"Name": "千米每小时"
		},
		{
			"Symbol": "m/s",
			"Name": "米每秒"
		},
		{
			"Symbol": "″",
			"Name": "秒"
		},
		{
			"Symbol": "′",
			"Name": "分"
		},
		{
			"Symbol": "°",
			"Name": "度"
		},
		{
			"Symbol": "rad",
			"Name": "弧度"
		},
		{
			"Symbol": "Hz",
			"Name": "赫兹"
		},
		{
			"Symbol": "μW",
			"Name": "微瓦"
		},
		{
			"Symbol": "mW",
			"Name": "毫瓦"
		},
		{
			"Symbol": "kW",
			"Name": "千瓦特"
		},
		{
			"Symbol": "W",
			"Name": "瓦特"
		},
		{
			"Symbol": "cal",
			"Name": "卡路里"
		},
		{
			"Symbol": "kW·h",
			"Name": "千瓦时"
		},
		{
			"Symbol": "Wh",
			"Name": "瓦时"
		},
		{
			"Symbol": "eV",
			"Name": "电子伏"
		},
		{
			"Symbol": "kJ",
			"Name": "千焦"
		},
		{
			"Symbol": "J",
			"Name": "焦耳"
		},
		{
			"Symbol": "℉",
			"Name": "华氏度"
		},
		{
			"Symbol": "K",
			"Name": "开尔文"
		},
		{
			"Symbol": "t",
			"Name": "吨"
		},
		{
			"Symbol": "°C",
			"Name": "摄氏度"
		},
		{
			"Symbol": "mPa",
			"Name": "毫帕"
		},
		{
			"Symbol": "hPa",
			"Name": "百帕"
		},
		{
			"Symbol": "kPa",
			"Name": "千帕"
		},
		{
			"Symbol": "Pa",
			"Name": "帕斯卡"
		},
		{
			"Symbol": "mg",
			"Name": "毫克"
		},
		{
			"Symbol": "g",
			"Name": "克"
		},
		{
			"Symbol": "kg",
			"Name": "千克"
		},
		{
			"Symbol": "N",
			"Name": "牛"
		},
		{
			"Symbol": "mL",
			"Name": "毫升"
		},
		{
			"Symbol": "L",
			"Name": "升"
		},
		{
			"Symbol": "mm³",
			"Name": "立方毫米"
		},
		{
			"Symbol": "cm³",
			"Name": "立方厘米"
		},
		{
			"Symbol": "km³",
			"Name": "立方千米"
		},
		{
			"Symbol": "m³",
			"Name": "立方米"
		},
		{
			"Symbol": "h㎡",
			"Name": "公顷"
		},
		{
			"Symbol": "c㎡",
			"Name": "平方厘米"
		},
		{
			"Symbol": "m㎡",
			"Name": "平方毫米"
		},
		{
			"Symbol": "k㎡",
			"Name": "平方千米"
		},
		{
			"Symbol": "㎡",
			"Name": "平方米"
		},
		{
			"Symbol": "nm",
			"Name": "纳米"
		},
		{
			"Symbol": "μm",
			"Name": "微米"
		},
		{
			"Symbol": "mm",
			"Name": "毫米"
		},
		{
			"Symbol": "cm",
			"Name": "厘米"
		},
		{
			"Symbol": "dm",
			"Name": "分米"
		},
		{
			"Symbol": "km",
			"Name": "千米"
		},
		{
			"Symbol": "m",
			"Name": "米"
		}
	],
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.Symbol | mg/kg | string | 单位英文名. 基本不变,建议缓存 |
| data.Name | 毫克每千克 | string | 单位中文名 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 物模型_插入功能

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-16 15:02:30

> 更新时间: 2023-03-06 15:17:45

**//属性,服务,事件 数据格式, 取值参考原型,//属性
{
"name": "属性名",
"key": "属性标识",
"dataType": "数据类型",
"permission": "操作权限",
"min": "最小值",
"max": "最大值",
"step": "步长",
"unit": "单位"
},//服务
{
"name": "服务名",
"key": "服务标识",
"invokeType":"调用类型",
"inputParam": [ ... ] //格式参考下方参数格式
"outputParam": [ ... ] //格式参考下方参数格式
},//事件
{
"name": "事件名",
"key": "事件标识",
"eventType":"事件类型",
"permission":"读写权限",
"inputParam": [ ... ] //格式参考下方参数格式
},//参数
{
"name": "属性名",
"key": "属性标识",
"dataType": "数据类型",
"min": "最小值",
"max": "最大值",
"step": "步长",
"unit": "单位"
}**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/insertThingFun

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | string | 是 | 产品key |
| funDetail | {      "identifier": "cpu_usage5",      "name": "CPU使用率5",      "accessMode": "rw",      "required": false,      "dataType": {        "type": "float",        "specs": {          "min": "0",          "max": "100",          "unit": "%",          "unitName": "百分比",          "step": "0.1"        }      }    } | string | 是 | 功能详情json, 格式参考: https://help.aliyun.com/document_detail/213902.html |
| funType | properties | string | 是 | 功能类型: properties=属性,services=服务,events=事件 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"modelId": 3,
		"thingModelJson": "{\"properties\":[{\"createTs\":1652148128115,\"custom\":true,\"customFlag\":true,\"dataSpecs\":{\"dataType\":\"FLOAT\",\"max\":\"100\",\"min\":\"0\",\"step\":\"0.1\",\"unit\":\"°C\",\"unitName\":\"摄氏度\"},\"dataType\":\"FLOAT\",\"description\":\"温度\",\"identifier\":\"Temperature\",\"name\":\"温度\",\"productKey\":\"h7s72qjeGaM\",\"required\":false,\"rwFlag\":\"READ_WRITE\",\"std\":false},{\"createTs\":1652148128115,\"custom\":true,\"customFlag\":true,\"dataSpecs\":{\"dataType\":\"FLOAT\",\"max\":\"100\",\"min\":\"0\",\"step\":\"0.1\",\"unit\":\"°C\",\"unitName\":\"摄氏度\"},\"dataType\":\"FLOAT\",\"description\":\"温度\",\"identifier\":\"Temperature2\",\"name\":\"温度\",\"productKey\":\"h7s72qjeGaM\",\"required\":false,\"rwFlag\":\"READ_WRITE\",\"std\":false}],\"services\":[],\"events\":[]}",
		"productKey": "h7s7PwecpHX",
		"createTime": "2022-06-22 03:43:36",
		"updateTime": "2022-06-22 05:54:30",
		"modelKey": null,
		"isFill": null
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.modelId | 3 | number | - |
| data.thingModelJson | {"properties":[{"createTs":1652148128115,"custom":true,"customFlag":true,"dataSpecs":{"dataType":"FLOAT","max":"100","min":"0","step":"0.1","unit":"°C","unitName":"摄氏度"},"dataType":"FLOAT","description":"温度","identifier":"Temperature","name":"温度","productKey":"h7s72qjeGaM","required":false,"rwFlag":"READ_WRITE","std":false},{"createTs":1652148128115,"custom":true,"customFlag":true,"dataSpecs":{"dataType":"FLOAT","max":"100","min":"0","step":"0.1","unit":"°C","unitName":"摄氏度"},"dataType":"FLOAT","description":"温度","identifier":"Temperature2","name":"温度","productKey":"h7s72qjeGaM","required":false,"rwFlag":"READ_WRITE","std":false}],"services":[],"events":[]} | string | 物模型json |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.createTime | 2022-06-22 03:43:36 | string | 创建时间 |
| data.updateTime | 2022-06-22 05:54:30 | string | 更新时间 |
| data.modelKey | - | object | - |
| data.isFill | - | object | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 物模型_更新功能

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-17 15:00:40

> 更新时间: 2022-11-08 14:54:05

**//属性,服务,事件 数据格式, 取值参考原型,//属性
{
"name": "属性名",
"key": "属性标识",
"dataType": "数据类型",
"permission": "操作权限",
"min": "最小值",
"max": "最大值",
"step": "步长",
"unit": "单位"
},//服务
{
"name": "服务名",
"key": "服务标识",
"invokeType":"调用类型",
"inputParam": [ ... ] //格式参考下方参数格式
"outputParam": [ ... ] //格式参考下方参数格式
},//事件
{
"name": "事件名",
"key": "事件标识",
"eventType":"事件类型",
"permission":"读写权限",
"inputParam": [ ... ] //格式参考下方参数格式
},//参数
{
"name": "属性名",
"key": "属性标识",
"dataType": "数据类型",
"min": "最小值",
"max": "最大值",
"step": "步长",
"unit": "单位"
}**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/updateThingFun

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | string | 是 | 产品key |
| funType | services | string | 是 | 功能类型: properties=属性,services=服务,events=事件 |
| funDetail | {      "custom": false,      "customFlag": false,      "dataSpecsList": [        {          "dataType": "BOOL",          "name": "关",          "value": 0        },        {          "dataType": "BOOL",          "name": "开",          "value": 1        }      ],      "dataType": "BOOL",      "description": "",      "identifier": "ChildLockSwitch2",      "serviceName": "童锁开关3",      "required": true,      "rwFlag": "READ_WRITE",      "std": true    } | string | 是 | 功能详情json |
| updateIdentifier | ChildLockSwitch2 | Text | 是 | 修改的功能的identifier |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"modelId": 1,
		"thingModelJson": "{\"events\":[{\"createTs\":1655799762332,\"custom\":true,\"eventName\":\"内容加载完成\",\"eventType\":\"INFO_EVENT_TYPE\",\"identifier\":\"UpdateContentCompleteEvent\",\"outputData\":[{\"custom\":true,\"dataSpecs\":{\"dataType\":\"TEXT\",\"length\":128},\"dataType\":\"TEXT\",\"direction\":\"PARAM_OUTPUT\",\"identifier\":\"UpdateTaskID\",\"name\":\"下发任务ID\",\"paraOrder\":0},{\"custom\":true,\"dataSpecs\":{\"dataType\":\"INT\",\"max\":\"1024\",\"min\":\"-1024\",\"precise\":0,\"step\":\"1\",\"unit\":\"\",\"unitName\":\"无\"},\"dataType\":\"INT\",\"direction\":\"PARAM_OUTPUT\",\"identifier\":\"Status\",\"name\":\"状态\",\"paraOrder\":1},{\"custom\":true,\"dataSpecs\":{\"childDataType\":\"STRUCT\",\"customFlag\":true,\"dataSpecsList\":[{\"childDataType\":\"TEXT\",\"childName\":\"内容创意ID\",\"childSpecsDTO\":{\"dataType\":\"TEXT\",\"length\":128},\"dataSpecs\":{\"dataType\":\"TEXT\",\"length\":128},\"dataType\":\"STRUCT\",\"identifier\":\"CreativeID\",\"name\":\"失败创意列表\"},{\"childDataType\":\"INT\",\"childName\":\"错误代码\",\"childSpecsDTO\":{\"dataType\":\"INT\",\"max\":\"1024\",\"min\":\"-1024\",\"precise\":0,\"step\":\"1\",\"unit\":\"\",\"unitName\":\"无\"},\"dataSpecs\":{\"dataType\":\"INT\",\"max\":\"1024\",\"min\":\"-1024\",\"precise\":0,\"step\":\"1\",\"unit\":\"\",\"unitName\":\"无\"},\"dataType\":\"STRUCT\",\"identifier\":\"Code\",\"name\":\"失败创意列表\"},{\"childDataType\":\"TEXT\",\"childName\":\"错误描述\",\"childSpecsDTO\":{\"dataType\":\"TEXT\",\"length\":1024},\"dataSpecs\":{\"dataType\":\"TEXT\",\"length\":1024},\"dataType\":\"STRUCT\",\"identifier\":\"Message\",\"name\":\"失败创意列表\"}],\"dataType\":\"ARRAY\",\"size\":128},\"dataType\":\"ARRAY\",\"direction\":\"PARAM_OUTPUT\",\"identifier\":\"FailedCreativeIDs\",\"name\":\"失败创意列表\",\"paraOrder\":2}],\"productKey\":\"h7s72qjeGaM\",\"required\":false}],\"properties\":[{\"createTs\":1652148141379,\"custom\":true,\"customFlag\":true,\"dataSpecs\":{\"dataType\":\"FLOAT\",\"max\":\"100\",\"min\":\"0\",\"step\":\"0.1\",\"unit\":\"%RH\",\"unitName\":\"相对湿度\"},\"dataType\":\"FLOAT\",\"description\":\"湿度\",\"identifier\":\"Humidity\",\"name\":\"湿度\",\"productKey\":\"h7s72qjeGaM\",\"required\":false,\"rwFlag\":\"READ_WRITE\",\"std\":false},{\"createTs\":1652148128115,\"custom\":true,\"customFlag\":true,\"dataSpecs\":{\"dataType\":\"FLOAT\",\"max\":\"100\",\"min\":\"0\",\"step\":\"0.1\",\"unit\":\"°C\",\"unitName\":\"摄氏度\"},\"dataType\":\"FLOAT\",\"description\":\"温度2\",\"identifier\":\"Temperature\",\"name\":\"温度2\",\"productKey\":\"h7s72qjeGaM\",\"required\":false,\"rwFlag\":\"READ_WRITE\",\"std\":false}],\"services\":[{\"callType\":\"SYNC\",\"createTs\":1655799752090,\"custom\":true,\"identifier\":\"DeleteModel\",\"inputParams\":[{\"custom\":true,\"dataSpecs\":{\"dataType\":\"TEXT\",\"length\":128},\"dataType\":\"TEXT\",\"direction\":\"PARAM_INPUT\",\"identifier\":\"AlgorithmID\",\"name\":\"算法任务唯一标识\",\"paraOrder\":0}],\"outputParams\":[],\"productKey\":\"h7s72qjeGaM\",\"required\":false,\"serviceName\":\"删除模型\"}]}",
		"productKey": "h7s7PwecpHX",
		"createTime": "2022-06-21 09:04:45",
		"updateTime": "2022-06-22 03:03:54",
		"modelKey": null,
		"isFill": null
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.modelId | 1 | number | - |
| data.thingModelJson | {"events":[{"createTs":1655799762332,"custom":true,"eventName":"内容加载完成","eventType":"INFO_EVENT_TYPE","identifier":"UpdateContentCompleteEvent","outputData":[{"custom":true,"dataSpecs":{"dataType":"TEXT","length":128},"dataType":"TEXT","direction":"PARAM_OUTPUT","identifier":"UpdateTaskID","name":"下发任务ID","paraOrder":0},{"custom":true,"dataSpecs":{"dataType":"INT","max":"1024","min":"-1024","precise":0,"step":"1","unit":"","unitName":"无"},"dataType":"INT","direction":"PARAM_OUTPUT","identifier":"Status","name":"状态","paraOrder":1},{"custom":true,"dataSpecs":{"childDataType":"STRUCT","customFlag":true,"dataSpecsList":[{"childDataType":"TEXT","childName":"内容创意ID","childSpecsDTO":{"dataType":"TEXT","length":128},"dataSpecs":{"dataType":"TEXT","length":128},"dataType":"STRUCT","identifier":"CreativeID","name":"失败创意列表"},{"childDataType":"INT","childName":"错误代码","childSpecsDTO":{"dataType":"INT","max":"1024","min":"-1024","precise":0,"step":"1","unit":"","unitName":"无"},"dataSpecs":{"dataType":"INT","max":"1024","min":"-1024","precise":0,"step":"1","unit":"","unitName":"无"},"dataType":"STRUCT","identifier":"Code","name":"失败创意列表"},{"childDataType":"TEXT","childName":"错误描述","childSpecsDTO":{"dataType":"TEXT","length":1024},"dataSpecs":{"dataType":"TEXT","length":1024},"dataType":"STRUCT","identifier":"Message","name":"失败创意列表"}],"dataType":"ARRAY","size":128},"dataType":"ARRAY","direction":"PARAM_OUTPUT","identifier":"FailedCreativeIDs","name":"失败创意列表","paraOrder":2}],"productKey":"h7s72qjeGaM","required":false}],"properties":[{"createTs":1652148141379,"custom":true,"customFlag":true,"dataSpecs":{"dataType":"FLOAT","max":"100","min":"0","step":"0.1","unit":"%RH","unitName":"相对湿度"},"dataType":"FLOAT","description":"湿度","identifier":"Humidity","name":"湿度","productKey":"h7s72qjeGaM","required":false,"rwFlag":"READ_WRITE","std":false},{"createTs":1652148128115,"custom":true,"customFlag":true,"dataSpecs":{"dataType":"FLOAT","max":"100","min":"0","step":"0.1","unit":"°C","unitName":"摄氏度"},"dataType":"FLOAT","description":"温度2","identifier":"Temperature","name":"温度2","productKey":"h7s72qjeGaM","required":false,"rwFlag":"READ_WRITE","std":false}],"services":[{"callType":"SYNC","createTs":1655799752090,"custom":true,"identifier":"DeleteModel","inputParams":[{"custom":true,"dataSpecs":{"dataType":"TEXT","length":128},"dataType":"TEXT","direction":"PARAM_INPUT","identifier":"AlgorithmID","name":"算法任务唯一标识","paraOrder":0}],"outputParams":[],"productKey":"h7s72qjeGaM","required":false,"serviceName":"删除模型"}]} | string | 物模型json |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.createTime | 2022-06-21 09:04:45 | string | 创建时间 |
| data.updateTime | 2022-06-22 03:03:54 | string | 更新时间 |
| data.modelKey | - | object | - |
| data.isFill | - | object | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 物模型_删除功能

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-17 15:42:49

> 更新时间: 2022-10-28 10:04:50

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/deleteThingFun

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 产品key |
| funType | properties | Text | 是 | 功能类型: properties=属性,services=服务,events=事件 |
| funDetail | {"identifier": "cpu_usage4" } | Text | 是 | 功能详情json |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"modelId": 1,
		"thingModelJson": "{\"events\":[{\"createTs\":1655799762332,\"custom\":true,\"eventName\":\"内容加载完成\",\"eventType\":\"INFO_EVENT_TYPE\",\"identifier\":\"UpdateContentCompleteEvent\",\"outputData\":[{\"custom\":true,\"dataSpecs\":{\"dataType\":\"TEXT\",\"length\":128},\"dataType\":\"TEXT\",\"direction\":\"PARAM_OUTPUT\",\"identifier\":\"UpdateTaskID\",\"name\":\"下发任务ID\",\"paraOrder\":0},{\"custom\":true,\"dataSpecs\":{\"dataType\":\"INT\",\"max\":\"1024\",\"min\":\"-1024\",\"precise\":0,\"step\":\"1\",\"unit\":\"\",\"unitName\":\"无\"},\"dataType\":\"INT\",\"direction\":\"PARAM_OUTPUT\",\"identifier\":\"Status\",\"name\":\"状态\",\"paraOrder\":1},{\"custom\":true,\"dataSpecs\":{\"childDataType\":\"STRUCT\",\"customFlag\":true,\"dataSpecsList\":[{\"childDataType\":\"TEXT\",\"childName\":\"内容创意ID\",\"childSpecsDTO\":{\"dataType\":\"TEXT\",\"length\":128},\"dataSpecs\":{\"dataType\":\"TEXT\",\"length\":128},\"dataType\":\"STRUCT\",\"identifier\":\"CreativeID\",\"name\":\"失败创意列表\"},{\"childDataType\":\"INT\",\"childName\":\"错误代码\",\"childSpecsDTO\":{\"dataType\":\"INT\",\"max\":\"1024\",\"min\":\"-1024\",\"precise\":0,\"step\":\"1\",\"unit\":\"\",\"unitName\":\"无\"},\"dataSpecs\":{\"dataType\":\"INT\",\"max\":\"1024\",\"min\":\"-1024\",\"precise\":0,\"step\":\"1\",\"unit\":\"\",\"unitName\":\"无\"},\"dataType\":\"STRUCT\",\"identifier\":\"Code\",\"name\":\"失败创意列表\"},{\"childDataType\":\"TEXT\",\"childName\":\"错误描述\",\"childSpecsDTO\":{\"dataType\":\"TEXT\",\"length\":1024},\"dataSpecs\":{\"dataType\":\"TEXT\",\"length\":1024},\"dataType\":\"STRUCT\",\"identifier\":\"Message\",\"name\":\"失败创意列表\"}],\"dataType\":\"ARRAY\",\"size\":128},\"dataType\":\"ARRAY\",\"direction\":\"PARAM_OUTPUT\",\"identifier\":\"FailedCreativeIDs\",\"name\":\"失败创意列表\",\"paraOrder\":2}],\"productKey\":\"h7s72qjeGaM\",\"required\":false}],\"properties\":[{\"createTs\":1652148141379,\"custom\":true,\"customFlag\":true,\"dataSpecs\":{\"dataType\":\"FLOAT\",\"max\":\"100\",\"min\":\"0\",\"step\":\"0.1\",\"unit\":\"%RH\",\"unitName\":\"相对湿度\"},\"dataType\":\"FLOAT\",\"description\":\"湿度\",\"identifier\":\"Humidity\",\"name\":\"湿度\",\"productKey\":\"h7s72qjeGaM\",\"required\":false,\"rwFlag\":\"READ_WRITE\",\"std\":false}],\"services\":[{\"callType\":\"SYNC\",\"createTs\":1655799752090,\"custom\":true,\"identifier\":\"DeleteModel\",\"inputParams\":[{\"custom\":true,\"dataSpecs\":{\"dataType\":\"TEXT\",\"length\":128},\"dataType\":\"TEXT\",\"direction\":\"PARAM_INPUT\",\"identifier\":\"AlgorithmID\",\"name\":\"算法任务唯一标识\",\"paraOrder\":0}],\"outputParams\":[],\"productKey\":\"h7s72qjeGaM\",\"required\":false,\"serviceName\":\"删除模型\"}]}",
		"productKey": "h7s7PwecpHX",
		"createTime": "2022-06-21 09:04:45",
		"updateTime": "2022-06-22 03:05:56",
		"modelKey": null,
		"isFill": null
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.modelId | 1 | number | - |
| data.thingModelJson | {"events":[{"createTs":1655799762332,"custom":true,"eventName":"内容加载完成","eventType":"INFO_EVENT_TYPE","identifier":"UpdateContentCompleteEvent","outputData":[{"custom":true,"dataSpecs":{"dataType":"TEXT","length":128},"dataType":"TEXT","direction":"PARAM_OUTPUT","identifier":"UpdateTaskID","name":"下发任务ID","paraOrder":0},{"custom":true,"dataSpecs":{"dataType":"INT","max":"1024","min":"-1024","precise":0,"step":"1","unit":"","unitName":"无"},"dataType":"INT","direction":"PARAM_OUTPUT","identifier":"Status","name":"状态","paraOrder":1},{"custom":true,"dataSpecs":{"childDataType":"STRUCT","customFlag":true,"dataSpecsList":[{"childDataType":"TEXT","childName":"内容创意ID","childSpecsDTO":{"dataType":"TEXT","length":128},"dataSpecs":{"dataType":"TEXT","length":128},"dataType":"STRUCT","identifier":"CreativeID","name":"失败创意列表"},{"childDataType":"INT","childName":"错误代码","childSpecsDTO":{"dataType":"INT","max":"1024","min":"-1024","precise":0,"step":"1","unit":"","unitName":"无"},"dataSpecs":{"dataType":"INT","max":"1024","min":"-1024","precise":0,"step":"1","unit":"","unitName":"无"},"dataType":"STRUCT","identifier":"Code","name":"失败创意列表"},{"childDataType":"TEXT","childName":"错误描述","childSpecsDTO":{"dataType":"TEXT","length":1024},"dataSpecs":{"dataType":"TEXT","length":1024},"dataType":"STRUCT","identifier":"Message","name":"失败创意列表"}],"dataType":"ARRAY","size":128},"dataType":"ARRAY","direction":"PARAM_OUTPUT","identifier":"FailedCreativeIDs","name":"失败创意列表","paraOrder":2}],"productKey":"h7s72qjeGaM","required":false}],"properties":[{"createTs":1652148141379,"custom":true,"customFlag":true,"dataSpecs":{"dataType":"FLOAT","max":"100","min":"0","step":"0.1","unit":"%RH","unitName":"相对湿度"},"dataType":"FLOAT","description":"湿度","identifier":"Humidity","name":"湿度","productKey":"h7s72qjeGaM","required":false,"rwFlag":"READ_WRITE","std":false}],"services":[{"callType":"SYNC","createTs":1655799752090,"custom":true,"identifier":"DeleteModel","inputParams":[{"custom":true,"dataSpecs":{"dataType":"TEXT","length":128},"dataType":"TEXT","direction":"PARAM_INPUT","identifier":"AlgorithmID","name":"算法任务唯一标识","paraOrder":0}],"outputParams":[],"productKey":"h7s72qjeGaM","required":false,"serviceName":"删除模型"}]} | string | 物模型json |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.createTime | 2022-06-21 09:04:45 | string | 创建时间 |
| data.updateTime | 2022-06-22 03:05:56 | string | 更新时间 |
| data.modelKey | - | object | - |
| data.isFill | - | object | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 导出物模型文件

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-30 15:59:11

> 更新时间: 2023-06-30 16:04:59

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/exportThingModel?productKey=iy4uX2jWJz1

**请求方式**

> POST

**Content-Type**

> urlencoded

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uX2jWJz1 | string | 是 | 产品key |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"byteArray":[{}],"description":""}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| byteArray | - | array | - |
| description | - | string | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 导入物模型文件

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-30 15:40:16

> 更新时间: 2023-07-05 10:02:29

**导入文件示例:,{"schema":"https://iotx-tsl.oss-ap-southeast-1.aliyuncs.com/schema.json","profile":{"version":"1.5","productKey":"iy4uJzbjy1H"},"properties":[{"name":"温度","identifier":"temperature","required":false,"accessMode":"rw","dataType":{"type":"float","specs":{"min":"0","max":"100","step":"0.01","unitName":"摄氏度","unit":"°C"}}},{"name":"湿度","identifier":"humidity","required":false,"accessMode":"r","dataType":{"type":"float","specs":{"min":"0","max":"100","step":"0.01","unitName":"相对湿度","unit":"%RH"}}}],"services":[{"name":"服务2","identifier":"service2","callType":"async","required":false,"inputData":[{"name":"参数1","identifier":"param1","required":false,"dataType":{"type":"int","specs":{"min":"0","max":"100","step":"1","unitName":"无"}}}],"outputData":[],"method":"thing.service.service2"},{"name":"服务1","identifier":"service1","callType":"async","required":false,"inputData":[{"name":"参数1","identifier":"param1","required":false,"dataType":{"type":"int","specs":{"min":"0","max":"100","step":"1","unitName":"无"}}}],"outputData":[],"method":"thing.service.service1"}],"events":[]}**

**[object Object]**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/importThingModel

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| file | - | string | 是 | - |
| productKey | iy4uX2jWJz1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 物模型json示例

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-10-24 11:19:39

> 更新时间: 2022-10-24 11:18:38

**[object Object]**

**Query**

# 设备模型(产品)

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-16 10:56:27

> 更新时间: 2022-12-07 16:13:14

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 设备模型列表和搜索

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 13:40:22

> 更新时间: 2023-12-29 10:41:06

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/listSearch?sort=createTime,desc&projectId=2

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | 0 | Text | 否 | 页数 |
| size | 10 | Text | 否 | 每页元素个数 |
| sort | createTime,desc | Text | 否 | 排序 |
| nodeType | 2 | Text | 否 | 设备类型:0=直连设备,1=网关设备,2=非直连子设备 |
| productName | 测试 | Text | 否 | 产品名 |
| projectId | 2 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"iotInstanceId": "iot-06z00ei6cjy8564",
				"productName": "接口测试产品_fTbbB",
				"productNameNote": "接口测试产品",
				"productKey": "h7s71pvlJzx",
				"productSecret": "RaKGl4fGYaMtXPGB",
				"code": "",
				"deviceCnt": 0,
				"nodeType": 0,
				"userId": 0,
				"description": "沃尔沃二",
				"categoryKey": "无",
				"netType": "WIFI",
				"dataFormat": 1,
				"authType": "secret",
				"createTime": "2022-06-20 03:08:04",
				"updateTime": "2022-06-20 03:08:04",
				"productStatus": null,
				"joinPermissionId": null,
				"projectId": 3
			},
			{
				"iotInstanceId": "iot-06z00ei6cjy8564",
				"productName": "test2_uP0HV",
				"productNameNote": "test2",
				"productKey": "h7s72qjeGaM",
				"productSecret": "gDn4fyiWN3ERo8FR",
				"code": "",
				"deviceCnt": 0,
				"nodeType": 0,
				"userId": 0,
				"description": "沃尔沃二",
				"categoryKey": "路灯照明",
				"netType": null,
				"dataFormat": 1,
				"authType": "secret",
				"createTime": "2022-06-02 03:29:45",
				"updateTime": "2022-09-06 01:46:33",
				"productStatus": 1,
				"joinPermissionId": null,
				"projectId": 3
			}
		],
		"last": true,
		"totalElements": 2,
		"totalPages": 1,
		"number": 0,
		"size": 20,
		"sort": [
			{
				"direction": "DESC",
				"property": "createTime",
				"ignoreCase": false,
				"nullHandling": "NATIVE",
				"ascending": false,
				"descending": true
			}
		],
		"first": true,
		"numberOfElements": 2
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | array | 参考产品详情 |
| data.content.iotInstanceId | iot-06z00ei6cjy8564 | string | - |
| data.content.productName | 接口测试产品_fTbbB | string | 产品名(阿里云平台) |
| data.content.productNameNote | 接口测试产品 | string | 产品名 |
| data.content.productKey | h7s71pvlJzx | string | 产品标识 |
| data.content.productSecret | RaKGl4fGYaMtXPGB | string | 产品秘钥 |
| data.content.code | - | string | - |
| data.content.deviceCnt | 0 | integer | 设备数 |
| data.content.nodeType | 0 | integer | 设备类型: |
| data.content.userId | 0 | integer | 用户id |
| data.content.description | 沃尔沃二 | string | 描述 |
| data.content.categoryKey | 无 | string | 产品物模型 |
| data.content.netType | WIFI | string | 联网方式:WIFI=wifi,CELLULAR=2/3/4/5G/NB-IoT,ETHERNET=以太网 |
| data.content.dataFormat | 1 | integer | 数据格式:0=自定义,1=json |
| data.content.authType | secret | string | 认证方式:secret=设备秘钥,x509=x509证书 |
| data.content.createTime | 2022-06-20 03:08:04 | string | 创建时间 |
| data.content.updateTime | 2022-06-20 03:08:04 | string | 更新时间 |
| data.content.productStatus | null | null | 产品状态: 0=未发布,1=已发布 |
| data.content.joinPermissionId | null | null | 接入网关协议:modbus,opc-ua,customize,ble,zigbee |
| data.content.projectId | 3 | integer | - |
| data.last | true | boolean | 最后一页 |
| data.totalElements | 2 | integer | 总元素数 |
| data.totalPages | 1 | integer | 总页数 |
| data.number | 0 | integer | 当前页数 |
| data.size | 20 | integer | 每页数 |
| data.sort | - | array | 排序信息 |
| data.sort.direction | DESC | string | - |
| data.sort.property | createTime | string | 属性名 |
| data.sort.ignoreCase | false | boolean | - |
| data.sort.nullHandling | NATIVE | string | - |
| data.sort.ascending | false | boolean | - |
| data.sort.descending | true | boolean | - |
| data.first | true | boolean | 是否是第一页 |
| data.numberOfElements | 2 | integer | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备模型新建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 14:25:14

> 更新时间: 2025-04-14 15:41:04

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productName | testx3 | Text | 是 | 产品名 |
| nodeType | 2 | Text | 是 | 设备类型: 0=直连设备,1=网关设备,2=非直连子设备 |
| netType | WiFi | Text | 否 | 联网方式: WiFi, 蓝牙(BlueTooth), 蜂窝(Cellular), 以太网(Ethernet), LoRaWAN |
| authType | secret | Text | 是 | 认证方式: secret=设备秘钥,x509=x509证书 |
| categoryKey | Lighting | Text | 否 | 物模型模板, 模型标识,自定义传空 |
| dataFormat | 1 | Text | 否 | 数据格式: 0=自定义,1=json |
| description | 沃尔沃二 | Text | 否 | 备注 |
| projectId | 2 | Text | 是 | 工程id |
| productType | Modbus | Text | 否 | 接入协议: Modbus, OPC UA(OPCUA), ZigBee, BLE, 自定义(Custom) |
| linkObj | real | Text | 是 | 映射对象: virtual=虚拟设备,real=硬件设备,virtualReal=虚实联动设备 |
| belong | private | Text | 是 | 模型归属: public=租户共用,private=工程私有 |
| dataParseRule | - | string | 是 | 数据解析规则 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"iotInstanceId": "iot-06z00ei6cjy8564",
		"productName": "testx3_dBuqI",
		"productNameNote": "testx3",
		"productKey": "h7s7a0lUxNh",
		"productSecret": "koZCuCxJTPgrzyQ5",
		"code": "",
		"deviceCnt": 0,
		"nodeType": 2,
		"userId": 0,
		"description": "沃尔沃二",
		"categoryKey": "Lighting",
		"netType": "WiFi",
		"dataFormat": 1,
		"authType": "secret",
		"createTime": "2023-03-02 10:23:58",
		"updateTime": "2023-03-02 10:23:58",
		"productStatus": 0,
		"joinPermissionId": null,
		"projectId": 2,
		"protocolType": null,
		"linkObj": "real"
	},
	"requestId": "f6cb3f3ba54a4a108c837f5682989acc",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.iotInstanceId | iot-06z00ei6cjy8564 | string | - |
| data.productName | testx3_dBuqI | string | 产品名(阿里云平台) |
| data.productNameNote | testx3 | string | 产品名 |
| data.productKey | h7s7a0lUxNh | string | 产品标识 |
| data.productSecret | koZCuCxJTPgrzyQ5 | string | 产品秘钥 |
| data.code | - | object | - |
| data.deviceCnt | 0 | object | 设备数 |
| data.nodeType | 2 | number | 设备类型: |
| data.userId | 0 | object | 用户id |
| data.description | 沃尔沃二 | string | 描述 |
| data.categoryKey | Lighting | object | 产品物模型 |
| data.netType | WiFi | string | 联网方式:WIFI=wifi,CELLULAR=2/3/4/5G/NB-IoT,ETHERNET=以太网 |
| data.dataFormat | 1 | number | 数据格式:0=自定义,1=json |
| data.authType | secret | string | 认证方式:secret=设备秘钥,x509=x509证书 |
| data.createTime | 2023-03-02 10:23:58 | object | 创建时间 |
| data.updateTime | 2023-03-02 10:23:58 | object | 更新时间 |
| data.productStatus | 0 | object | 产品状态 |
| data.joinPermissionId | - | object | 接入网关协议:modbus,opc-ua,customize,ble,zigbee |
| data.projectId | 2 | number | 工程id |
| data.protocolType | - | object | - |
| data.linkObj | real | string | 映射对象 |
| requestId | f6cb3f3ba54a4a108c837f5682989acc | string | 请求唯一id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 批量导入产品

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-30 09:06:28

> 更新时间: 2023-06-30 10:48:02

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/importProducts

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| file | - | string | 是 | - |
| projectId | 107 | integer | 是 | 项目id |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 获取导入模板文件

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-30 11:39:10

> 更新时间: 2023-06-30 11:39:54

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/common/getExampleFile?fileName=设备模型导入模板.xlsx

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| fileName | 设备模型导入模板.xlsx | Text | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"file":{"path":"","status":"","prefixLength":"","filePath":{"fileSystem":{},"absolute":"","root":{},"fileName":{},"parent":{},"nameCount":"","name":{}}},"path":""}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| file | - | object | - |
| file.path | - | string | This abstract pathname's normalized pathname string. A normalized |
| file.status | - | string | The flag indicating whether the file path is invalid. (INVALID, CHECKED) |
| file.prefixLength | - | integer | The length of this abstract pathname's prefix, or zero if it has no |
| file.filePath | - | object | - |
| file.filePath.fileSystem | - | object | - |
| file.filePath.absolute | - | boolean | - |
| file.filePath.root | - | object | - |
| file.filePath.fileName | - | object | - |
| file.filePath.parent | - | object | - |
| file.filePath.nameCount | - | integer | - |
| file.filePath.name | - | object | - |
| path | - | string | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备模型修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-07 17:13:06

> 更新时间: 2025-04-14 15:41:14

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | string | 是 | 产品key |
| productNameNote | hjkjhkj | string | 否 | 产品名 |
| description | asdf | string | 否 | 描述 |
| dataParseRule | - | string | 是 | 数据解析规则 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备模型删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 14:09:12

> 更新时间: 2022-10-24 11:33:38

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/delete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": null,
	"status": "S",
	"sysMsg": "操作成功"
}
```

* 失败(404)

```javascript
{
	"data": null,
	"status": "F",
	"sysMsg": "产品不存在"
}
```

**Query**

## 设备模型详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 14:08:10

> 更新时间: 2022-10-24 11:33:39

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/get?productKey=iy4uY75WdQj

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"iotInstanceId": "iot-06z00ei6cjy8564",
		"productName": "test1_uP0HV",
		"productNameNote": "test1",
		"productKey": "h7s74Od2Awn",
		"productSecret": "gDn4fyiWN3ERo8FR",
		"code": "",
		"deviceCnt": null,
		"nodeType": 0,
		"userId": null,
		"description": "沃尔沃二",
		"categoryKey": "Lighting",
		"netType": null,
		"dataFormat": 1,
		"authType": "secret",
		"createTime": 1654140585000,
		"updateTime": 1654746874000,
		"productStatus": 1,
		"joinPermissionId": null
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.iotInstanceId | iot-06z00ei6cjy8564 | string | - |
| data.productName | test1_uP0HV | string | 产品名(阿里云平台) |
| data.productNameNote | test1 | string | 产品名 |
| data.productKey | h7s74Od2Awn | string | 产品标识 |
| data.productSecret | gDn4fyiWN3ERo8FR | string | 产品秘钥 |
| data.code | - | object | - |
| data.deviceCnt | - | object | 设备数量 |
| data.nodeType | 0 | number | 设备类型:0=直连设备,1=网关设备,2=非直连子设备 |
| data.userId | - | object | 用户id |
| data.description | 沃尔沃二 | string | 描述 |
| data.categoryKey | Lighting | string | 设备模型识别码 |
| data.netType | - | object | 联网方式:WIFI=wifi,CELLULAR=2/3/4/5G/NB-IoT,ETHERNET=以太网 |
| data.dataFormat | 1 | number | 数据格式:0=自定义,1=json |
| data.authType | secret | string | 认证方式:secret=设备秘钥,x509=x509证书 |
| data.createTime | 1654140585000 | number | 创建时间 |
| data.updateTime | 1654746874000 | number | 更新时间 |
| data.productStatus | 1 | number | 产品状态:0=开发中,1=已发布 |
| data.joinPermissionId | - | object | 接入网关协议:modbus,opc-ua,customize,ble,zigbee |
| status | S | string | 状态: S=成功, F=失败 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 简单设备模型列表_用于模型选择

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-25 16:24:22

> 更新时间: 2023-06-05 15:59:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/simpleList

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 2 | Text | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": [
		{
			"productNameNote": "接口测试产品",
			"productKey": "h7s71pvlJzx"
		},
		{
			"productNameNote": "test2",
			"productKey": "h7s72qjeGaM"
		},
		{
			"productNameNote": "test1",
			"productKey": "h7s77I86w61"
		},
		{
			"productNameNote": null,
			"productKey": "h7s77Ko9bcX"
		},
		{
			"productNameNote": "厂家测试",
			"productKey": "h7s78fVAG3A"
		},
		{
			"productNameNote": "1111",
			"productKey": "h7s7AY04IUu"
		},
		{
			"productNameNote": "testasdaq012",
			"productKey": "h7s7BNvkt1h"
		},
		{
			"productNameNote": "test23",
			"productKey": "h7s7bRfUjbq"
		},
		{
			"productNameNote": "test5",
			"productKey": "h7s7EcTiWxQ"
		},
		{
			"productNameNote": "test",
			"productKey": "h7s7fJKsRpc"
		},
		{
			"productNameNote": "test22",
			"productKey": "h7s7G8fPTEu"
		},
		{
			"productNameNote": "test54",
			"productKey": "h7s7H7kfhxS"
		},
		{
			"productNameNote": "testasda",
			"productKey": "h7s7HHHDj2n"
		},
		{
			"productNameNote": "test21",
			"productKey": "h7s7Hm12Fx9"
		},
		{
			"productNameNote": "test24",
			"productKey": "h7s7HTd4Jdl"
		},
		{
			"productNameNote": "we",
			"productKey": "h7s7huXA47j"
		},
		{
			"productNameNote": "test2",
			"productKey": "h7s7INGrAZ5"
		},
		{
			"productNameNote": null,
			"productKey": "h7s7jysyiJ0"
		},
		{
			"productNameNote": "test51",
			"productKey": "h7s7LQ5ReHS"
		},
		{
			"productNameNote": "344",
			"productKey": "h7s7n5LDyCM"
		},
		{
			"productNameNote": "testasdaq01",
			"productKey": "h7s7nQnmKQk"
		},
		{
			"productNameNote": "test",
			"productKey": "h7s7NxjuhLw"
		},
		{
			"productNameNote": "接口测试产品199",
			"productKey": "h7s7OykfA3p"
		},
		{
			"productNameNote": "we",
			"productKey": "h7s7p5WbVKq"
		},
		{
			"productNameNote": "test4",
			"productKey": "h7s7PwecpHX"
		},
		{
			"productNameNote": "haveThing",
			"productKey": "h7s7q14YOoF"
		},
		{
			"productNameNote": "test3",
			"productKey": "h7s7QflDAUH"
		},
		{
			"productNameNote": "3234234",
			"productKey": "h7s7QUiUg3w"
		},
		{
			"productNameNote": "testasd",
			"productKey": "h7s7sZRKxLY"
		},
		{
			"productNameNote": "2222",
			"productKey": "h7s7Tho9mFD"
		},
		{
			"productNameNote": "test52",
			"productKey": "h7s7TqnPDxJ"
		},
		{
			"productNameNote": "testasdaq",
			"productKey": "h7s7uR3fApg"
		},
		{
			"productNameNote": null,
			"productKey": "h7s7W8BVAKo"
		},
		{
			"productNameNote": "test53",
			"productKey": "h7s7WlXim8b"
		}
	],
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.productNameNote | 接口测试产品 | string | 产品名 |
| data.productKey | h7s71pvlJzx | string | 产品key |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备模型发布

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-10-19 16:29:26

> 更新时间: 2022-10-24 11:33:41

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/release

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | h7s7aSewTsm | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": null,
	"status": "S",
	"sysMsg": "操作成功"
}
```

* 失败(201)

```javascript
{
	"data": null,
	"status": "F",
	"sysMsg": "产品不存在"
}
```

**Query**

# 设备

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-16 10:55:51

> 更新时间: 2022-06-16 10:55:51

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 设备实例列表和搜索

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 14:26:36

> 更新时间: 2026-07-24 15:07:52

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/listSearch?page=0&size=10&sort=&projectId=113

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | 0 | Text | 否 | 分页页码，数字类型 |
| size | 10 | Text | 否 | 每页元素个数 |
| sort | - | Text | 否 | 排序 |
| productKey | iy4uY75WdQj | Text | 否 | 产品名 |
| nodeType | 0 | Text | 否 | 设备类型:0=直连设备,1=网关设备,2=非直连子设备 |
| deviceName | 12 | Text | 否 | 设备名称或uuid |
| projectId | 113 | Text | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"last": true,
		"totalPages": 1,
		"totalElements": 2,
		"number": 0,
		"size": 10,
		"content": [
			{
				"description": null,
				"version": "15.0",
				"labels": null,
				"status": "ONLINE",
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_2",
				"iotId": "LMpSMbqSYBYepOd2aJbRh7s700",
				"userId": 0,
				"createTime": null,
				"deviceSecret": null,
				"destVersion": "16.0",
				"updateTime": "2022-07-05 14:26:20",
				"srcIotId": null,
				"joinEui": null,
				"nickname": null,
				"activeTime": "2022-07-04 15:59:13",
				"productNameNote": "test2",
				"nodeType": 0,
				"workUpdateTime": "",
				"scenes": null
			},
			{
				"description": null,
				"version": "15.0",
				"labels": null,
				"status": "OFFLINE",
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"iotId": "XUbvGwMcOCvmEz6Rbi71h7s700",
				"userId": 0,
				"createTime": null,
				"deviceSecret": null,
				"destVersion": "16.0",
				"updateTime": "2022-07-05 14:26:20",
				"srcIotId": null,
				"joinEui": null,
				"nickname": null,
				"activeTime": "2022-07-04 15:59:13",
				"productNameNote": "test2",
				"nodeType": 0,
				"workUpdateTime": "2022-11-21 15:38:06",
				"scenes": [
					"场景名称"
				]
			}
		],
		"sort": null,
		"first": true,
		"numberOfElements": 2
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.last | true | string | 最后一页 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 2 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 10 | number | 每页元素个数 |
| data.content | - | object | 消息详情 |
| data.content.description | - | object | 描述 |
| data.content.version | 15.0 | string | 版本 |
| data.content.labels | - | object | 设备标签 |
| data.content.status | ONLINE | string | 设备状态:ONLINE=设备在线,OFFLINE=设备离线,UNACTIVE=设备未激活,DISABLE=设备已禁用 |
| data.content.productKey | h7s72qjeGaM | string | 产品key |
| data.content.deviceName | test2_2 | string | 设备名称 |
| data.content.iotId | LMpSMbqSYBYepOd2aJbRh7s700 | string | 设备全局id |
| data.content.userId | 0 | object | 用户id |
| data.content.createTime | - | number | 创建时间 |
| data.content.deviceSecret | - | string | 设备秘钥 |
| data.content.destVersion | 16.0 | string | 目标版本 |
| data.content.updateTime | 2022-07-05 14:26:20 | string | 更新时间 |
| data.content.srcIotId | - | object | - |
| data.content.joinEui | - | object | - |
| data.content.nickname | - | object | 设备备注名 |
| data.content.activeTime | 2022-07-04 15:59:13 | string | 激活时间 |
| data.content.productNameNote | test2 | string | 产品名 |
| data.content.nodeType | 0 | number | 节点类型 |
| data.content.workUpdateTime | - | object | 工况更新时间 |
| data.content.scenes | - | object | 关联场景 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 2 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备实例列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-29 14:22:05

> 更新时间: 2026-03-06 11:46:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/list?productKey=iy4uY75WdQj&page=0&size=5

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 产品key |
| page | 0 | Text | 否 | 分页页码，数字类型 |
| size | 5 | Text | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"iotId": "LMpSMbqSYBYepOd2aJbRh7s700",
				"deviceSecret": null,
				"productKey": "h7s72qjeGaM",
				"joinEui": null,
				"deviceName": "test2_2",
				"nickname": null,
				"createTime": null,
				"userId": 0,
				"status": "ONLINE",
				"labels": null,
				"description": null,
				"updateTime": "2022-07-05 02:26:20",
				"activeTime": "2022-07-04 03:59:13",
				"version": "15.0",
				"destVersion": "16.0",
				"srcIotId": null
			},
			{
				"iotId": "XUbvGwMcOCvmEz6Rbi71h7s700",
				"deviceSecret": null,
				"productKey": "h7s72qjeGaM",
				"joinEui": null,
				"deviceName": "test2_1",
				"nickname": null,
				"createTime": null,
				"userId": 0,
				"status": "OFFLINE",
				"labels": null,
				"description": null,
				"updateTime": "2022-07-05 02:26:20",
				"activeTime": "2022-07-04 03:59:13",
				"version": "15.0",
				"destVersion": "16.0",
				"srcIotId": null
			}
		],
		"last": true,
		"totalPages": 1,
		"totalElements": 2,
		"number": 0,
		"size": 20,
		"sort": null,
		"first": true,
		"numberOfElements": 2
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | array | 消息详情 |
| data.content.iotId | LMpSMbqSYBYepOd2aJbRh7s700 | string | 设备全局id |
| data.content.deviceSecret | null | null | 设备秘钥 |
| data.content.productKey | h7s72qjeGaM | string | 产品key |
| data.content.joinEui | null | null | - |
| data.content.deviceName | test2_2 | string | 设备名称 |
| data.content.nickname | null | null | 设备备注名 |
| data.content.createTime | null | null | 创建时间 |
| data.content.userId | 0 | integer | 用户id |
| data.content.status | ONLINE | string | 状态 |
| data.content.labels | null | null | 设备标签 |
| data.content.description | null | null | 描述 |
| data.content.updateTime | 2022-07-05 02:26:20 | string | 更新时间 |
| data.content.activeTime | 2022-07-04 03:59:13 | string | 激活时间 |
| data.content.version | 15.0 | string | 版本 |
| data.content.destVersion | 16.0 | string | 目标版本 |
| data.content.srcIotId | null | null | - |
| data.last | true | boolean | 最后一页 |
| data.totalPages | 1 | integer | 总页数 |
| data.totalElements | 2 | integer | 总元素个数 |
| data.number | 0 | integer | 页码 |
| data.size | 20 | integer | 每页元素个数 |
| data.sort | null | null | 排序 |
| data.first | true | boolean | 是否是第一页 |
| data.numberOfElements | 2 | integer | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备实例列表_简版

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-03 15:21:10

> 更新时间: 2022-10-24 11:50:03

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/simpleList?productKey=iy4uY75WdQj

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 产品key |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"iotId": "nCkCiloU2jKwMu1xN3tqh7s700",
				"deviceSecret": "dfcc001eb872866114ad18631576867e",
				"productKey": "h7s7NxjuhLw",
				"joinEui": "",
				"deviceName": "test_haha",
				"nickname": null,
				"createTime": 1654142312000,
				"userId": null
			},
			{
				"iotId": "A4o4Kd0VNrWgyMvwLFcQh7s700",
				"deviceSecret": "40bf771eab243cae477ac24a22a90d6a",
				"productKey": "h7s7NxjuhLw",
				"joinEui": "",
				"deviceName": "test_haha2",
				"nickname": null,
				"createTime": 1654477801000,
				"userId": null
			}
		],
		"last": true,
		"totalPages": 1,
		"totalElements": 2,
		"number": 0,
		"size": 20,
		"sort": null,
		"numberOfElements": 2,
		"first": true
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | - |
| data.content.iotId | nCkCiloU2jKwMu1xN3tqh7s700 | string | 设备全局id |
| data.content.deviceSecret | dfcc001eb872866114ad18631576867e | string | 设备秘钥 |
| data.content.productKey | h7s7NxjuhLw | string | 产品key |
| data.content.joinEui | - | object | - |
| data.content.deviceName | test_haha | string | 设备名称 |
| data.content.nickname | - | object | 设备备注名 |
| data.content.createTime | 1654142312000 | number | 创建时间 |
| data.content.userId | - | object | 用户id |
| data.last | true | string | 最后一页 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 2 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 20 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.numberOfElements | 2 | number | - |
| data.first | true | string | 是否是第一页 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备实例详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 14:28:06

> 更新时间: 2023-03-08 14:11:34

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/get?iotId=H58oQIREH0MpQhFaItH0TAlnq4

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | 设备全局id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"description": null,
		"labels": null,
		"version": "15.0",
		"status": "ONLINE",
		"productKey": "h7s72qjeGaM",
		"deviceName": "test2_1",
		"iotId": "XUbvGwMcOCvmEz6Rbi71h7s700",
		"projectId": null,
		"userId": 0,
		"createTime": null,
		"deviceSecret": "bd22f7b9a60ad551f506bdf62498144a",
		"destVersion": "16.0",
		"updateTime": "2022-07-05 14:26:20",
		"srcIotId": null,
		"joinEui": null,
		"nickname": null,
		"activeTime": "2022-07-04 15:59:13",
		"product": {
			"iotInstanceId": "iot-06z00ei6cjy8564",
			"productName": "test2_uP0HV",
			"productNameNote": "test2",
			"productKey": "h7s72qjeGaM",
			"productSecret": "gDn4fyiWN3ERo8FR",
			"code": "",
			"deviceCnt": 0,
			"nodeType": 0,
			"userId": 0,
			"description": "沃尔沃二",
			"categoryKey": "Lighting",
			"netType": null,
			"dataFormat": 1,
			"authType": "secret",
			"createTime": "2022-06-02 11:29:45",
			"updateTime": "2022-09-06 09:46:33",
			"productStatus": 1,
			"joinPermissionId": null,
			"projectId": 2
		},
		"clientIp": "113.90.209.34",
		"scenes": [
			"场景名称"
		],
		"gwDevice": null
	},
	"requestId": "7533220e-7d70-4788-b78b-842727faac25",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.description | - | object | 描述 |
| data.labels | - | object | 标签 |
| data.version | 15.0 | string | 版本 |
| data.status | ONLINE | string | 状态 |
| data.productKey | h7s72qjeGaM | string | 产品key |
| data.deviceName | test2_1 | string | 设备名称 |
| data.iotId | XUbvGwMcOCvmEz6Rbi71h7s700 | string | 设备全局id |
| data.projectId | - | object | 工程id |
| data.userId | 0 | object | 用户id |
| data.createTime | - | number | 创建时间 |
| data.deviceSecret | bd22f7b9a60ad551f506bdf62498144a | string | 设备秘钥 |
| data.destVersion | 16.0 | string | - |
| data.updateTime | 2022-07-05 14:26:20 | string | 更新时间 |
| data.srcIotId | - | object | - |
| data.joinEui | - | object | - |
| data.nickname | - | object | 设备备注名 |
| data.activeTime | 2022-07-04 15:59:13 | string | 激活时间 |
| data.product | - | object | 产品 |
| data.product.iotInstanceId | iot-06z00ei6cjy8564 | string | - |
| data.product.productName | test2_uP0HV | string | 产品名(阿里云平台) |
| data.product.productNameNote | test2 | string | 产品名 |
| data.product.productKey | h7s72qjeGaM | string | 产品key |
| data.product.productSecret | gDn4fyiWN3ERo8FR | string | 产品秘钥 |
| data.product.code | - | object | - |
| data.product.deviceCnt | 0 | number | 设备数 |
| data.product.nodeType | 0 | number | - |
| data.product.userId | 0 | number | 用户id |
| data.product.description | 沃尔沃二 | string | 描述 |
| data.product.categoryKey | Lighting | string | 设备模型识别码 |
| data.product.netType | - | object | - |
| data.product.dataFormat | 1 | number | - |
| data.product.authType | secret | string | - |
| data.product.createTime | 2022-06-02 11:29:45 | string | 创建时间 |
| data.product.updateTime | 2022-09-06 09:46:33 | string | 更新时间 |
| data.product.productStatus | 1 | number | - |
| data.product.joinPermissionId | - | object | - |
| data.product.projectId | 2 | number | 工程id |
| data.clientIp | 113.90.209.34 | string | 客户端ip地址 |
| data.scenes | 场景名称 | string | 场景 |
| data.gwDevice | - | object | 网关设备 |
| requestId | 7533220e-7d70-4788-b78b-842727faac25 | string | 请求id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备实例详情_基本信息

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-12-08 17:01:18

> 更新时间: 2022-12-15 14:50:32

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/getBasicInfo?iotId=H58oQIREH0MpQhFaItH0TAlnq4

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | 设备全局id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"iotId": "XUbvGwMcOCvmEz6Rbi71h7s700",
		"deviceSecret": "bd22f7b9a60ad551f506bdf62498144a",
		"productKey": "h7s72qjeGaM",
		"joinEui": null,
		"deviceName": "test2_1",
		"nickname": "驱蚊器无",
		"createTime": "2022-11-24 16:29:24",
		"userId": 0,
		"status": "ONLINE",
		"labels": "qqq",
		"description": "qeqweq",
		"updateTime": "2022-07-05 14:26:20",
		"activeTime": "2022-07-04 15:59:13",
		"version": "15.0",
		"destVersion": "16.0",
		"srcIotId": null,
		"projectId": 2
	},
	"requestId": "95b58347-1cce-486c-8c4d-5f40a27c4b0b",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.iotId | XUbvGwMcOCvmEz6Rbi71h7s700 | string | 设备全局id |
| data.deviceSecret | bd22f7b9a60ad551f506bdf62498144a | string | 设备秘钥 |
| data.productKey | h7s72qjeGaM | string | 产品key |
| data.joinEui | - | object | - |
| data.deviceName | test2_1 | string | 设备名称 |
| data.nickname | 驱蚊器无 | object | 设备备注名 |
| data.createTime | 2022-11-24 16:29:24 | number | 创建时间 |
| data.userId | 0 | object | 用户id |
| data.status | ONLINE | string | 状态 |
| data.labels | qqq | object | 标签 |
| data.description | qeqweq | object | 描述 |
| data.updateTime | 2022-07-05 14:26:20 | string | 更新时间 |
| data.activeTime | 2022-07-04 15:59:13 | string | 激活时间 |
| data.version | 15.0 | string | 版本 |
| data.destVersion | 16.0 | string | - |
| data.srcIotId | - | object | - |
| data.projectId | 2 | object | 工程id |
| requestId | 95b58347-1cce-486c-8c4d-5f40a27c4b0b | string | 请求id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 设备实例状态

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-12-09 10:17:38

> 更新时间: 2022-12-09 11:23:20

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/getStatus?iotId=H58oQIREH0MpQhFaItH0TAlnq4

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"lastTime": "2022-12-08 14:21:06.744",
		"iotId": "XUbvGwMcOCvmEz6Rbi71h7s700",
		"utcLastTime": "2022-12-08T06:21:06.744Z",
		"clientIp": "113.90.211.190",
		"utcTime": "2022-12-08T06:21:06.744Z",
		"time": "2022-12-08 14:21:06.744",
		"productKey": "h7s72qjeGaM",
		"deviceName": "test2_1",
		"status": "online"
	},
	"requestId": "9365d6ef-ad46-46d9-9771-f9a46b1e48df",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.lastTime | 2022-12-08 14:21:06.744 | string | - |
| data.iotId | XUbvGwMcOCvmEz6Rbi71h7s700 | string | 设备全局id |
| data.utcLastTime | 2022-12-08T06:21:06.744Z | string | 最后登陆时间 |
| data.clientIp | 113.90.211.190 | string | 最后登陆ip |
| data.utcTime | 2022-12-08T06:21:06.744Z | string | - |
| data.time | 2022-12-08 14:21:06.744 | string | - |
| data.productKey | h7s72qjeGaM | string | 产品key |
| data.deviceName | test2_1 | string | 设备名称 |
| data.status | online | string | 状态 |
| requestId | 9365d6ef-ad46-46d9-9771-f9a46b1e48df | string | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 设备实例删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 14:31:17

> 更新时间: 2022-11-25 17:01:41

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/delete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | hqmerEyehKiVxqurWaQHh7s700 | Text | 是 | 设备全局id |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": null,
	"status": "S",
	"sysMsg": "操作成功"
}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备实例创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-06 14:29:38

> 更新时间: 2023-09-22 10:37:12

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 归属产品的key |
| nickname | test_96 | Text | 是 | 设备名 |
| labels | aaa,bbb, | Text | 否 | 标签, 用,分割, 前后都加上, |
| description | dsfasdf | Text | 否 | 描述 |
| GWDevice | - | Text | 否 | 网关设备的iotId |
| hardwareId | 80980809 | string | 否 | 硬件UUID |
| sceneId | 40 | string | 否 | 关联场景id |
| sceneDeviceId | 8 | string | 否 | 关联场景设备id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"iotId": "fZnXVMm6eoxglWg73Y0nh7s700",
		"deviceSecret": "5ddffae5b0ded5121a3f763d6a13456e",
		"productKey": "h7s7NxjuhLw",
		"joinEui": "",
		"deviceName": "test_4",
		"nickname": "备注名二二二",
		"createTime": null,
		"userId": null
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.iotId | fZnXVMm6eoxglWg73Y0nh7s700 | string | 设备全局id |
| data.deviceSecret | 5ddffae5b0ded5121a3f763d6a13456e | string | 设备秘钥 |
| data.productKey | h7s7NxjuhLw | string | 产品key |
| data.joinEui | - | object | - |
| data.deviceName | test_4 | string | 设备名称 |
| data.nickname | 备注名二二二 | string | 设备备注名 |
| data.createTime | - | object | 创建时间 |
| data.userId | - | object | 用户id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 批量导入设备

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-30 14:45:49

> 更新时间: 2023-06-30 14:46:36

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/importDevices

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| file | - | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 获取导入模板文件

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-30 14:48:09

> 更新时间: 2023-06-30 15:41:30

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/common/getExampleFile?fileName=设备导入模板.xlsx

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| fileName | 设备导入模板.xlsx | Text | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"file":{"path":"","status":"","prefixLength":"","filePath":{"fileSystem":{},"absolute":"","root":{},"fileName":{},"parent":{},"nameCount":"","name":{}}},"path":""}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| file | - | object | - |
| file.path | - | string | This abstract pathname's normalized pathname string. A normalized |
| file.status | - | string | The flag indicating whether the file path is invalid. (INVALID, CHECKED) |
| file.prefixLength | - | integer | The length of this abstract pathname's prefix, or zero if it has no |
| file.filePath | - | object | - |
| file.filePath.fileSystem | - | object | - |
| file.filePath.absolute | - | boolean | - |
| file.filePath.root | - | object | - |
| file.filePath.fileName | - | object | - |
| file.filePath.parent | - | object | - |
| file.filePath.nameCount | - | integer | - |
| file.filePath.name | - | object | - |
| path | - | string | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备实例运行日志

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-05 14:16:47

> 更新时间: 2023-06-09 10:15:39

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/log?iotId=H58oQIREH0MpQhFaItH0TAlnq4&page=0&size=5&startTime=1586326400000&endTime=1686326400000&search=

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | string | 是 | 设备全局id |
| page | 0 | string | 否 | 分页页码，数字类型 |
| size | 5 | string | 否 | 每页元素个数 |
| startTime | 1586326400000 | Text | 否 | 开始时间 |
| endTime | 1686326400000 | Text | 否 | 结束时间 |
| search | - | Text | 是 | 搜索, type字段 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"topic": "/h7s72qjeGaM/test2_1/thing/event/property/post",
				"messageId": "1544215204244931584",
				"generateTime": "2022-07-05 15:02:49",
				"type": "push",
				"content": "{\"deviceType\":\"CustomCategory\",\"iotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\"requestId\":\"123\",\"checkFailedData\":{},\"productKey\":\"h7s72qjeGaM\",\"gmtCreate\":1657004569478,\"deviceName\":\"test2_1\",\"items\":{\"Temperature\":{\"value\":30,\"time\":1524448722000},\"Humidity\":{\"value\":82,\"time\":1524448722000}}}"
			},
			{
				"topic": "/h7s72qjeGaM/test2_1/thing/event/property/post",
				"messageId": "1544215199782029312",
				"generateTime": "2022-07-05 15:02:48",
				"type": "push",
				"content": "{\"deviceType\":\"CustomCategory\",\"iotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\"requestId\":\"123\",\"checkFailedData\":{},\"productKey\":\"h7s72qjeGaM\",\"gmtCreate\":1657004568410,\"deviceName\":\"test2_1\",\"items\":{\"Temperature\":{\"value\":30,\"time\":1524448722000},\"Humidity\":{\"value\":82,\"time\":1524448722000}}}"
			},
			{
				"topic": "/h7s72qjeGaM/test2_1/thing/event/property/post_11",
				"messageId": "1544206769348739072",
				"generateTime": "2022-07-05 14:29:18",
				"type": "push",
				"content": "{\"deviceType\":\"CustomCategory\",\"iotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\"requestId\":\"123\",\"checkFailedData\":{},\"productKey\":\"h7s72qjeGaM\",\"gmtCreate\":1657002558440,\"deviceName\":\"test2_1\",\"items\":{\"Temperature\":{\"value\":30,\"time\":1524448722000},\"Humidity\":{\"value\":82,\"time\":1524448722000}}}"
			},
			{
				"topic": "/h7s72qjeGaM/test2_1/thing/event/property/post",
				"messageId": "1544206768614787584",
				"generateTime": "2022-07-05 14:29:18",
				"type": "push",
				"content": "{\"deviceType\":\"CustomCategory\",\"iotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\"requestId\":\"123\",\"checkFailedData\":{},\"productKey\":\"h7s72qjeGaM\",\"gmtCreate\":1657002558267,\"deviceName\":\"test2_1\",\"items\":{\"Temperature\":{\"value\":30,\"time\":1524448722000},\"Humidity\":{\"value\":82,\"time\":1524448722000}}}"
			},
			{
				"topic": "/h7s72qjeGaM/test2_1/thing/event/property/post",
				"messageId": "1544206767905794560",
				"generateTime": "2022-07-05 14:29:18",
				"type": "push",
				"content": "{\"deviceType\":\"CustomCategory\",\"iotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\"requestId\":\"123\",\"checkFailedData\":{},\"productKey\":\"h7s72qjeGaM\",\"gmtCreate\":1657002558096,\"deviceName\":\"test2_1\",\"items\":{\"Temperature\":{\"value\":30,\"time\":1524448722000},\"Humidity\":{\"value\":82,\"time\":1524448722000}}}"
			}
		],
		"last": false,
		"totalPages": 6,
		"totalElements": 26,
		"number": 0,
		"size": 5,
		"sort": null,
		"first": true,
		"numberOfElements": 5
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | - |
| data.content.topic | /h7s72qjeGaM/test2_1/thing/event/property/post | string | 消息的topic |
| data.content.messageId | 1544215204244931584 | string | 消息id |
| data.content.generateTime | 2022-07-05 15:02:49 | string | 消息生成时间 |
| data.content.type | push | string | 消息类型:statusChange=状态变化,invokeService=调用服务, push=消息推送 |
| data.content.content | {"deviceType":"CustomCategory","iotId":"XUbvGwMcOCvmEz6Rbi71h7s700","requestId":"123","checkFailedData":{},"productKey":"h7s72qjeGaM","gmtCreate":1657004569478,"deviceName":"test2_1","items":{"Temperature":{"value":30,"time":1524448722000},"Humidity":{"value":82,"time":1524448722000}}} | string | 消息详情 |
| data.last | false | string | 最后一页 |
| data.totalPages | 6 | number | 总页数 |
| data.totalElements | 26 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 5 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 5 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备属性工况

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-05 16:21:54

> 更新时间: 2026-07-24 16:52:13

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/getProperties?iotId=H58oQIREH0MpQhFaItH0TAlnq4

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | 设备全局id |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 获取设备实时属性

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-24 14:24:09

> 更新时间: 2024-02-23 15:14:59

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> ws://iot.iuvtech.com/getDeviceProperties?token=13a0e1fe-2e92-4636-8b6e-5b2c2f5719bc&iotId=qyDrXzDnM2pWc4nMHD0eiy4u00

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 13a0e1fe-2e92-4636-8b6e-5b2c2f5719bc | String | 是 | 用户token |
| iotId | qyDrXzDnM2pWc4nMHD0eiy4u00 | String | 是 | 设备id |

**设置**


| 启用服务器证书验证 | 否 |
| 最大内容大小 | 5 |
| 连接超时设置 | 0 |

**Socket消息**

> 消息

* 请求(text)
```javascript
暂无数据
```

* 响应(text)
```javascript
暂无数据
```

**Query**

## 设备实时运行日志

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-24 14:27:02

> 更新时间: 2024-02-23 17:12:03

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> ws://iot.iuvtech.com/getDeviceLog?token=13a0e1fe-2e92-4636-8b6e-5b2c2f5719bc&iotId=qyDrXzDnM2pWc4nMHD0eiy4u00

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 13a0e1fe-2e92-4636-8b6e-5b2c2f5719bc | String | 是 | 用户token |
| iotId | qyDrXzDnM2pWc4nMHD0eiy4u00 | String | 是 | 设备id |

**设置**


| 启用服务器证书验证 | 否 |
| 最大内容大小 | 5 |
| 连接超时设置 | 0 |

**Socket消息**

> 消息

* 请求(text)
```javascript
暂无数据
```

* 响应(text)
```javascript
暂无数据
```

**Query**

## 设备属性历史工况

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-05 17:33:26

> 更新时间: 2023-03-10 16:05:23

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/getHistoryProperties?iotId=H58oQIREH0MpQhFaItH0TAlnq4&startTime=1646896057362&endTime=1678432057362&property=Temperature&page=0&size=1000

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | 设备全局id |
| startTime | 1646896057362 | Text | 是 | 开始时间戳 |
| endTime | 1678432057362 | Text | 是 | 结束时间戳 |
| property | Temperature | Text | 是 | 属性名, 如需获取多个属性的历史数据一条属性一个请求 |
| page | 0 | Text | 否 | 分页页码，数字类型 |
| size | 1000 | Text | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"Temperature": {
					"value": 60,
					"time": 1658283588772
				},
				"Humidity": {
					"value": 89,
					"time": 1658283588772
				},
				"__genTimestamp": "2022-07-20 10:19:48"
			}
		],
		"last": false,
		"totalElements": 534,
		"totalPages": 54,
		"number": 1,
		"size": 10,
		"sort": null,
		"first": false,
		"numberOfElements": 10
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.Temperature | - | object | - |
| data.content.Temperature.value | 60 | number | - |
| data.content.Temperature.time | 1658283588772 | number | - |
| data.content.Humidity | - | object | - |
| data.content.Humidity.value | 89 | number | - |
| data.content.Humidity.time | 1658283588772 | number | - |
| data.content.__genTimestamp | 2022-07-20 10:19:48 | string | - |
| data.last | false | string | 最后一页 |
| data.totalElements | 534 | number | 总元素个数 |
| data.totalPages | 54 | number | 总页数 |
| data.number | 1 | number | 页码 |
| data.size | 10 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.first | false | string | 是否是第一页 |
| data.numberOfElements | 10 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备topic列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-06 08:42:16

> 更新时间: 2022-11-25 17:01:51

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/getTopics?iotId=21323

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | 21323 | Text | 是 | 设备全局id |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": [
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/event/property/post",
			"topicName": "属性上报",
			"topicDesc": "设备属性上报",
			"operation": 0,
			"topicType": 1,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/event/property/post_reply",
			"topicName": "属性上报",
			"topicDesc": "云端响应属性上报",
			"operation": 1,
			"topicType": 1,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/service/property/set",
			"topicName": "属性设置",
			"topicDesc": "设备属性设置",
			"operation": 1,
			"topicType": 1,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/event/${tsl.event.identifier}/post",
			"topicName": "事件上报",
			"topicDesc": "设备事件上报",
			"operation": 0,
			"topicType": 1,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/event/${tsl.event.identifier}/post_reply",
			"topicName": "事件上报",
			"topicDesc": "云端响应事件上报",
			"operation": 1,
			"topicType": 1,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/service/${tsl.service.identifier}",
			"topicName": "服务调用",
			"topicDesc": "设备服务调用",
			"operation": 1,
			"topicType": 1,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/service/${tsl.service.identifier}_reply",
			"topicName": "服务调用",
			"topicDesc": "设备端响应服务调用",
			"operation": 0,
			"topicType": 1,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/ota/device/inform/h7s72qjeGaM/test2_1",
			"topicName": "OTA 升级",
			"topicDesc": "设备上报固件升级信息",
			"operation": 0,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/ota/device/upgrade/h7s72qjeGaM/test2_1",
			"topicName": "OTA 升级",
			"topicDesc": "固件升级信息下行",
			"operation": 1,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/ota/device/progress/h7s72qjeGaM/test2_1",
			"topicName": "OTA 升级",
			"topicDesc": "设备上报固件升级进度",
			"operation": 0,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/ota/firmware/get",
			"topicName": "OTA 升级",
			"topicDesc": "设备主动拉取固件升级信息",
			"operation": 0,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/deviceinfo/update",
			"topicName": "设备标签",
			"topicDesc": "设备上报标签数据",
			"operation": 0,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/deviceinfo/update_reply",
			"topicName": "设备标签",
			"topicDesc": "云端响应标签上报",
			"operation": 1,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/deviceinfo/delete",
			"topicName": "设备标签",
			"topicDesc": "设备删除标签信息",
			"operation": 1,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/deviceinfo/delete_reply",
			"topicName": "设备标签",
			"topicDesc": "云端响应标签删除",
			"operation": 0,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/ext/ntp/h7s72qjeGaM/test2_1/request",
			"topicName": "时钟同步",
			"topicDesc": "NTP 时钟同步请求",
			"operation": 0,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/ext/ntp/h7s72qjeGaM/test2_1/response",
			"topicName": "时钟同步",
			"topicDesc": "NTP 时钟同步响应",
			"operation": 1,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/shadow/update/h7s72qjeGaM/test2_1",
			"topicName": "设备影子",
			"topicDesc": "设备影子发布",
			"operation": 0,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/shadow/get/h7s72qjeGaM/test2_1",
			"topicName": "设备影子",
			"topicDesc": "设备接收影子变更",
			"operation": 1,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/config/push",
			"topicName": "配置更新",
			"topicDesc": "云端主动下推配置信息",
			"operation": 1,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/config/get",
			"topicName": "配置更新",
			"topicDesc": "设备端查询配置信息",
			"operation": 0,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/sys/h7s72qjeGaM/test2_1/thing/config/get_reply",
			"topicName": "配置更新",
			"topicDesc": "云端响应配置信息",
			"operation": 1,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		},
		{
			"topicId": null,
			"productKey": null,
			"topicKey": "/broadcast/h7s72qjeGaM/${identifier}",
			"topicName": "广播",
			"topicDesc": "广播 Topic，identifier 为用户自定义字符串",
			"operation": 1,
			"topicType": 0,
			"updateTime": null,
			"topicIdIot": null
		}
	],
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.topicId | - | object | - |
| data.productKey | - | object | 产品key |
| data.topicKey | /sys/h7s72qjeGaM/test2_1/thing/event/property/post | string | topickey |
| data.topicName | 属性上报 | string | topic名称 |
| data.topicDesc | 设备属性上报 | string | topic描述 |
| data.operation | 0 | number | 操作权限:0=发布,1=订阅,2=发布订阅 |
| data.topicType | 1 | number | topic类型:0=基础通信,1=物模型通信,null=自定义 |
| data.updateTime | - | object | 更新时间 |
| data.topicIdIot | - | object | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 服务调用

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-06 14:49:14

> 更新时间: 2023-12-11 14:25:04

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/invokeService

**请求方式**

> POST

**Content-Type**

> urlencoded

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | 设备全局id |
| identifier | clear | Text | 是 | 服务标识符 |
| arg | {"type":"temp5"} | Text | 是 | 服务调用参数 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设备服务调用记录

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-06 10:13:57

> 更新时间: 2022-12-01 15:21:39

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/getServiceInvokes?iotId=H58oQIREH0MpQhFaItH0TAlnq4&startTime=1567072296973&endTime=1757014613079&identifier=clear&size=3&page=1

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | 设备全局id |
| startTime | 1567072296973 | Text | 否 | 开始时间 默认最近1个星期 |
| endTime | 1757014613079 | Text | 否 | 结束时间 |
| identifier | clear | Text | 否 | 服务标识符 |
| size | 3 | Text | 否 | 每页显示个数, 分页参考: https://help.aliyun.com/document_detail/69574.htm?spm=a2c4g.11186623.0.0.25b33982ihoWyt#reference-j2n-lrz-wdb |
| page | 1 | Text | 否 | 分页页码，数字类型 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"outputData": "{\"id\":\"303502733\",\"version\":\"1.0\",\"message\":success}",
				"identifier": "clear",
				"inputData": "{\"type\":\"temp3\"}",
				"name": "清理垃圾",
				"time": "2022-12-01 11:21:59"
			},
			{
				"outputData": "{\"id\":\"\",\"version\":\"1.0\",\"message\":设备不在线}",
				"identifier": "clear",
				"inputData": "{\"type\":\"temp3\"}",
				"name": "清理垃圾",
				"time": "2022-12-01 11:19:42"
			}
		],
		"last": true,
		"totalElements": 5,
		"totalPages": 2,
		"number": 1,
		"size": 3,
		"sort": null,
		"numberOfElements": 2,
		"first": false
	},
	"requestId": "b1752d31-14e8-4381-9991-7ca7e944dd6f",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.outputData | {"id":"303502733","version":"1.0","message":success} | string | - |
| data.content.identifier | clear | string | - |
| data.content.inputData | {"type":"temp3"} | string | - |
| data.content.name | 清理垃圾 | string | - |
| data.content.time | 2022-12-01 11:21:59 | string | - |
| data.last | true | string | 最后一页 |
| data.totalElements | 5 | number | 总元素个数 |
| data.totalPages | 2 | number | 总页数 |
| data.number | 1 | number | 页码 |
| data.size | 3 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.numberOfElements | 2 | number | 总元素个数 |
| data.first | false | string | 是否是第一页 |
| requestId | b1752d31-14e8-4381-9991-7ca7e944dd6f | string | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 设置属性

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-03 14:37:02

> 更新时间: 2023-12-11 14:25:06

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/setProperty

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | 设备全局id |
| data | {"Humidity": 66, "Temperature": 60 } | Text | 是 | 服务标识符 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 鉴权_绑定设备

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-30 15:54:06

> 更新时间: 2022-09-16 10:25:05

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDeviceAuth/bind

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | Y98fb6fc1a511470f9716dc0565a9a77d | Text | 是 | 设备全局id |
| deviceIdentify | 12312 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 根据产品列表查询设备列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-27 16:29:30

> 更新时间: 2022-12-20 15:20:54

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/listByProducts?productKeys=h7s7NxjuhLw,h7s72qjeGaM&page=&size=

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKeys | h7s7NxjuhLw,h7s72qjeGaM | Text | 是 | 文件包含产品 |
| page | - | Text | 否 | 分页页码，数字类型 |
| size | - | Text | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"iotId": "QxDn30BdD816c9ZwFQokh7s700",
				"deviceSecret": null,
				"productKey": "h7s7NxjuhLw",
				"joinEui": "",
				"deviceName": "test_3",
				"nickname": null,
				"createTime": "2022-06-10 06:23:47",
				"userId": null,
				"status": "UNACTIVE",
				"labels": null,
				"description": null,
				"updateTime": "2022-07-04 06:34:33",
				"activeTime": "2022-07-04 07:25:33",
				"version": null,
				"destVersion": null
			},
			{
				"iotId": "KxrULkCkNwaCItI0TkA6h7s700",
				"deviceSecret": null,
				"productKey": "h7s7NxjuhLw",
				"joinEui": "",
				"deviceName": "test_haha3",
				"nickname": null,
				"createTime": "2022-06-10 06:23:12",
				"userId": null,
				"status": "UNACTIVE",
				"labels": null,
				"description": null,
				"updateTime": "2022-07-04 06:34:33",
				"activeTime": "2022-07-04 06:34:33",
				"version": null,
				"destVersion": null
			},
			{
				"iotId": "A4o4Kd0VNrWgyMvwLFcQh7s700",
				"deviceSecret": null,
				"productKey": "h7s7NxjuhLw",
				"joinEui": "",
				"deviceName": "test_haha2",
				"nickname": null,
				"createTime": "2022-06-06 01:10:01",
				"userId": null,
				"status": "UNACTIVE",
				"labels": null,
				"description": null,
				"updateTime": "2022-07-04 06:34:33",
				"activeTime": null,
				"version": null,
				"destVersion": null
			},
			{
				"iotId": "nCkCiloU2jKwMu1xN3tqh7s700",
				"deviceSecret": null,
				"productKey": "h7s7NxjuhLw",
				"joinEui": "",
				"deviceName": "test_haha",
				"nickname": null,
				"createTime": "2022-06-02 03:58:32",
				"userId": null,
				"status": "UNACTIVE",
				"labels": null,
				"description": null,
				"updateTime": "2022-07-04 06:34:33",
				"activeTime": null,
				"version": null,
				"destVersion": null
			},
			{
				"iotId": "XUbvGwMcOCvmEz6Rbi71h7s700",
				"deviceSecret": null,
				"productKey": "h7s72qjeGaM",
				"joinEui": null,
				"deviceName": "test2_1",
				"nickname": null,
				"createTime": null,
				"userId": null,
				"status": "ONLINE",
				"labels": null,
				"description": null,
				"updateTime": "2022-07-05 06:26:20",
				"activeTime": "2022-07-04 07:59:13",
				"version": "15.0",
				"destVersion": "13.0"
			}
		],
		"last": true,
		"totalPages": 1,
		"totalElements": 5,
		"number": 0,
		"size": 20,
		"sort": null,
		"first": true,
		"numberOfElements": 5
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.iotId | QxDn30BdD816c9ZwFQokh7s700 | string | 设备全局id |
| data.content.deviceSecret | - | object | 设备秘钥 |
| data.content.productKey | h7s7NxjuhLw | string | 产品key |
| data.content.joinEui | - | object | - |
| data.content.deviceName | test_3 | string | 设备名称 |
| data.content.nickname | - | object | 设备备注名 |
| data.content.createTime | 2022-06-10 06:23:47 | string | 创建时间 |
| data.content.userId | - | object | 用户id |
| data.content.status | UNACTIVE | string | 状态 |
| data.content.labels | - | object | 设备标签 |
| data.content.description | - | object | 描述 |
| data.content.updateTime | 2022-07-04 06:34:33 | string | 更新时间 |
| data.content.activeTime | 2022-07-04 07:25:33 | string | - |
| data.content.version | - | object | 设备版本 |
| data.content.destVersion | - | object | 目标版本 |
| data.last | true | string | 最后一页 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 5 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 20 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 5 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 鉴权_获取设备鉴权信息

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-15 16:14:49

> 更新时间: 2023-06-16 10:41:14

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDeviceAuth/getAuthInfo?deviceIdentify=12312&devicePassword=123456

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| deviceIdentify | 12312 | string | 是 | 设备唯一标识, 写死在设备中 |
| devicePassword | 123456 | string | 是 | 设备密码, 写死在设备中 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"deviceSecret": "bd22f7b9a60ad551f506bdf62498144a",
		"productKey": "h7s72qjeGaM",
		"deviceName": "test2_1",
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.deviceSecret | bd22f7b9a60ad551f506bdf62498144a | string | 设备秘钥 |
| data.productKey | h7s72qjeGaM | string | 产品key |
| data.deviceName | test2_1 | string | 设备名称 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 获取网关设备

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-11-22 15:52:46

> 更新时间: 2023-08-22 10:40:40

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/getGWDevice

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 2 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": [
		{
			"productKey": "h7s7HMBiPiy",
			"deviceName": "netDevice1",
			"productNameNote": "网关产品"
		},
		{
			"productKey": "h7s7HMBiPiy",
			"deviceName": "netDevice2",
			"productNameNote": "网关产品"
		}
	],
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.productKey | h7s7HMBiPiy | string | 产品key |
| data.deviceName | netDevice1 | string | 设备名称 |
| data.productNameNote | 网关产品 | string | 产品名 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 设备修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-08 17:08:29

> 更新时间: 2023-03-08 17:10:08

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | string | 是 | 设备全局id |
| nickname | 恶趣味群 | string | 是 | 设备备注名 |
| hardwareId | 123123 | string | 否 | 硬件设备UUID |
| description | 恶趣味群翁 | string | 否 | 描述 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 告警

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-18 15:06:42

> 更新时间: 2022-07-18 15:06:43

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 保存告警规则

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-18 14:56:02

> 更新时间: 2023-03-08 08:44:42

**[
    //条件1
    {
        "property":"属性1",
        "condition":">",
        "value":"属性值",
        "assoc": "and"	// and or
    }
    //条件2,3,...
]**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotWarning/save

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 产品key |
| warningName | 警告名1 | Text | 是 | 告警名 |
| warningKey | warning1 | Text | 是 | 告警标识 |
| warningLevel | 1 | Text | 是 | 告警规则: 1=普通. 2=重要, 3=严重, 4=紧急 |
| warningRule | [{"property":"Humidity","condition":">","value":"50","assoc": "and" }] | Text | 是 | 告警条件规则, 详细格式参见 保存告警 接口说明 |
| warningDesc | 123 | Text | 否 | 告警描述 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": null,
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 告警规则列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-18 15:18:50

> 更新时间: 2022-11-07 14:17:06

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotWarning/listSearch?productKey=iy4uY75WdQj

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 产品key |
| warningKeyOrName | warning5 | Text | 否 | 告警名或者标识符 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": [
		{
			"warningId": 1,
			"productKey": "h7s7PwecpHX",
			"warningName": "警告名1",
			"warningKey": "warning1",
			"warningLevel": 1,
			"warningRule": "[\n\t//条件1\n\t{\n\t\t\"property\":\"属性1\",\n\t\t\"condition\":\">\",\n\t\t\"value\":\"属性值\",\n\t\t\"assoc\": \"&\"\t//值: & | !\n\t}\n\t//条件2,3,...\n]",
			"warningDesc": "123"
		}
	],
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.warningId | 1 | number | - |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.warningName | 警告名1 | string | 告警名 |
| data.warningKey | warning1 | string | 告警标识 |
| data.warningLevel | 10 | number | 告警规则: 10=普通. 20=重要, 30=严重, 40=紧急 |
| data.warningRule | [{"property":"属性1","condition":">","value":"属性值","assoc":"and", //值: and,or }, ...] | string | 告警条件规则, 详细格式参见 保存告警 接口说明 |
| data.warningDesc | 123 | string | 告警描述 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 更新告警规则

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-18 15:31:34

> 更新时间: 2022-08-03 13:58:12

**[
    {
        "property":"属性1",
        "condition":">",
        "value":"属性值",
        "assoc": "and"
    }
]**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotWarning/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 产品key |
| warningName | 警告名5 | Text | 是 | 告警名 |
| warningKey | warning5 | Text | 是 | 告警标识 |
| warningLevel | 3 | Text | 是 | 告警规则: 10=普通. 20=重要, 30=严重, 40=紧急 |
| warningRule | [{"property":"Humidity","condition":">","value":"50","assoc": "and" }] | Text | 是 | 告警条件规则, 详细格式参见 保存告警 接口说明 |
| warningDesc | 123 | Text | 否 | 告警描述 |
| warningId | 7 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"data": null,
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 删除告警规则

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-18 16:24:43

> 更新时间: 2022-08-03 14:38:20

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotWarning/delete?warningId=9

**请求方式**

> POST

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| warningId | 9 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 告警确认

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-20 11:26:14

> 更新时间: 2022-11-29 16:31:45

**[
    {
        "property":"属性1",
        "condition":">",
        "value":"属性值",
        "assoc": "and"
    }
]**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotWarning/ensure

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| warningId | 8 | Text | 是 | 告警标识 |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | Text | 是 | 设备名称 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 告警信息

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-20 14:51:29

> 更新时间: 2022-12-06 16:49:02

**[
    {
        "property":"属性1",
        "condition":">",
        "value":"属性值",
        "assoc": "and"
    }
]**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotWarning/warningList?iotId=H58oQIREH0MpQhFaItH0TAlnq4&isHistory=1&size=5

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| iotId | H58oQIREH0MpQhFaItH0TAlnq4 | string | 是 | 产品key |
| isHistory | 1 | Text | 是 | 0=实时告警, 1=历史告警 |
| warningName | 警告 | Text | 否 | 告警标识 |
| page | 1 | Text | 否 | 分页页码，数字类型 |
| size | 5 | Text | 否 | 每页元素个数 |
| startTime | - | Text | 否 | 开始时间 |
| endTime | 1669708002940 | Text | 否 | 结束时间 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"warningId": 7,
				"warningKey": "warning5",
				"warningLevel": 30,
				"warningName": "警告名5",
				"warningDesc": "123",
				"userId": 0,
				"properties": "Humidity:66",
				"uuid": "d3960af1-ae20-4b52-b8e2-b31ed53cc5ba",
				"ensureTime": null,
				"createTime": "2022-12-06 14:11:22",
				"status": 3,
				"endTime": "2022-12-06 16:38:56"
			},
			{
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"warningId": 8,
				"warningKey": "warning1",
				"warningLevel": 30,
				"warningName": "警告名1",
				"warningDesc": "123",
				"userId": 0,
				"properties": "Humidity:65.2",
				"uuid": "218acf0d-2e22-422f-a7ce-62b808cb375c",
				"ensureTime": null,
				"createTime": "2022-12-06 14:11:22",
				"status": 3,
				"endTime": "2022-12-06 16:38:56"
			},
			{
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"warningId": 8,
				"warningKey": "warning1",
				"warningLevel": 30,
				"warningName": "警告名1",
				"warningDesc": "123",
				"userId": 0,
				"properties": "Humidity:65.2",
				"uuid": "2532ee61-bf6c-4d5a-b4a3-34082456ee47",
				"ensureTime": null,
				"createTime": "2022-12-06 14:11:22",
				"status": 3,
				"endTime": "2022-12-06 16:38:56"
			},
			{
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"warningId": 8,
				"warningKey": "warning1",
				"warningLevel": 30,
				"warningName": "警告名1",
				"warningDesc": "123",
				"userId": 0,
				"properties": "Humidity:82",
				"uuid": "65509893-b1ad-445b-88c1-44c5f9a90aa7",
				"ensureTime": null,
				"createTime": "2022-12-06 14:11:22",
				"status": 3,
				"endTime": "2022-12-06 16:38:56"
			},
			{
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"warningId": 8,
				"warningKey": "warning1",
				"warningLevel": 30,
				"warningName": "警告名1",
				"warningDesc": "123",
				"userId": 0,
				"properties": "Humidity:82",
				"uuid": "748b8688-82f6-45f9-8774-fceb627f80b6",
				"ensureTime": null,
				"createTime": "2022-12-06 14:11:22",
				"status": 3,
				"endTime": "2022-12-06 16:38:56"
			}
		],
		"last": false,
		"totalPages": 2,
		"totalElements": 7,
		"number": 0,
		"size": 5,
		"sort": null,
		"first": true,
		"numberOfElements": 5
	},
	"requestId": "35cb265e-65ca-4c51-a502-84226ab26b27",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.productKey | h7s72qjeGaM | string | 产品key |
| data.content.deviceName | test2_1 | string | 设备名称 |
| data.content.warningId | 7 | number | 告警id |
| data.content.warningKey | warning5 | string | 告警标识 |
| data.content.warningLevel | 30 | string | 告警规则: 10=普通. 20=重要, 30=严重, 40=紧急 |
| data.content.warningName | 警告名5 | string | 告警名 |
| data.content.warningDesc | 123 | string | 告警描述 |
| data.content.userId | 0 | number | 用户id |
| data.content.properties | Humidity:66 | string | 关联属性 |
| data.content.uuid | d3960af1-ae20-4b52-b8e2-b31ed53cc5ba | string | - |
| data.content.ensureTime | - | object | 确认时间 |
| data.content.createTime | 2022-12-06 14:11:22 | string | 创建时间 |
| data.content.status | 3 | number | 状态: 1=待确认,2=处理中,3=已处理 |
| data.content.endTime | 2022-12-06 16:38:56 | string | 结束时间 |
| data.last | false | string | 最后一页 |
| data.totalPages | 2 | number | 总页数 |
| data.totalElements | 7 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 5 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 5 | number | 总元素个数 |
| requestId | 35cb265e-65ca-4c51-a502-84226ab26b27 | string | 网关设备 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 告警中心

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-03 11:40:06

> 更新时间: 2022-12-06 16:53:43

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotWarning/warningCenter?startTime=1638301041000&endTime=1668301041000&warningName=1&page=0&size=10&status=1

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| startTime | 1638301041000 | Text | 是 | 开始时间 |
| endTime | 1668301041000 | Text | 是 | 结束时间 |
| warningName | 1 | Text | 否 | 告警标识 |
| page | 0 | Text | 否 | 分页页码，数字类型 |
| size | 10 | Text | 否 | 每页元素个数 |
| status | 1 | Text | 是 | 状态:1=待确认, 2=处理中,3=已处理 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"warningId": 8,
				"warningKey": "warning1",
				"warningName": "警告名1",
				"warningDesc": "123",
				"userId": 0,
				"properties": "Humidity:89",
				"uuid": "37f54ac7-ae0b-4444-a5d5-1ea08bedb7bb",
				"ensureTime": null,
				"createTime": "2022-08-03 03:21:39",
				"isHistory": 1
			},
			{
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"warningId": 6,
				"warningKey": "warning1",
				"warningName": "警告名1",
				"warningDesc": "123",
				"userId": 0,
				"properties": "Humidity:89",
				"uuid": "37f54ac7-ae0b-4444-a5d5-1ea08bedb7bb",
				"ensureTime": null,
				"createTime": "2022-08-03 03:21:39",
				"isHistory": 1
			}
		],
		"last": true,
		"totalPages": 1,
		"totalElements": 2,
		"number": 0,
		"size": 10,
		"sort": null,
		"first": true,
		"numberOfElements": 2
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.productKey | h7s72qjeGaM | string | 产品key |
| data.content.deviceName | test2_1 | string | 设备名称 |
| data.content.warningId | 8 | number | - |
| data.content.warningKey | warning1 | string | 告警标识 |
| data.content.warningName | 警告名1 | string | 告警名 |
| data.content.warningDesc | 123 | string | 告警描述 |
| data.content.userId | 0 | number | 用户id |
| data.content.properties | Humidity:89 | string | - |
| data.content.uuid | 37f54ac7-ae0b-4444-a5d5-1ea08bedb7bb | string | - |
| data.content.ensureTime | - | object | - |
| data.content.createTime | 2022-08-03 03:21:39 | string | 创建时间 |
| data.content.isHistory | 1 | number | - |
| data.last | true | string | 最后一页 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 2 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 10 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 2 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

# OTA升级

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-25 10:33:28

> 更新时间: 2022-07-25 10:33:27

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 业务逻辑

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-01-04 10:55:29

> 更新时间: 2023-01-04 10:55:02

**OTA基于阿里云升级逻辑:
创建文件
    接口:	/iotOTA/createFile
    阿里云:	升级包列表会创建n个升级包, //n=选择产品数
    数据库:	iot_ota_file_tbl添加一条记录
创建升级任务(下发文件)
    接口:	/iotOTA/createJob
    阿里云:	每个升级包文件下会创建一个任务, 
        调用阿里云添加设备到队列接口	//升级包下一个产品会调用一次接口
    数据库:	iot_ota_job_tbl添加一条记录, iot_ota_job_log_tbl添加n条记录(n对应设备数)**

**Query**

## 上传升级文件包

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-25 10:35:15

> 更新时间: 2023-03-21 10:45:54

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/uploadFile

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| file | - | string | 是 | ota升级文件 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"objectStorage": "OSS",
		"firmwareUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin"
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.objectStorage | OSS | string | 文件储存引擎 |
| data.firmwareUrl | https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin | string | 文件url,创建固件会使用 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 文件上传所有信息提交

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-25 14:41:08

> 更新时间: 2023-03-21 10:56:11

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/createFile

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| fileName | v41 | Text | 是 | - |
| fileVersion | 4.0 | Text | 是 | - |
| fileUrl | https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin | Text | 是 | - |
| fileComment | 哈哈哈 | Text | 是 | - |
| productKeys | h7s7NxjuhLw,h7s72qjeGaM | Text | 否 | - |
| projectId | 2 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"fileId": "7"
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.fileId | 7 | string | 文件id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 新建升级任务

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-26 14:50:34

> 更新时间: 2023-10-18 09:57:40

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/createJob

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobName | job2 | Text | 是 | 任务名 |
| scheduleTime | 1679987727000 | Text | 否 | 任务执行时间, 毫秒时间戳, 不传或null为立即升级 |
| needConfirm | false | boolean | 是 | APP确认升级 |
| needPush | true | Text | 是 | 云端主动推送升级 |
| retryCount | 2 | Text | 是 | 最大重试次数 |
| retryInterval | 10 | Text | 是 | 升级重试间隔（min） |
| timeoutInMinutes | 10 | Text | 是 | 升级超时时间（min） |
| overwriteMode | false | boolean | 是 | 是否覆盖设备之前的升级任务 |
| devices | h7s72qjeGaM\|test2_1,h7s7NxjuhLw\|test_1 | Text | 是 | 升级设备 |
| fileId | 11 | Text | 是 | 升级文件id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"jobId": 11,
		"jobName": "job2",
		"scheduleTime": null,
		"needConfirm": true,
		"needPush": true,
		"retryCount": 2,
		"retryInterval": 10,
		"timeoutInMinutes": 10,
		"overwriteMode": 2,
		"userId": 0,
		"createTime": null,
		"deviceCnt": 6,
		"iotJobIds": "5mFmX6evJcvRX3mlpfLV020200,0i3npMftxtnLIBh0ghDl020200",
		"successCnt": null,
		"groupId": 2,
		"fileId": 8
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.jobId | 11 | number | - |
| data.jobName | job2 | string | 任务名 |
| data.scheduleTime | - | object | 任务执行时间 |
| data.needConfirm | true | string | APP确认升级 |
| data.needPush | true | string | 云端主动推送升级 |
| data.retryCount | 2 | number | 最大重试次数 |
| data.retryInterval | 10 | number | 升级重试间隔（min） |
| data.timeoutInMinutes | 10 | number | 升级超时时间（min） |
| data.overwriteMode | 2 | number | 是否覆盖设备之前的升级任务 |
| data.userId | 0 | number | 用户id |
| data.createTime | - | object | 创建时间 |
| data.deviceCnt | 6 | number | - |
| data.iotJobIds | 5mFmX6evJcvRX3mlpfLV020200,0i3npMftxtnLIBh0ghDl020200 | string | - |
| data.successCnt | - | object | - |
| data.groupId | 2 | number | - |
| data.fileId | 8 | number | 文件id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 升级文件列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-25 16:54:14

> 更新时间: 2022-12-20 14:43:02

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/fileList?projectId=2&productKey=&fileName=&page=&size=

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 2 | Text | 是 | - |
| productKey | - | string | 否 | 产品key |
| fileName | - | string | 否 | - |
| page | - | string | 否 | 分页页码，数字类型 |
| size | - | string | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"content": [
			{
				"fileId": 11,
				"userId": 0,
				"fileName": "v4",
				"fileVersion": "4.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-08-01 14:26:00",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": "h7s7NxjuhLw=8lk2f2NxnGB769t3q9ZW030100,h7s72qjeGaM=QDedkY3eTxEjNxdzOfu1030100",
				"projectId": 2
			},
			{
				"fileId": 10,
				"userId": 0,
				"fileName": "apiTest17",
				"fileVersion": "17.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-08-01 10:06:03",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": "h7s7NxjuhLw=jYiQahmas0Pmyy8gXQuA030100,h7s72qjeGaM=UEwGvcuepulCcreX2J2P030100",
				"projectId": 2
			},
			{
				"fileId": 9,
				"userId": 0,
				"fileName": "apiTest16",
				"fileVersion": "16.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-08-01 09:29:11",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": "h7s7NxjuhLw=fmAiptGuwrg6AxtzObGu030100,h7s72qjeGaM=uk7vi1oBijXKFeDYCY5w030100",
				"projectId": 2
			},
			{
				"fileId": 8,
				"userId": 0,
				"fileName": "apiTest15",
				"fileVersion": "13.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-07-27 15:21:38",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": "h7s7NxjuhLw=AR5sJagWc2lANPBwWAhJ030100,h7s72qjeGaM=1DrJKlz0VX2c2MEa8x8B030100",
				"projectId": 2
			},
			{
				"fileId": 7,
				"userId": 0,
				"fileName": "修改后的名称2",
				"fileVersion": "12.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-07-26 16:43:54",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": "",
				"projectId": 2
			},
			{
				"fileId": 6,
				"userId": 0,
				"fileName": "apiTest13",
				"fileVersion": "11.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-07-26 15:55:59",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": "h7s7NxjuhLw=xWV8zLN3LMzDQXo4OOaZ030100,h7s72qjeGaM=ueT2GkRG8qGxv5UsxtLv030100",
				"projectId": 2
			},
			{
				"fileId": 5,
				"userId": 0,
				"fileName": "apiTest12",
				"fileVersion": "10.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-07-26 15:48:31",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": "h7s7NxjuhLw=WZu6jVLUcf7vjMmJ2UES030100,h7s72qjeGaM=MR9gdxm0htW8Hwkcp2Su030100",
				"projectId": 2
			},
			{
				"fileId": 4,
				"userId": 0,
				"fileName": "apiTest11",
				"fileVersion": "9.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-07-25 16:08:05",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": null,
				"projectId": 2
			},
			{
				"fileId": 2,
				"userId": 0,
				"fileName": "apiTest10",
				"fileVersion": "8.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-07-25 15:38:15",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": null,
				"projectId": 2
			},
			{
				"fileId": 1,
				"userId": 0,
				"fileName": "apiTest9",
				"fileVersion": "8.0",
				"filePath": null,
				"fileComment": "哈哈哈",
				"createTime": "2022-07-25 14:58:26",
				"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"productFirmware": null,
				"projectId": 2
			}
		],
		"last": true,
		"totalElements": 10,
		"totalPages": 1,
		"number": 0,
		"size": 20,
		"sort": null,
		"first": true,
		"numberOfElements": 10
	},
	"requestId": "a7e7ba58-1f7a-47e6-b838-95bb605672c0",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.fileId | 11 | number | 文件id |
| data.content.userId | 0 | number | 用户id |
| data.content.fileName | v4 | string | 文件名 |
| data.content.fileVersion | 4.0 | string | 文件版本 |
| data.content.filePath | - | object | 文件路径 |
| data.content.fileComment | 哈哈哈 | string | 文件描述 |
| data.content.createTime | 2022-08-01 14:26:00 | string | 创建时间 |
| data.content.fileUrl | https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin | string | 文件上传后的url |
| data.content.productKeys | h7s7NxjuhLw,h7s72qjeGaM | string | 文件包含产品 |
| data.content.productFirmware | h7s7NxjuhLw=8lk2f2NxnGB769t3q9ZW030100,h7s72qjeGaM=QDedkY3eTxEjNxdzOfu1030100 | string | - |
| data.content.projectId | 2 | number | - |
| data.last | true | string | 最后一页 |
| data.totalElements | 10 | number | 总元素个数 |
| data.totalPages | 1 | number | 总页数 |
| data.number | 0 | number | 页码 |
| data.size | 20 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 10 | number | 总元素个数 |
| requestId | a7e7ba58-1f7a-47e6-b838-95bb605672c0 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 修改文件信息

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-27 09:28:03

> 更新时间: 2023-03-21 10:56:15

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/updateFile

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| fileId | 7 | Text | 是 | 文件id |
| fileName | 修改后的名称2 | Text | 否 | 文件名 |
| productKeys | h7s7NxjuhLw,h7s72qjeGaM | Text | 否 | 文件包含产品 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"fileId": 7,
		"userId": 0,
		"fileName": "修改后的名称2",
		"fileVersion": "12.0",
		"filePath": null,
		"fileComment": "哈哈哈",
		"createTime": "2022-07-26 08:43:54",
		"fileUrl": "https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin",
		"productKeys": "h7s7NxjuhLw,h7s72qjeGaM,223",
		"productFirmware": ""
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.fileId | 7 | number | 文件id |
| data.userId | 0 | number | 用户id |
| data.fileName | 修改后的名称2 | string | 文件名 |
| data.fileVersion | 12.0 | string | 文件版本 |
| data.filePath | - | object | 文件路径 |
| data.fileComment | 哈哈哈 | string | 文件描述 |
| data.createTime | 2022-07-26 08:43:54 | string | 创建时间 |
| data.fileUrl | https://iotx-ota.oss-cn-shanghai.aliyuncs.com/ota/7ffdfbca143d5dda176f9d48765b3162/00B6D9A9D45D4C69921C0BA2FD624E62.bin | string | 文件url |
| data.productKeys | h7s7NxjuhLw,h7s72qjeGaM,223 | string | 文件包含产品 |
| data.productFirmware | - | object | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 升级文件详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-12-20 14:36:32

> 更新时间: 2022-12-20 14:36:50

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/fileInfo?fileId=13

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| fileId | 13 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 升级批次详细信息

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-28 14:43:34

> 更新时间: 2023-03-22 17:16:23

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/jobInfo?jobId=10

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobId | 10 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"deviceCnt": 6,
		"userId": 0,
		"groupId": 2,
		"createTime": null,
		"timeoutInMinutes": 10,
		"iotJobIds": "oNNopLCGsFksnHnx04PA020200,VemuURBHt83VuNd6P1B1020200",
		"fileId": 8,
		"overwriteMode": 2,
		"retryCount": 2,
		"jobId": 10,
		"needPush": true,
		"retryInterval": 10,
		"needConfirm": true,
		"scheduleTime": null,
		"jobName": "job2",
		"IN_PROGRESS": 0,
		"ALL": 6,
		"FAILED": 0,
		"SUCCEEDED": 0,
		"CANCELED": 2,
		"WAIT": 0
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.deviceCnt | 6 | number | - |
| data.userId | 0 | number | 用户id |
| data.groupId | 2 | number | - |
| data.createTime | - | object | 创建时间 |
| data.timeoutInMinutes | 10 | number | 升级超时时间（min） |
| data.iotJobIds | oNNopLCGsFksnHnx04PA020200,VemuURBHt83VuNd6P1B1020200 | string | - |
| data.fileId | 8 | number | 文件id |
| data.overwriteMode | 2 | number | 是否覆盖设备之前的升级任务 |
| data.retryCount | 2 | number | 最大重试次数 |
| data.jobId | 10 | number | - |
| data.needPush | true | string | 云端主动推送升级 |
| data.retryInterval | 10 | number | 升级重试间隔（min） |
| data.needConfirm | true | string | APP确认升级 |
| data.scheduleTime | - | object | 任务执行时间 |
| data.jobName | job2 | string | 任务名 |
| data.IN_PROGRESS | 0 | number | - |
| data.ALL | 6 | number | - |
| data.FAILED | 0 | number | - |
| data.SUCCEEDED | 0 | number | - |
| data.CANCELED | 2 | number | - |
| data.WAIT | 0 | number | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 升级批次设备列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-28 16:48:02

> 更新时间: 2023-01-04 10:55:53

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/jobDeviceInfo?jobId=135&page=0&size=10&upStatus=CANCELED

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobId | 135 | Text | 是 | - |
| page | 0 | Text | 否 | 分页页码，数字类型 |
| size | 10 | Text | 否 | 每页元素个数 |
| productKey | h7s72qjeGaM | Text | 否 | 产品key |
| upStatus | CANCELED | Text | 否 | 升级状态: PLANNE=等待中, IN_PROGRESS=升级中, COMPLETED=已完成, CANCELED=已取消 |
| deviceName | 1 | Text | 否 | 设备名称 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"last": true,
		"totalElements": 3,
		"totalPages": 1,
		"number": 0,
		"size": 5,
		"content": [
			{
				"fileName": "apiTest15",
				"destVersion": null,
				"updateTime": null,
				"upStatus": null,
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_2",
				"srcVersion": null,
				"productName": "test2"
			},
			{
				"fileName": "apiTest15",
				"destVersion": "13.0",
				"updateTime": "2022-07-28 06:44:50",
				"upStatus": "CANCELED",
				"productKey": "h7s72qjeGaM",
				"deviceName": "test2_1",
				"srcVersion": "15.0",
				"productName": "test2"
			},
			{
				"fileName": "apiTest15",
				"destVersion": null,
				"updateTime": null,
				"upStatus": null,
				"productKey": "h7s7NxjuhLw",
				"deviceName": "test_1",
				"srcVersion": null,
				"productName": "test"
			}
		],
		"sort": null,
		"first": true,
		"numberOfElements": 3
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.last | true | string | 最后一页 |
| data.totalElements | 3 | number | 总元素个数 |
| data.totalPages | 1 | number | 总页数 |
| data.number | 0 | number | 页码 |
| data.size | 5 | number | 每页元素个数 |
| data.content | - | object | 消息详情 |
| data.content.fileName | apiTest15 | string | 文件名 |
| data.content.destVersion | - | object | 目标版本 |
| data.content.updateTime | - | object | 更新时间 |
| data.content.upStatus | - | object | 升级状态, 空为等待 |
| data.content.productKey | h7s72qjeGaM | string | 产品key |
| data.content.deviceName | test2_2 | string | 设备名称 |
| data.content.srcVersion | - | object | - |
| data.content.productName | test2 | string | 产品名(阿里云平台) |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 3 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 升级批次列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-29 09:24:16

> 更新时间: 2023-01-03 11:19:42

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/jobListSearch?page=0&size=5&mainJobStatus=COMPLETED&startTime=1656608400000

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | 0 | Text | 否 | 分页页码，数字类型 |
| size | 5 | Text | 否 | 每页元素个数 |
| mainJobStatus | COMPLETED | Text | 否 | 状态: PLANNE=等待中, IN_PROGRESS=升级中, COMPLETED=已完成, CANCELED=已取消 |
| jobName | 232 | Text | 否 | - |
| startTime | 1656608400000 | Text | 否 | 开始时间 |
| endTime | 1659425962000 | Text | 否 | 结束时间 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"last": false,
		"totalPages": 3,
		"totalElements": 11,
		"number": 0,
		"size": 5,
		"content": [
			{
				"endTime": "2022-08-02 15:38:45",
				"startTime": "2022-08-02 15:37:49",
				"deviceCnt": 2,
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"userId": 0,
				"jobId": 129,
				"groupId": null,
				"createTime": "2022-08-02 15:37:50",
				"fileId": 11,
				"iotJobIds": "qdHu9VK1NqvK2SBJyihU020200,GT1RVoHBl1bNRSIRuopx020200",
				"overwriteMode": 2,
				"scheduleTime": null,
				"retryInterval": 10,
				"needPush": true,
				"retryCount": 2,
				"needConfirm": false,
				"timeoutInMinutes": 10,
				"jobStatusDetail": "qdHu9VK1NqvK2SBJyihU020200=COMPLETED,GT1RVoHBl1bNRSIRuopx020200=COMPLETED",
				"jobName": "job2",
				"jobCnt": 2,
				"mainJobStatus": "COMPLETED",
				"IN_PROGRESS": 0,
				"ALL": 2,
				"FAILED": 0,
				"SUCCEEDED": 0,
				"CANCELED": 2,
				"PLANNED": 0,
				"productNames": "",
				"userName": "abcj"
			},
			{
				"endTime": "2022-08-02 15:37:54",
				"startTime": "2022-08-02 15:37:27",
				"deviceCnt": 2,
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"userId": 0,
				"jobId": 128,
				"groupId": null,
				"createTime": "2022-08-02 15:37:28",
				"fileId": 11,
				"iotJobIds": "h41qsDID2sbsDAG0zI90020200,4T3BFVxMtKc8sVBVLdKZ020200",
				"overwriteMode": 2,
				"scheduleTime": null,
				"retryInterval": 10,
				"needPush": true,
				"retryCount": 2,
				"needConfirm": false,
				"timeoutInMinutes": 10,
				"jobStatusDetail": "4T3BFVxMtKc8sVBVLdKZ020200=COMPLETED,h41qsDID2sbsDAG0zI90020200=COMPLETED",
				"jobName": "job2232",
				"jobCnt": 2,
				"mainJobStatus": "COMPLETED",
				"IN_PROGRESS": 0,
				"ALL": 2,
				"FAILED": 0,
				"SUCCEEDED": 0,
				"CANCELED": 2,
				"PLANNED": 0,
				"productNames": "",
				"userName": "abcj"
			},
			{
				"endTime": "2022-08-02 15:37:29",
				"startTime": "2022-08-02 15:37:18",
				"deviceCnt": 2,
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"userId": 0,
				"jobId": 127,
				"groupId": null,
				"createTime": "2022-08-02 15:37:18",
				"fileId": 11,
				"iotJobIds": "6Hw2NLmwFVGMgBEbZ7G5020200,ZpSvmBYwvIKQSaMeC5KJ020200",
				"overwriteMode": 2,
				"scheduleTime": null,
				"retryInterval": 10,
				"needPush": true,
				"retryCount": 2,
				"needConfirm": false,
				"timeoutInMinutes": 10,
				"jobStatusDetail": "6Hw2NLmwFVGMgBEbZ7G5020200=COMPLETED,ZpSvmBYwvIKQSaMeC5KJ020200=COMPLETED",
				"jobName": "job2",
				"jobCnt": 2,
				"mainJobStatus": "COMPLETED",
				"IN_PROGRESS": 0,
				"ALL": 2,
				"FAILED": 0,
				"SUCCEEDED": 0,
				"CANCELED": 2,
				"PLANNED": 0,
				"productNames": "",
				"userName": "abcj"
			},
			{
				"endTime": "2022-08-02 15:36:53",
				"startTime": "2022-08-02 14:18:39",
				"deviceCnt": 2,
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"userId": 0,
				"jobId": 125,
				"groupId": null,
				"createTime": "2022-08-02 14:18:39",
				"fileId": 11,
				"iotJobIds": "byeICvAMeTnxm8LZPoI3020200,5nJPNYHsUNCgFslZtfJR020200",
				"overwriteMode": 2,
				"scheduleTime": null,
				"retryInterval": 10,
				"needPush": true,
				"retryCount": 2,
				"needConfirm": false,
				"timeoutInMinutes": 10,
				"jobStatusDetail": "5nJPNYHsUNCgFslZtfJR020200=COMPLETED,byeICvAMeTnxm8LZPoI3020200=COMPLETED",
				"jobName": "job2",
				"jobCnt": 2,
				"mainJobStatus": "COMPLETED",
				"IN_PROGRESS": 0,
				"ALL": 2,
				"FAILED": 0,
				"SUCCEEDED": 0,
				"CANCELED": 2,
				"PLANNED": 0,
				"productNames": "",
				"userName": "abcj"
			},
			{
				"endTime": null,
				"startTime": "2022-08-02 14:18:14",
				"deviceCnt": 2,
				"productKeys": "h7s7NxjuhLw,h7s72qjeGaM",
				"userId": 0,
				"jobId": 123,
				"groupId": null,
				"createTime": "2022-08-02 14:18:15",
				"fileId": 11,
				"iotJobIds": "qwe1wehNiMV6XAQBl7Fr020200,sORjkkb1ncWPnhlfCTrK020200",
				"overwriteMode": 2,
				"scheduleTime": null,
				"retryInterval": 10,
				"needPush": true,
				"retryCount": 2,
				"needConfirm": false,
				"timeoutInMinutes": 10,
				"jobStatusDetail": "sORjkkb1ncWPnhlfCTrK020200=COMPLETED,qwe1wehNiMV6XAQBl7Fr020200=COMPLETED",
				"jobName": "job2",
				"jobCnt": 2,
				"mainJobStatus": "COMPLETED",
				"IN_PROGRESS": 0,
				"ALL": 2,
				"FAILED": 0,
				"SUCCEEDED": 0,
				"CANCELED": 2,
				"PLANNED": 0,
				"productNames": "",
				"userName": "abcj"
			}
		],
		"sort": null,
		"first": true,
		"numberOfElements": 5
	},
	"requestId": "2bc69abc975f4a75bab05c3d64665602",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.last | false | string | 最后一页 |
| data.totalPages | 3 | number | 总页数 |
| data.totalElements | 11 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 5 | number | 每页元素个数 |
| data.content | - | object | 消息详情 |
| data.content.endTime | 2022-08-02 15:38:45 | string | 结束时间 |
| data.content.startTime | 2022-08-02 15:37:49 | string | 开始时间 |
| data.content.deviceCnt | 2 | number | 设备数 |
| data.content.jobId | 129 | number | - |
| data.content.userId | 0 | number | 用户id |
| data.content.productKeys | h7s7NxjuhLw,h7s72qjeGaM | string | - |
| data.content.groupId | - | object | 分组id, 创建升级任务会使用 |
| data.content.needPush | true | string | 云端主动推送升级 |
| data.content.createTime | 2022-08-02 15:37:50 | object | 创建时间,下达时间 |
| data.content.iotJobIds | qdHu9VK1NqvK2SBJyihU020200,GT1RVoHBl1bNRSIRuopx020200 | string | - |
| data.content.fileId | 11 | object | 文件id |
| data.content.timeoutInMinutes | 10 | number | 升级超时时间（min） |
| data.content.needConfirm | false | string | APP确认升级 |
| data.content.overwriteMode | 2 | number | 是否覆盖设备之前的升级任务 |
| data.content.retryInterval | 10 | number | 升级重试间隔（min） |
| data.content.retryCount | 2 | number | 最大重试次数 |
| data.content.scheduleTime | - | object | 任务执行时间, 如果是立即执行=null, 实际执行时间时startTime |
| data.content.jobStatusDetail | qdHu9VK1NqvK2SBJyihU020200=COMPLETED,GT1RVoHBl1bNRSIRuopx020200=COMPLETED | string | - |
| data.content.jobCnt | 2 | number | - |
| data.content.jobName | job2 | string | 任务名 |
| data.content.mainJobStatus | COMPLETED | string | 状态: PLANNED：等待中。IN_PROGRESS：升级中。COMPLETED：已完成。CANCELED：已取消。 |
| data.content.IN_PROGRESS | 0 | number | 升级中个数 |
| data.content.ALL | 2 | number | 全部个数 |
| data.content.FAILED | 0 | number | 失败个数 |
| data.content.SUCCEEDED | 0 | number | 成功个数 |
| data.content.CANCELED | 2 | number | 取消个数 |
| data.content.PLANNED | 0 | number | - |
| data.content.productNames | - | string | 产品名 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 5 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 取消升级任务

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-22 17:13:48

> 更新时间: 2023-03-24 14:47:29

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/cancelJob

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobId | 145 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 修改升级任务

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-24 15:01:34

> 更新时间: 2023-03-28 15:11:08

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/updateJob

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| jobId | 154 | string | 是 | - |
| jobName | qweqqq | string | 是 | 任务名 |
| scheduleTime | 1679989727000 | string | 否 | 任务执行时间, 毫秒时间戳, 不传或null为立即升级 |
| needConfirm | true | string | 是 | APP确认升级 |
| needPush | true | string | 是 | 云端主动推送升级 |
| retryCount | 1 | string | 是 | 最大重试次数 |
| retryInterval | 0 | string | 是 | 升级重试间隔（min） |
| timeoutInMinutes | 10 | string | 是 | 升级超时时间（min） |
| overwriteMode | false | string | 是 | 是否覆盖设备之前的升级任务 |
| fileId | 28 | string | 是 | 升级文件id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 工程任务

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-23 15:10:30

> 更新时间: 2022-08-23 15:10:28

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 业务逻辑

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-06 15:37:37

> 更新时间: 2022-09-06 15:36:40

```text
任务中心
初始化: 将工程还原到初始状态

任务\_工程\_场景\_模型 关系
![微信图片_20220906154346.png](https://img.cdn.apipost.cn/client/user/1092169/avatar/cfa77c8a6a2f1b1758b1d10c37dc42026316fa3f837fe.png)
```

**Query**

## 工程创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-23 15:16:54

> 更新时间: 2023-12-05 11:33:18

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectName | 测试工程96 | Text | 是 | - |
| projectType | 1 | Text | 是 | 工程类型:1=实训,2=竞技,3=教学 |
| maxSceneNum | 10 | number | 是 | 场景最大数量 |
| maxDevNum | 10 | Text | 否 | 终端最大数量 |
| projectTag | 测试,设备接入 | Text | 否 | 标签, 用","分割 |
| scenes | [{	"sceneTemp":"场景1xxx",		"sceneId":1,		"devicePlan":[		{			"deviceModel":"机械臂",			"id":"",				"deviceType":"0",				"accessType":"WIFI",				"linkObj":"real",			"maxFeatNum":10,			"maxServNum":8		}	]}] | array | 是 | 场景信息, json格式, 字段和说明如下 ↓
[{
	"sceneType":"home",	//场景类型:custom=自定义,home=智能家居,factory=智能制造,traffic=智慧交通,hospital=远程医疗
	"sceneTemp":"场景xxx",	//场景模板名
	"sceneId":1,	//场景id
	"devicePlan":[
		{
			"deviceModel":"机械臂",	//设备型号
			"id":"",	//规划设备id
			"deviceType":"0",	//设备类型:0=直连设备,1=网关设备,2=非直连子设备
			"accessType","WiFi",	//联网方式: 根据类型变化，当类型为非直连子设备时，取值: Modbus, OPC UA, ZigBee, BLE, 自定义(Custom)；当类型不为非直连子设备时，取值 WiFi, 蓝牙(BlueTooth), 蜂窝(Cellular), 以太网(Ethernet), LoRaWAN
			"linkObj":"real"	//映射对象:virtual=虚拟设备,real=硬件设备,virtualReal=虚实联动设备
			"maxFeatNum":10,	//最大属性数
			"maxServNum":8,		//最大服务数
		}
	]
}] |
| trainModule | scene,device,ops | Text | 是 | 实训模块: scene=场景规划,device=设备接入,ops=设备运维,digital=数字孪生 |
| scores | {"sceneScore":100,"modelScore"100,"deviceScore":100,"linkCloudScore":100,"sideWorkScore":100,"orderScore":100,"documScore":100,"twinsScore":100,"policyScore":100,"appScore":100} | Text | 否 | 实训分数, json格式, 字段说明如下 ↓
实训分数-数字场景新建	sceneScore
实训分数-设备模型创建	modelScore
实训分数-设备实例创建	deviceScore
实训分数-智能设备上云	linkCloudScore
实训分数-端侧工况上报	sideWorkScore
实训分数-云端指令下发	orderScore
实训分数-云端文件下发	documScore
实训分数-孪生场景搭建	twinsScore
实训分数-场景策略下发	policyScore
实训分数-数字孪生应用	appScore |
| referDocum | 教程.doc=cad23b2.doc,教程2.doc=bad23b2.doc | Text | 否 | 参考文档,格式: 原文件名=保存文件名, 多个用逗号分割, 暂支持doc,docx,ppt,pptx,pdf,xls,xlsx,vsd,vsdx,eddx,json格式 |
| publicSchool | 0 | integer | 是 | 是否学校内公开 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"projectId": 2,
		"sceneType": 0,
		"projectName": "测试工程",
		"projectType": 1,
		"projectLabel": "测试,设备接入",
		"steps": "[0:\"步骤1\", 1:\"步骤2\"]",
		"taskId": null,
		"createTime": "2022-08-237: 029:52",
		"updateTime": "2022-08-23 07:29:52"
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.projectId | 2 | number | 工程id |
| data.sceneType | 0 | number | 场景类型:0=自定义,1=智能家居,2=工业互联网,3=智慧交通,4=远程医疗 |
| data.projectName | 测试工程 | string | 工程名 |
| data.projectType | 1 | number | 工程类型:1=实训,2=竞技,3=教学 |
| data.projectLabel | 测试,设备接入 | string | 标签 |
| data.steps | [0:"步骤1", 1:"步骤2"] | string | 步骤 |
| data.taskId | - | object | - |
| data.createTime | 2022-08-23 07:29:52 | string | 创建时间 |
| data.updateTime | 2022-08-23 07:29:52 | string | 更新时间 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 工程场景列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-02-21 15:52:38

> 更新时间: 2023-02-22 11:25:54

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/sceneList?page=0&size=10&sceneType=home

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | 0 | string | 是 | 分页页码，数字类型 |
| size | 10 | string | 是 | 每页元素个数 |
| sceneType | home | string | 是 | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"sceneId": 15,
				"sceneName": "场景名称",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfsqwqewq",
				"createTime": "2022-09-14 16:22:44",
				"updateTime": "2022-09-14 16:22:44",
				"userId": 0,
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"projectId": 5,
				"sceneDevicePlanList": [
					{
						"id": 4,
						"sceneId": 15,
						"deviceModel": "机械臂",
						"deviceType": 0,
						"accessType": "WiFi",
						"linkObj": 2,
						"maxFeatNum": 10,
						"maxServNum": 10
					},
					{
						"id": 5,
						"sceneId": 15,
						"deviceModel": "智能音箱",
						"deviceType": 0,
						"accessType": "WiFi",
						"linkObj": 2,
						"maxFeatNum": 8,
						"maxServNum": 10
					},
					{
						"id": 6,
						"sceneId": 15,
						"deviceModel": "门禁闸机",
						"deviceType": 0,
						"accessType": "WiFi",
						"linkObj": 2,
						"maxFeatNum": 5,
						"maxServNum": 8
					}
				]
			},
			{
				"sceneId": 5,
				"sceneName": "场景名称2_副本",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfs",
				"createTime": "2022-09-13 14:55:05",
				"updateTime": "2022-09-13 14:55:05",
				"userId": 0,
				"sceneDevices": null,
				"projectId": 0,
				"sceneDevicePlanList": []
			},
			{
				"sceneId": 7,
				"sceneName": "场景名称2_副本",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfs",
				"createTime": "2022-09-13 14:55:41",
				"updateTime": "2022-09-13 14:55:41",
				"userId": 0,
				"sceneDevices": null,
				"projectId": 0,
				"sceneDevicePlanList": []
			},
			{
				"sceneId": 8,
				"sceneName": "场景名称",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfsqwqewq",
				"createTime": "2022-09-13 16:11:15",
				"updateTime": "2022-09-13 16:12:23",
				"userId": 0,
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"projectId": 5,
				"sceneDevicePlanList": []
			},
			{
				"sceneId": 9,
				"sceneName": "场景名称4",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfs",
				"createTime": "2022-09-13 16:11:38",
				"updateTime": "2022-09-13 16:11:38",
				"userId": 0,
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"projectId": 5,
				"sceneDevicePlanList": []
			},
			{
				"sceneId": 10,
				"sceneName": "场景名称_副本",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfsqwqewq",
				"createTime": "2022-09-13 16:29:06",
				"updateTime": "2022-09-13 16:29:06",
				"userId": 0,
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"projectId": 6,
				"sceneDevicePlanList": []
			},
			{
				"sceneId": 11,
				"sceneName": "场景名称_副本",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfsqwqewq",
				"createTime": "2022-09-13 16:29:53",
				"updateTime": "2022-09-13 16:29:53",
				"userId": 0,
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"projectId": 6,
				"sceneDevicePlanList": []
			},
			{
				"sceneId": 12,
				"sceneName": "场景名称4",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfs",
				"createTime": "2022-09-14 11:26:58",
				"updateTime": "2022-09-14 11:26:58",
				"userId": 0,
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"projectId": 6,
				"sceneDevicePlanList": []
			},
			{
				"sceneId": 1,
				"sceneName": "测试场景",
				"sceneType": "home",
				"sceneBelong": 1,
				"sceneModelBelong": null,
				"sceneData": "sdfs",
				"createTime": "2023-02-20 16:14:24",
				"updateTime": "2023-02-20 16:14:24",
				"userId": 0,
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"projectId": 2,
				"sceneDevicePlanList": [
					{
						"id": 1,
						"sceneId": 1,
						"deviceModel": "机械臂",
						"deviceType": 0,
						"accessType": "WiFi",
						"linkObj": 2,
						"maxFeatNum": 10,
						"maxServNum": 10
					},
					{
						"id": 2,
						"sceneId": 1,
						"deviceModel": "智能音箱",
						"deviceType": 0,
						"accessType": "WiFi",
						"linkObj": 2,
						"maxFeatNum": 8,
						"maxServNum": 10
					},
					{
						"id": 3,
						"sceneId": 1,
						"deviceModel": "门禁闸机",
						"deviceType": 0,
						"accessType": "WiFi",
						"linkObj": 2,
						"maxFeatNum": 5,
						"maxServNum": 8
					}
				]
			}
		],
		"totalPages": 1,
		"totalElements": 9,
		"last": true,
		"number": 0,
		"size": 10,
		"sort": null,
		"numberOfElements": 9,
		"first": true
	},
	"requestId": "3dddfe133d5144f8bba6dcbf194bf5f3",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.sceneId | 15 | number | 场景模板id |
| data.content.sceneName | 场景名称 | string | 场景模板名称 |
| data.content.sceneType | home | string | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| data.content.sceneBelong | 1 | number | 场景归属: 1=工程共有, 2=工程私有 |
| data.content.sceneModelBelong | - | object | 场景模板归属:1=平台通用,2=场景私有,3=系统存档 |
| data.content.sceneData | sdfsqwqewq | string | - |
| data.content.createTime | 2022-09-14 16:22:44 | string | 创建时间 |
| data.content.updateTime | 2022-09-14 16:22:44 | string | 更新时间 |
| data.content.userId | 0 | number | 用户id |
| data.content.sceneDevices | [{"deviceIotId":"XUbvGwMcOCvmEz6Rbi71h7s700","productKey":"h7s72qjeGaM","deviceName":"test2_1"},{"deviceIotId":"QxDn30BdD816c9ZwFQokh7s700","productKey":"h7s7NxjuhLw","deviceName":"test_3"}] | string | - |
| data.content.projectId | 5 | number | 工程id |
| data.content.sceneDevicePlanList | - | object | 场景终端规划 |
| data.content.sceneDevicePlanList.id | 4 | number | - |
| data.content.sceneDevicePlanList.sceneId | 15 | number | 场景id |
| data.content.sceneDevicePlanList.deviceModel | 机械臂 | string | 设备型号 |
| data.content.sceneDevicePlanList.deviceType | 0 | number | 设备类型 |
| data.content.sceneDevicePlanList.accessType | WiFi | string | 接入方式 |
| data.content.sceneDevicePlanList.linkObj | 2 | number | 映射对象 |
| data.content.sceneDevicePlanList.maxFeatNum | 10 | number | 最大属性数 |
| data.content.sceneDevicePlanList.maxServNum | 10 | number | 最大服务数 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 9 | number | 总元素个数 |
| data.last | true | string | 最后一页 |
| data.number | 0 | number | 页码 |
| data.size | 10 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.numberOfElements | 9 | number | 总元素个数 |
| data.first | true | string | 是否是第一页 |
| requestId | 958b790c28e64ef38eb1a72ad85758ed | string | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 工程详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-02-22 11:06:00

> 更新时间: 2023-02-22 11:13:51

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/detail?projectId=2

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 2 | Text | 是 | 工程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"projectId": 2,
		"projectName": "测试工程3",
		"projectType": 1,
		"projectTag": "测试,设备接入",
		"createTime": "2023-02-21 11:36:36",
		"updateTime": "2023-02-21 11:36:36",
		"creatorId": 0,
		"userId": 0,
		"initialize": null,
		"srcProjectId": null,
		"maxSceneNum": 10,
		"maxDevNum": 10,
		"trainModule": "scene,device",
		"referDocum": "http://xxx.com/xxx,http://aa.com/a",
		"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
		"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
	},
	"requestId": "881b3db6a49b4ac7a9d5614646221acd",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.projectId | 2 | number | 工程id |
| data.projectName | 测试工程3 | string | 工程名 |
| data.projectType | 1 | number | 工程类型:1=实训,2=金晒 |
| data.projectTag | 测试,设备接入 | string | 标签, 用","分割 |
| data.createTime | 2023-02-21 11:36:36 | string | 创建时间 |
| data.updateTime | 2023-02-21 11:36:36 | string | 更新时间 |
| data.creatorId | 0 | number | 创建用户id |
| data.userId | 0 | number | 使用用户id |
| data.initialize | - | object | 是否已经初始化 |
| data.srcProjectId | - | object | 被复制的工程id |
| data.maxSceneNum | 10 | number | 场景最大数量 |
| data.maxDevNum | 10 | number | 终端最大数量 |
| data.trainModule | scene,device | string | 实训模块: scene=场景规划,device=设备接入,ops=设备运维,digital=数字孪生 |
| data.referDocum | http://xxx.com/xxx,http://aa.com/a | string | 参考文档 |
| data.scores | {"sceneScore":100,"modelScore"100,"deviceScore":100,"linkCloudScore":100,"sideWorkScore":100,"orderScore":100,"documScore":100,"twinsScore":100,"policyScore":100,"appScore":100} | string | 实训分数, json格式, 字段说明如下 ↓
实训分数-数字场景新建	sceneScore
实训分数-设备模型创建	modelScore
实训分数-设备实例创建	deviceScore
实训分数-智能设备上云	linkCloudScore
实训分数-端侧工况上报	sideWorkScore
实训分数-云端指令下发	orderScore
实训分数-云端文件下发	documScore
实训分数-孪生场景搭建	twinsScore
实训分数-场景策略下发	policyScore
实训分数-数字孪生应用	appScore |
| data.scenes | [{	"sceneTemp":"场景1xxx",		"sceneId":1,		"devicePlan":[		{			"deviceModel":"机械臂",			"id":"",				"deviceType":"0",				"accessType","WIFI",				"linkObj":"real",			"maxFeatNum":10,			"maxServNum":8		}	]}] | string | 场景信息, json格式, 字段和说明如下 ↓
[{
	"sceneType":"home",	//场景类型:custom=自定义,home=智能家居,factory=智能制造,traffic=智慧交通,hospital=远程医疗
	"sceneTemp":"场景xxx",	//场景模板名
	"sceneId":1,	//场景id
	"devicePlan":[
		{
			"deviceModel":"机械臂",	//设备型号
			"id":"",	//规划设备id
			"deviceType":"0",	//设备类型:0=直连设备,1=网关设备,2=非直连子设备
			"accessType","WIFI",	//联网方式: 根据类型变化，当类型为非直连子设备时，取值: Modbus, OPC UA, ZigBee, BLE, 自定义(Custom)；当类型不为非直连子设备时，取值Wi-Fi(WIFI),蓝牙(BLUE),蜂窝,以太网,LoRaWAN WIFI=wifi,CELLULAR=蜂窝,ETHERNET=以太网
			"linkObj":"real"	//映射对象:virtual=虚拟设备,real=硬件设备,virtualReal=虚实联动设备
			"maxFeatNum":10,	//最大属性数
			"maxServNum":8,		//最大服务数
		}
	]
}] |
| requestId | 881b3db6a49b4ac7a9d5614646221acd | string | 请求唯一id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 工程删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-23 15:29:20

> 更新时间: 2024-12-26 14:36:27

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/delete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 162 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": null,
	"requestId": "e0435a46f2ed4b9dbb286712d80d0fdb",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| requestId | e0435a46f2ed4b9dbb286712d80d0fdb | string | 请求唯一id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 工程修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-02-21 14:01:50

> 更新时间: 2023-02-22 11:27:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 35 | Text | 是 | 工程id |
| projectName | 测试工程6 | Text | 是 | - |
| projectType | 1 | Text | 是 | 工程类型:1=实训,2=竞技,3=教学 |
| maxSceneNum | 10 | number | 是 | 场景最大数量 |
| maxDevNum | 10 | Text | 否 | 终端最大数量 |
| projectTag | 测试,设备接入 | Text | 否 | 标签, 用","分割 |
| scenes | [{	"sceneTemp":"场景1xxx",		"sceneId":1,		"devicePlan":[		{			"deviceModel":"机械臂",			"id":"",				"deviceType":"0",				"accessType","WIFI",				"linkObj":"real",			"maxFeatNum":10,			"maxServNum":8		}	]}] | array | 是 | 场景信息, json格式, 字段和说明如下 ↓
[{
	"sceneType":"home",	//场景类型:custom=自定义,home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗
	"sceneTemp":"场景xxx",	//场景模板名
	"sceneId":1,	//场景id
	"devicePlan":[
		{
			"deviceModel":"机械臂",	//设备型号
			"id":"",	//规划设备id
			"deviceType":"0",	//设备类型:0=直连设备,1=网关设备,2=非直连子设备
			"accessType","WIFI",	//联网方式: 根据类型变化，当类型为非直连子设备时，取值: Modbus, OPC UA, ZigBee, BLE, 自定义(Custom)；当类型不为非直连子设备时，取值 WiFi, 蓝牙(BlueTooth), 蜂窝(Cellular), 以太网(Ethernet), LoRaWAN
			"linkObj":"real"	//映射对象:virtual=虚拟设备,real=硬件设备,virtualReal=虚实联动设备
			"maxFeatNum":10,	//最大属性数
			"maxServNum":8,		//最大服务数
		}
	]
}] |
| trainModule | scene | Text | 是 | 实训模块: scene=场景规划,device=设备接入,ops=设备运维,digital=数字孪生 |
| scores | {"sceneScore":100,"modelScore"100,"deviceScore":100,"linkCloudScore":100,"sideWorkScore":100,"orderScore":100,"documScore":100,"twinsScore":100,"policyScore":100,"appScore":100} | Text | 否 | 实训分数, json格式, 字段说明如下 ↓
实训分数-数字场景新建	sceneScore
实训分数-设备模型创建	modelScore
实训分数-设备实例创建	deviceScore
实训分数-智能设备上云	linkCloudScore
实训分数-端侧工况上报	sideWorkScore
实训分数-云端指令下发	orderScore
实训分数-云端文件下发	documScore
实训分数-孪生场景搭建	twinsScore
实训分数-场景策略下发	policyScore
实训分数-数字孪生应用	appScore |
| referDocum | http://xxx.com/xxx | Text | 否 | 参考文档,多个用逗号分割,暂支持doc,docx,ppt,pptx,pdf,xls,xlsx,vsd,vsdx,eddx,json格式 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"projectId": 35,
		"projectName": "测试工程6",
		"projectType": 1,
		"projectTag": "测试,设备接入",
		"createTime": "2023-02-21 11:45:02",
		"updateTime": "2023-02-22 11:27:13",
		"creatorId": 0,
		"userId": 0,
		"initialize": null,
		"srcProjectId": null,
		"maxSceneNum": 10,
		"maxDevNum": 10,
		"trainModule": "scene",
		"referDocum": "http://xxx.com/xxx",
		"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
		"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
	},
	"requestId": "e6ccfe6783f040719dec69b0c1a6451d",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.projectId | 2 | number | 工程id |
| data.sceneType | 0 | number | 场景类型:0=自定义,1=智能家居,2=工业互联网,3=智慧交通,4=远程医疗 |
| data.projectName | 测试工程 | string | 工程名 |
| data.projectType | 1 | number | 工程类型:1=实训,2=竞技,3=教学 |
| data.projectLabel | 测试,设备接入 | string | 标签 |
| data.steps | [0:"步骤1", 1:"步骤2"] | string | 步骤 |
| data.taskId | - | object | - |
| data.createTime | 2022-08-23 07:29:52 | string | 创建时间 |
| data.updateTime | 2022-08-23 07:29:52 | string | 更新时间 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 工程列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-05 11:48:57

> 更新时间: 2023-02-22 11:25:43

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/list?page=0&size=10&type=myCreate

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | 0 | Text | 否 | 分页页码，数字类型 |
| size | 10 | Text | 否 | 每页元素个数 |
| type | myCreate | Text | 是 | 类型: recent=最近工程, myCreate=自建工程, system=系统工程 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"projectId": 3,
				"projectName": "测试工程",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 11:44:34",
				"updateTime": "2023-02-22 11:19:36",
				"creatorId": 0,
				"userId": 0,
				"initialize": 1,
				"srcProjectId": 2,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene,device",
				"referDocum": "http://xxx.com/xxx,http://aa.com/a",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			},
			{
				"projectId": 41,
				"projectName": "测试工程6_副本_副本",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 14:28:06",
				"updateTime": "2023-02-21 14:28:06",
				"creatorId": 0,
				"userId": 0,
				"initialize": null,
				"srcProjectId": 40,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene",
				"referDocum": "http://xxx.com/xxx",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			},
			{
				"projectId": 40,
				"projectName": "测试工程6_副本",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 14:27:47",
				"updateTime": "2023-02-21 14:27:47",
				"creatorId": 0,
				"userId": 0,
				"initialize": null,
				"srcProjectId": 36,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene",
				"referDocum": "http://xxx.com/xxx",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			},
			{
				"projectId": 36,
				"projectName": "测试工程6",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 11:45:06",
				"updateTime": "2023-02-21 14:04:17",
				"creatorId": 0,
				"userId": 0,
				"initialize": null,
				"srcProjectId": null,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene",
				"referDocum": "http://xxx.com/xxx",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			},
			{
				"projectId": 35,
				"projectName": "测试工程5",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 11:45:02",
				"updateTime": "2023-02-21 11:45:02",
				"creatorId": 0,
				"userId": 0,
				"initialize": null,
				"srcProjectId": null,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene,device",
				"referDocum": "http://xxx.com/xxx,http://aa.com/a",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			},
			{
				"projectId": 34,
				"projectName": "测试工程4",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 11:44:58",
				"updateTime": "2023-02-21 11:44:58",
				"creatorId": 0,
				"userId": 0,
				"initialize": null,
				"srcProjectId": null,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene,device",
				"referDocum": "http://xxx.com/xxx,http://aa.com/a",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			},
			{
				"projectId": 33,
				"projectName": "测试工程2",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 11:44:53",
				"updateTime": "2023-02-21 11:44:53",
				"creatorId": 0,
				"userId": 0,
				"initialize": null,
				"srcProjectId": null,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene,device",
				"referDocum": "http://xxx.com/xxx,http://aa.com/a",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			},
			{
				"projectId": 32,
				"projectName": "测试工程1",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 11:44:49",
				"updateTime": "2023-02-21 11:44:49",
				"creatorId": 0,
				"userId": 0,
				"initialize": null,
				"srcProjectId": null,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene,device",
				"referDocum": "http://xxx.com/xxx,http://aa.com/a",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			},
			{
				"projectId": 2,
				"projectName": "测试工程3",
				"projectType": 1,
				"projectTag": "测试,设备接入",
				"createTime": "2023-02-21 11:36:36",
				"updateTime": "2023-02-21 11:36:36",
				"creatorId": 0,
				"userId": 0,
				"initialize": null,
				"srcProjectId": null,
				"maxSceneNum": 10,
				"maxDevNum": 10,
				"trainModule": "scene,device",
				"referDocum": "http://xxx.com/xxx,http://aa.com/a",
				"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
				"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
			}
		],
		"last": true,
		"totalPages": 1,
		"totalElements": 9,
		"number": 0,
		"size": 10,
		"sort": null,
		"first": true,
		"numberOfElements": 9
	},
	"requestId": "45c1f5d497004713942f2ac3c8ef7f02",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.projectId | 3 | number | 工程id |
| data.content.projectName | 测试工程 | string | 工程名 |
| data.content.projectType | 1 | number | 工程类型:1=实训,2=金晒 |
| data.content.projectTag | 测试,设备接入 | string | 标签, 用","分割 |
| data.content.createTime | 2023-02-21 11:44:34 | string | 创建时间 |
| data.content.updateTime | 2023-02-22 11:19:36 | string | 更新时间 |
| data.content.creatorId | 0 | number | 创建用户id |
| data.content.userId | 0 | number | 用户id |
| data.content.initialize | 1 | number | 是否已经初始化 |
| data.content.srcProjectId | 2 | number | 被复制的工程id |
| data.content.maxSceneNum | 10 | number | 场景最大数量 |
| data.content.maxDevNum | 10 | number | 终端最大数量 |
| data.content.trainModule | scene,device | string | 实训模块: scene=场景规划,device=设备接入,ops=设备运维,digital=数字孪生 |
| data.content.referDocum | http://xxx.com/xxx,http://aa.com/a | string | 参考文档 |
| data.content.scores | {"sceneScore":100,"modelScore"100,"deviceScore":100,"linkCloudScore":100,"sideWorkScore":100,"orderScore":100,"documScore":100,"twinsScore":100,"policyScore":100,"appScore":100} | string | 实训分数, json: {
sceneScore
modelScore
deviceScore
linkCloudScore
sideWorkScore
orderScore
documScore
twinsScore
policyScore
appScore

} |
| data.content.scenes | [{	"sceneTemp":"场景1xxx",		"sceneId":1,		"devicePlan":[		{			"deviceModel":"机械臂",			"id":"",				"deviceType":"0",				"accessType","WIFI",				"linkObj":"real",			"maxFeatNum":10,			"maxServNum":8		}	]}] | string | 场景信息, json格式 |
| data.last | true | string | 最后一页 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 9 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 10 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 9 | number | 总元素个数 |
| requestId | 45c1f5d497004713942f2ac3c8ef7f02 | string | 请求唯一id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 工程复制

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-02-21 14:21:24

> 更新时间: 2024-12-26 15:13:31

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/copy

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| srcProjectId | 3 | Text | 是 | 被复制的工程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"projectId": 42,
		"projectName": "测试工程_副本",
		"projectType": 1,
		"projectTag": "测试,设备接入",
		"createTime": "2023-02-22 11:31:15",
		"updateTime": "2023-02-22 11:31:15",
		"creatorId": 0,
		"userId": 0,
		"initialize": null,
		"srcProjectId": 3,
		"maxSceneNum": 10,
		"maxDevNum": 10,
		"trainModule": "scene,device",
		"referDocum": "http://xxx.com/xxx,http://aa.com/a",
		"scores": "{\"sceneScore\":100,\n\"modelScore\"100,\n\"deviceScore\":100,\n\"linkCloudScore\":100,\n\"sideWorkScore\":100,\n\"orderScore\":100,\n\"documScore\":100,\n\"twinsScore\":100,\n\"policyScore\":100,\n\"appScore\":100\n}",
		"scenes": "[{\n\t\"sceneTemp\":\"场景1xxx\",\t\n\t\"sceneId\":1,\t\n\t\"devicePlan\":[\n\t\t{\n\t\t\t\"deviceModel\":\"机械臂\",\n\t\t\t\"id\":\"\",\t\n\t\t\t\"deviceType\":\"0\",\t\n\t\t\t\"accessType\",\"WIFI\",\t\n\t\t\t\"linkObj\":\"real\",\n\t\t\t\"maxFeatNum\":10,\n\t\t\t\"maxServNum\":8\n\t\t}\n\t]\n}]"
	},
	"requestId": "f7bcde9ecd894af7a95ed89cc6ab4b09",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.projectId | 42 | number | 工程id |
| data.projectName | 测试工程_副本 | string | 工程名 |
| data.projectType | 1 | number | 工程类型:1=实训,2=金晒 |
| data.projectTag | 测试,设备接入 | string | 标签, 用","分割 |
| data.createTime | 2023-02-22 11:31:15 | string | 创建时间 |
| data.updateTime | 2023-02-22 11:31:15 | string | 更新时间 |
| data.creatorId | 0 | number | 创建用户id |
| data.userId | 0 | number | 用户id |
| data.initialize | - | object | 是否已经初始化 |
| data.srcProjectId | 3 | number | 被复制的工程id |
| data.maxSceneNum | 10 | number | 场景最大数量 |
| data.maxDevNum | 10 | number | 终端最大数量 |
| data.trainModule | scene,device | string | 实训模块: scene=场景规划,device=设备接入,ops=设备运维,digital=数字孪生 |
| data.referDocum | http://xxx.com/xxx,http://aa.com/a | string | 参考文档 |
| data.scores | {"sceneScore":100,"modelScore"100,"deviceScore":100,"linkCloudScore":100,"sideWorkScore":100,"orderScore":100,"documScore":100,"twinsScore":100,"policyScore":100,"appScore":100} | string | 实训分数, json格式, 字段说明如下 ↓
实训分数-数字场景新建	sceneScore
实训分数-设备模型创建	modelScore
实训分数-设备实例创建	deviceScore
实训分数-智能设备上云	linkCloudScore
实训分数-端侧工况上报	sideWorkScore
实训分数-云端指令下发	orderScore
实训分数-云端文件下发	documScore
实训分数-孪生场景搭建	twinsScore
实训分数-场景策略下发	policyScore
实训分数-数字孪生应用	appScore |
| data.scenes | [{	"sceneTemp":"场景1xxx",		"sceneId":1,		"devicePlan":[		{			"deviceModel":"机械臂",			"id":"",				"deviceType":"0",				"accessType","WIFI",				"linkObj":"real",			"maxFeatNum":10,			"maxServNum":8		}	]}] | string | 场景信息, json格式, 字段和说明如下 ↓
[{
	"sceneType":"home",	//场景类型:custom=自定义,home=智能家居,factory=智能制造,traffic=智慧交通,hospital=远程医疗
	"sceneTemp":"场景xxx",	//场景模板名
	"sceneId":1,	//场景id
	"devicePlan":[
		{
			"deviceModel":"机械臂",	//设备型号
			"id":"",	//规划设备id
			"deviceType":"0",	//设备类型:0=直连设备,1=网关设备,2=非直连子设备
			"accessType","WIFI",	//联网方式: 根据类型变化，当类型为非直连子设备时，取值: Modbus, OPC UA, ZigBee, BLE, 自定义(Custom)；当类型不为非直连子设备时，取值Wi-Fi(WIFI),蓝牙(BLUE),蜂窝,以太网,LoRaWAN WIFI=wifi,CELLULAR=蜂窝,ETHERNET=以太网
			"linkObj":"real"	//映射对象:virtual=虚拟设备,real=硬件设备,virtualReal=虚实联动设备
			"maxFeatNum":10,	//最大属性数
			"maxServNum":8,		//最大服务数
		}
	]
}] |
| requestId | f7bcde9ecd894af7a95ed89cc6ab4b09 | string | 请求唯一id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
{
	"requestId": "ae6fbbf260194e6794398605cb9bfb9f",
	"status": "F",
	"sysMsg": "该工程已经复制过,工程名为:测试工程"
}
```

**Query**

## 工程初始化

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-06 14:56:33

> 更新时间: 2023-02-22 11:25:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/initial

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 3 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": null,
	"requestId": "27d52fe44d814096842400b22a2f0dbb",
	"status": "S",
	"sysMsg": "操作成功"
}
```

* 失败(201)

```javascript
{
	"requestId": "945ae9efed49453fb8e6719dbb9e0653",
	"status": "F",
	"sysMsg": "已初始化"
}
```

**Query**

## 获取关联工程

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-12-26 13:57:16

> 更新时间: 2024-12-26 15:13:35

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProject/getAssocProject?projectId=113

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 113 | string | 是 | 原始工程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 任务创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-23 15:52:15

> 更新时间: 2022-09-08 15:52:27

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTask/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| taskName | 测试任务6 | Text | 是 | 任务名称 |
| taskLevel | 1 | Text | 是 | 任务层级:1=初级,2=中级,3=高级,4=专业级 |
| projectRelation | 1 | Text | 是 | 关联工程方式:1=新建工程,2=关联已有工程 |
| projectId | - | Text | 是 | 工程id |
| startTime | 1661241247000 | Text | 是 | 开始时间 |
| endTime | 1661241247000 | Text | 是 | 结束时间 |
| description | 任务描述内容 | Text | 否 | 描述 |
| sceneType | 1 | Text | 否 | 场景类型:0=自定义,1=智能家居,2=工业互联网,3=智慧交通,4=远程医疗,  关联工程方式为新建工程时必填 |
| projectName | 测试工程2 | Text | 否 | 工程名称, 关联工程方式为新建工程时必填 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"taskId": 11,
		"taskName": "测试任务6",
		"taskLevel": 1,
		"projectRelation": 1,
		"projectId": 21,
		"startTime": "2022-08-23 07:54:07",
		"endTime": "2022-08-23 07:54:07",
		"createTime": null,
		"updateTime": null,
		"description": "任务描述内容",
		"creatorId": 0,
		"groupId": 1,
		"distribute": null,
		"newProjectId": null
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.taskId | 11 | number | 工程名称 |
| data.taskName | 测试任务6 | string | 任务名称 |
| data.taskLevel | 1 | number | - |
| data.projectRelation | 1 | number | - |
| data.projectId | 21 | number | - |
| data.startTime | 2022-08-23 07:54:07 | string | 开始时间 |
| data.endTime | 2022-08-23 07:54:07 | string | 结束时间 |
| data.createTime | - | object | 创建时间 |
| data.updateTime | - | object | 更新时间 |
| data.description | 任务描述内容 | string | 描述 |
| data.creatorId | 0 | number | - |
| data.groupId | 1 | number | - |
| data.distribute | - | object | - |
| data.newProjectId | - | object | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 任务删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-23 17:11:46

> 更新时间: 2022-08-23 17:12:11

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTask/delete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| taskId | 1 | Text | 是 | 任务名称 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 任务领取

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-05 15:10:51

> 更新时间: 2022-09-08 15:53:51

**返新建工程**

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTask/pull

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| taskId | 11 | Text | 是 | 工程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 任务列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-06 15:03:48

> 更新时间: 2022-09-07 16:53:07

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTask/list?type=pulled

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| type | pulled | string | 是 | 任务类型: needPull=待处理, pulled=已领取, myCreate=我创建的 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 任务复制

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-07 16:54:53

> 更新时间: 2022-09-07 16:54:53

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTask/copy

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| taskId | 1 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 任务修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-07 17:16:49

> 更新时间: 2022-09-08 16:11:31

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTask/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| taskName | 测试任务7 | Text | 是 | 任务名称 |
| taskLevel | 1 | Text | 是 | 任务层级:1=初级,2=中级,3=高级,4=专业级 |
| projectRelation | 1 | Text | 是 | 关联工程方式:1=新建工程,2=关联已有工程 |
| projectId | 4 | Text | 是 | 工程id |
| startTime | 1661241247000 | Text | 是 | 开始时间 |
| endTime | 1661241247000 | Text | 是 | 结束时间 |
| description | 任务描述内容 | Text | 否 | 描述 |
| sceneType | 1 | Text | 否 | 场景类型:0=自定义,1=智能家居,2=工业互联网,3=智慧交通,4=远程医疗,  关联工程方式为新建工程时必填 |
| projectName | 测试工程3 | Text | 否 | 工程名称, 关联工程方式为新建工程时必填 |
| taskId | 10 | Text | 是 | 工程名称 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 任务下发

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-15 13:59:16

> 更新时间: 2022-09-15 14:00:13

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTask/distribute

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| taskId | 6 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

# 场景

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-08 16:27:47

> 更新时间: 2022-09-08 16:27:46

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 场景新建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-13 11:27:49

> 更新时间: 2023-09-21 14:31:14

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneName | 场景名称4 | Text | 是 | 场景名称 |
| sceneType | home | Text | 是 | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| sceneBelong | 1 | Text | 是 | 场景归属:1=平台通用,2=工程私有,3=租户通用 |
| sceneModelBelong | 1 | Text | 是 | 场景模板:1=平台通用,2=场景私有,3=系统存档 |
| sceneData | {...} | Text | 否 | 场景数据, 元素,坐标参数等 |
| projectId | 112 | Text | 是 | 工程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"sceneId": 3,
		"sceneName": "场景名称2",
		"sceneType": 0,
		"sceneBelong": 1,
		"sceneModelBelong": null,
		"sceneData": "sdfs",
		"createTime": "2022-09-13 06:34:57",
		"updateTime": "2022-09-13 06:34:57",
		"userId": 0
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.sceneId | 3 | number | 场景id |
| data.sceneName | 场景名称2 | string | 场景名称 |
| data.sceneType | 0 | number | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| data.sceneBelong | 1 | number | 场景归属:1=平台通用,2=工程私有,3=租户通用 |
| data.sceneModelBelong | - | object | 场景模板:1=平台通用,2=场景私有,3=系统存档 |
| data.sceneData | sdfs | string | 场景数据 |
| data.createTime | 2022-09-13 06:34:57 | string | 创建时间 |
| data.updateTime | 2022-09-13 06:34:57 | string | 更新时间 |
| data.userId | 0 | number | 用户id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 场景更新

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-13 14:23:31

> 更新时间: 2022-10-10 11:04:19

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneName | 场景名称 | Text | 是 | 场景名称 |
| sceneType | 2 | Text | 是 | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| sceneBelong | 1 | Text | 是 | 场景归属:1=平台通用,2=工程私有,3=租户通用 |
| sceneModelBelong | 1 | Text | 是 | 场景模板:1=平台通用,2=场景私有,3=系统存档 |
| sceneData | sdfsqwqewq | Text | 否 | 场景数据 |
| sceneId | 8 | Text | 是 | 场景id |
| sceneDevices | [{"deviceIotId":"XUbvGwMcOCvmEz6Rbi71h7s700","productKey":"h7s72qjeGaM","deviceName":"test2_1"},{"deviceIotId":"QxDn30BdD816c9ZwFQokh7s700","productKey":"h7s7NxjuhLw","deviceName":"test_3"}] | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"sceneId": 1,
		"sceneName": "场景名称",
		"sceneType": 2,
		"sceneBelong": 1,
		"sceneModelBelong": null,
		"sceneData": "sdfsqwqewq",
		"createTime": "2022-09-13 06:33:38",
		"updateTime": "2022-09-13 06:36:07",
		"userId": 0
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.sceneId | 1 | number | - |
| data.sceneName | 场景名称 | string | - |
| data.sceneType | 2 | number | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| data.sceneBelong | 1 | number | - |
| data.sceneModelBelong | - | object | - |
| data.sceneData | sdfsqwqewq | string | - |
| data.createTime | 2022-09-13 06:33:38 | string | 创建时间 |
| data.updateTime | 2022-09-13 06:36:07 | string | 更新时间 |
| data.userId | 0 | number | 用户id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 场景删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-13 14:25:47

> 更新时间: 2023-09-21 15:10:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/delete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneId | 39 | Text | 是 | 场景id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 场景列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-13 14:27:21

> 更新时间: 2023-09-22 10:12:12

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/list?page=0&size=10

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | 0 | string | 否 | 场景id |
| size | 10 | string | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"last": true,
		"totalPages": 1,
		"totalElements": 8,
		"number": 0,
		"size": 10,
		"content": [
			{
				"userId": 0,
				"sceneName": "场景名称2_副本_副本",
				"sceneDevices": null,
				"sceneId": 6,
				"createTime": "2022-09-13 14:55:22",
				"updateTime": "2022-09-13 14:55:22",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 0,
				"deviceCount": 0
			},
			{
				"userId": 0,
				"sceneName": "场景名称2",
				"sceneDevices": null,
				"sceneId": 3,
				"createTime": "2022-09-13 14:34:57",
				"updateTime": "2022-09-13 14:34:57",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 0,
				"deviceCount": 0
			},
			{
				"userId": 0,
				"sceneName": "场景名称2_副本",
				"sceneDevices": null,
				"sceneId": 5,
				"createTime": "2022-09-13 14:55:05",
				"updateTime": "2022-09-13 14:55:05",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 0,
				"deviceCount": 0
			},
			{
				"userId": 0,
				"sceneName": "场景名称2_副本",
				"sceneDevices": null,
				"sceneId": 7,
				"createTime": "2022-09-13 14:55:41",
				"updateTime": "2022-09-13 14:55:41",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 0,
				"deviceCount": 0
			},
			{
				"userId": 0,
				"sceneName": "场景名称",
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"sceneId": 8,
				"createTime": "2022-09-13 16:11:15",
				"updateTime": "2022-09-13 16:12:23",
				"sceneModelBelong": null,
				"sceneType": 2,
				"sceneBelong": 1,
				"sceneData": "sdfsqwqewq",
				"productCount": 2,
				"deviceCount": 2
			},
			{
				"userId": 0,
				"sceneName": "场景名称4",
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"sceneId": 9,
				"createTime": "2022-09-13 16:11:38",
				"updateTime": "2022-09-13 16:11:38",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 2,
				"deviceCount": 2
			},
			{
				"userId": 0,
				"sceneName": "场景名称_副本",
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"sceneId": 10,
				"createTime": "2022-09-13 16:29:06",
				"updateTime": "2022-09-13 16:29:06",
				"sceneModelBelong": null,
				"sceneType": 2,
				"sceneBelong": 1,
				"sceneData": "sdfsqwqewq",
				"productCount": 2,
				"deviceCount": 2
			},
			{
				"userId": 0,
				"sceneName": "场景名称_副本",
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"sceneId": 11,
				"createTime": "2022-09-13 16:29:53",
				"updateTime": "2022-09-13 16:29:53",
				"sceneModelBelong": null,
				"sceneType": 2,
				"sceneBelong": 1,
				"sceneData": "sdfsqwqewq",
				"productCount": 2,
				"deviceCount": 2
			}
		],
		"sort": null,
		"first": true,
		"numberOfElements": 8
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.last | true | string | 最后一页 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 8 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 10 | number | 每页元素个数 |
| data.content | - | object | 消息详情 |
| data.content.userId | 0 | number | 用户id |
| data.content.sceneName | 场景名称2_副本_副本 | string | - |
| data.content.sceneDevices | - | object | - |
| data.content.sceneId | 6 | number | - |
| data.content.createTime | 2022-09-13 14:55:22 | string | 创建时间 |
| data.content.updateTime | 2022-09-13 14:55:22 | string | 更新时间 |
| data.content.sceneModelBelong | - | object | - |
| data.content.sceneType | 0 | number | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| data.content.sceneBelong | 1 | number | 场景模型 |
| data.content.sceneData | sdfs | string | 场景数据 |
| data.content.productCount | 0 | number | 产品数 |
| data.content.deviceCount | 0 | number | 设备数 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 8 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 场景详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-13 17:33:40

> 更新时间: 2023-07-19 09:30:21

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/get?sceneId=18

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneId | 18 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"last": true,
		"totalPages": 1,
		"totalElements": 8,
		"number": 0,
		"size": 10,
		"content": [
			{
				"userId": 0,
				"sceneName": "场景名称2_副本_副本",
				"sceneDevices": null,
				"sceneId": 6,
				"createTime": "2022-09-13 14:55:22",
				"updateTime": "2022-09-13 14:55:22",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 0,
				"deviceCount": 0
			},
			{
				"userId": 0,
				"sceneName": "场景名称2",
				"sceneDevices": null,
				"sceneId": 3,
				"createTime": "2022-09-13 14:34:57",
				"updateTime": "2022-09-13 14:34:57",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 0,
				"deviceCount": 0
			},
			{
				"userId": 0,
				"sceneName": "场景名称2_副本",
				"sceneDevices": null,
				"sceneId": 5,
				"createTime": "2022-09-13 14:55:05",
				"updateTime": "2022-09-13 14:55:05",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 0,
				"deviceCount": 0
			},
			{
				"userId": 0,
				"sceneName": "场景名称2_副本",
				"sceneDevices": null,
				"sceneId": 7,
				"createTime": "2022-09-13 14:55:41",
				"updateTime": "2022-09-13 14:55:41",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 0,
				"deviceCount": 0
			},
			{
				"userId": 0,
				"sceneName": "场景名称",
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"sceneId": 8,
				"createTime": "2022-09-13 16:11:15",
				"updateTime": "2022-09-13 16:12:23",
				"sceneModelBelong": null,
				"sceneType": 2,
				"sceneBelong": 1,
				"sceneData": "sdfsqwqewq",
				"productCount": 2,
				"deviceCount": 2
			},
			{
				"userId": 0,
				"sceneName": "场景名称4",
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"sceneId": 9,
				"createTime": "2022-09-13 16:11:38",
				"updateTime": "2022-09-13 16:11:38",
				"sceneModelBelong": null,
				"sceneType": 0,
				"sceneBelong": 1,
				"sceneData": "sdfs",
				"productCount": 2,
				"deviceCount": 2
			},
			{
				"userId": 0,
				"sceneName": "场景名称_副本",
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"sceneId": 10,
				"createTime": "2022-09-13 16:29:06",
				"updateTime": "2022-09-13 16:29:06",
				"sceneModelBelong": null,
				"sceneType": 2,
				"sceneBelong": 1,
				"sceneData": "sdfsqwqewq",
				"productCount": 2,
				"deviceCount": 2
			},
			{
				"userId": 0,
				"sceneName": "场景名称_副本",
				"sceneDevices": "[{\"deviceIotId\":\"XUbvGwMcOCvmEz6Rbi71h7s700\",\n\"productKey\":\"h7s72qjeGaM\",\n\"deviceName\":\"test2_1\"\n},\n{\"deviceIotId\":\"QxDn30BdD816c9ZwFQokh7s700\",\n\"productKey\":\"h7s7NxjuhLw\",\n\"deviceName\":\"test_3\"\n}]",
				"sceneId": 11,
				"createTime": "2022-09-13 16:29:53",
				"updateTime": "2022-09-13 16:29:53",
				"sceneModelBelong": null,
				"sceneType": 2,
				"sceneBelong": 1,
				"sceneData": "sdfsqwqewq",
				"productCount": 2,
				"deviceCount": 2
			}
		],
		"sort": null,
		"first": true,
		"numberOfElements": 8
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.last | true | string | 最后一页 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 8 | number | 总元素个数 |
| data.number | 0 | number | 页码 |
| data.size | 10 | number | 每页元素个数 |
| data.content | - | object | 消息详情 |
| data.content.userId | 0 | number | 用户id |
| data.content.sceneName | 场景名称2_副本_副本 | string | - |
| data.content.sceneDevices | - | object | - |
| data.content.sceneId | 6 | number | - |
| data.content.createTime | 2022-09-13 14:55:22 | string | 创建时间 |
| data.content.updateTime | 2022-09-13 14:55:22 | string | 更新时间 |
| data.content.sceneModelBelong | - | object | - |
| data.content.sceneType | 0 | number | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| data.content.sceneBelong | 1 | number | 场景模型 |
| data.content.sceneData | sdfs | string | 场景数据 |
| data.content.productCount | 0 | number | 产品数 |
| data.content.deviceCount | 0 | number | 设备数 |
| data.sort | - | object | 排序 |
| data.first | true | string | 是否是第一页 |
| data.numberOfElements | 8 | number | 总元素个数 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 场景复制

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-13 14:50:23

> 更新时间: 2023-09-22 09:08:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/copy

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneId | 40 | Text | 是 | 场景id |
| projectId | 112 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"sceneId": 6,
		"sceneName": "场景名称2_副本_副本",
		"sceneType": 0,
		"sceneBelong": 1,
		"sceneModelBelong": null,
		"sceneData": "sdfs",
		"createTime": "2022-09-13 06:55:22",
		"updateTime": "2022-09-13 06:55:22",
		"userId": 0
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 场景组件

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-14 17:06:43

> 更新时间: 2022-10-10 11:04:30

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/widgetList?sceneType=home

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneType | home | Text | 否 | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| isBackground | 1 | Text | 否 | 是否是背景: 1=是, 0=否 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"widgetId": 1,
				"widgetName": "三室一厅",
				"widgetPic": "https://pic1.zhimg.com/v2-06071ea7ddba087551589139324a0c4c_720w.webp?source=d6434cab",
				"sceneType": "home",
				"isBackground": 1
			},
			{
				"widgetId": 2,
				"widgetName": "二室一厅",
				"widgetPic": "https://pic1.zhimg.com/v2-06071ea7ddba087551589139324a0c4c_720w.webp?source=d6434cab",
				"sceneType": "home",
				"isBackground": 1
			},
			{
				"widgetId": 3,
				"widgetName": "智能开关",
				"widgetPic": "https://pic1.zhimg.com/v2-06071ea7ddba087551589139324a0c4c_720w.webp?source=d6434cab",
				"sceneType": "home",
				"isBackground": null
			},
			{
				"widgetId": 4,
				"widgetName": "智能插座",
				"widgetPic": "https://pic1.zhimg.com/v2-06071ea7ddba087551589139324a0c4c_720w.webp?source=d6434cab",
				"sceneType": "home",
				"isBackground": null
			}
		],
		"totalPages": 1,
		"totalElements": 4,
		"last": true,
		"number": 0,
		"size": 20,
		"sort": null,
		"numberOfElements": 4,
		"first": true
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.content | - | object | 消息详情 |
| data.content.widgetId | 1 | number | - |
| data.content.widgetName | 三室一厅 | string | - |
| data.content.widgetPic | https://pic1.zhimg.com/v2-06071ea7ddba087551589139324a0c4c_720w.webp?source=d6434cab | string | - |
| data.content.sceneType | home | string | 场景类型:home=智能家居,factory=工业互联网,traffic=智慧交通,hospital=远程医疗,custom=自定义 |
| data.content.isBackground | 1 | number | 是否是背景: 1=是, 0=否 |
| data.totalPages | 1 | number | 总页数 |
| data.totalElements | 4 | number | 总元素个数 |
| data.last | true | string | 最后一页 |
| data.number | 0 | number | 页码 |
| data.size | 20 | number | 每页元素个数 |
| data.sort | - | object | 排序 |
| data.numberOfElements | 4 | number | 总元素个数 |
| data.first | true | string | 是否是第一页 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 批量获取设备运行数据

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-10-14 17:06:11

> 更新时间: 2022-10-14 17:23:48

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/batchGetDeviceInfo

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
	"deviceIds": [
		"{{iotId}}",
		"1232"
	]
}
```

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 场景设备_创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-09-20 16:48:18

> 更新时间: 2023-10-18 15:52:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/createDevice

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| nickname | 测试设备96 | string | 是 | 设备名称 |
| productKey | iy4u34KeDme | string | 是 | 设备模型key |
| sceneId | 40 | integer | 是 | 场景id |
| instanceName | 测试设备 | string | 是 | 实例名称 |
| newInstance | 1 | integer | 是 | 是否新建实例:1=是,0=否 |
| netType | WIFI | string | 是 | 联网方式:WIFI=wifi,CELLULAR=2/3/4/5G/NB-IoT,ETHERNET=以太网 |
| nodeType | 0 | integer | 是 | 设备类型:0=直连设备,1=网关设备,2=非直连子设备 |
| productName | 产品名 | string | 是 | 产品名称 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 场景设备_列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-09-21 14:57:42

> 更新时间: 2023-09-22 10:07:43

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/getDevices?sceneId=40

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneId | 40 | string | 是 | 场景id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 场景设备_删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-09-21 15:06:17

> 更新时间: 2023-09-21 15:07:39

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/deleteDevice

**请求方式**

> POST

**Content-Type**

> urlencoded

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneDeviceId | 2 | integer | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 场景设备_更新

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-09-21 17:38:36

> 更新时间: 2023-09-21 17:55:48

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/updateDevice

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sceneDeviceId | 6 | string | 是 | - |
| nickname | 测试设备96 | string | 是 | 设备名称 |
| instanceName | 测试设备 | string | 是 | 实例名称 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 场景模型_列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-09-22 09:47:39

> 更新时间: 2023-10-18 15:45:23

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/getModels?page=&size=&sort=&modelName=&sceneType=&modelType=&customType=custom

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | - | Text | 否 | 页码 |
| size | - | Text | 否 | 每页大小 |
| sort | - | Text | 否 | 排序 |
| modelName | - | Text | 否 | 模型名称 |
| sceneType | - | Text | 否 | 场景类型:factory=智慧工业,traffic=智慧交通,port=智慧港口,home=智能家居,office=智慧办公 |
| modelType | - | Text | 是 | 模型类别:environment=环境,terminal=终端 |
| customType | custom | Text | 否 | 自定义类型: system=系统模型, custom=自定义模型 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 场景模型_上传

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-09-22 09:47:36

> 更新时间: 2023-10-18 15:55:23

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/createModel

**请求方式**

> POST

**Content-Type**

> urlencoded

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| modelName | qweq | string | 是 | 模型名称 |
| modelPic | /aaa.jpg | string | 是 | 模型图片 |
| sceneType | factory | string | 是 | 场景类型:factory=智慧工业,traffic=智慧交通,port=智慧港口,home=智能家居,office=智慧办公 |
| modelPath | /model/1697015591287908/model/test.FBX | string | 是 | 模型路径 |
| modelType | terminal | string | 是 | 模型类别:environment=环境,terminal=终端 |
| modelDesc | 模型描述内容xxx | string | 是 | 模型描述 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 场景模型_删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-09-22 09:47:42

> 更新时间: 2023-10-18 15:53:29

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotScene/deleteModel

**请求方式**

> POST

**Content-Type**

> urlencoded

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| modelId | 14 | integer | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{"KEY":{}}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| KEY | - | object | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 场景模型_上传文件

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-10-11 16:33:53

> 更新时间: 2024-02-23 17:06:26

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/common/uploadModel

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| file | - | string | 是 | 模型文件,zip格式 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"modelName": "/model/1697015591287908/model/test.FBX"
	},
	"errCode": null,
	"requestId": "31b2b5b15ada4b6197b80da7ef0083ea",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.modelName | /model/1697015591287908/model/test.FBX | string | - |
| errCode | null | null | - |
| requestId | 31b2b5b15ada4b6197b80da7ef0083ea | string | 请求唯一id |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

# 用户

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-24 14:37:33

> 更新时间: 2022-08-03 16:15:02

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 用户登陆

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-24 14:42:30

> 更新时间: 2024-07-22 15:21:40

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/userLogin

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| userName | fw | Text | 是 | - |
| password | 7da418ac9a44987244b313ce7b61dacd | Text | 是 | 密码签名 = md5(用户名+md5(密码)) |
| verifyCode | 4bsx | Text | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"role": 2,
	"unReadMsgCount": 0,
	"totalMsgCount": 0,
	"nickName": "fff",
	"userName": "abcj",
	"userId": 3,
	"iotToken": "0cdf39a6-4fa0-4895-9b1f-367256b62301",
	"token": "0cdf39a6-4fa0-4895-9b1f-367256b62301",
	"status": "S"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| role | 2 | number | - |
| unReadMsgCount | 0 | number | - |
| totalMsgCount | 0 | number | - |
| nickName | fff | string | 用户昵称 |
| userName | abcj | string | 用户名 |
| userId | 3 | number | 用户id |
| iotToken | 0cdf39a6-4fa0-4895-9b1f-367256b62301 | string | 用户iot平台token |
| token | 0cdf39a6-4fa0-4895-9b1f-367256b62301 | string | 认证令牌 |
| status | S | string | 状态 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户登出

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-10 13:58:36

> 更新时间: 2023-05-24 14:24:48

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/userLogout

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-04 10:43:36

> 更新时间: 2024-06-20 15:49:54

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/createUser

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| userName | cc96 | string | 是 | 用户名 |
| nickName | qqq | string | 是 | 昵称 |
| stuNo | 123 | string | 是 | 学号 |
| className | 1班 | string | 是 | 班级名称 |
| emailAddr | yx96@163.com | string | 是 | 邮箱名称 |
| telNum | 12312345696 | string | 是 | 电话 |
| password | e52cc10d | string | 是 | 密码 |
| role | 4 | string | 是 | 1:学生   2：老师, 4: 主任老师 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 17:04:59

> 更新时间: 2023-05-22 17:19:14

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/updateUser

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| userName | qq96 | string | 是 | 用户名 |
| nickName | qqq | string | 是 | 昵称 |
| stuNo | 123 | string | 是 | 学号 |
| classId | 4 | string | 是 | 班级名称 |
| emailAddr | fww296@163.com | string | 是 | 邮箱名称 |
| telNum | 17312345696 | string | 是 | 电话 |
| password | 123457675 | string | 是 | 密码 |
| userId | 25 | string | 是 | 用户id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-06 11:36:49

> 更新时间: 2023-05-06 11:52:38

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/deleteMany

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| userIds | 11,12 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-06 17:26:52

> 更新时间: 2023-05-06 17:34:29

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/userDetail?userId=1

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| userId | 1 | string | 是 | 用户id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"userInfo": {
			"userId": 1,
			"groupId": 1,
			"nickName": "liuzhong",
			"realName": "liuzhong",
			"password": null,
			"emailAddr": "liuzhong@qq.com",
			"mobileNum": null,
			"telNum": "18316621695",
			"majorName": null,
			"userName": "lz",
			"personIcon": null,
			"createTime": null,
			"schoolName": null,
			"creatorId": null,
			"role": 3,
			"stuNo": null,
			"isDelete": 0,
			"className": null,
			"sex": null,
			"lastUpdateTime": null,
			"departmentName": null,
			"contactAddr": null,
			"learningTime": 0,
			"creatorUsername": null,
			"portalToken": null,
			"classYearName": null,
			"deleteDate": null,
			"classId": 4,
			"updateAdminId": null
		},
		"runtimeInfo": {
			"userStatus": "online",
			"courseCount": 0,
			"courseUnStartCount": 0,
			"thisWeekOnlineTime": 0,
			"courseProcessCount": 0,
			"thisWeekOnlineTimeUpRate": 0,
			"projectUnStartCount": 0,
			"projectProcessCount": 0,
			"courseCompleteCount": 0
		}
	},
	"errCode": null,
	"requestId": "48fa044d1ac9435bac40dde7debafbec",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.userInfo | - | object | - |
| data.userInfo.userId | 1 | integer | 用户id |
| data.userInfo.groupId | 1 | integer | - |
| data.userInfo.nickName | liuzhong | string | 昵称 |
| data.userInfo.realName | liuzhong | string | - |
| data.userInfo.password | null | null | 密码 |
| data.userInfo.emailAddr | liuzhong@qq.com | string | 邮箱 |
| data.userInfo.mobileNum | null | null | - |
| data.userInfo.telNum | 18316621695 | string | 电话 |
| data.userInfo.majorName | null | null | - |
| data.userInfo.userName | lz | string | 用户名 |
| data.userInfo.personIcon | null | null | - |
| data.userInfo.createTime | null | null | 创建时间 |
| data.userInfo.schoolName | null | null | - |
| data.userInfo.creatorId | null | null | - |
| data.userInfo.role | 3 | integer | - |
| data.userInfo.stuNo | null | null | 学号 |
| data.userInfo.isDelete | 0 | integer | - |
| data.userInfo.className | null | null | 班级名 |
| data.userInfo.sex | null | null | - |
| data.userInfo.lastUpdateTime | null | null | - |
| data.userInfo.departmentName | null | null | - |
| data.userInfo.contactAddr | null | null | - |
| data.userInfo.learningTime | 0 | integer | - |
| data.userInfo.creatorUsername | null | null | - |
| data.userInfo.portalToken | null | null | - |
| data.userInfo.classYearName | null | null | - |
| data.userInfo.deleteDate | null | null | - |
| data.userInfo.classId | 4 | integer | - |
| data.userInfo.updateAdminId | null | null | - |
| data.runtimeInfo | - | object | - |
| data.runtimeInfo.userStatus | online | string | 用户状态: online=状态, offline=离线 |
| data.runtimeInfo.courseCount | 0 | integer | 课程总数 |
| data.runtimeInfo.courseUnStartCount | 0 | integer | 未开始课程数 |
| data.runtimeInfo.thisWeekOnlineTime | 0 | integer | 本周在线时长 |
| data.runtimeInfo.courseProcessCount | 0 | integer | 进行中课程 |
| data.runtimeInfo.thisWeekOnlineTimeUpRate | 0 | integer | 在线时长同比上周 |
| data.runtimeInfo.projectUnStartCount | 0 | integer | 未开始工程数 |
| data.runtimeInfo.projectProcessCount | 0 | integer | 进行中工程数 |
| data.runtimeInfo.courseCompleteCount | 0 | integer | 已完成课程数 |
| errCode | null | null | - |
| requestId | 48fa044d1ac9435bac40dde7debafbec | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户列表查询

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 14:47:35

> 更新时间: 2023-05-24 08:44:27

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/listSearch?allSearch=62&className=&classYearName=&majorName=&departmentName=&schoolName=&size=10&page=0

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| allSearch | 62 | string | 否 | 所有参数查询 |
| className | - | string | 否 | - |
| classYearName | - | string | 否 | - |
| majorName | - | string | 否 | - |
| departmentName | - | string | 否 | - |
| schoolName | - | string | 否 | - |
| size | 10 | string | 否 | 每页元素个数 |
| page | 0 | string | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"userId": 3,
				"groupId": 1,
				"nickName": "qqq",
				"realName": null,
				"password": null,
				"emailAddr": "fw@163.com",
				"mobileNum": null,
				"telNum": "17312345678",
				"majorName": null,
				"userName": "q",
				"personIcon": null,
				"createTime": "2023-05-04 11:14:00",
				"schoolName": null,
				"creatorId": 0,
				"role": null,
				"stuNo": "123",
				"isDelete": null,
				"className": "班级1",
				"sex": null,
				"lastUpdateTime": "2023-05-04 11:14:00",
				"departmentName": null,
				"contactAddr": null,
				"learningTime": 0,
				"creatorUsername": "abcj",
				"portalToken": null,
				"classYearName": null,
				"deleteDate": null
			},
			{
				"userId": 5,
				"groupId": 1,
				"nickName": "qqq",
				"realName": null,
				"password": null,
				"emailAddr": "fw2@163.com",
				"mobileNum": null,
				"telNum": "17312345678",
				"majorName": "软件工程",
				"userName": "q2",
				"personIcon": null,
				"createTime": "2023-05-04 15:40:33",
				"schoolName": "信息技术学校",
				"creatorId": 0,
				"role": null,
				"stuNo": "123",
				"isDelete": null,
				"className": "1班",
				"sex": null,
				"lastUpdateTime": "2023-05-04 15:40:33",
				"departmentName": "软件学院",
				"contactAddr": null,
				"learningTime": 0,
				"creatorUsername": "abcj",
				"portalToken": null,
				"classYearName": "2016级",
				"deleteDate": null
			}
		],
		"last": true,
		"totalElements": 2,
		"totalPages": 1,
		"number": 0,
		"size": 10,
		"sort": null,
		"first": true,
		"numberOfElements": 2
	},
	"errCode": null,
	"requestId": "a49c7a9636a8452eb231e4da8591c673",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.content | - | array | 消息详情 |
| data.content.userId | 3 | integer | 用户id |
| data.content.groupId | 1 | integer | 分组id |
| data.content.nickName | qqq | string | 昵称 |
| data.content.realName | null | null | 真实姓名 |
| data.content.password | null | null | - |
| data.content.emailAddr | fw@163.com | string | 邮箱 |
| data.content.mobileNum | null | null | 手机号 |
| data.content.telNum | 17312345678 | string | 电话号码 |
| data.content.majorName | null | null | 专业名称 |
| data.content.userName | q | string | 用户名 |
| data.content.personIcon | null | null | 头像 |
| data.content.createTime | 2023-05-04 11:14:00 | string | 创建时间 |
| data.content.schoolName | null | null | 学校名称 |
| data.content.creatorId | 0 | integer | 创建者id |
| data.content.role | null | null | 权限类型 |
| data.content.stuNo | 123 | string | 学号 |
| data.content.isDelete | null | null | 是否删除 |
| data.content.className | 班级1 | string | 班级名称 |
| data.content.sex | null | null | 性别 |
| data.content.lastUpdateTime | 2023-05-04 11:14:00 | string | 更新时间 |
| data.content.departmentName | null | null | 学院名称 |
| data.content.contactAddr | null | null | 联系地址 |
| data.content.learningTime | 0 | integer | 学习时间 |
| data.content.creatorUsername | abcj | string | 创建者用户名 |
| data.content.portalToken | null | null | - |
| data.content.classYearName | null | null | 年级名称 |
| data.content.deleteDate | null | null | 删除时间 |
| data.last | true | boolean | 最后一页 |
| data.totalElements | 2 | integer | 总元素个数 |
| data.totalPages | 1 | integer | 总页数 |
| data.number | 0 | integer | 页码 |
| data.size | 10 | integer | 每页元素个数 |
| data.sort | null | null | 排序 |
| data.first | true | boolean | 是否是第一页 |
| data.numberOfElements | 2 | integer | 总元素个数 |
| errCode | null | null | - |
| requestId | a49c7a9636a8452eb231e4da8591c673 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户列表查询2

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-22 17:22:56

> 更新时间: 2023-05-23 09:44:52

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/listSearch2?classId=4&className=&majorName=&departmentName=&schoolName=&size=10&page=0

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| classId | 4 | string | 否 | - |
| className | - | string | 否 | - |
| majorName | - | string | 否 | - |
| departmentName | - | string | 否 | - |
| schoolName | - | string | 否 | - |
| size | 10 | string | 否 | 每页元素个数 |
| page | 0 | string | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"userId": 3,
				"groupId": 1,
				"nickName": "qqq",
				"realName": null,
				"password": null,
				"emailAddr": "fw@163.com",
				"mobileNum": null,
				"telNum": "17312345678",
				"majorName": null,
				"userName": "q",
				"personIcon": null,
				"createTime": "2023-05-04 11:14:00",
				"schoolName": null,
				"creatorId": 0,
				"role": null,
				"stuNo": "123",
				"isDelete": null,
				"className": "班级1",
				"sex": null,
				"lastUpdateTime": "2023-05-04 11:14:00",
				"departmentName": null,
				"contactAddr": null,
				"learningTime": 0,
				"creatorUsername": "abcj",
				"portalToken": null,
				"classYearName": null,
				"deleteDate": null
			},
			{
				"userId": 5,
				"groupId": 1,
				"nickName": "qqq",
				"realName": null,
				"password": null,
				"emailAddr": "fw2@163.com",
				"mobileNum": null,
				"telNum": "17312345678",
				"majorName": "软件工程",
				"userName": "q2",
				"personIcon": null,
				"createTime": "2023-05-04 15:40:33",
				"schoolName": "信息技术学校",
				"creatorId": 0,
				"role": null,
				"stuNo": "123",
				"isDelete": null,
				"className": "1班",
				"sex": null,
				"lastUpdateTime": "2023-05-04 15:40:33",
				"departmentName": "软件学院",
				"contactAddr": null,
				"learningTime": 0,
				"creatorUsername": "abcj",
				"portalToken": null,
				"classYearName": "2016级",
				"deleteDate": null
			}
		],
		"last": true,
		"totalElements": 2,
		"totalPages": 1,
		"number": 0,
		"size": 10,
		"sort": null,
		"first": true,
		"numberOfElements": 2
	},
	"errCode": null,
	"requestId": "a49c7a9636a8452eb231e4da8591c673",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.content | - | array | 消息详情 |
| data.content.userId | 3 | integer | 用户id |
| data.content.groupId | 1 | integer | 分组id |
| data.content.nickName | qqq | string | 昵称 |
| data.content.realName | null | null | 真实姓名 |
| data.content.password | null | null | - |
| data.content.emailAddr | fw@163.com | string | 邮箱 |
| data.content.mobileNum | null | null | 手机号 |
| data.content.telNum | 17312345678 | string | 电话号码 |
| data.content.majorName | null | null | 专业名称 |
| data.content.userName | q | string | 用户名 |
| data.content.personIcon | null | null | 头像 |
| data.content.createTime | 2023-05-04 11:14:00 | string | 创建时间 |
| data.content.schoolName | null | null | 学校名称 |
| data.content.creatorId | 0 | integer | 创建者id |
| data.content.role | null | null | 权限类型 |
| data.content.stuNo | 123 | string | 学号 |
| data.content.isDelete | null | null | 是否删除 |
| data.content.className | 班级1 | string | 班级名称 |
| data.content.sex | null | null | 性别 |
| data.content.lastUpdateTime | 2023-05-04 11:14:00 | string | 更新时间 |
| data.content.departmentName | null | null | 学院名称 |
| data.content.contactAddr | null | null | 联系地址 |
| data.content.learningTime | 0 | integer | 学习时间 |
| data.content.creatorUsername | abcj | string | 创建者用户名 |
| data.content.portalToken | null | null | - |
| data.content.classYearName | null | null | 年级名称 |
| data.content.deleteDate | null | null | 删除时间 |
| data.last | true | boolean | 最后一页 |
| data.totalElements | 2 | integer | 总元素个数 |
| data.totalPages | 1 | integer | 总页数 |
| data.number | 0 | integer | 页码 |
| data.size | 10 | integer | 每页元素个数 |
| data.sort | null | null | 排序 |
| data.first | true | boolean | 是否是第一页 |
| data.numberOfElements | 2 | integer | 总元素个数 |
| errCode | null | null | - |
| requestId | a49c7a9636a8452eb231e4da8591c673 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户列表导出

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-08 14:34:48

> 更新时间: 2023-05-24 15:39:26

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/exportUsers?className=&classYearName=&majorName=&departmentName=&schoolName=

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| className | - | string | 否 | - |
| classYearName | - | string | 否 | - |
| majorName | - | string | 否 | - |
| departmentName | - | string | 否 | - |
| schoolName | - | string | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"userId": 3,
				"groupId": 1,
				"nickName": "qqq",
				"realName": null,
				"password": null,
				"emailAddr": "fw@163.com",
				"mobileNum": null,
				"telNum": "17312345678",
				"majorName": null,
				"userName": "q",
				"personIcon": null,
				"createTime": "2023-05-04 11:14:00",
				"schoolName": null,
				"creatorId": 0,
				"role": null,
				"stuNo": "123",
				"isDelete": null,
				"className": "班级1",
				"sex": null,
				"lastUpdateTime": "2023-05-04 11:14:00",
				"departmentName": null,
				"contactAddr": null,
				"learningTime": 0,
				"creatorUsername": "abcj",
				"portalToken": null,
				"classYearName": null,
				"deleteDate": null
			},
			{
				"userId": 5,
				"groupId": 1,
				"nickName": "qqq",
				"realName": null,
				"password": null,
				"emailAddr": "fw2@163.com",
				"mobileNum": null,
				"telNum": "17312345678",
				"majorName": "软件工程",
				"userName": "q2",
				"personIcon": null,
				"createTime": "2023-05-04 15:40:33",
				"schoolName": "信息技术学校",
				"creatorId": 0,
				"role": null,
				"stuNo": "123",
				"isDelete": null,
				"className": "1班",
				"sex": null,
				"lastUpdateTime": "2023-05-04 15:40:33",
				"departmentName": "软件学院",
				"contactAddr": null,
				"learningTime": 0,
				"creatorUsername": "abcj",
				"portalToken": null,
				"classYearName": "2016级",
				"deleteDate": null
			}
		],
		"last": true,
		"totalElements": 2,
		"totalPages": 1,
		"number": 0,
		"size": 10,
		"sort": null,
		"first": true,
		"numberOfElements": 2
	},
	"errCode": null,
	"requestId": "a49c7a9636a8452eb231e4da8591c673",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.content | - | array | 消息详情 |
| data.content.userId | 3 | integer | 用户id |
| data.content.groupId | 1 | integer | 分组id |
| data.content.nickName | qqq | string | 昵称 |
| data.content.realName | null | null | 真实姓名 |
| data.content.password | null | null | - |
| data.content.emailAddr | fw@163.com | string | 邮箱 |
| data.content.mobileNum | null | null | 手机号 |
| data.content.telNum | 17312345678 | string | 电话号码 |
| data.content.majorName | null | null | 专业名称 |
| data.content.userName | q | string | 用户名 |
| data.content.personIcon | null | null | 头像 |
| data.content.createTime | 2023-05-04 11:14:00 | string | 创建时间 |
| data.content.schoolName | null | null | 学校名称 |
| data.content.creatorId | 0 | integer | 创建者id |
| data.content.role | null | null | 权限类型 |
| data.content.stuNo | 123 | string | 学号 |
| data.content.isDelete | null | null | 是否删除 |
| data.content.className | 班级1 | string | 班级名称 |
| data.content.sex | null | null | 性别 |
| data.content.lastUpdateTime | 2023-05-04 11:14:00 | string | 更新时间 |
| data.content.departmentName | null | null | 学院名称 |
| data.content.contactAddr | null | null | 联系地址 |
| data.content.learningTime | 0 | integer | 学习时间 |
| data.content.creatorUsername | abcj | string | 创建者用户名 |
| data.content.portalToken | null | null | - |
| data.content.classYearName | null | null | 年级名称 |
| data.content.deleteDate | null | null | 删除时间 |
| data.last | true | boolean | 最后一页 |
| data.totalElements | 2 | integer | 总元素个数 |
| data.totalPages | 1 | integer | 总页数 |
| data.number | 0 | integer | 页码 |
| data.size | 10 | integer | 每页元素个数 |
| data.sort | null | null | 排序 |
| data.first | true | boolean | 是否是第一页 |
| data.numberOfElements | 2 | integer | 总元素个数 |
| errCode | null | null | - |
| requestId | a49c7a9636a8452eb231e4da8591c673 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户列表导入

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-08 17:29:28

> 更新时间: 2023-05-23 09:47:57

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/importUsers

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| file | - | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": [
		{
			"userName": "e1",
			"error": "用户名已被使用！"
		},
		{
			"userName": "e2",
			"error": "手机号已被使用！"
		}
	],
	"status": "F",
	"sysMsg": "导入失败2条数据"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | array | - |
| data.userName | e1 | string | 导入失败的用户名 |
| data.error | 用户名已被使用！ | string | 导入失败信息 |
| status | F | string | 状态 |
| sysMsg | 导入失败2条数据 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 用户登陆检测(在header传token)

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-24 14:45:37

> 更新时间: 2022-11-25 17:02:11

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/checkUserLogin

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"role": 2,
	"unReadMsgCount": 0,
	"totalMsgCount": 0,
	"nickName": "fff",
	"userName": "abcj",
	"userId": 3,
	"iotToken": "0cdf39a6-4fa0-4895-9b1f-367256b62301",
	"token": "0cdf39a6-4fa0-4895-9b1f-367256b62301",
	"status": "S"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| role | 2 | number | - |
| unReadMsgCount | 0 | number | - |
| totalMsgCount | 0 | number | - |
| nickName | fff | string | 用户昵称 |
| userName | abcj | string | 用户名 |
| userId | 3 | number | 用户id |
| iotToken | 0cdf39a6-4fa0-4895-9b1f-367256b62301 | string | 用户iot平台token |
| token | 0cdf39a6-4fa0-4895-9b1f-367256b62301 | string | 认证令牌 |
| status | S | string | 状态 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 获取验证码

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-12-13 11:20:26

> 更新时间: 2022-12-13 14:05:30

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/getCheckCode

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

## 班级创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-04 14:55:51

> 更新时间: 2023-05-04 15:17:19

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/createClass

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| className | 1班 | string | 是 | 班级名称 |
| classYearName | 2016级 | string | 是 | 年级名称 |
| majorName | 软件工程 | string | 是 | 专业名称 |
| departmentName | 软件学院 | string | 是 | 学院名称 |
| schoolName | 信息技术学校 | string | 是 | 学校名称 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 班级修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 10:59:20

> 更新时间: 2023-05-05 11:40:55

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/updateClass

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| className | 3.1班 | string | 是 | 班级名称 |
| classYearName | 2016级 | string | 是 | 年级名称 |
| majorName | 软件工程 | string | 是 | 专业名称 |
| departmentName | 软件学院 | string | 是 | 学院名称 |
| schoolName | 信息技术学校 | string | 是 | 学校名称 |
| classId | 3 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 班级删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 11:40:43

> 更新时间: 2023-05-05 11:41:15

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/deleteClass

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| classId | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 班级批量删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 14:20:27

> 更新时间: 2023-05-05 14:21:31

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/deleteManyClass

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| classIds | 2,3 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 班级用户查询

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 15:51:55

> 更新时间: 2023-05-09 15:59:15

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/listClassUsers?classId=4

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| classId | 4 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 班级列表查询

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 11:42:10

> 更新时间: 2023-05-24 08:44:27

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/listSearchClass?allSearch=4&className=&classYearName=&majorName=&departmentName=&schoolName=&size=10&page=0

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| allSearch | 4 | string | 否 | 所有参数查询 |
| className | - | string | 否 | - |
| classYearName | - | string | 否 | - |
| majorName | - | string | 否 | - |
| departmentName | - | string | 否 | - |
| schoolName | - | string | 否 | - |
| size | 10 | string | 否 | 每页元素个数 |
| page | 0 | string | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"classId": 4,
				"className": "4班",
				"classYearName": "2016级",
				"majorName": "软件工程",
				"departmentName": "软件学院",
				"schoolName": "信息技术学校",
				"createTime": "2023-05-04 15:21:10",
				"updateTime": "2023-05-04 15:21:10",
				"studentCnt": null,
				"groupId": 1
			}
		],
		"last": true,
		"totalElements": 1,
		"totalPages": 1,
		"number": 0,
		"size": 10,
		"sort": null,
		"first": true,
		"numberOfElements": 1
	},
	"errCode": null,
	"requestId": "bcaed83c47bd47bfb1e3b3496b975bfa",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.content | - | array | 消息详情 |
| data.content.classId | 4 | integer | 班级id |
| data.content.className | 4班 | string | 班级名称 |
| data.content.classYearName | 2016级 | string | 连接名称 |
| data.content.majorName | 软件工程 | string | 主修 |
| data.content.departmentName | 软件学院 | string | 学院名称 |
| data.content.schoolName | 信息技术学校 | string | 学校名称 |
| data.content.createTime | 2023-05-04 15:21:10 | string | 创建时间 |
| data.content.updateTime | 2023-05-04 15:21:10 | string | 更新时间 |
| data.content.studentCnt | null | null | - |
| data.content.groupId | 1 | integer | 分组id |
| data.last | true | boolean | 最后一页 |
| data.totalElements | 1 | integer | 总元素个数 |
| data.totalPages | 1 | integer | 总页数 |
| data.number | 0 | integer | 页码 |
| data.size | 10 | integer | 每页元素个数 |
| data.sort | null | null | 排序 |
| data.first | true | boolean | 是否是第一页 |
| data.numberOfElements | 1 | integer | 总元素个数 |
| errCode | null | null | - |
| requestId | bcaed83c47bd47bfb1e3b3496b975bfa | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 班级列表导出

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-09 09:13:02

> 更新时间: 2023-10-30 11:39:32

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/exportClasses?className=&classYearName=&majorName=&departmentName=&schoolName=&search=

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| className | - | string | 否 | - |
| classYearName | - | string | 否 | - |
| majorName | - | string | 否 | - |
| departmentName | - | string | 否 | - |
| schoolName | - | string | 否 | - |
| search | - | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"classId": 4,
				"className": "4班",
				"classYearName": "2016级",
				"majorName": "软件工程",
				"departmentName": "软件学院",
				"schoolName": "信息技术学校",
				"createTime": "2023-05-04 15:21:10",
				"updateTime": "2023-05-04 15:21:10",
				"studentCnt": null,
				"groupId": 1
			}
		],
		"last": true,
		"totalElements": 1,
		"totalPages": 1,
		"number": 0,
		"size": 10,
		"sort": null,
		"first": true,
		"numberOfElements": 1
	},
	"errCode": null,
	"requestId": "bcaed83c47bd47bfb1e3b3496b975bfa",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.content | - | array | 消息详情 |
| data.content.classId | 4 | integer | 班级id |
| data.content.className | 4班 | string | 班级名称 |
| data.content.classYearName | 2016级 | string | 连接名称 |
| data.content.majorName | 软件工程 | string | 主修 |
| data.content.departmentName | 软件学院 | string | 学院名称 |
| data.content.schoolName | 信息技术学校 | string | 学校名称 |
| data.content.createTime | 2023-05-04 15:21:10 | string | 创建时间 |
| data.content.updateTime | 2023-05-04 15:21:10 | string | 更新时间 |
| data.content.studentCnt | null | null | - |
| data.content.groupId | 1 | integer | 分组id |
| data.last | true | boolean | 最后一页 |
| data.totalElements | 1 | integer | 总元素个数 |
| data.totalPages | 1 | integer | 总页数 |
| data.number | 0 | integer | 页码 |
| data.size | 10 | integer | 每页元素个数 |
| data.sort | null | null | 排序 |
| data.first | true | boolean | 是否是第一页 |
| data.numberOfElements | 1 | integer | 总元素个数 |
| errCode | null | null | - |
| requestId | bcaed83c47bd47bfb1e3b3496b975bfa | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 班级列表导入

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-09 11:06:31

> 更新时间: 2023-05-09 15:34:36

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/importClasses

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| file | - | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"classId": null,
		"className": "12班",
		"classYearName": "2016级",
		"majorName": "软件工程",
		"departmentName": "软件学院",
		"schoolName": "信息技术学校",
		"createTime": "2023-05-04 15:21:10",
		"updateTime": "2023-05-04 15:21:10",
		"studentCnt": null,
		"groupId": null
	},
	"status": "F",
	"sysMsg": "第2行,班级名称已存在"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.classId | null | null | - |
| data.className | 12班 | string | - |
| data.classYearName | 2016级 | string | - |
| data.majorName | 软件工程 | string | - |
| data.departmentName | 软件学院 | string | - |
| data.schoolName | 信息技术学校 | string | - |
| data.createTime | 2023-05-04 15:21:10 | string | 创建时间 |
| data.updateTime | 2023-05-04 15:21:10 | string | 更新时间 |
| data.studentCnt | null | null | - |
| data.groupId | null | null | - |
| status | F | string | 状态 |
| sysMsg | 第2行,班级名称已存在 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 群组创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-04 17:23:47

> 更新时间: 2023-05-09 13:54:20

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/createGroup2

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| group2Name | 群组96 | string | 是 | - |
| group2Type | class | string | 是 | 群组类型:class=班级内,major=专业内,department=学院内,school=学校内 |
| userIds | 1,2,3,4 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 群组修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 13:52:39

> 更新时间: 2023-05-05 13:57:35

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/updateGroup2

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| group2Name | 群组1 | string | 是 | - |
| group2Type | 1 | string | 是 | 群组类型:1=班级内,2=专业内,3=学院内,4=学校内 |
| userIds | 1,2,3,4 | string | 是 | - |
| group2Id | 2 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 群组删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 14:23:00

> 更新时间: 2023-05-05 14:23:30

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/deleteGroup2

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| group2Id | 3 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 群组批量删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 14:24:06

> 更新时间: 2023-05-05 14:24:16

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/deleteManyGroup2

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| group2Ids | 4,5 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 群组用户查询

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 15:27:00

> 更新时间: 2023-05-05 17:24:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/listGroup2Users?group2Id=6

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| group2Id | 6 | string | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 群组列表查询

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 14:03:24

> 更新时间: 2023-05-05 17:23:16

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/listSearchGroup2?group2Name=3&group2Type=1&size=10&page=0

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| group2Name | 3 | string | 否 | - |
| group2Type | 1 | string | 否 | - |
| size | 10 | string | 否 | 每页元素个数 |
| page | 0 | string | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 群组列表导出

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-09 10:26:25

> 更新时间: 2023-05-24 15:39:05

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/exportGroup2s?group2Name=&group2Type=

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| group2Name | - | string | 否 | - |
| group2Type | - | string | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 群组列表导入

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-09 15:02:43

> 更新时间: 2023-05-09 15:34:10

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/group/importGroup2s

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| file | - | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"group2Id": null,
		"group2Name": "群组67",
		"userCnt": 4,
		"group2Type": "班级内",
		"createTime": "2023-05-05 13:53:39",
		"updateTime": "2023-05-05 13:53:39",
		"groupId": 1,
		"userIds": "1,2,3"
	},
	"status": "F",
	"sysMsg": "第1条数据,群组名称已存在"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.group2Id | null | null | - |
| data.group2Name | 群组67 | string | - |
| data.userCnt | 4 | integer | - |
| data.group2Type | 班级内 | string | 群组类型:class=班级内,major=专业内,department=学院内,school=学校内 |
| data.createTime | 2023-05-05 13:53:39 | string | 创建时间 |
| data.updateTime | 2023-05-05 13:53:39 | string | 更新时间 |
| data.groupId | 1 | integer | - |
| data.userIds | 1,2,3 | string | - |
| status | F | string | 状态 |
| sysMsg | 第1条数据,群组名称已存在 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 获取设备数据访问token

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-08-23 10:22:07

> 更新时间: 2023-08-23 10:24:35

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/createDeviceAccessToken

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 公共

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-02-21 16:15:30

> 更新时间: 2023-02-21 16:15:29

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 文件上传

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-02-21 16:15:42

> 更新时间: 2023-10-11 17:15:53

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/common/upload

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| type | image | Text | 是 | 上传文件类型, 用于校验后缀, 值: document, image, video |
| file | - | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"saveName": "/upload/202305/8f1130dd9507bbcad78be53a14f8813a.jpg",
		"originName": "菜单.jpg"
	},
	"errCode": null,
	"requestId": "250e0ce5e2c1477a8d8d34d0061d86c5",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.saveName | /upload/202305/8f1130dd9507bbcad78be53a14f8813a.jpg | string | 文件保存名称 |
| data.originName | 菜单.jpg | string | 文件原始名称 |
| errCode | null | null | - |
| requestId | 250e0ce5e2c1477a8d8d34d0061d86c5 | string | 请求唯一id |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 获取上传文件_接口

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-02-28 09:54:01

> 更新时间: 2023-05-24 14:21:36

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/common/getUploadFile?fileName=/upload/202305/8f1130dd9507bbcad78be53a14f881a.jpg&originName=哈哈.jpg

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| fileName | /upload/202305/8f1130dd9507bbcad78be53a14f881a.jpg | Text | 是 | 文件名, 用于查找文件 |
| originName | 哈哈.jpg | Text | 否 | 文件原始名称, 没有就不传, 仅用于命名文件,不传用fileName |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"saveName": "74ba98d30350c2d4e4fd8295fb22541f.doc",
		"originName": "教程.doc"
	},
	"requestId": "a0f973adfb154f058927c2d1fe90f4f3",
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.saveName | 74ba98d30350c2d4e4fd8295fb22541f.doc | string | 文件保存名称 |
| data.originName | 教程.doc | string | 文件原始名称 |
| requestId | a0f973adfb154f058927c2d1fe90f4f3 | string | 请求唯一id |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(201)

```javascript
暂无数据
```

**Query**

## 获取上传文件_路径

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-17 14:48:32

> 更新时间: 2023-05-17 14:52:44

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/upload/202305/8f1130dd9507bbcad78be53a14f8813a.jpg

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 内容管理

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-04-27 11:45:58

> 更新时间: 2023-04-27 11:45:58

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 管理_内容列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-04-27 11:46:52

> 更新时间: 2023-04-28 16:49:50

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/content/listSearch

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 管理_新增和修改内容

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-17 15:07:14

> 更新时间: 2023-05-24 14:22:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/content/save

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | - | string | 否 | 内容id, 新增不传, 更新传 |
| contentPage | 首页 | string | 否 | 内容页 |
| type1 | 13 | string | 否 | 类型1 |
| type2 | 12312 | string | 否 | 类型2 |
| type3 | 123 | string | 否 | 类型3 |
| title | 23123 | string | 否 | 标题 |
| intro | 31231 | string | 否 | 简介 |
| image | 12312 | string | 否 | 图片 |
| url | http://12321 | string | 否 | 相关url |
| sort | 10 | array | 否 | 排序值 |
| document | 打发第三方 | string | 否 | 内容,富文本 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 管理_获取类型_用于填写提示

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-17 15:15:58

> 更新时间: 2023-05-24 14:22:07

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/content/getTypes

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 管理_获取内容详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-17 15:19:01

> 更新时间: 2023-05-24 14:22:11

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/content/get?id=2

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 2 | string | 是 | 新增不传, 更新传 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 管理_修改内容状态

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-17 15:21:48

> 更新时间: 2023-05-24 14:22:14

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/content/changeStatus

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 2 | string | 是 | 新增不传, 更新传 |
| status | 1 | string | 是 | 状态:1=使用中,2=未使用 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 查看_内容列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-04-28 16:50:20

> 更新时间: 2023-05-17 15:14:02

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/content/getPageContent?contentPage=主页

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| contentPage | 主页 | string | 是 | 值: 主页, 文档与支持 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": [
		{
			"id": 2,
			"contentPage": "主页",
			"image": "3b8bda31f5a64ce8ac9ab1ed2426ad81.png",
			"title": "",
			"intro": "",
			"type1": "轮播图",
			"type2": "",
			"type3": "",
			"document": "<p><br></p>",
			"createTime": null,
			"updateTime": "2023-04-28 16:02:00",
			"status": 2,
			"sort": null,
			"url": ""
		},
		{
			"id": 5,
			"contentPage": "主页",
			"image": "69d60b5db9e677da21238dcbdb188cf2.png",
			"title": "",
			"intro": "",
			"type1": "轮播图",
			"type2": "",
			"type3": "",
			"document": "<p><br></p>",
			"createTime": "2023-04-28 16:00:19",
			"updateTime": "2023-04-28 16:00:19",
			"status": null,
			"sort": null,
			"url": null
		},
		{
			"id": 6,
			"contentPage": "主页",
			"image": "09f86cb11d47ee0e773257bdde32a3c5.png",
			"title": "",
			"intro": "",
			"type1": "轮播图",
			"type2": "",
			"type3": "",
			"document": "<p><br></p>",
			"createTime": "2023-04-28 16:01:45",
			"updateTime": "2023-04-28 16:01:45",
			"status": null,
			"sort": null,
			"url": null
		},
		{
			"id": 7,
			"contentPage": "主页",
			"image": "45711af190dcce462129ca88044a1a33.png",
			"title": "",
			"intro": "",
			"type1": "更丰富的接入场景",
			"type2": "",
			"type3": "",
			"document": "<p><br></p>",
			"createTime": "2023-04-28 16:04:09",
			"updateTime": "2023-04-28 16:09:49",
			"status": null,
			"sort": -10,
			"url": ""
		},
		{
			"id": 8,
			"contentPage": "主页",
			"image": "676e647218e3c278d179cf3b20606dc3.png",
			"title": "智慧港口",
			"intro": "",
			"type1": "更丰富的接入场景",
			"type2": "",
			"type3": "",
			"document": "<p><br></p>",
			"createTime": "2023-04-28 16:12:34",
			"updateTime": "2023-04-28 16:12:34",
			"status": null,
			"sort": 0,
			"url": null
		},
		{
			"id": 9,
			"contentPage": "主页",
			"image": "f2e7a48bb0e4798e1b90cd45b15a1beb.png",
			"title": "智慧矿山",
			"intro": "",
			"type1": "更丰富的接入场景",
			"type2": "",
			"type3": "",
			"document": "<p><br></p>",
			"createTime": "2023-04-28 16:13:26",
			"updateTime": "2023-04-28 16:13:26",
			"status": null,
			"sort": 0,
			"url": null
		},
		{
			"id": 10,
			"contentPage": "主页",
			"image": "f50f94de538991ece86406a907b485c0.png",
			"title": "南向协议广泛匹配",
			"intro": "#支持mqtt协议上云\r\n#开放以太网\r\n#支持子设备",
			"type1": "更灵活的接入方式",
			"type2": "",
			"type3": "",
			"document": "<p><br></p>",
			"createTime": "2023-04-28 16:16:48",
			"updateTime": "2023-04-28 16:16:48",
			"status": null,
			"sort": 0,
			"url": null
		}
	],
	"errCode": null,
	"requestId": "016b89820492476aa1b3de02d0c32a87",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | array | - |
| data.id | 2 | integer | - |
| data.contentPage | 主页 | string | 值: 首页, |
| data.image | 3b8bda31f5a64ce8ac9ab1ed2426ad81.png | string | 图片地址需要拼接前缀: 后端主机/common/getUploadFile?fileName= |
| data.title | - | string | - |
| data.intro | - | string | - |
| data.type1 | 轮播图 | string | - |
| data.type2 | - | string | - |
| data.type3 | - | string | - |
| data.document | <p><br></p> | string | - |
| data.createTime | null | null | 创建时间 |
| data.updateTime | 2023-04-28 16:02:00 | string | 更新时间 |
| data.status | 2 | integer | 状态 |
| data.sort | null | null | 排序 |
| data.url | - | string | - |
| errCode | null | null | - |
| requestId | 016b89820492476aa1b3de02d0c32a87 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 课程

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-11 09:34:43

> 更新时间: 2023-05-24 14:24:52

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 课程创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-11 15:15:05

> 更新时间: 2023-12-06 10:58:51

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseName | 课程名称96 | string | 是 | 课程名称 |
| courseStartTime | 2023-05-12 10:41:55 | string | 是 | 课程开始时间 |
| courseEndTime | 2023-05-12 10:41:55 | string | 是 | 课程结束时间 |
| courseCnt | 10 | number | 是 | 课程数量 |
| courseImage | 课程图片96 | string | 否 | 课程图片 |
| courseType | 1 | number | 是 | 课程类型:1=公开课,2=私有课 |
| courseIntro | 课程概述96 | string | 是 | 课程概述 |
| courseTarget | 课程目标96 | string | 是 | 课程目标 |
| courseOutline | 课程大纲96 | string | 否 | 课程大纲, 格式:[
	{
	"section":"章节名称"
	"content":[
		{
			"number":"序号",
			"name":"小节名称",
			"type":"小节类型",
			"preCourseware":['课前课件1'],
			"preProjectId":课前资源工程id,
			"preProjectName":课前资源工程名称,
			"inCourseware":['课中课件1'],
			"inProjectId":课中资源工程id,
			"inProjectName":课中资源工程名称,
			"afterCourseware":['课后课件1'],
			"afterProjectId":课后资源工程id,
			"afterProjectName":课后资源工程名称,
			"courseNumber":2
		}
		]
	}
] |
| courseBase | 预备知识96 | string | 否 | 预备知识 |
| courseRef | 参考资料96 | string | 否 | 参考资料 |
| major | 专业1 | string | 是 | 专业 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"courseEndTime": "Fri May 12 10:41:55 CST 2023",
		"courseType": "1",
		"courseBase": "预备知识47",
		"teacherName": "abcj",
		"courseIntro": "课程概述47",
		"courseRef": "参考资料47",
		"creatorId": "0",
		"updateTime": "Fri May 12 16:35:09 CST 2023",
		"courseTarget": "课程目标47",
		"courseStartTime": "Fri May 12 10:41:55 CST 2023",
		"courseOutline": "课程大纲47",
		"courseCnt": "10",
		"courseName": "课程名称47",
		"courseImage": "课程图片47",
		"teacherId": "0",
		"major": null,
		"createTime": "Fri May 12 16:35:09 CST 2023",
		"school": null,
		"studyCnt": "0",
		"tag": null,
		"department": null,
		"courseId": "12",
		"status": "1"
	},
	"errCode": null,
	"requestId": "4bca44167de24b2a8acc6dc08abe674c",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.courseEndTime | Fri May 12 10:41:55 CST 2023 | string | 课程结束时间 |
| data.courseType | 1 | string | 课程类型:1=公开课,2=私有课 |
| data.courseBase | 预备知识47 | string | 预备知识 |
| data.teacherName | abcj | string | 老师名称 |
| data.courseIntro | 课程概述47 | string | 课程概述 |
| data.courseRef | 参考资料47 | string | 参考资料 |
| data.creatorId | 0 | string | 创建者 |
| data.updateTime | Fri May 12 16:35:09 CST 2023 | string | 更新时间 |
| data.courseTarget | 课程目标47 | string | 课程目标 |
| data.courseStartTime | Fri May 12 10:41:55 CST 2023 | string | 课程开始时间 |
| data.courseOutline | 课程大纲47 | string | 课程大纲 |
| data.courseCnt | 10 | string | 课程数量 |
| data.courseName | 课程名称47 | string | 课程名称 |
| data.courseImage | 课程图片47 | string | 课程图片 |
| data.teacherId | 0 | string | 老师名称 |
| data.major | null | null | 专业 |
| data.createTime | Fri May 12 16:35:09 CST 2023 | string | 创建时间 |
| data.school | null | null | 学校 |
| data.studyCnt | 0 | string | 学习人数 |
| data.tag | null | null | 课程标签 |
| data.department | null | null | 学院 |
| data.courseId | 12 | string | 课程id |
| data.status | 1 | string | 状态 |
| errCode | null | null | - |
| requestId | 4bca44167de24b2a8acc6dc08abe674c | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-12 16:36:21

> 更新时间: 2023-05-15 08:52:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseId | 13 | string | 是 | 课程id |
| courseName | 课程名称2 | string | 是 | 课程名称 |
| courseStartTime | 2023-05-12 10:41:55 | string | 是 | 课程开始时间 |
| courseEndTime | 2023-05-12 10:41:55 | string | 是 | 课程结束时间 |
| courseCnt | 12 | number | 是 | 课程数量 |
| courseImage | 课程图片96 | string | 否 | 课程图片 |
| courseType | 1 | number | 是 | 课程类型:1=公开课,2=私有课 |
| courseIntro | 课程概述96 | string | 是 | 课程概述 |
| courseTarget | 课程目标96 | string | 是 | 课程目标 |
| courseOutline | 课程大纲96 | string | 否 | 课程大纲 |
| courseBase | 预备知识96 | string | 否 | 预备知识 |
| courseRef | 参考资料96 | string | 否 | 参考资料 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"courseEndTime": "Fri May 12 10:41:55 CST 2023",
		"courseType": "1",
		"courseBase": "预备知识47",
		"teacherName": "abcj",
		"courseIntro": "课程概述47",
		"courseRef": "参考资料47",
		"creatorId": "0",
		"updateTime": "Fri May 12 16:35:09 CST 2023",
		"courseTarget": "课程目标47",
		"courseStartTime": "Fri May 12 10:41:55 CST 2023",
		"courseOutline": "课程大纲47",
		"courseCnt": "10",
		"courseName": "课程名称47",
		"courseImage": "课程图片47",
		"teacherId": "0",
		"major": null,
		"createTime": "Fri May 12 16:35:09 CST 2023",
		"school": null,
		"studyCnt": "0",
		"tag": null,
		"department": null,
		"courseId": "12",
		"status": "1"
	},
	"errCode": null,
	"requestId": "4bca44167de24b2a8acc6dc08abe674c",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.courseEndTime | Fri May 12 10:41:55 CST 2023 | string | 课程结束时间 |
| data.courseType | 1 | string | 课程类型:1=公开课,2=私有课 |
| data.courseBase | 预备知识47 | string | 预备知识 |
| data.teacherName | abcj | string | 老师名称 |
| data.courseIntro | 课程概述47 | string | 课程概述 |
| data.courseRef | 参考资料47 | string | 参考资料 |
| data.creatorId | 0 | string | 创建者 |
| data.updateTime | Fri May 12 16:35:09 CST 2023 | string | 更新时间 |
| data.courseTarget | 课程目标47 | string | 课程目标 |
| data.courseStartTime | Fri May 12 10:41:55 CST 2023 | string | 课程开始时间 |
| data.courseOutline | 课程大纲47 | string | 课程大纲 |
| data.courseCnt | 10 | string | 课程数量 |
| data.courseName | 课程名称47 | string | 课程名称 |
| data.courseImage | 课程图片47 | string | 课程图片 |
| data.teacherId | 0 | string | 老师名称 |
| data.major | null | null | 专业 |
| data.createTime | Fri May 12 16:35:09 CST 2023 | string | 创建时间 |
| data.school | null | null | 学校 |
| data.studyCnt | 0 | string | 学习人数 |
| data.tag | null | null | 课程标签 |
| data.department | null | null | 学院 |
| data.courseId | 12 | string | 课程id |
| data.status | 1 | string | 状态 |
| errCode | null | null | - |
| requestId | 4bca44167de24b2a8acc6dc08abe674c | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程列表_我的

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-11 16:10:10

> 更新时间: 2023-12-06 10:58:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/myCourses?school=&department=&major=&courseName=&status=&page=0&size=10

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| school | - | string | 否 | 学校 |
| department | - | string | 否 | 学院 |
| major | - | string | 否 | 专业 |
| courseName | - | string | 否 | 课程名称搜索 |
| status | - | string | 否 | 状态:1=未开始,2=进行中,3=已完成 |
| page | 0 | number | 否 | - |
| size | 10 | number | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程列表_公开课

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-17 10:09:59

> 更新时间: 2023-12-11 14:34:03

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/publicCourses?isBest=1&isHot=0&page=0&size=10

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| isBest | 1 | integer | 否 | 精品课程,传1筛选 |
| isHot | 0 | integer | 否 | 热门课程,传1筛选 |
| page | 0 | number | 否 | - |
| size | 10 | number | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程列表_教师端

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-26 11:07:12

> 更新时间: 2023-05-30 09:29:02

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/teacherCourses?courseName=&courseType=2&page=0&size=10

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseName | - | string | 否 | 课程名称 |
| courseType | 2 | number | 否 | 课程类型:1=公开课,2=私有课 |
| page | 0 | number | 否 | - |
| size | 10 | number | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-15 16:55:12

> 更新时间: 2023-12-06 10:35:12

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/detail?courseId=1

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseId | 1 | string | 是 | 课程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-15 16:57:39

> 更新时间: 2023-05-24 14:24:50

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/delete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseId | 13 | string | 是 | 课程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程状态数量统计

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-11 16:34:32

> 更新时间: 2023-05-24 14:24:49

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/statusCount

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程复制

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-15 17:03:34

> 更新时间: 2023-05-16 11:18:00

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/copy

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseId | 1 | string | 是 | 课程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 开始学习

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-16 11:24:22

> 更新时间: 2023-05-24 14:24:50

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/startStudy

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseId | 1 | string | 是 | 课程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程评论

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-16 15:23:11

> 更新时间: 2023-05-24 14:24:50

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/comment

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseId | 1 | string | 是 | 课程id |
| rating | 5 | string | 是 | 评分, 最多5星 |
| content | very good | string | 是 | 评论内容 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 评论点赞

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-16 15:43:06

> 更新时间: 2023-05-24 14:24:51

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/commentLike

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| commentId | 2 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 评论列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-16 15:56:23

> 更新时间: 2023-05-24 14:24:51

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/commentList?courseId=1

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseId | 1 | string | 是 | 课程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"content": [
			{
				"commentId": 1,
				"content": "very good",
				"rating": 5,
				"createTime": "2023-05-16 15:28:28",
				"likes": 6,
				"courseId": 1,
				"userId": 0,
				"updateTime": "2023-05-16 15:49:30"
			}
		],
		"totalPages": 1,
		"totalElements": 1,
		"last": true,
		"number": 0,
		"size": 20,
		"sort": null,
		"numberOfElements": 1,
		"first": true
	},
	"errCode": null,
	"requestId": "fa693112c1104297898eae4c58f345fd",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.content | - | array | 消息详情 |
| data.content.commentId | 1 | integer | - |
| data.content.content | very good | string | 消息详情 |
| data.content.rating | 5 | integer | 评分, 最多5星 |
| data.content.createTime | 2023-05-16 15:28:28 | string | 创建时间 |
| data.content.likes | 6 | integer | 点赞数 |
| data.content.courseId | 1 | integer | 课程id |
| data.content.userId | 0 | integer | 用户id |
| data.content.updateTime | 2023-05-16 15:49:30 | string | 更新时间 |
| data.totalPages | 1 | integer | 总页数 |
| data.totalElements | 1 | integer | 总元素个数 |
| data.last | true | boolean | 最后一页 |
| data.number | 0 | integer | 页码 |
| data.size | 20 | integer | 每页元素个数 |
| data.sort | null | null | 排序 |
| data.numberOfElements | 1 | integer | 总元素个数 |
| data.first | true | boolean | 是否是第一页 |
| errCode | null | null | - |
| requestId | fa693112c1104297898eae4c58f345fd | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 课程下发

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-16 16:17:41

> 更新时间: 2023-12-06 10:58:02

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/distribute

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| courseId | 1 | string | 是 | 课程id |
| userIds | 0,1,2,3 | string | 是 | 用户id列表 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 专业列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-12-05 11:33:09

> 更新时间: 2023-12-05 11:48:27

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/course/majorList

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": [
		"专业1"
	],
	"errCode": null,
	"requestId": "8170cd1bfc8f4750ac9b8e975c973904",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | ["专业1"] | array | 专业名称列表 |
| errCode | null | null | - |
| requestId | 8170cd1bfc8f4750ac9b8e975c973904 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

# 集成模型

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-05 14:52:24

> 更新时间: 2023-06-05 14:52:24

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 集成模型实例_创建

> 创建人: fuwei

> 更新人: 刘浩

> 创建时间: 2023-06-06 10:33:14

> 更新时间: 2023-07-03 09:49:52

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/createModelInstance

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 107 | number | 是 | 工程id |
| integraDevName | 模型实例名称96 | string | 是 | 模型实例名称 |
| belongScene | 1 | number | 否 | 场景id |
| linkDev | [{"productKey":"iy4uJzbjy1H","productNameNote":"test","deviceName":"test_1","deviceNickname":"测试设备"}] | string | 否 | 关联设备 |
| description | 描述96 | string | 否 | 描述 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 集成模型实例_修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-06 11:13:31

> 更新时间: 2023-06-25 15:08:34

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/updateModelInstance

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| integraDevName | 模型实例名称96 | string | 是 | 模型实例名称 |
| description | 描述96 | string | 否 | 描述 |
| instanceId | 22 | string | 是 | 实例id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 集成模型实例_删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-06 11:26:41

> 更新时间: 2023-06-25 15:08:44

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/deleteModelInstance

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| instanceId | 22 | string | 是 | 实例id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 集成模型实例_列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-06 11:48:32

> 更新时间: 2023-07-24 11:46:37

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/getModelInstances?integraDevName=&projectId=107&belongScene=&page=&size=

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| integraDevName | - | string | 否 | 实例id |
| projectId | 107 | string | 否 | 工程id |
| belongScene | - | string | 否 | 场景id |
| page | - | string | 否 | - |
| size | - | string | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 集成模型实例_详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-07 17:16:36

> 更新时间: 2023-06-28 11:52:42

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/getModelInstanceDetail?instanceId=21

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| instanceId | 21 | string | 否 | 实例id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"instanceId": 21,
		"integraDevName": "模型实例名称84",
		"modelId": null,
		"belongScene": 1,
		"linkDev": "[{\n\"productKey\":\"iy4uJzbjy1H\",\n\"productNameNote\":\"test\",\n\"deviceName\":\"ae4Q0SXMROCwA3FPTWzt\",\n\"deviceNickname\":\"测试设备\"\n},{\n  \"productKey\":\"iy4uJzbjy1H\",\n  \"productNameNote\":\"test\",\n  \"deviceName\":\"74EAwv4afnc5gpi7WCke\",\n  \"deviceNickname\":\"测试设备2\"\n  }]",
		"description": "描述84",
		"createTime": "2023-06-25 09:26:39",
		"updateTime": "2023-06-25 09:26:39",
		"projectId": 107,
		"userId": 21,
		"lastTime": null,
		"integraDevStatus": null,
		"strategyCnt": 4,
		"thingModels": [
			{
				"thingModel": "{\"schema\":\"https://iotx-tsl.oss-ap-southeast-1.aliyuncs.com/schema.json\",\"profile\":{\"version\":\"1.5\",\"productKey\":\"iy4uJzbjy1H\"},\"properties\":[{\"name\":\"温度\",\"identifier\":\"temperature\",\"required\":false,\"accessMode\":\"rw\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"step\":\"0.01\",\"unitName\":\"摄氏度\",\"unit\":\"°C\"}}},{\"name\":\"湿度\",\"identifier\":\"humidity\",\"required\":false,\"accessMode\":\"r\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"step\":\"0.01\",\"unitName\":\"相对湿度\",\"unit\":\"%RH\"}}}],\"services\":[{\"name\":\"服务2\",\"identifier\":\"service2\",\"callType\":\"async\",\"required\":false,\"inputData\":[{\"name\":\"参数1\",\"identifier\":\"param1\",\"required\":false,\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"step\":\"1\",\"unitName\":\"无\"}}}],\"outputData\":[],\"method\":\"thing.service.service2\"},{\"name\":\"服务1\",\"identifier\":\"service1\",\"callType\":\"async\",\"required\":false,\"inputData\":[{\"name\":\"参数1\",\"identifier\":\"param1\",\"required\":false,\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"step\":\"1\",\"unitName\":\"无\"}}}],\"outputData\":[],\"method\":\"thing.service.service1\"}],\"events\":[]}",
				"productKey": "iy4uJzbjy1H"
			}
		],
		"customFunList": [
			{
				"funId": 3,
				"funName": "测试26",
				"funKey": "test26",
				"cond": "[{\n\t\"productKey\":\"iy4uJzbjy1H\",\n\t\"deviceName\":\"ae4Q0SXMROCwA3FPTWzt\",\n\t\"property\":\"humidity\",\n\t\"condition\":\">\",\n\t\"value\":\"50\",\n\t\"assoc\":\"and\"\n},{\n\t\"productKey\":\"iy4uJzbjy1H\",\n\t\"deviceName\":\"74EAwv4afnc5gpi7WCke\",\n\t\"property\":\"temperature\",\n\t\"condition\":\">\",\n\t\"value\":\"50\",\n\t\"assoc\":\"and\"\n}]",
				"action": "[{\n\t\"type\":\"property\",\n\t\"operator\":\"+\",\n\t\"productKey\":\"iy4uJzbjy1H\",\n\t\"deviceName\":\"74EAwv4afnc5gpi7WCke\",\n\t\"property\":\"temperature\"\n},\n{\n\t\"type\":\"number\",\n\t\"operator\":\"+\",\n\t\"value\":\"200\"\n}]",
				"modelInstanceId": 21,
				"projectId": 107,
				"execTime": null,
				"type": "property"
			},
			{
				"funId": 8,
				"funName": "测试43",
				"funKey": "test43",
				"cond": "[{\n\t\"productKey\":\"iy4uJzbjy1H\",\n\t\"deviceName\":\"ae4Q0SXMROCwA3FPTWzt\",\n\t\"service\":\"service1\",\n\t\"value\":\"{\\\"param1\\\":60}\",\n\t\"assoc\":\"and\"\n}]",
				"action": "[{\n\t\"productKey\":\"iy4uJzbjy1H\",\n\t\"deviceName\":\"ae4Q0SXMROCwA3FPTWzt\",\n\t\"type\":\"invokeService\",\n\t\"functionKey\":\"service2\",\n\t\"value\":\"{\\\"param1\\\":88}\"\n}]",
				"modelInstanceId": 21,
				"projectId": 107,
				"execTime": null,
				"type": "service"
			},
			{
				"funId": 9,
				"funName": "测试66",
				"funKey": "test66",
				"cond": "[{\n\t\"productKey\":\"iy4uJzbjy1H\",\n\t\"deviceName\":\"ae4Q0SXMROCwA3FPTWzt\",\n\t\"service\":\"service1\",\n\t\"value\":\"{\\\"param1\\\":60}\",\n\t\"assoc\":\"and\"\n}]",
				"action": "[{\n\t\"productKey\":\"iy4uJzbjy1H\",\n\t\"deviceName\":\"ae4Q0SXMROCwA3FPTWzt\",\n\t\"type\":\"invokeService\",\n\t\"functionKey\":\"service2\",\n\t\"value\":\"{\\\"param1\\\":88}\"\n}]",
				"modelInstanceId": 21,
				"projectId": 107,
				"execTime": null,
				"type": "service"
			}
		]
	},
	"errCode": null,
	"requestId": "e646ecc4e315475ab8cea592b2e3df84",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.instanceId | 21 | integer | - |
| data.integraDevName | 模型实例名称84 | string | - |
| data.modelId | null | null | - |
| data.belongScene | 1 | integer | - |
| data.linkDev | [{"productKey":"iy4uJzbjy1H","productNameNote":"test","deviceName":"ae4Q0SXMROCwA3FPTWzt","deviceNickname":"测试设备"},{  "productKey":"iy4uJzbjy1H",  "productNameNote":"test",  "deviceName":"74EAwv4afnc5gpi7WCke",  "deviceNickname":"测试设备2"  }] | string | - |
| data.description | 描述84 | string | 描述 |
| data.createTime | 2023-06-25 09:26:39 | string | 创建时间 |
| data.updateTime | 2023-06-25 09:26:39 | string | 更新时间 |
| data.projectId | 107 | integer | - |
| data.userId | 21 | integer | 用户id |
| data.lastTime | null | null | - |
| data.integraDevStatus | null | null | - |
| data.strategyCnt | 4 | integer | - |
| data.thingModels | - | array | - |
| data.thingModels.thingModel | {"schema":"https://iotx-tsl.oss-ap-southeast-1.aliyuncs.com/schema.json","profile":{"version":"1.5","productKey":"iy4uJzbjy1H"},"properties":[{"name":"温度","identifier":"temperature","required":false,"accessMode":"rw","dataType":{"type":"float","specs":{"min":"0","max":"100","step":"0.01","unitName":"摄氏度","unit":"°C"}}},{"name":"湿度","identifier":"humidity","required":false,"accessMode":"r","dataType":{"type":"float","specs":{"min":"0","max":"100","step":"0.01","unitName":"相对湿度","unit":"%RH"}}}],"services":[{"name":"服务2","identifier":"service2","callType":"async","required":false,"inputData":[{"name":"参数1","identifier":"param1","required":false,"dataType":{"type":"int","specs":{"min":"0","max":"100","step":"1","unitName":"无"}}}],"outputData":[],"method":"thing.service.service2"},{"name":"服务1","identifier":"service1","callType":"async","required":false,"inputData":[{"name":"参数1","identifier":"param1","required":false,"dataType":{"type":"int","specs":{"min":"0","max":"100","step":"1","unitName":"无"}}}],"outputData":[],"method":"thing.service.service1"}],"events":[]} | string | - |
| data.thingModels.productKey | iy4uJzbjy1H | string | 产品key |
| data.customFunList | - | array | 自定义属性或服务 |
| data.customFunList.funId | 3 | integer | - |
| data.customFunList.funName | 测试26 | string | - |
| data.customFunList.funKey | test26 | string | - |
| data.customFunList.cond | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"property":"humidity",	"condition":">",	"value":"50",	"assoc":"and"},{	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"property":"temperature",	"condition":">",	"value":"50",	"assoc":"and"}] | string | 条件:示例: [{
	"productKey":"h7s72qjeGaM"
	"deviceName":"test2_1",
	"property":"temperature",
	"condition":">",
	"value":"50",
	"assoc":"and"
}] |
| data.customFunList.action | [{	"type":"property",	"operator":"+",	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"property":"temperature"},{	"type":"number",	"operator":"+",	"value":"200"}] | string | 动作:示例: [{
	"productKey":"h7s72qjeGaM",
	"deviceName":"test2_",
	"type":"property/service"
	"functionKey":"属性/服务标识",
	"functionName":"属性/服务名",
	"value":"参数值"
}] |
| data.customFunList.modelInstanceId | 21 | integer | - |
| data.customFunList.projectId | 107 | integer | - |
| data.customFunList.execTime | null | null | - |
| data.customFunList.type | property | string | 消息类型 |
| errCode | null | null | - |
| requestId | e646ecc4e315475ab8cea592b2e3df84 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 集成模型实例_获取多个设备属性值

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-14 16:32:31

> 更新时间: 2023-07-06 14:27:34

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/getProperties?instanceId=21

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| instanceId | 21 | string | 否 | 设备标识, 格式productKey.deviceName, 多个设备用","分割 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": [
		{
			"productKey": "iy4uJzbjy1H",
			"deviceName": "ae4Q0SXMROCwA3FPTWzt",
			"properties": {
				"OnlineStatus": {
					"value": "online",
					"time": 1687920174310
				},
				"temperature": {
					"value": 78,
					"time": 1687767476007
				},
				"humidity": {
					"value": 60,
					"time": 1687767476007
				}
			}
		},
		{
			"productKey": "iy4uJzbjy1H",
			"deviceName": "74EAwv4afnc5gpi7WCke",
			"properties": {
				"temperature": {
					"value": 68,
					"time": 1687660946214
				},
				"OnlineStatus": {
					"value": "offline",
					"time": 1687920178668
				},
				"humidity": {
					"value": 69,
					"time": 1687660946214
				}
			}
		},
		{
			"productKey": "customFun",
			"deviceName": "customFun",
			"properties": {
				"test26": {
					"time": 1687660946214,
					"value": 268
				}
			}
		}
	],
	"errCode": null,
	"requestId": "e5e649f6ae9d411984e62047965364b2",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | array | - |
| data.productKey | iy4uJzbjy1H | string | 产品key |
| data.deviceName | ae4Q0SXMROCwA3FPTWzt | string | 设备名称 |
| data.properties | - | object | - |
| data.properties.OnlineStatus | - | object | - |
| data.properties.OnlineStatus.value | online | string | - |
| data.properties.OnlineStatus.time | 1687920174310 | integer | - |
| data.properties.temperature | - | object | - |
| data.properties.temperature.value | 78 | integer | - |
| data.properties.temperature.time | 1687767476007 | integer | - |
| data.properties.humidity | - | object | - |
| data.properties.humidity.value | 60 | integer | - |
| data.properties.humidity.time | 1687767476007 | integer | - |
| errCode | null | null | - |
| requestId | e5e649f6ae9d411984e62047965364b2 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 集成模型实例_获取多个设备服务最近调用记录

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-25 14:32:56

> 更新时间: 2023-07-06 14:27:54

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/getServiceInvokes?instanceId=21

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| instanceId | 21 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": [
		{
			"identifier": "test3",
			"param": "",
			"type": "invokeService",
			"generateTime": 1687922478375,
			"productKey": "iy4uJzbjy1H",
			"operation": "",
			"deviceName": "ae4Q0SXMROCwA3FPTWzt",
			"content": ""
		},
		{
			"identifier": "service2",
			"param": "{\"param1\":88}",
			"type": "invokeService",
			"generateTime": 1687922478367,
			"productKey": "iy4uJzbjy1H",
			"operation": "/sys/iy4uJzbjy1H/ae4Q0SXMROCwA3FPTWzt/service/thing/service2",
			"deviceName": "ae4Q0SXMROCwA3FPTWzt",
			"content": "{\"method\":\"thing.service.service2\",\"id\":\"567627305\",\"params\":{\"param1\":88},\"version\":\"1.0.0\"}"
		},
		{
			"identifier": "service1",
			"param": "{\"param1\":60}",
			"type": "invokeService",
			"generateTime": 1687922478288,
			"productKey": "iy4uJzbjy1H",
			"operation": "/sys/iy4uJzbjy1H/ae4Q0SXMROCwA3FPTWzt/service/thing/service1",
			"deviceName": "ae4Q0SXMROCwA3FPTWzt",
			"content": "{\"method\":\"thing.service.service1\",\"id\":\"566962441\",\"params\":{\"param1\":60},\"version\":\"1.0.0\"}"
		},
		{
			"identifier": "service1",
			"param": "{\"param1\":1}",
			"type": "invokeService",
			"generateTime": 1687767525181,
			"productKey": "iy4uJzbjy1H",
			"operation": "/sys/iy4uJzbjy1H/74EAwv4afnc5gpi7WCke/service/thing/service1",
			"deviceName": "74EAwv4afnc5gpi7WCke",
			"content": "{\"method\":\"thing.service.service1\",\"id\":\"354998386\",\"params\":{\"param1\":1},\"version\":\"1.0.0\"}"
		},
		{
			"identifier": "temperature",
			"type": "setProperty",
			"generateTime": 1687767525081,
			"productKey": "iy4uJzbjy1H",
			"operation": "/sys/iy4uJzbjy1H/74EAwv4afnc5gpi7WCke/service/thing/temperature",
			"deviceName": "74EAwv4afnc5gpi7WCke",
			"content": "{\"method\":\"thing.service.temperature\",\"id\":\"354080088\",\"params\":10,\"version\":\"1.0.0\"}"
		}
	],
	"errCode": null,
	"requestId": "5eaf4e9654d349cab0d5a2957e56e3e6",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | array | - |
| data.identifier | test3 | string | - |
| data.param | - | string | - |
| data.type | invokeService | string | 消息类型 |
| data.generateTime | 1687922478375 | integer | 消息生成时间 |
| data.productKey | iy4uJzbjy1H | string | 产品key |
| data.operation | - | string | 操作权限:0=发布,1=订阅,2=发布订阅 |
| data.deviceName | ae4Q0SXMROCwA3FPTWzt | string | 设备名称 |
| data.content | - | string | 消息详情 |
| errCode | null | null | - |
| requestId | 5eaf4e9654d349cab0d5a2957e56e3e6 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 策略_新建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-14 15:43:57

> 更新时间: 2023-06-25 15:02:21

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/createStrategy

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| strategyName | 测试96 | string | 是 | - |
| strategyKey | test96 | string | 是 | - |
| cond | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"property":"humidity",	"condition":">",	"value":"50",	"assoc":"and"},{	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"property":"temperature",	"condition":">",	"value":"50",	"assoc":"and"}] | string | 是 | 条件:示例: [{
	"productKey":"h7s72qjeGaM",
	"deviceName":"test2_1",
	"property":"temperature",
	"propertyName":"温度",
	"condition":">",
	"value":"50",
	"assoc":"and"
}] |
| action | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"type":"setProperty",	"functionKey":"temperature",	"value":"22"}] | string | 是 | 动作:示例: [{
	"productKey":"h7s72qjeGaM",
	"deviceName":"test2_",
	"type":"setProperty/invokeService"
	"functionKey":"属性/服务标识",
	"functionName":"属性/服务名",
	"value":"参数值"
}] |
| modelInstanceId | 21 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 策略_修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-07-19 09:58:24

> 更新时间: 2023-07-19 15:05:22

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/updateStrategy

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| strategyName | 测试96 | string | 是 | - |
| strategyKey | test96 | string | 是 | - |
| cond | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"property":"humidity",	"condition":">",	"value":"51",	"assoc":"and"},{	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"property":"temperature",	"condition":">",	"value":"50",	"assoc":"and"}] | string | 是 | 条件:示例: [{
	"productKey":"h7s72qjeGaM",
	"deviceName":"test2_1",
	"property":"temperature",
	"propertyName":"温度",
	"condition":">",
	"value":"50",
	"assoc":"and"
}] |
| action | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"type":"setProperty",	"functionKey":"temperature",	"value":"22"}] | string | 是 | 动作:示例: [{
	"productKey":"h7s72qjeGaM",
	"deviceName":"test2_",
	"type":"setProperty/invokeService"
	"functionKey":"属性/服务标识",
	"functionName":"属性/服务名",
	"value":"参数值"
}] |
| modelInstanceId | 2 | string | 是 | - |
| strategyId | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 策略_修改状态

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-14 16:10:55

> 更新时间: 2023-07-19 10:25:47

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/changeStrategyStatus

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| status | 1 | string | 是 | 状态:0=禁用,1=启用 |
| strategyId | 10 | string | 是 | 策略id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 策略_修改所有策略状态

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-09-25 15:43:01

> 更新时间: 2023-09-25 17:49:43

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/changeStrategiesStatus

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| status | 1 | string | 是 | 状态:0=禁用,1=启用 |
| modelInstanceId | 19 | string | 是 | 策略id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 策略_删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-14 16:16:20

> 更新时间: 2023-06-14 16:16:35

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/deleteStrategy

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| strategyId | 7 | string | 是 | 策略id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 策略_获取策略列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-14 16:17:48

> 更新时间: 2023-06-25 15:17:59

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/getStrategies?modelInstanceId=21

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| modelInstanceId | 21 | string | 是 | 集成实例id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 自定义属性_新建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-27 09:57:06

> 更新时间: 2023-06-27 15:40:39

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/createCustomProperty

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| funName | 测试96 | string | 是 | - |
| funKey | test96 | string | 是 | - |
| cond | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"property":"humidity",	"condition":">",	"value":"50",	"assoc":"and"},{	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"property":"temperature",	"condition":">",	"value":"50",	"assoc":"and"}] | string | 是 | 条件:示例: [{
	"productKey":"h7s72qjeGaM",
	"deviceName":"test2_1",
	"property":"temperature",
	"propertyName":"温度",
	"condition":">",
	"value":"50",
	"assoc":"and"
}] |
| action | [{	"type":"property",	"operator":"+",	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"property":"temperature"},{	"type":"number",	"operator":"+",	"value":"200"}] | string | 是 | 动作:示例: [{
	"type":"property/number",
	"operator":"+/-/*//",
	"value":"自定义值",
	"productKey":"iy4uJzbjy1H",
	"deviceName":"74EAwv4afnc5gpi7WCke",
	"property":"属性名"
}] |
| modelInstanceId | 21 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 自定义属性_修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-27 15:20:34

> 更新时间: 2023-06-27 15:37:49

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/updateCustomProperty

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| funName | 测试96 | string | 是 | - |
| funKey | test96 | string | 是 | - |
| cond | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"property":"humidity",	"condition":">",	"value":"50",	"assoc":"and"},{	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"property":"temperature",	"condition":">",	"value":"50",	"assoc":"and"}] | string | 是 | 条件:示例: [{
	"productKey":"h7s72qjeGaM",
	"deviceName":"test2_1",
	"property":"temperature",
	"propertyName":"温度",
	"condition":">",
	"value":"50",
	"assoc":"and"
}] |
| action | [{	"type":"property",	"operator":"+",	"productKey":"iy4uJzbjy1H",	"deviceName":"74EAwv4afnc5gpi7WCke",	"property":"temperature"},{	"type":"number",	"operator":"+",	"value":"200"}] | string | 是 | 动作:示例: [{
	"type":"property/number",
	"operator":"+/-/*//",
	"value":"自定义值",
	"productKey":"iy4uJzbjy1H",
	"deviceName":"74EAwv4afnc5gpi7WCke",
	"property":"属性名"
}] |
| modelInstanceId | 21 | string | 是 | - |
| funId | 3 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 自定义属性_删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-27 15:40:25

> 更新时间: 2023-06-27 15:42:18

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/deleteCustomProperty

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| funId | 7 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 自定义服务_新建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-27 15:43:49

> 更新时间: 2023-07-12 15:52:58

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/createCustomService

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| funName | 测试96 | string | 是 | - |
| funKey | test96 | string | 是 | - |
| cond | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"service":"service1",	"value":"{\"param1\":60}",	"assoc":"and"}] | string | 是 | 条件:示例: [{
	"productKey":"iy4uJzbjy1H",
	"deviceName":"74EAwv4afnc5gpi7WCke",
	"service":"服务标识",
	"value":"参数值",
	"assoc":"and"
}] |
| action | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"type":"invokeService",	"functionKey":"service2",	"value":"{\"param1\":88}"}] | string | 是 | 动作:示例: [{
	"productKey":"iy4uJzbjy1H",
	"deviceName":"ae4Q0SXMROCwA3FPTWzt",
	"type":"invokeService"
	"functionKey":"服务标识",
	"value":"参数值"
}] |
| modelInstanceId | 21 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 自定义服务_修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-28 11:30:19

> 更新时间: 2023-06-28 11:32:13

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/updateCustomService

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| funName | 测试96 | string | 是 | - |
| funKey | test96 | string | 是 | - |
| cond | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"service":"service1",	"value":"{\"param1\":60}",	"assoc":"and"}] | string | 是 | 条件:示例: [{
	"productKey":"iy4uJzbjy1H",
	"deviceName":"74EAwv4afnc5gpi7WCke",
	"service":"服务名",
	"value":"参数值",
	"assoc":"and"
}] |
| action | [{	"productKey":"iy4uJzbjy1H",	"deviceName":"ae4Q0SXMROCwA3FPTWzt",	"type":"invokeService",	"functionKey":"service2",	"value":"{\"param1\":88}"}] | string | 是 | 动作:示例: [{
	"productKey":"iy4uJzbjy1H",
	"deviceName":"ae4Q0SXMROCwA3FPTWzt",
	"type":"invokeService"
	"functionKey":"服务标识",
	"value":"参数值"
}] |
| modelInstanceId | 21 | string | 是 | - |
| funId | 9 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 自定义服务_删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-28 11:31:56

> 更新时间: 2023-06-28 11:39:35

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/deleteCustomService

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| funId | 10 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 开放接口

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-07-31 10:36:33

> 更新时间: 2023-08-23 08:58:11

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## http协议接入

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-10-26 14:33:42

> 更新时间: 2023-10-30 10:43:56

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 获取token

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-07-28 10:25:28

> 更新时间: 2023-11-06 16:09:16

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/broker/auth

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| username | iy4uY75WdQj.10ZWOUWTkriFKa5bFGqL | Text | 是 | 用户名: productKey.devicename |
| password | - | string | 是 | 签名算法: md5(productKey+"."+deviceName+"."+deviceSecret) |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": {
		"token": "9e08fd1db03546d2b2375615e483ca5e"
	},
	"errCode": null,
	"requestId": "331eceac1f7545a78ac187717ebef68a",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.token | 9e08fd1db03546d2b2375615e483ca5e | string | - |
| errCode | null | null | - |
| requestId | 331eceac1f7545a78ac187717ebef68a | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 推送数据

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-07-31 10:24:11

> 更新时间: 2024-05-29 09:54:58

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> iot.iuvtech.com:8080/post

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | 470a94f4-9fae-4210-8cb0-7deaf5cb395f | string | 是 | {{token}} |
| topic | /sys/iy4uY75WdQj/10ZWOUWTkriFKa5bFGqL/thing/event/property/post | Text | 是 | 设备全局id |
| payload | {  "id": 123,  "version": "1.0",  "sys":{    "ack":0  },  "params": {    "p1": 922,    "temperature": {      "value": 31    }  },  "method": "thing.event.property.post"} | Text | 是 | 服务标识符 |

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
{
	"data": null,
	"errCode": null,
	"requestId": "2a0f3090da5a4ab2a5e9dbbeff76cf18",
	"status": "S",
	"sysMsg": "操作完成"
}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 其他

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-21 16:18:15

> 更新时间: 2023-07-03 15:15:06

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 管理

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-21 15:34:00

> 更新时间: 2024-09-26 11:57:19

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 学校列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-09-26 13:57:33

> 更新时间: 2025-10-30 17:17:16

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/admin/listSearchSchool

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| size | 10 | string | 是 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 用户列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-09-26 14:44:13

> 更新时间: 2025-11-03 09:49:04

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/admin/listSearchTeacher

**请求方式**

> POST

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| page | 0 | string | 是 | - |
| size | 20 | string | 是 | 每页元素个数 |
| schoolId | 1 | string | 是 | - |
| userName | 36 | string | 是 | - |

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| schoolName | a3 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 复制沙盘相关实例

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-11 16:37:29

> 更新时间: 2025-12-04 14:48:34

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host2}}/task/initSandboxProject

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| fromProject | 165 | string | 是 | - |
| toUserName | CQSX_teacher01 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 学校创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-09-26 14:04:19

> 更新时间: 2025-10-30 15:00:05

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/admin/createSchool

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| schoolName | 重庆三峡学院 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 创建学校管理员

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-09-26 14:08:57

> 更新时间: 2024-10-14 14:54:20

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/admin/createSchoolAdmin

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| userName | CCZY_teacher02 | string | 是 | 示例: CQGC_teacher01 |
| password | 4d2cb092 | string | 是 | 密码 |
| schoolName | 长春职业技术学院 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 批量创建学生

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-09-26 15:01:25

> 更新时间: 2025-03-14 11:24:34

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/admin/createStudents

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| prefix | CCZY_Student | string | 是 | - |
| start | 3 | string | 是 | 密码 |
| end | 4 | string | 是 | - |
| schoolName | 长春职业技术学院 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 调试

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-22 16:03:31

> 更新时间: 2023-03-21 15:34:08

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 打印字符串

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-22 16:06:56

> 更新时间: 2023-03-08 13:44:26

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/env

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 更新

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-22 16:21:35

> 更新时间: 2022-06-22 16:21:35

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/other/update

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 测试接口

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-06 15:06:23

> 更新时间: 2023-05-09 11:40:27

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/other/test

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 钉钉告警

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-08-18 16:44:13

> 更新时间: 2022-08-18 16:51:07

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> https://oapi.dingtalk.com/robot/send?access_token=3e4d3b2a51f8006c891a5f34a568c2131914fd350c2527e82ce2e4ebcb5cb02a&timestamp=1660812056505&sign=0bBy7%2F2RtSTTr4vQDN57s45LT7ObH7v9qHzqizYEBOw%3D

**请求方式**

> POST

**Content-Type**

> json

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | Text | 是 | - |

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| access_token | 3e4d3b2a51f8006c891a5f34a568c2131914fd350c2527e82ce2e4ebcb5cb02a | Text | 是 | - |
| timestamp | 1660812056505 | Text | 是 | - |
| sign | 0bBy7/2RtSTTr4vQDN57s45LT7ObH7v9qHzqizYEBOw= | Text | 是 | - |

**请求Body参数**

```javascript
{
	"msgtype": "text",
	"text": {
		"content": "花都发送卫栖梧", 
	}
}
```

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Content-Type | application/json | Text | 是 | - |

**Query**

### 测试消费组topic限制

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-22 10:41:32

> 更新时间: 2023-03-22 10:42:24

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/other/testConsumerLimit

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 测试消费组产品订阅限制

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-22 13:52:18

> 更新时间: 2023-03-22 13:53:32

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/other/testSubscribeLimit

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 测试jpa删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-05 17:31:49

> 更新时间: 2023-05-06 11:36:52

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/test/testJpaDelete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 1 | string | 是 | - |
| val | 2 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 测试jpa实体

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-09 11:40:25

> 更新时间: 2023-10-19 13:39:07

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/test/testJpaEntity

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 测试testObjectToMap

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-12 16:09:57

> 更新时间: 2023-05-24 14:24:49

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/test/testObjectToMap

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 测试testJpaCond

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-16 17:20:52

> 更新时间: 2023-05-16 17:23:48

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/test/testJpaCond

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 测试错误日志

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-17 14:26:01

> 更新时间: 2023-07-25 10:22:47

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/test/testErrorLog

**请求方式**

> POST

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 钉钉告警2

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-02 11:43:36

> 更新时间: 2023-06-06 11:06:14

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> https://oapi.dingtalk.com/robot/send?access_token=bb6786d9738c5d266e13d985f722e0841275497acdedf0782f1a7cef74cb948e

**请求方式**

> POST

**Content-Type**

> json

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| access_token | bb6786d9738c5d266e13d985f722e0841275497acdedf0782f1a7cef74cb948e | string | 是 | - |

**请求Body参数**

```javascript
{
	"msgtype": "text",
	"text": {
		"content": "服务状态: 大发大", 
	}
}
```

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 测试更新

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-07-28 10:46:23

> 更新时间: 2023-07-28 10:46:23

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/test/testUpdate

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* (404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 实例数据接口

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-19 10:34:25

> 更新时间: 2024-07-19 10:35:23

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/test/exampleData

**请求方式**

> POST

**Content-Type**

> none

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 废弃

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-22 16:03:44

> 更新时间: 2023-06-25 15:06:20

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 设备模型

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-13 17:58:27

> 更新时间: 2023-06-13 17:58:27

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

#### 集成模型_模型详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-05 15:52:10

> 更新时间: 2023-06-06 15:43:34

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/getModelDetail?modelId=12

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| modelId | 12 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"data": {
		"modelId": 12,
		"modelName": "模型名称45",
		"relationProduct": "h7s72qjeGaM=test2,h7s7RpbNFrL=testx3",
		"deviceCnt": null,
		"createTime": "2023-06-05 16:07:08",
		"updateTime": "2023-06-05 16:07:08",
		"status": null,
		"modelBelong": 0,
		"description": "描述45",
		"userId": 26,
		"thingModelList": [
			{
				"thingModel": "{\"schema\":\"https://iotx-tsl.oss-ap-southeast-1.aliyuncs.com/schema.json\",\"profile\":{\"version\":\"1.5\",\"productKey\":\"h7s72qjeGaM\"},\"properties\":[{\"identifier\":\"Temperature\",\"name\":\"温度\",\"accessMode\":\"rw\",\"desc\":\"温度\",\"required\":false,\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"0.1\"}}},{\"identifier\":\"Humidity\",\"name\":\"湿度\",\"accessMode\":\"rw\",\"desc\":\"湿度\",\"required\":false,\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%RH\",\"unitName\":\"相对湿度\",\"step\":\"0.1\"}}},{\"identifier\":\"PowerLed\",\"name\":\"power_LED\",\"accessMode\":\"rw\",\"required\":false,\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"关2323\",\"1\":\"开\"}}},{\"name\":\"开关\",\"identifier\":\"switch\",\"required\":false,\"accessMode\":\"rw\",\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"关\",\"1\":\"开\"}}},{\"name\":\"test2\",\"identifier\":\"test2\",\"required\":false,\"accessMode\":\"rw\",\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"step\":\"1\",\"unitName\":\"个\",\"unit\":\"pcs\"}}}],\"events\":[{\"identifier\":\"post\",\"name\":\"post\",\"type\":\"info\",\"required\":true,\"desc\":\"属性上报\",\"method\":\"thing.event.property.post\",\"outputData\":[{\"identifier\":\"cpu_usage\",\"name\":\"CPU使用率\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%\",\"unitName\":\"百分比\",\"step\":\"0.1\"}}},{\"identifier\":\"Temperature\",\"name\":\"温度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"0.1\"}}},{\"identifier\":\"Humidity\",\"name\":\"湿度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%RH\",\"unitName\":\"相对湿度\",\"step\":\"0.1\"}}},{\"identifier\":\"DISK_used_percentage\",\"name\":\"磁盘空间\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%\",\"unitName\":\"百分比\",\"step\":\"0.1\"}}},{\"identifier\":\"cpu_temperature\",\"name\":\"cpu温度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"-1.4E-45\",\"max\":\"3.4028235E38\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"0.1\"}}},{\"identifier\":\"other\",\"name\":\"其他\",\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"200\",\"step\":\"1\"}}},{\"identifier\":\"other3\",\"name\":\"other3\",\"dataType\":{\"type\":\"double\",\"specs\":{\"min\":\"16\",\"max\":\"55\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"1\"}}},{\"identifier\":\"jiaodu\",\"name\":\"角度\",\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"180\",\"step\":\"1\"}}},{\"identifier\":\"PowerLed\",\"name\":\"power_LED\",\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"关2323\",\"1\":\"开\"}}},{\"identifier\":\"DH11status\",\"name\":\"温度计运行状态\",\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"异dsadas\",\"1\":\"正常\"}}},{\"identifier\":\"ChildLockSwitch2\",\"name\":\"童锁开关2\",\"dataType\":{\"type\":\"enum\",\"specs\":{\"1\":\"232\",\"2\":\"123\",\"3\":\"333\"}}},{\"identifier\":\"tempSpace\",\"name\":\"临时文件空间\",\"dataType\":{\"type\":\"text\",\"specs\":{\"length\":\"10240\"}}},{\"identifier\":\"mytime\",\"name\":\"时间\",\"dataType\":{\"type\":\"date\",\"specs\":{}}}]},{\"identifier\":\"TemperatureSensorExceptional\",\"name\":\"环境温度传感器异常2\",\"type\":\"error\",\"required\":false,\"method\":\"thing.event.TemperatureSensorExceptional.post\",\"outputData\":[{\"identifier\":\"Error\",\"name\":\"环境温度传感器异常\",\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"正常\",\"1\":\"环境温度传感器异常\"}}}]}],\"services\":[{\"identifier\":\"set\",\"name\":\"set\",\"required\":true,\"callType\":\"async\",\"desc\":\"属性设置\",\"method\":\"thing.service.property.set\",\"inputData\":[{\"identifier\":\"cpu_usage\",\"name\":\"CPU使用率\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%\",\"unitName\":\"百分比\",\"step\":\"0.1\"}}},{\"identifier\":\"Temperature\",\"name\":\"温度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"0.1\"}}},{\"identifier\":\"Humidity\",\"name\":\"湿度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%RH\",\"unitName\":\"相对湿度\",\"step\":\"0.1\"}}},{\"identifier\":\"DISK_used_percentage\",\"name\":\"磁盘空间\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%\",\"unitName\":\"百分比\",\"step\":\"0.1\"}}},{\"identifier\":\"cpu_temperature\",\"name\":\"cpu温度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"-1.4E-45\",\"max\":\"3.4028235E38\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"0.1\"}}},{\"identifier\":\"other\",\"name\":\"其他\",\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"200\",\"step\":\"1\"}}},{\"identifier\":\"other3\",\"name\":\"other3\",\"dataType\":{\"type\":\"double\",\"specs\":{\"min\":\"16\",\"max\":\"55\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"1\"}}},{\"identifier\":\"jiaodu\",\"name\":\"角度\",\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"180\",\"step\":\"1\"}}},{\"identifier\":\"PowerLed\",\"name\":\"power_LED\",\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"关2323\",\"1\":\"开\"}}},{\"identifier\":\"DH11status\",\"name\":\"温度计运行状态\",\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"异dsadas\",\"1\":\"正常\"}}},{\"identifier\":\"ChildLockSwitch2\",\"name\":\"童锁开关2\",\"dataType\":{\"type\":\"enum\",\"specs\":{\"1\":\"232\",\"2\":\"123\",\"3\":\"333\"}}},{\"identifier\":\"tempSpace\",\"name\":\"临时文件空间\",\"dataType\":{\"type\":\"text\",\"specs\":{\"length\":\"10240\"}}},{\"identifier\":\"mytime\",\"name\":\"时间\",\"dataType\":{\"type\":\"date\",\"specs\":{}}}],\"outputData\":[]},{\"identifier\":\"get\",\"name\":\"get\",\"required\":true,\"callType\":\"async\",\"desc\":\"属性获取\",\"method\":\"thing.service.property.get\",\"inputData\":[\"cpu_usage\",\"Temperature\",\"Humidity\",\"DISK_used_percentage\",\"cpu_temperature\",\"other\",\"other3\",\"jiaodu\",\"PowerLed\",\"DH11status\",\"ChildLockSwitch2\",\"tempSpace\",\"mytime\"],\"outputData\":[{\"identifier\":\"cpu_usage\",\"name\":\"CPU使用率\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%\",\"unitName\":\"百分比\",\"step\":\"0.1\"}}},{\"identifier\":\"Temperature\",\"name\":\"温度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"0.1\"}}},{\"identifier\":\"Humidity\",\"name\":\"湿度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%RH\",\"unitName\":\"相对湿度\",\"step\":\"0.1\"}}},{\"identifier\":\"DISK_used_percentage\",\"name\":\"磁盘空间\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"0\",\"max\":\"100\",\"unit\":\"%\",\"unitName\":\"百分比\",\"step\":\"0.1\"}}},{\"identifier\":\"cpu_temperature\",\"name\":\"cpu温度\",\"dataType\":{\"type\":\"float\",\"specs\":{\"min\":\"-1.4E-45\",\"max\":\"3.4028235E38\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"0.1\"}}},{\"identifier\":\"other\",\"name\":\"其他\",\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"200\",\"step\":\"1\"}}},{\"identifier\":\"other3\",\"name\":\"other3\",\"dataType\":{\"type\":\"double\",\"specs\":{\"min\":\"16\",\"max\":\"55\",\"unit\":\"°C\",\"unitName\":\"摄氏度\",\"step\":\"1\"}}},{\"identifier\":\"jiaodu\",\"name\":\"角度\",\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"0\",\"max\":\"180\",\"step\":\"1\"}}},{\"identifier\":\"PowerLed\",\"name\":\"power_LED\",\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"关2323\",\"1\":\"开\"}}},{\"identifier\":\"DH11status\",\"name\":\"温度计运行状态\",\"dataType\":{\"type\":\"bool\",\"specs\":{\"0\":\"异dsadas\",\"1\":\"正常\"}}},{\"identifier\":\"ChildLockSwitch2\",\"name\":\"童锁开关2\",\"dataType\":{\"type\":\"enum\",\"specs\":{\"1\":\"232\",\"2\":\"123\",\"3\":\"333\"}}},{\"identifier\":\"tempSpace\",\"name\":\"临时文件空间\",\"dataType\":{\"type\":\"text\",\"specs\":{\"length\":\"10240\"}}},{\"identifier\":\"mytime\",\"name\":\"时间\",\"dataType\":{\"type\":\"date\",\"specs\":{}}}]},{\"identifier\":\"clear\",\"name\":\"清理垃圾\",\"required\":false,\"callType\":\"async\",\"desc\":\"12321\",\"method\":\"thing.service.clear\",\"inputData\":[{\"identifier\":\"type\",\"name\":\"类型\",\"dataType\":{\"type\":\"text\",\"specs\":{\"length\":\"50\"}}}],\"outputData\":[]},{\"identifier\":\"switchbling\",\"name\":\"调整灯开关\",\"required\":false,\"callType\":\"async\",\"method\":\"thing.service.switchbling\",\"inputData\":[{\"identifier\":\"switch\",\"name\":\"调整颜色\",\"dataType\":{\"type\":\"text\",\"specs\":{\"length\":\"10240\"}}}],\"outputData\":[]},{\"identifier\":\"clear123\",\"name\":\"清理垃圾\",\"required\":false,\"callType\":\"sync\",\"desc\":\"12321\",\"method\":\"thing.service.clear123\",\"inputData\":[{\"identifier\":\"type\",\"name\":\"类型\",\"dataType\":{\"type\":\"text\",\"specs\":{\"length\":\"50\"}}}],\"outputData\":[]},{\"identifier\":\"fun2\",\"name\":\"功能2\",\"required\":false,\"callType\":\"async\",\"method\":\"thing.service.fun2\",\"inputData\":[{\"identifier\":\"a\",\"name\":\"a\",\"dataType\":{\"type\":\"int\",\"specs\":{\"min\":\"1\",\"max\":\"100\",\"step\":\"1\"}}}],\"outputData\":[{\"identifier\":\"b\",\"name\":\"b\",\"dataType\":{\"type\":\"date\",\"specs\":{}}}]},{\"name\":\"test\",\"identifier\":\"test\",\"callType\":\"sync\",\"accessMode\":\"rw\",\"method\":\"thing.service.test\",\"required\":false,\"inputData\":[{\"name\":\"a\",\"identifier\":\"a\",\"required\":false,\"dataType\":{\"type\":\"date\",\"specs\":{}}}],\"outputData\":[{\"name\":\"v\",\"identifier\":\"v\",\"required\":false,\"dataType\":{\"type\":\"text\",\"specs\":{\"length\":\"10\"}}}]}],\"functionBlocks\":[{\"functionBlockId\":\"add\",\"functionBlockName\":\"add\",\"gmtCreated\":1666669166493,\"productKey\":\"h7s72qjeGaM\"},{\"functionBlockId\":\"add2\",\"functionBlockName\":\"add2\",\"gmtCreated\":1666677006065,\"productKey\":\"h7s72qjeGaM\"}]}",
				"productKey": "h7s72qjeGaM",
				"productName": "test2"
			}
		]
	},
	"test": "bbb",
	"errCode": null,
	"requestId": "76a66e9afed74d29a611f387942a8cd9",
	"status": "S",
	"sysMsg": "操作完成"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | - |
| data.modelId | 12 | integer | - |
| data.modelName | 模型名称45 | string | - |
| data.relationProduct | h7s72qjeGaM=test2,h7s7RpbNFrL=testx3 | string | 关联设备模型格式: productkey=模型名 多个模型逗号分割 |
| data.deviceCnt | null | null | 设备数 |
| data.createTime | 2023-06-05 16:07:08 | string | 创建时间 |
| data.updateTime | 2023-06-05 16:07:08 | string | 更新时间 |
| data.status | null | null | 状态 |
| data.modelBelong | 0 | integer | 模型归属:0=租户通用,x=私有群组id |
| data.description | 描述45 | string | 描述 |
| data.userId | 26 | integer | 用户id |
| data.thingModelList | - | array | 物模型列表 |
| data.thingModelList.thingModel | {"schema":"https://iotx-tsl.oss-ap-southeast-1.aliyuncs.com/schema.json","profile":{"version":"1.5","productKey":"h7s72qjeGaM"},"properties":[{"identifier":"Temperature","name":"温度","accessMode":"rw","desc":"温度","required":false,"dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"°C","unitName":"摄氏度","step":"0.1"}}},{"identifier":"Humidity","name":"湿度","accessMode":"rw","desc":"湿度","required":false,"dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%RH","unitName":"相对湿度","step":"0.1"}}},{"identifier":"PowerLed","name":"power_LED","accessMode":"rw","required":false,"dataType":{"type":"bool","specs":{"0":"关2323","1":"开"}}},{"name":"开关","identifier":"switch","required":false,"accessMode":"rw","dataType":{"type":"bool","specs":{"0":"关","1":"开"}}},{"name":"test2","identifier":"test2","required":false,"accessMode":"rw","dataType":{"type":"int","specs":{"min":"0","max":"100","step":"1","unitName":"个","unit":"pcs"}}}],"events":[{"identifier":"post","name":"post","type":"info","required":true,"desc":"属性上报","method":"thing.event.property.post","outputData":[{"identifier":"cpu_usage","name":"CPU使用率","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%","unitName":"百分比","step":"0.1"}}},{"identifier":"Temperature","name":"温度","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"°C","unitName":"摄氏度","step":"0.1"}}},{"identifier":"Humidity","name":"湿度","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%RH","unitName":"相对湿度","step":"0.1"}}},{"identifier":"DISK_used_percentage","name":"磁盘空间","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%","unitName":"百分比","step":"0.1"}}},{"identifier":"cpu_temperature","name":"cpu温度","dataType":{"type":"float","specs":{"min":"-1.4E-45","max":"3.4028235E38","unit":"°C","unitName":"摄氏度","step":"0.1"}}},{"identifier":"other","name":"其他","dataType":{"type":"int","specs":{"min":"0","max":"200","step":"1"}}},{"identifier":"other3","name":"other3","dataType":{"type":"double","specs":{"min":"16","max":"55","unit":"°C","unitName":"摄氏度","step":"1"}}},{"identifier":"jiaodu","name":"角度","dataType":{"type":"int","specs":{"min":"0","max":"180","step":"1"}}},{"identifier":"PowerLed","name":"power_LED","dataType":{"type":"bool","specs":{"0":"关2323","1":"开"}}},{"identifier":"DH11status","name":"温度计运行状态","dataType":{"type":"bool","specs":{"0":"异dsadas","1":"正常"}}},{"identifier":"ChildLockSwitch2","name":"童锁开关2","dataType":{"type":"enum","specs":{"1":"232","2":"123","3":"333"}}},{"identifier":"tempSpace","name":"临时文件空间","dataType":{"type":"text","specs":{"length":"10240"}}},{"identifier":"mytime","name":"时间","dataType":{"type":"date","specs":{}}}]},{"identifier":"TemperatureSensorExceptional","name":"环境温度传感器异常2","type":"error","required":false,"method":"thing.event.TemperatureSensorExceptional.post","outputData":[{"identifier":"Error","name":"环境温度传感器异常","dataType":{"type":"bool","specs":{"0":"正常","1":"环境温度传感器异常"}}}]}],"services":[{"identifier":"set","name":"set","required":true,"callType":"async","desc":"属性设置","method":"thing.service.property.set","inputData":[{"identifier":"cpu_usage","name":"CPU使用率","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%","unitName":"百分比","step":"0.1"}}},{"identifier":"Temperature","name":"温度","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"°C","unitName":"摄氏度","step":"0.1"}}},{"identifier":"Humidity","name":"湿度","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%RH","unitName":"相对湿度","step":"0.1"}}},{"identifier":"DISK_used_percentage","name":"磁盘空间","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%","unitName":"百分比","step":"0.1"}}},{"identifier":"cpu_temperature","name":"cpu温度","dataType":{"type":"float","specs":{"min":"-1.4E-45","max":"3.4028235E38","unit":"°C","unitName":"摄氏度","step":"0.1"}}},{"identifier":"other","name":"其他","dataType":{"type":"int","specs":{"min":"0","max":"200","step":"1"}}},{"identifier":"other3","name":"other3","dataType":{"type":"double","specs":{"min":"16","max":"55","unit":"°C","unitName":"摄氏度","step":"1"}}},{"identifier":"jiaodu","name":"角度","dataType":{"type":"int","specs":{"min":"0","max":"180","step":"1"}}},{"identifier":"PowerLed","name":"power_LED","dataType":{"type":"bool","specs":{"0":"关2323","1":"开"}}},{"identifier":"DH11status","name":"温度计运行状态","dataType":{"type":"bool","specs":{"0":"异dsadas","1":"正常"}}},{"identifier":"ChildLockSwitch2","name":"童锁开关2","dataType":{"type":"enum","specs":{"1":"232","2":"123","3":"333"}}},{"identifier":"tempSpace","name":"临时文件空间","dataType":{"type":"text","specs":{"length":"10240"}}},{"identifier":"mytime","name":"时间","dataType":{"type":"date","specs":{}}}],"outputData":[]},{"identifier":"get","name":"get","required":true,"callType":"async","desc":"属性获取","method":"thing.service.property.get","inputData":["cpu_usage","Temperature","Humidity","DISK_used_percentage","cpu_temperature","other","other3","jiaodu","PowerLed","DH11status","ChildLockSwitch2","tempSpace","mytime"],"outputData":[{"identifier":"cpu_usage","name":"CPU使用率","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%","unitName":"百分比","step":"0.1"}}},{"identifier":"Temperature","name":"温度","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"°C","unitName":"摄氏度","step":"0.1"}}},{"identifier":"Humidity","name":"湿度","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%RH","unitName":"相对湿度","step":"0.1"}}},{"identifier":"DISK_used_percentage","name":"磁盘空间","dataType":{"type":"float","specs":{"min":"0","max":"100","unit":"%","unitName":"百分比","step":"0.1"}}},{"identifier":"cpu_temperature","name":"cpu温度","dataType":{"type":"float","specs":{"min":"-1.4E-45","max":"3.4028235E38","unit":"°C","unitName":"摄氏度","step":"0.1"}}},{"identifier":"other","name":"其他","dataType":{"type":"int","specs":{"min":"0","max":"200","step":"1"}}},{"identifier":"other3","name":"other3","dataType":{"type":"double","specs":{"min":"16","max":"55","unit":"°C","unitName":"摄氏度","step":"1"}}},{"identifier":"jiaodu","name":"角度","dataType":{"type":"int","specs":{"min":"0","max":"180","step":"1"}}},{"identifier":"PowerLed","name":"power_LED","dataType":{"type":"bool","specs":{"0":"关2323","1":"开"}}},{"identifier":"DH11status","name":"温度计运行状态","dataType":{"type":"bool","specs":{"0":"异dsadas","1":"正常"}}},{"identifier":"ChildLockSwitch2","name":"童锁开关2","dataType":{"type":"enum","specs":{"1":"232","2":"123","3":"333"}}},{"identifier":"tempSpace","name":"临时文件空间","dataType":{"type":"text","specs":{"length":"10240"}}},{"identifier":"mytime","name":"时间","dataType":{"type":"date","specs":{}}}]},{"identifier":"clear","name":"清理垃圾","required":false,"callType":"async","desc":"12321","method":"thing.service.clear","inputData":[{"identifier":"type","name":"类型","dataType":{"type":"text","specs":{"length":"50"}}}],"outputData":[]},{"identifier":"switchbling","name":"调整灯开关","required":false,"callType":"async","method":"thing.service.switchbling","inputData":[{"identifier":"switch","name":"调整颜色","dataType":{"type":"text","specs":{"length":"10240"}}}],"outputData":[]},{"identifier":"clear123","name":"清理垃圾","required":false,"callType":"sync","desc":"12321","method":"thing.service.clear123","inputData":[{"identifier":"type","name":"类型","dataType":{"type":"text","specs":{"length":"50"}}}],"outputData":[]},{"identifier":"fun2","name":"功能2","required":false,"callType":"async","method":"thing.service.fun2","inputData":[{"identifier":"a","name":"a","dataType":{"type":"int","specs":{"min":"1","max":"100","step":"1"}}}],"outputData":[{"identifier":"b","name":"b","dataType":{"type":"date","specs":{}}}]},{"name":"test","identifier":"test","callType":"sync","accessMode":"rw","method":"thing.service.test","required":false,"inputData":[{"name":"a","identifier":"a","required":false,"dataType":{"type":"date","specs":{}}}],"outputData":[{"name":"v","identifier":"v","required":false,"dataType":{"type":"text","specs":{"length":"10"}}}]}],"functionBlocks":[{"functionBlockId":"add","functionBlockName":"add","gmtCreated":1666669166493,"productKey":"h7s72qjeGaM"},{"functionBlockId":"add2","functionBlockName":"add2","gmtCreated":1666677006065,"productKey":"h7s72qjeGaM"}]} | string | 物模型 |
| data.thingModelList.productKey | h7s72qjeGaM | string | 产品key |
| data.thingModelList.productName | test2 | string | 产品名(阿里云平台) |
| test | bbb | string | - |
| errCode | null | null | - |
| requestId | 76a66e9afed74d29a611f387942a8cd9 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作完成 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

#### 模型_简单列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-06 11:05:18

> 更新时间: 2023-06-14 14:14:13

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/getSimpleModels?projectId=108

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 108 | string | 是 | 工程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

#### 集成模型_创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-05 14:53:28

> 更新时间: 2023-06-06 15:05:11

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/createModel

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| integraModelName | 模型名称59 | string | 否 | 模型名称 |
| linkDevModel | [{"productKey":"h7s72qjeGaM","productNameNote":"test2",}] | string | 否 | 关联设备模型格式: productkey=模型名 多个模型逗号分割 |
| integraModelAuth | 1 | number | 否 | 模型归属:1=租户通用,2=工程私有 |
| description | 描述96 | string | 否 | 描述 |
| projectId | 108 | string | 是 | 工程id |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

#### 集成模型_修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-05 15:47:21

> 更新时间: 2023-06-06 15:25:49

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/updateModel

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| integraModelName | 模型名称96 | string | 否 | 模型名称 |
| description | 描述96 | string | 否 | 描述 |
| modelId | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

#### 集成模型_发布

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-06 17:05:07

> 更新时间: 2023-06-06 17:07:09

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/publishModel

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| modelId | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

#### 集成模型_删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-05 15:41:41

> 更新时间: 2023-06-05 15:46:57

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/deleteModel

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| modelId | 8 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

#### 集成模型_列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-06-05 15:50:55

> 更新时间: 2023-06-06 15:33:41

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotIntegrate/getModels?integraModelName=9&projectId=108&page=&size=

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| integraModelName | 9 | string | 否 | 模型名称 |
| projectId | 108 | string | 是 | 工程id |
| page | - | string | 否 | - |
| size | - | string | 否 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 获取访问者id(session替代方案)

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-12-19 14:29:27

> 更新时间: 2023-01-04 10:56:25

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/getUUid

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

### 鉴权_获取时间戳

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-16 10:24:23

> 更新时间: 2022-09-16 10:28:26

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDeviceAuth/getTimestamp

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**Query**

### 加入升级队列

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-07-26 10:13:31

> 更新时间: 2022-08-01 10:28:16

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotOTA/addQueue

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| fileId | 10 | Text | 是 | - |
| devices | h7s72qjeGaM\|test2_1,h7s7NxjuhLw\|test_1 | string | 是 | 设备列表, 格式: 产品1\|设备1,产品2\|设备3 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"data": {
		"groupId": 4,
		"groupDesc": null,
		"groupName": "OTA_8_0_fQP",
		"userId": 0,
		"fileId": 8,
		"superGroupId": null,
		"groupDevices": "h7s72qjeGaM|test2_1,h7s72qjeGaM|test2_2,h7s7NxjuhLw|test_1",
		"iotGroupId": "Q877zfWGASmj273GGiTA010200"
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.groupId | 4 | number | 分组id, 创建升级任务会使用 |
| data.groupDesc | - | object | - |
| data.groupName | OTA_8_0_fQP | string | - |
| data.userId | 0 | number | 用户id |
| data.fileId | 8 | number | 文件id |
| data.superGroupId | - | object | - |
| data.groupDevices | h7s72qjeGaM\|test2_1,h7s72qjeGaM\|test2_2,h7s7NxjuhLw\|test_1 | string | - |
| data.iotGroupId | Q877zfWGASmj273GGiTA010200 | string | - |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 获取品类物模型

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-22 15:17:28

> 更新时间: 2022-06-22 15:44:58

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/getStdThingModel?categoryKey=Lighting

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| categoryKey | Lighting | Text | 是 | 设备模型识别码 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 物模型功能_列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-17 15:45:01

> 更新时间: 2022-06-21 17:00:13

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/listThingFun?productKey=iy4uY75WdQj

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"data": [
		{
			"funId": 3,
			"productKey": "h7s7PwecpHX",
			"funType": 0,
			"funName": "属性名",
			"funKey": "属性标识",
			"funDetail": "{\n\"name\": \"属性名\",\n\"key\": \"属性标识\",\n\"dataType\": \"数据类型\",\n\"permission\": \"操作权限\",\n\"min\": \"最小值\",\n\"max\": \"最大值\",\n\"step\": \"步长\",\n\"unit\": \"单位\"\n}",
			"updateTime": "2022-06-17 07:45:54"
		},
		{
			"funId": 4,
			"productKey": "h7s7PwecpHX",
			"funType": 0,
			"funName": "属性名22",
			"funKey": "属性标识22",
			"funDetail": "{\"name\":\"属性名22\",\"key\":\"属性标识22\",\"dataType\":\"数据类型\",\"permission\":\"操作权限\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":\"单位\"}",
			"updateTime": "2022-06-17 07:58:29"
		},
		{
			"funId": 5,
			"productKey": "h7s7PwecpHX",
			"funType": 0,
			"funName": "属性名2233",
			"funKey": "属性标识2233",
			"funDetail": "{\"name\":\"属性名2233\",\"key\":\"属性标识2233\",\"dataType\":\"数据类型\",\"permission\":\"操作权限\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":null}",
			"updateTime": "2022-06-17 08:01:13"
		},
		{
			"funId": 6,
			"productKey": "h7s7PwecpHX",
			"funType": 0,
			"funName": "属性名223312",
			"funKey": "属性标识223332",
			"funDetail": "{\"name\":\"属性名223312\",\"key\":\"属性标识223332\",\"dataType\":\"数据类型\",\"permission\":\"操作权限\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":\"单位\"}",
			"updateTime": "2022-06-17 08:07:52"
		},
		{
			"funId": 7,
			"productKey": "h7s7PwecpHX",
			"funType": 1,
			"funName": "服务名",
			"funKey": "服务标识",
			"funDetail": "{\"name\":\"服务名\",\"key\":\"服务标识\",\"invokeType\":\"调用类型\",\"inputParam\":[{\"name\":\"属性名\",\"key\":\"属性标识\",\"dataType\":\"数据类型\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":\"单位\"},{\"name\":\"属性名\",\"key\":\"属性标识\",\"dataType\":\"数据类型\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":\"单位\"}],\"outputParam\":[{\"name\":\"属性名\",\"key\":\"属性标识\",\"dataType\":\"数据类型\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":\"单位\"}]}",
			"updateTime": "2022-06-17 08:11:25"
		},
		{
			"funId": 8,
			"productKey": "h7s7PwecpHX",
			"funType": 1,
			"funName": "服务名2",
			"funKey": "服务标识2",
			"funDetail": "{\"name\":\"服务名2\",\"key\":\"服务标识2\",\"invokeType\":\"调用类型\",\"inputParam\":[{\"name\":\"属性名\",\"key\":\"参数名\",\"dataType\":\"数据类型\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":\"单位\"},{\"name\":\"属性名\",\"key\":\"属性标识\",\"dataType\":\"数据类型\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":\"单位\"}],\"outputParam\":[{\"name\":\"属性名\",\"key\":\"属性标识\",\"dataType\":\"数据类型\",\"min\":\"最小值\",\"max\":\"最大值\",\"step\":\"步长\",\"unit\":\"单位\"}]}",
			"updateTime": "2022-06-20 07:15:57"
		}
	],
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.funId | 3 | number | 功能id |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.funType | 0 | number | 功能类型:0=属性,1=服务,2=事件 |
| data.funName | 属性名 | string | 功能名称 |
| data.funKey | 属性标识 | string | 功能标识 |
| data.funDetail | {"name": "属性名","key": "属性标识","dataType": "数据类型","permission": "操作权限","min": "最小值","max": "最大值","step": "步长","unit": "单位"} | string | 功能详细数据 |
| data.updateTime | 2022-06-17 07:45:54 | string | 更新时间 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 物模型_创建&修改

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-06-21 16:30:00

> 更新时间: 2022-06-21 17:10:18

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotThing/saveThingModel

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | iy4uY75WdQj | Text | 是 | 产品key |
| thingModelJson | {  "events": [    {      "createTs": 1655799762332,      "custom": true,      "eventName": "内容加载完成",      "eventType": "INFO_EVENT_TYPE",      "identifier": "UpdateContentCompleteEvent",      "outputData": [        {          "custom": true,          "dataSpecs": {            "dataType": "TEXT",            "length": 128          },          "dataType": "TEXT",          "direction": "PARAM_OUTPUT",          "identifier": "UpdateTaskID",          "name": "下发任务ID",          "paraOrder": 0        },        {          "custom": true,          "dataSpecs": {            "dataType": "INT",            "max": "1024",            "min": "-1024",            "precise": 0,            "step": "1",            "unit": "",            "unitName": "无"          },          "dataType": "INT",          "direction": "PARAM_OUTPUT",          "identifier": "Status",          "name": "状态",          "paraOrder": 1        },        {          "custom": true,          "dataSpecs": {            "childDataType": "STRUCT",            "customFlag": true,            "dataSpecsList": [              {                "childDataType": "TEXT",                "childName": "内容创意ID",                "childSpecsDTO": {                  "dataType": "TEXT",                  "length": 128                },                "dataSpecs": {                  "dataType": "TEXT",                  "length": 128                },                "dataType": "STRUCT",                "identifier": "CreativeID",                "name": "失败创意列表"              },              {                "childDataType": "INT",                "childName": "错误代码",                "childSpecsDTO": {                  "dataType": "INT",                  "max": "1024",                  "min": "-1024",                  "precise": 0,                  "step": "1",                  "unit": "",                  "unitName": "无"                },                "dataSpecs": {                  "dataType": "INT",                  "max": "1024",                  "min": "-1024",                  "precise": 0,                  "step": "1",                  "unit": "",                  "unitName": "无"                },                "dataType": "STRUCT",                "identifier": "Code",                "name": "失败创意列表"              },              {                "childDataType": "TEXT",                "childName": "错误描述",                "childSpecsDTO": {                  "dataType": "TEXT",                  "length": 1024                },                "dataSpecs": {                  "dataType": "TEXT",                  "length": 1024                },                "dataType": "STRUCT",                "identifier": "Message",                "name": "失败创意列表"              }            ],            "dataType": "ARRAY",            "size": 128          },          "dataType": "ARRAY",          "direction": "PARAM_OUTPUT",          "identifier": "FailedCreativeIDs",          "name": "失败创意列表",          "paraOrder": 2        }      ],      "productKey": "h7s72qjeGaM",      "required": false    }  ],  "properties": [    {      "createTs": 1652148128115,      "custom": true,      "customFlag": true,      "dataSpecs": {        "dataType": "FLOAT",        "max": "100",        "min": "0",        "step": "0.1",        "unit": "°C",        "unitName": "摄氏度"      },      "dataType": "FLOAT",      "description": "温度",      "identifier": "Temperature",      "name": "温度",      "productKey": "h7s72qjeGaM",      "required": false,      "rwFlag": "READ_WRITE",      "std": false    },    {      "createTs": 1652148141379,      "custom": true,      "customFlag": true,      "dataSpecs": {        "dataType": "FLOAT",        "max": "100",        "min": "0",        "step": "0.1",        "unit": "%RH",        "unitName": "相对湿度"      },      "dataType": "FLOAT",      "description": "湿度",      "identifier": "Humidity",      "name": "湿度",      "productKey": "h7s72qjeGaM",      "required": false,      "rwFlag": "READ_WRITE",      "std": false    }  ],  "services": [    {      "callType": "SYNC",      "createTs": 1655799752090,      "custom": true,      "identifier": "DeleteModel",      "inputParams": [        {          "custom": true,          "dataSpecs": {            "dataType": "TEXT",            "length": 128          },          "dataType": "TEXT",          "direction": "PARAM_INPUT",          "identifier": "AlgorithmID",          "name": "算法任务唯一标识",          "paraOrder": 0        }      ],      "outputParams": [],      "productKey": "h7s72qjeGaM",      "required": false,      "serviceName": "删除模型"    }  ]} | Text | 是 | 物模型json, 详参阿里云物模型示例 |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
{
	"data": {
		"modelId": 1,
		"thingModelJson": "{\n  \"events\": [\n    {\n      \"createTs\": 1655799762332,\n      \"custom\": true,\n      \"eventName\": \"内容加载完成\",\n      \"eventType\": \"INFO_EVENT_TYPE\",\n      \"identifier\": \"UpdateContentCompleteEvent\",\n      \"outputData\": [\n        {\n          \"custom\": true,\n          \"dataSpecs\": {\n            \"dataType\": \"TEXT\",\n            \"length\": 128\n          },\n          \"dataType\": \"TEXT\",\n          \"direction\": \"PARAM_OUTPUT\",\n          \"identifier\": \"UpdateTaskID\",\n          \"name\": \"下发任务ID\",\n          \"paraOrder\": 0\n        },\n        {\n          \"custom\": true,\n          \"dataSpecs\": {\n            \"dataType\": \"INT\",\n            \"max\": \"1024\",\n            \"min\": \"-1024\",\n            \"precise\": 0,\n            \"step\": \"1\",\n            \"unit\": \"\",\n            \"unitName\": \"无\"\n          },\n          \"dataType\": \"INT\",\n          \"direction\": \"PARAM_OUTPUT\",\n          \"identifier\": \"Status\",\n          \"name\": \"状态\",\n          \"paraOrder\": 1\n        },\n        {\n          \"custom\": true,\n          \"dataSpecs\": {\n            \"childDataType\": \"STRUCT\",\n            \"customFlag\": true,\n            \"dataSpecsList\": [\n              {\n                \"childDataType\": \"TEXT\",\n                \"childName\": \"内容创意ID\",\n                \"childSpecsDTO\": {\n                  \"dataType\": \"TEXT\",\n                  \"length\": 128\n                },\n                \"dataSpecs\": {\n                  \"dataType\": \"TEXT\",\n                  \"length\": 128\n                },\n                \"dataType\": \"STRUCT\",\n                \"identifier\": \"CreativeID\",\n                \"name\": \"失败创意列表\"\n              },\n              {\n                \"childDataType\": \"INT\",\n                \"childName\": \"错误代码\",\n                \"childSpecsDTO\": {\n                  \"dataType\": \"INT\",\n                  \"max\": \"1024\",\n                  \"min\": \"-1024\",\n                  \"precise\": 0,\n                  \"step\": \"1\",\n                  \"unit\": \"\",\n                  \"unitName\": \"无\"\n                },\n                \"dataSpecs\": {\n                  \"dataType\": \"INT\",\n                  \"max\": \"1024\",\n                  \"min\": \"-1024\",\n                  \"precise\": 0,\n                  \"step\": \"1\",\n                  \"unit\": \"\",\n                  \"unitName\": \"无\"\n                },\n                \"dataType\": \"STRUCT\",\n                \"identifier\": \"Code\",\n                \"name\": \"失败创意列表\"\n              },\n              {\n                \"childDataType\": \"TEXT\",\n                \"childName\": \"错误描述\",\n                \"childSpecsDTO\": {\n                  \"dataType\": \"TEXT\",\n                  \"length\": 1024\n                },\n                \"dataSpecs\": {\n                  \"dataType\": \"TEXT\",\n                  \"length\": 1024\n                },\n                \"dataType\": \"STRUCT\",\n                \"identifier\": \"Message\",\n                \"name\": \"失败创意列表\"\n              }\n            ],\n            \"dataType\": \"ARRAY\",\n            \"size\": 128\n          },\n          \"dataType\": \"ARRAY\",\n          \"direction\": \"PARAM_OUTPUT\",\n          \"identifier\": \"FailedCreativeIDs\",\n          \"name\": \"失败创意列表\",\n          \"paraOrder\": 2\n        }\n      ],\n      \"productKey\": \"h7s72qjeGaM\",\n      \"required\": false\n    }\n  ],\n  \"properties\": [\n    {\n      \"createTs\": 1652148128115,\n      \"custom\": true,\n      \"customFlag\": true,\n      \"dataSpecs\": {\n        \"dataType\": \"FLOAT\",\n        \"max\": \"100\",\n        \"min\": \"0\",\n        \"step\": \"0.1\",\n        \"unit\": \"°C\",\n        \"unitName\": \"摄氏度\"\n      },\n      \"dataType\": \"FLOAT\",\n      \"description\": \"温度\",\n      \"identifier\": \"Temperature\",\n      \"name\": \"温度\",\n      \"productKey\": \"h7s72qjeGaM\",\n      \"required\": false,\n      \"rwFlag\": \"READ_WRITE\",\n      \"std\": false\n    },\n    {\n      \"createTs\": 1652148141379,\n      \"custom\": true,\n      \"customFlag\": true,\n      \"dataSpecs\": {\n        \"dataType\": \"FLOAT\",\n        \"max\": \"100\",\n        \"min\": \"0\",\n        \"step\": \"0.1\",\n        \"unit\": \"%RH\",\n        \"unitName\": \"相对湿度\"\n      },\n      \"dataType\": \"FLOAT\",\n      \"description\": \"湿度\",\n      \"identifier\": \"Humidity\",\n      \"name\": \"湿度\",\n      \"productKey\": \"h7s72qjeGaM\",\n      \"required\": false,\n      \"rwFlag\": \"READ_WRITE\",\n      \"std\": false\n    }\n  ],\n  \"services\": [\n    {\n      \"callType\": \"SYNC\",\n      \"createTs\": 1655799752090,\n      \"custom\": true,\n      \"identifier\": \"DeleteModel\",\n      \"inputParams\": [\n        {\n          \"custom\": true,\n          \"dataSpecs\": {\n            \"dataType\": \"TEXT\",\n            \"length\": 128\n          },\n          \"dataType\": \"TEXT\",\n          \"direction\": \"PARAM_INPUT\",\n          \"identifier\": \"AlgorithmID\",\n          \"name\": \"算法任务唯一标识\",\n          \"paraOrder\": 0\n        }\n      ],\n      \"outputParams\": [],\n      \"productKey\": \"h7s72qjeGaM\",\n      \"required\": false,\n      \"serviceName\": \"删除模型\"\n    }\n  ]\n}",
		"productKey": "h7s7PwecpHX",
		"createTime": "2022-06-21 09:04:45",
		"updateTime": "2022-06-21 09:10:09"
	},
	"status": "S",
	"sysMsg": "操作成功"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | object | 返回数据 |
| data.modelId | 1 | number | - |
| data.thingModelJson | {  "_ppk": {},  "events": [    {      "createTs": 1655799762332,      "custom": true,      "eventName": "内容加载完成",      "eventType": "INFO_EVENT_TYPE",      "identifier": "UpdateContentCompleteEvent",      "outputData": [        {          "custom": true,          "dataSpecs": {            "dataType": "TEXT",            "length": 128          },          "dataType": "TEXT",          "direction": "PARAM_OUTPUT",          "identifier": "UpdateTaskID",          "name": "下发任务ID",          "paraOrder": 0        },        {          "custom": true,          "dataSpecs": {            "dataType": "INT",            "max": "1024",            "min": "-1024",            "precise": 0,            "step": "1",            "unit": "",            "unitName": "无"          },          "dataType": "INT",          "direction": "PARAM_OUTPUT",          "identifier": "Status",          "name": "状态",          "paraOrder": 1        },        {          "custom": true,          "dataSpecs": {            "childDataType": "STRUCT",            "customFlag": true,            "dataSpecsList": [              {                "childDataType": "TEXT",                "childName": "内容创意ID",                "childSpecsDTO": {                  "dataType": "TEXT",                  "length": 128                },                "dataSpecs": {                  "dataType": "TEXT",                  "length": 128                },                "dataType": "STRUCT",                "identifier": "CreativeID",                "name": "失败创意列表"              },              {                "childDataType": "INT",                "childName": "错误代码",                "childSpecsDTO": {                  "dataType": "INT",                  "max": "1024",                  "min": "-1024",                  "precise": 0,                  "step": "1",                  "unit": "",                  "unitName": "无"                },                "dataSpecs": {                  "dataType": "INT",                  "max": "1024",                  "min": "-1024",                  "precise": 0,                  "step": "1",                  "unit": "",                  "unitName": "无"                },                "dataType": "STRUCT",                "identifier": "Code",                "name": "失败创意列表"              },              {                "childDataType": "TEXT",                "childName": "错误描述",                "childSpecsDTO": {                  "dataType": "TEXT",                  "length": 1024                },                "dataSpecs": {                  "dataType": "TEXT",                  "length": 1024                },                "dataType": "STRUCT",                "identifier": "Message",                "name": "失败创意列表"              }            ],            "dataType": "ARRAY",            "size": 128          },          "dataType": "ARRAY",          "direction": "PARAM_OUTPUT",          "identifier": "FailedCreativeIDs",          "name": "失败创意列表",          "paraOrder": 2        }      ],      "productKey": "h7s72qjeGaM",      "required": false    }  ],  "properties": [    {      "createTs": 1652148128115,      "custom": true,      "customFlag": true,      "dataSpecs": {        "dataType": "FLOAT",        "max": "100",        "min": "0",        "step": "0.1",        "unit": "°C",        "unitName": "摄氏度"      },      "dataType": "FLOAT",      "description": "温度",      "identifier": "Temperature",      "name": "温度",      "productKey": "h7s72qjeGaM",      "required": false,      "rwFlag": "READ_WRITE",      "std": false    },    {      "createTs": 1652148141379,      "custom": true,      "customFlag": true,      "dataSpecs": {        "dataType": "FLOAT",        "max": "100",        "min": "0",        "step": "0.1",        "unit": "%RH",        "unitName": "相对湿度"      },      "dataType": "FLOAT",      "description": "湿度",      "identifier": "Humidity",      "name": "湿度",      "productKey": "h7s72qjeGaM",      "required": false,      "rwFlag": "READ_WRITE",      "std": false    }  ],  "services": [    {      "callType": "SYNC",      "createTs": 1655799752090,      "custom": true,      "identifier": "DeleteModel",      "inputParams": [        {          "custom": true,          "dataSpecs": {            "dataType": "TEXT",            "length": 128          },          "dataType": "TEXT",          "direction": "PARAM_INPUT",          "identifier": "AlgorithmID",          "name": "算法任务唯一标识",          "paraOrder": 0        }      ],      "outputParams": [],      "productKey": "h7s72qjeGaM",      "required": false,      "serviceName": "删除模型"    }  ]} | string | 物模型json |
| data.productKey | h7s7PwecpHX | string | 产品key |
| data.createTime | 2022-06-21 09:04:45 | string | 创建时间 |
| data.updateTime | 2022-06-21 09:04:45 | string | 更新时间 |
| status | S | string | 状态 |
| sysMsg | 操作成功 | string | 消息 |

* 失败(404)

```javascript
暂无数据
```

**Query**

## 其他平台

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-15 14:22:18

> 更新时间: 2023-07-03 10:59:31

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 总平台下发任务

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2022-09-15 14:22:29

> 更新时间: 2022-09-15 14:28:02

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> http://172.18.18.253:8088/simulate_platform/pages/ExaminationTbl/pushExamToUser.do

**请求方式**

> POST

**Content-Type**

> urlencoded

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 | Text | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9 | Text | 是 | - |
| Cache-Control | max-age=0 | Text | 是 | - |
| Connection | keep-alive | Text | 是 | - |
| Content-Type | application/x-www-form-urlencoded | Text | 是 | - |
| Origin | http://172.18.18.253:8088 | Text | 是 | - |
| Referer | http://172.18.18.253:8088/simulate_platform/pages/ExaminationTbl/pushExamToUserPre.do?examId=16& | Text | 是 | - |
| Upgrade-Insecure-Requests | 1 | Text | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 | Text | 是 | - |

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| examId | 16 | Text | 是 | 试题 |
| needPushGameId | 80 | Text | 是 | 比赛 |
| pushObjectStr | 测试战队3,测试战队4, | Text | 是 | 战队 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(201)

```javascript
暂无数据
```

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 | Text | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9 | Text | 是 | - |
| Cache-Control | max-age=0 | Text | 是 | - |
| Connection | keep-alive | Text | 是 | - |
| Content-Type | application/x-www-form-urlencoded | Text | 是 | - |
| Origin | http://172.18.18.253:8088 | Text | 是 | - |
| Referer | http://172.18.18.253:8088/simulate_platform/pages/ExaminationTbl/pushExamToUserPre.do?examId=16& | Text | 是 | - |
| Upgrade-Insecure-Requests | 1 | Text | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36 | Text | 是 | - |

**Query**

### 阿里云http连接获取token

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-07-28 11:46:41

> 更新时间: 2023-07-28 13:53:09

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> https://iot-06z00dsogje3o1n.http.iothub.aliyuncs.com/auth

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
    "version": "default",
    "sign": "E2BB66BDB33358033119307040B1DA2E",
    "signmethod": "hmacmd5",
    "clientId": "iy4uJzbjy1H.ae4Q0SXMROCwA3FPTWzt",
    "deviceName": "ae4Q0SXMROCwA3FPTWzt",
    "productKey": "iy4uJzbjy1H",
    "timestamp": "1501668289957"
}
```

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 阿里云http连接获取token_2

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-08-22 16:38:59

> 更新时间: 2023-08-22 16:41:47

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> https://iot-06z00dsogje3o1n.http.iothub.aliyuncs.com/auth

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
    "version": "default",
    "sign": "E2BB66BDB33358033119307040B1DA2E",
    "signmethod": "hmacmd5",
    "clientId": "iy4uzLngMgw.hA0ePHJjsy6uSTAECHhn",
    "deviceName": "hA0ePHJjsy6uSTAECHhn",
    "productKey": "iy4uzLngMgw",
    "timestamp": "1501668289957"
}
```

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 临时

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-16 11:32:21

> 更新时间: 2023-03-16 11:32:21

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 测试1

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-16 11:35:18

> 更新时间: 2023-03-16 11:56:21

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/listSearch?nodeType=&productKey=&deviceName=烟雾&size=10&sort=createTime,desc&page=0

**请求方式**

> GET

**Content-Type**

> none

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | application/json, text/plain, */* | Text | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5 | Text | 是 | - |
| Connection | keep-alive | Text | 是 | - |
| Origin | http://172.18.18.137:7071 | Text | 是 | - |
| Referer | http://172.18.18.137:7071/ | Text | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69 | Text | 是 | - |
| X-Requested-With | XMLHttpRequest | Text | 是 | - |
| iotToken | 771fe62c-6cbb-4801-ac06-0a9ac1cf23c3 | Text | 是 | - |
| token | 771fe62c-6cbb-4801-ac06-0a9ac1cf23c3 | Text | 是 | - |
| Accept-Encoding | deflate, gzip | Text | 是 | - |

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| nodeType | - | Text | 是 | - |
| productKey | - | Text | 是 | - |
| deviceName | 烟雾 | Text | 是 | - |
| size | 10 | Text | 是 | - |
| sort | createTime,desc | Text | 是 | - |
| page | 0 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | application/json, text/plain, */* | Text | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5 | Text | 是 | - |
| Connection | keep-alive | Text | 是 | - |
| Origin | http://172.18.18.137:7071 | Text | 是 | - |
| Referer | http://172.18.18.137:7071/ | Text | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69 | Text | 是 | - |
| X-Requested-With | XMLHttpRequest | Text | 是 | - |
| iotToken | 771fe62c-6cbb-4801-ac06-0a9ac1cf23c3 | Text | 是 | - |
| token | 771fe62c-6cbb-4801-ac06-0a9ac1cf23c3 | Text | 是 | - |
| Accept-Encoding | deflate, gzip | Text | 是 | - |

**Query**

### 测试2

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-16 11:38:07

> 更新时间: 2023-03-16 11:39:42

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotDevice/listSearch?projectId=2&size=10&page=0

**请求方式**

> GET

**Content-Type**

> none

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | application/json, text/plain, */* | Text | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5 | Text | 是 | - |
| Connection | keep-alive | Text | 是 | - |
| Cookie | PHPSESSID=sjsad60irojbo9cutsc3rcvb30; ECS_ID=19958afa8864e7a3c3b4f6aa93dd2002dd223094; ECS[visit_times]=2; JSESSIONID=35C37149120E40B823C941122FF20E87 | Text | 是 | - |
| Origin | http://172.18.18.253:7071 | Text | 是 | - |
| Referer | http://172.18.18.253:7071/ | Text | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69 | Text | 是 | - |
| X-Requested-With | XMLHttpRequest | Text | 是 | - |
| iotToken | 28791f04-cc85-4f4f-b975-4cfc472e1167 | Text | 是 | - |
| token | 28791f04-cc85-4f4f-b975-4cfc472e1167 | Text | 是 | - |
| Accept-Encoding | deflate, gzip | Text | 是 | - |

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| projectId | 2 | Text | 是 | - |
| size | 10 | Text | 是 | - |
| page | 0 | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | application/json, text/plain, */* | Text | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5 | Text | 是 | - |
| Connection | keep-alive | Text | 是 | - |
| Cookie | PHPSESSID=sjsad60irojbo9cutsc3rcvb30; ECS_ID=19958afa8864e7a3c3b4f6aa93dd2002dd223094; ECS[visit_times]=2; JSESSIONID=35C37149120E40B823C941122FF20E87 | Text | 是 | - |
| Origin | http://172.18.18.253:7071 | Text | 是 | - |
| Referer | http://172.18.18.253:7071/ | Text | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.69 | Text | 是 | - |
| X-Requested-With | XMLHttpRequest | Text | 是 | - |
| iotToken | 28791f04-cc85-4f4f-b975-4cfc472e1167 | Text | 是 | - |
| token | 28791f04-cc85-4f4f-b975-4cfc472e1167 | Text | 是 | - |
| Accept-Encoding | deflate, gzip | Text | 是 | - |

**Query**

### 新建websocket

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-08-30 17:14:13

> 更新时间: 2023-08-30 17:23:18

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> ws://localhost:7070/getDeviceProperties?token=d761fd91-6d4e-41ba-83a2-a7da3e0a24f9&iotId=ae4Q0SXMROCwA3FPTWztiy4u00

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | d761fd91-6d4e-41ba-83a2-a7da3e0a24f9 | String | 是 | - |
| iotId | ae4Q0SXMROCwA3FPTWztiy4u00 | String | 是 | - |

**设置**


| 启用服务器证书验证 | 否 |
| 最大内容大小 | 5 |
| 连接超时设置 | 0 |

**Socket消息**

> 消息

* 请求(text)
```javascript
暂无数据
```

* 响应(text)
```javascript
暂无数据
```

**Query**

## 错误

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-07-05 10:24:11

> 更新时间: 2023-07-05 10:24:11

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 产品模型创建错误_指定模型

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-07-05 10:25:55

> 更新时间: 2023-07-05 14:56:27

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotProduct/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | application/json, text/plain, */* | Text | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6 | Text | 是 | - |
| Connection | keep-alive | Text | 是 | - |
| Content-Type | multipart/form-data; boundary=----WebKitFormBoundaryhy0KFmHW8HAc4XSa | Text | 是 | - |
| Origin | https://iot.iuvtech.com | Text | 是 | - |
| Referer | https://iot.iuvtech.com/ | Text | 是 | - |
| Sec-Fetch-Dest | empty | Text | 是 | - |
| Sec-Fetch-Mode | cors | Text | 是 | - |
| Sec-Fetch-Site | same-origin | Text | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67 | Text | 是 | - |
| X-Requested-With | XMLHttpRequest | Text | 是 | - |
| iotToken | 9e3756ff-e18e-4c06-bc3f-ea18197a6917 | Text | 是 | - |
| sec-ch-ua | "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114" | Text | 是 | - |
| sec-ch-ua-mobile | ?0 | Text | 是 | - |
| sec-ch-ua-platform | "Windows" | Text | 是 | - |
| token | 9e3756ff-e18e-4c06-bc3f-ea18197a6917 | Text | 是 | - |
| Accept-Encoding | deflate, gzip | Text | 是 | - |

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productName | 创建测试1 | Text | 是 | - |
| type | 0 | Text | 是 | - |
| categoryKeys.0 | SmartCity | Text | 是 | - |
| categoryKeys.1 | PublicService | Text | 是 | - |
| categoryKeys.2 | Locater | Text | 是 | - |
| categoryKey | Locater | Text | 是 | - |
| linkObj | real | Text | 是 | - |
| netType | BlueTooth | Text | 是 | - |
| productType | - | Text | 是 | - |
| modeAuth | - | Text | 是 | - |
| dataFormat | 1 | Text | 是 | - |
| authType | secret | Text | 是 | - |
| description | - | Text | 是 | - |
| projectId | 109 | Text | 是 | - |
| nodeType | 0 | Text | 是 | - |
| belong | private | Text | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 失败(404)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | application/json, text/plain, */* | Text | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6 | Text | 是 | - |
| Connection | keep-alive | Text | 是 | - |
| Content-Type | multipart/form-data; boundary=----WebKitFormBoundaryhy0KFmHW8HAc4XSa | Text | 是 | - |
| Origin | https://iot.iuvtech.com | Text | 是 | - |
| Referer | https://iot.iuvtech.com/ | Text | 是 | - |
| Sec-Fetch-Dest | empty | Text | 是 | - |
| Sec-Fetch-Mode | cors | Text | 是 | - |
| Sec-Fetch-Site | same-origin | Text | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67 | Text | 是 | - |
| X-Requested-With | XMLHttpRequest | Text | 是 | - |
| iotToken | 9e3756ff-e18e-4c06-bc3f-ea18197a6917 | Text | 是 | - |
| sec-ch-ua | "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114" | Text | 是 | - |
| sec-ch-ua-mobile | ?0 | Text | 是 | - |
| sec-ch-ua-platform | "Windows" | Text | 是 | - |
| token | 9e3756ff-e18e-4c06-bc3f-ea18197a6917 | Text | 是 | - |
| Accept-Encoding | deflate, gzip | Text | 是 | - |

**Query**

## 工具

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-23 09:28:31

> 更新时间: 2024-07-25 13:54:59

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### 用户登陆_副本

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-23 14:20:08

> 更新时间: 2023-06-30 15:53:33

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IUVUser/userLogin

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| userName | tl2 | Text | 是 | - |
| password | 33e9d59ef1d93f75869a70711440a3c2 | Text | 是 | 密码签名 = md5(userName+md5(密码)+verifyCode) |
| verifyCode | 4bsx | Text | 否 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
	"role": 2,
	"unReadMsgCount": 0,
	"totalMsgCount": 0,
	"nickName": "fff",
	"userName": "abcj",
	"userId": 3,
	"iotToken": "0cdf39a6-4fa0-4895-9b1f-367256b62301",
	"token": "0cdf39a6-4fa0-4895-9b1f-367256b62301",
	"status": "S"
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| role | 2 | number | - |
| unReadMsgCount | 0 | number | - |
| totalMsgCount | 0 | number | - |
| nickName | fff | string | 用户昵称 |
| userName | abcj | string | 用户名 |
| userId | 3 | number | 用户id |
| iotToken | 0cdf39a6-4fa0-4895-9b1f-367256b62301 | string | 用户iot平台token |
| token | 0cdf39a6-4fa0-4895-9b1f-367256b62301 | string | 认证令牌 |
| status | S | string | 状态 |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 获取MQTT鉴权信息

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-03-23 09:28:44

> 更新时间: 2023-08-17 10:52:12

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/tool/getMQTTAuthInfo?productKey=h7s74s9eX8o&deviceName=oGW5KKmb0q8F5eefpuK4&deviceSecret=86425a99e8cead181dd337188e70469e

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| productKey | h7s74s9eX8o | string | 是 | 产品key |
| deviceName | oGW5KKmb0q8F5eefpuK4 | string | 是 | 设备名称 |
| deviceSecret | 86425a99e8cead181dd337188e70469e | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### 获取数据库结构

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-30 14:08:51

> 更新时间: 2023-05-30 16:33:38

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> http://60.205.159.173:8081/getDbStruct

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| password | 181818 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{
  "data": [
    {
      "column_key": "PRI",
      "column_name": "group_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_level",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_introduct",
      "column_type": "varchar(255)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "parent_group",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "allow_max_member_count",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "allow_team",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "allow_second_admin",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "allow_game",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "allow_test_maker",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "allow_exam_count",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "allow_referee",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "portal_name",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute1",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute2",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute3",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute4",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute5",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute6",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute7",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute8",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute9",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute10",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "education_level",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "is_delete",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "delete_date",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "material_copy_record",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "onex",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "group_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_consumer_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_name",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_consumer_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_id",
      "column_type": "varchar(32)",
      "is_nullable": "YES",
      "table_name": "iot_consumer_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "sub_cnt",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_consumer_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_keys",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_consumer_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "iot_id",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_auth_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_auth_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_auth_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_secret",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_auth_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "device_identify",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_device_auth_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_password",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_auth_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "iot_id",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_map_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "hardware_product_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_map_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "hardware_device_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_map_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "hardware_device_secret",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_map_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "date",
      "is_nullable": "YES",
      "table_name": "iot_device_map_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_device_relation_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "gw_device",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_relation_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "sub_device",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_relation_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "iot_id",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_secret",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "product_key",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "join_eui",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "nickname",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "status",
      "column_type": "varchar(10)",
      "is_nullable": "NO",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "labels",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "active_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "description",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "version",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "dest_version",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "src_iot_id",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "hardware_id",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "file_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "file_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "file_version",
      "column_type": "varchar(15)",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "file_path",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "file_comment",
      "column_type": "varchar(500)",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "file_url",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_keys",
      "column_type": "varchar(1000)",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_firmware",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_file_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "group_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_ota_group_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_ota_group_device_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "group_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_ota_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_desc",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_name",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "file_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "super_group_id",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_devices",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "iot_group_id",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_ota_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "iot_job_id",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_ota_job_log_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "device_name",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_ota_job_log_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "dest_version",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_ota_job_log_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_log_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "up_status",
      "column_type": "varchar(15)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_log_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_log_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "src_version",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_log_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "job_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_log_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "job_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "job_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "schedule_time",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "need_confirm",
      "column_type": "tinyint(1)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "need_push",
      "column_type": "tinyint(1)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "retry_count",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "retry_interval",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "timeout_in_minutes",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "overwrite_mode",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_cnt",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "iot_job_ids",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "file_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "job_status_detail",
      "column_type": "varchar(500)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "main_job_status",
      "column_type": "varchar(15)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "start_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "end_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "job_cnt",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_keys",
      "column_type": "varchar(500)",
      "is_nullable": "YES",
      "table_name": "iot_ota_job_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "iot_instance_id",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_name",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_name_note",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "product_key",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_secret",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "code",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_cnt",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "node_type",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "description",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "category_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "net_type",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "data_format",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "auth_type",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_status",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "join_permission_id",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "protocol_type",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "link_obj",
      "column_type": "varchar(15)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "belong",
      "column_type": "varchar(15)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "consumer_group",
      "column_type": "varchar(32)",
      "is_nullable": "YES",
      "table_name": "iot_product_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_project_scene_tbl_temp",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_project_scene_tbl_temp",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_json",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_project_scene_tbl_temp",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_type",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "iot_project_scene_tbl_temp",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_model",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_project_scene_tbl_temp",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_project_scene_tbl_temp",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "project_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_type",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_tag",
      "column_type": "varchar(500)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "creator_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "initialize",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "src_project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "max_scene_num",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "max_dev_num",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "train_module",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "refer_docum",
      "column_type": "varchar(800)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scores",
      "column_type": "varchar(300)",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scenes",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_project_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "device_iot_id",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_scene_devices_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_scene_devices_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_scene_devices_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "scene_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_scene_devices_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "pos_id",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_scene_devices_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_scene_device_plan_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_scene_device_plan_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_model",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_scene_device_plan_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "device_type",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_scene_device_plan_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "access_type",
      "column_type": "varchar(15)",
      "is_nullable": "YES",
      "table_name": "iot_scene_device_plan_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "link_obj",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_scene_device_plan_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "max_feat_num",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_scene_device_plan_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "max_serv_num",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_scene_device_plan_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "scene_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_type",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_belong",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_model_belong",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_data",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_devices",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_scene_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "widget_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_scene_widget_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "widget_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_scene_widget_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "widget_pic",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_scene_widget_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "scene_type",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "iot_scene_widget_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "is_background",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_scene_widget_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "widget_model",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_scene_widget_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "widget_data",
      "column_type": "varchar(500)",
      "is_nullable": "YES",
      "table_name": "iot_scene_widget_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "task_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_task_pull_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_task_pull_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "src_project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_task_pull_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "new_project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_task_pull_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_task_pull_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "task_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "task_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "task_level",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "project_relation",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "creator_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "start_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "end_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "description",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "distribute",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_task_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "std",
      "column_type": "tinyint(1)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "identifier",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "description",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "ability_type",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "required",
      "column_type": "tinyint(1)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "category_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "data_type",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "rw_flag",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "category_type",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "ability_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "data_specs_list",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_thing_detail_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "fun_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_thing_fun_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "product_key",
      "column_type": "varchar(20)",
      "is_nullable": "NO",
      "table_name": "iot_thing_fun_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "fun_type",
      "column_type": "tinyint(4)",
      "is_nullable": "NO",
      "table_name": "iot_thing_fun_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "fun_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_thing_fun_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "fun_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_thing_fun_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "fun_detail",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_thing_fun_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_thing_fun_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "category_key",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "iot_thing_model_std_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "thing_model_json",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_thing_model_std_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "model_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_thing_model_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "thing_model_json",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_thing_model_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "product_key",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_thing_model_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "category_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_thing_model_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_thing_model_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_thing_model_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "is_standard",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_thing_model_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "thing_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_thing_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "super_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_thing_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "UNI",
      "column_name": "category_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_thing_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "category_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_thing_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "is_model",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_thing_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_key",
      "column_type": "varchar(500)",
      "is_nullable": "YES",
      "table_name": "iot_topic_base_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_name",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_topic_base_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_desc",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_topic_base_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "operation",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_topic_base_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_type",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_topic_base_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_topic_base_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "topic_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "product_key",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_key",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_key_short",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_name",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_desc",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "operation",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_id_iot",
      "column_type": "mediumtext",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "topic_type",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_topic_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "product_key",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "device_name",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "warning_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_level",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_desc",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "properties",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "uuid",
      "column_type": "varchar(50)",
      "is_nullable": "NO",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "ensure_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "end_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "status",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_warning_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "warning_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iot_warning_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "MUL",
      "column_name": "product_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_warning_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_warning_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_key",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iot_warning_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_level",
      "column_type": "tinyint(4)",
      "is_nullable": "YES",
      "table_name": "iot_warning_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_rule",
      "column_type": "text",
      "is_nullable": "YES",
      "table_name": "iot_warning_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "warning_desc",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "iot_warning_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iot_warning_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "seq_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "login_type",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "login_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "server_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "server_sn",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "login_ip",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "iuv_token",
      "column_type": "varchar(300)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "last_active_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "ilab_access_token",
      "column_type": "varchar(300)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "iuv_online_cache_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "class_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "school_name",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "department",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "grade",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "marjor",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "class_name",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "remove_flag",
      "column_type": "char(1)",
      "is_nullable": "YES",
      "table_name": "micro_class_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "seq_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "micro_class_user_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "class_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_class_user_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_class_user_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_class_role",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_class_user_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "msg_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "title",
      "column_type": "varchar(300)",
      "is_nullable": "YES",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "context",
      "column_type": "longtext",
      "is_nullable": "YES",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "msg_type",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "classify",
      "column_type": "varchar(10)",
      "is_nullable": "YES",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "pubilc_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "creator",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_message_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "record_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "micro_message_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "msg_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_message_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_message_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "read_flag",
      "column_type": "char(1)",
      "is_nullable": "YES",
      "table_name": "micro_message_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "read_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "micro_message_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "record_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "micro_study_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_study_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "learning_time",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_study_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "res_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "micro_study_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "record_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "micro_study_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "seq_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "step1_seq_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "server_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute1",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute2",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute3",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute4",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute5",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_server_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "seq_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "author_object_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "author_object",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "author_type",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_name",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "authorizate_count",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "start_day",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "end_day",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "authorizate_user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "authorizate_person",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "authorizate_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "auth_member_level_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "auth_member_level_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute1",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute2",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute3",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute4",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute5",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "tmp_authorizate_count",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "tmp_start_day",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "tmp_end_day",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "auth_language",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "product_author_step1_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "test_jpa",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "test_jpa",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "test_jpa",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "val",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "test_jpa",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "user_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "group_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "user_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "group_role",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "user_group_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_name",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "nick_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "real_name",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "password",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "email_addr",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "tel_num",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "mobile_num",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "contact_addr",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "school_name",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "department_name",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "major_name",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "class_name",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "person_icon",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "last_update_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "weixin_number",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "qq",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "person_id",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "iuv_code",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "invite_code",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "activaction_code",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "creator_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "creator_username",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "role",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "auth_member_level_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "auth_member_level_name",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "stu_no",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "g2_level",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "g2_experience",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "g2_title",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "is_delete",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "delete_date",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "sex",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "learning_time",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute1",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute2",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute3",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute4",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute5",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute6",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute7",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute8",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute9",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "attribute10",
      "column_type": "varchar(200)",
      "is_nullable": "YES",
      "table_name": "user_info_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "record_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "login_type",
      "column_type": "varchar(20)",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "login_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "logout_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "remark",
      "column_type": "varchar(100)",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "handle_flag",
      "column_type": "varchar(5)",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "product_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "server_id",
      "column_type": "int(11)",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "login_ip",
      "column_type": "varchar(30)",
      "is_nullable": "YES",
      "table_name": "user_login_out_record_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "user_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "user_role_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "PRI",
      "column_name": "role_id",
      "column_type": "int(11)",
      "is_nullable": "NO",
      "table_name": "user_role_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "relaction_introduct",
      "column_type": "varchar(50)",
      "is_nullable": "YES",
      "table_name": "user_role_tbl",
      "table_schema": "iuv_iot_db"
    },
    {
      "column_key": "",
      "column_name": "create_time",
      "column_type": "datetime",
      "is_nullable": "YES",
      "table_name": "user_role_tbl",
      "table_schema": "iuv_iot_db"
    }
  ],
  "success": 1
}
```

| 参数名 | 示例值 | 参数类型 | 参数描述 |
| --- | --- | ---- | ---- |
| data | - | array | - |
| data.column_key | PRI | string | - |
| data.column_name | group_id | string | - |
| data.column_type | int(11) | string | - |
| data.is_nullable | NO | string | - |
| data.table_name | group_info_tbl | string | - |
| data.table_schema | iuv_iot_db | string | - |
| success | 1 | integer | - |

* 失败(404)

```javascript
暂无数据
```

**Query**

### 获取服务状态

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-05-31 15:51:01

> 更新时间: 2023-06-05 15:40:46

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/tool/getServerStatus

**请求方式**

> GET

**Content-Type**

> form-data

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 临时

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2023-10-18 11:14:11

> 更新时间: 2023-10-18 11:14:11

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

# 数据引擎

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-05-29 09:54:51

> 更新时间: 2024-05-29 09:54:51

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## demo

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-05-29 09:55:14

> 更新时间: 2024-05-29 09:55:14

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

### get接口

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-05-29 09:55:39

> 更新时间: 2024-05-29 09:57:39

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> http://127.0.0.1:5000/api/v1/resources?arg=123

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| arg | 123 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### post接口

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-05-29 09:57:17

> 更新时间: 2024-05-29 10:49:24

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> http://127.0.0.1:5000/api/v1/resources?arg=123

**请求方式**

> POST

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| arg | 123 | string | 是 | - |

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| body | 2232323 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

### post接口_json

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-05-29 10:00:09

> 更新时间: 2024-05-29 10:28:59

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> http://127.0.0.1:5000/api/v1/resources

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
    "arg":323
}
```

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:36:03

> 更新时间: 2024-07-22 14:16:34

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| nodes | [     {       "x": 287,       "y": 99,       "name": "设备实例工况数据",       "type": "in",       "data": {         "inputName": null,         "devModeName": "64oANPNK8pm",         "deviceName": null,         "featureName": null       },       "id": "n1716859270539"     }   ] | string | 是 | - |
| links | [     {       source: "n1716859270539",       target: "eeeeeee"     }   ] | string | 是 | - |
| name | 测试数据引擎 | string | 是 | - |
| projectId | 112 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎更新

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:36:03

> 更新时间: 2024-06-11 16:14:48

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 1 | integer | 是 | - |
| nodes | [     {       "x": 287,       "y": 99,       "name": "设备实例工况数据",       "type": "in",       "data": {         "inputName": null,         "devModeName": "64oANPNK8pm",         "deviceName": null,         "featureName": null       },       "id": "n1716859270539"     }   ] | string | 是 | - |
| links | [     {       source: "n1716859270539",       target: "eeeeeee"     }   ] | string | 是 | - |
| name | hahah | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎获取

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:36:03

> 更新时间: 2024-06-11 16:15:07

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/get?id=1

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 1 | integer | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:36:03

> 更新时间: 2024-07-11 14:07:36

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/delete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 61 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎启用

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-11 09:29:42

> 更新时间: 2024-07-01 11:49:38

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/start

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 144 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎停用

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-11 09:30:07

> 更新时间: 2024-07-11 14:07:17

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/stop

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 58 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:36:03

> 更新时间: 2024-07-22 15:16:11

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/list?name=&aboutObject=实例&projectId=112

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| name | - | string | 是 | - |
| aboutObject | 实例 | string | 是 | - |
| projectId | 112 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎文本保存

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:36:03

> 更新时间: 2024-06-07 17:18:38

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/saveText

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| ruleId | 1 | integer | 是 | - |
| nodeId | xxx | string | 是 | - |
| content | {"test":"test val"} | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎文本获取

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 17:20:07

> 更新时间: 2024-06-07 17:22:16

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/getText?ruleId=1&nodeId=xxx

**请求方式**

> GET

**Content-Type**

> form-data

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| ruleId | 1 | integer | 是 | - |
| nodeId | xxx | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据源创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:43:39

> 更新时间: 2024-06-07 17:40:30

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRuleDb/create

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sourceName | 数据源1 | string | 是 | 数据源名称 |
| type | MySql | string | 是 | 数据库类型: MySql, PostgreSql, Oracle |
| version | 5.7 | string | 是 | 数据库版本 |
| host | 172.18.18.19 | string | 是 | 主机 |
| port | 3306 | integer | 是 | 端口 |
| username | root | string | 是 | 用户名 |
| password | 5fb5a420775da0b6 | string | 是 | 密码 |
| scope | 通用 | string | 是 | 数据源属性:通用,私有 |
| dbName | test | string | 是 | 数据库名 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据源更新

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:43:39

> 更新时间: 2024-07-11 14:07:01

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRuleDb/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sourceName | 数据源11w122 | string | 是 | 数据源名称 |
| type | MySql | string | 是 | 数据库类型: MySql, PostgreSql, Oracle |
| version | 5.7 | string | 是 | 数据库版本 |
| host | 172.18.18.19 | string | 是 | 主机 |
| port | 3306 | integer | 是 | 端口 |
| username | root | string | 是 | 用户名 |
| password | 5fb5a420775da0b6 | string | 是 | 密码 |
| scope | 通用 | string | 是 | 数据源属性:通用,私有 |
| dbName | test | string | 是 | 数据库名 |
| id | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据源列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:39:35

> 更新时间: 2024-06-12 10:32:30

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRuleDb/list?sourceName=&type=Mysql&scope=

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| sourceName | - | string | 是 | - |
| type | Mysql | string | 是 | - |
| scope | - | string | 是 | 通用, 专用 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据源删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-07 14:43:39

> 更新时间: 2024-06-11 08:58:13

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRuleDb/delete

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 4 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎输出

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-12 14:29:44

> 更新时间: 2024-07-23 10:05:57

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> ws://{{host2}}/dataEngine?token={{token}}

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | {{token}} | String | 是 | - |

**设置**


| 启用服务器证书验证 | 否 |
| 最大内容大小 | 5 |
| 连接超时设置 | 0 |

**Socket消息**

> 消息

* 请求(text)
```javascript
暂无数据
```

* 响应(text)
```javascript
暂无数据
```

**Query**

## 数据源sql检查

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-26 15:02:34

> 更新时间: 2024-06-26 15:07:24

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRuleDb/checkSql

**请求方式**

> POST

**Content-Type**

> form-data

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 1 | string | 是 | 数据源id |
| sql | select * from quests | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 数据引擎输出节点历史

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-01 15:28:43

> 更新时间: 2024-07-01 15:33:58

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/IotRule/getOutput?ruleId=144&page=0&size=10

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| ruleId | 144 | string | 是 | - |
| page | 0 | string | 是 | - |
| size | 10 | string | 是 | 每页元素个数 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 孪生空间

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-22 15:11:44

> 更新时间: 2024-07-25 13:54:58

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 孪生列表

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-22 15:11:57

> 更新时间: 2024-12-26 14:36:31

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTwin/listSearch?name=&projectId=162

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| name | - | string | 是 | - |
| projectId | 162 | integer | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 孪生创建

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-22 15:11:57

> 更新时间: 2024-07-25 13:54:58

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTwin/create?name=测试2&config={}&projectId=112

**请求方式**

> POST

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| name | 测试2 | string | 是 | - |
| config | {} | string | 是 | - |
| projectId | 112 | integer | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 孪生详情

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-22 15:11:57

> 更新时间: 2024-07-22 15:35:56

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTwin/get?id=2

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 2 | integer | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 孪生更新

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-22 15:11:57

> 更新时间: 2024-07-22 15:36:52

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTwin/update?id=2&name=测试3&config={}

**请求方式**

> POST

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 2 | integer | 是 | - |
| name | 测试3 | string | 是 | - |
| config | {} | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 孪生删除

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-22 15:11:57

> 更新时间: 2024-07-22 15:13:48

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTwin/delete?id=1

**请求方式**

> POST

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 1 | integer | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 孪生复制

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-22 15:40:23

> 更新时间: 2024-07-25 13:54:58

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTwin/create?id=1

**请求方式**

> POST

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 1 | string | 是 | - |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
{}
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 调用数据引擎输出

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-22 16:38:28

> 更新时间: 2024-07-25 14:54:53

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> ws://{{host2}}/dataEngineInvoke?token={{token}}

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | {{token}} | String | 是 | - |

**设置**


| 启用服务器证书验证 | 否 |
| 最大内容大小 | 5 |
| 连接超时设置 | 0 |

**Socket消息**

> 消息

* 请求(text)
```javascript
暂无数据
```

* 响应(text)
```javascript
暂无数据
```

**Query**

## 获取设备数据

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-25 15:46:40

> 更新时间: 2024-07-25 16:36:36

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> ws://{{host2}}/manyDevice?token={{token}}

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | {{token}} | String | 是 | - |

**设置**


| 启用服务器证书验证 | 否 |
| 最大内容大小 | 5 |
| 连接超时设置 | 0 |

**Socket消息**

> 消息

* 请求(text)
```javascript
暂无数据
```

* 响应(text)
```javascript
暂无数据
```

**Query**

## 获取设备数据 副本

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-07-29 11:11:00

> 更新时间: 2024-07-29 11:11:10

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> ws://{{host2}}/manyDevice?token={{token}}

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | {{token}} | String | 是 | - |

**设置**


| 启用服务器证书验证 | 否 |
| 最大内容大小 | 5 |
| 连接超时设置 | 0 |

**Socket消息**

> 消息

* 请求(text)
```javascript
暂无数据
```

* 响应(text)
```javascript
暂无数据
```

**Query**

# 新建websocket

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-06-25 16:09:24

> 更新时间: 2024-06-25 16:09:24

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host2}}/dataEngine?token=ed364a4e-cdb8-4a4d-9845-f8042886fcff&ruleId=34

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| token | ed364a4e-cdb8-4a4d-9845-f8042886fcff | String | 是 | - |
| ruleId | 34 | String | 是 | - |

**设置**


| 启用服务器证书验证 | 否 |
| 最大内容大小 | 5 |
| 连接超时设置 | 0 |

**Socket消息**

> 消息

* 请求(text)
```javascript
暂无数据
```

* 响应(text)
```javascript
暂无数据
```

**Query**

# 模拟设备

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-08-01 13:45:41

> 更新时间: 2024-08-20 15:19:09

```text
暂无描述
```

**目录Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| 暂无参数 |

**目录认证信息**

> 继承父级

**Query**

## 编译工程

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-08-01 13:46:07

> 更新时间: 2024-08-27 13:56:47

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/simulator/compileProject?project=stm32&type=run

**请求方式**

> GET

**Content-Type**

> none

**请求Query参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| project | stm32 | string | 是 | - |
| type | run | string | 是 | 消息类型 |

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

## 运行

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-08-27 13:56:18

> 更新时间: 2024-08-27 14:48:27

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> localhost:5001/run

**请求方式**

> POST

**Content-Type**

> json

**请求Body参数**

```javascript
{
    "project":123,
    "config":{
        "p1":1
    }
}
```

**认证方式**

> 继承父级

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**Query**

# 新建接口

> 创建人: fuwei

> 更新人: fuwei

> 创建时间: 2024-10-15 09:14:37

> 更新时间: 2024-10-15 09:14:37

```text
暂无描述
```

**接口状态**

> 开发中

**接口URL**

> {{host}}/iotTwin/update

**请求方式**

> POST

**Content-Type**

> form-data

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | application/json, text/plain, */* | string | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6 | string | 是 | - |
| Connection | keep-alive | string | 是 | - |
| Cookie | _clck=1bmvt0l%7C2%7Cflj%7C0%7C1587; _ga=GA1.1.91285543.1714988103; _ga_8NW26JNFDM=GS1.1.1714988103.1.1.1714988385.60.0.0; _pk_id.1.90a4=b03866383b65f9a1.1716126958.; ajs_anonymous_id=97e7e947-5798-41da-9b77-ccfdca4feb31 | string | 是 | - |
| Origin | http://172.18.18.19 | string | 是 | - |
| Referer | http://172.18.18.19/ | string | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0 | string | 是 | - |
| X-Requested-With | XMLHttpRequest | string | 是 | - |
| iotToken | 2abf8afe-82c8-49a8-8fc1-ae8f72154e5d | string | 是 | - |
| token | 2abf8afe-82c8-49a8-8fc1-ae8f72154e5d | string | 是 | - |

**请求Body参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| id | 33 | string | 是 | - |
| name | 23234243 | string | 是 | - |
| config | {"背景":{"id":"背景1723705209008","type":"背景","uikey":"UI_BACKGROUND_NUM4","zIndex":2,"params":{"width":1700,"height":1080,"scaleW":1,"scaleH":1,"backgroundColor":"rgba(5, 122, 38, 1)","backgroundImg":null,"backgroundImgType":"重复"}},"环境":[{"id":"环境1723705218263","type":"环境","uikey":"UI_GZT_1","zIndex":2,"params":{"cameraPosition":{"x":0.4169468855235527,"y":4317.573517638623,"z":-216.4495310860939},"cameraRotation":{"x":-1.6208866086015736,"y":0.00009644860115205451,"z":3.139668771335861},"cameraQuaternion":{"x":-0.0006637803914413724,"y":0.7245924566965561,"z":0.6891769323203035,"w":0.0006978908346833188},"modelSrc":"model/gzt.json","allowUI":["UI_Manipulator_1","UI_Sorting_1","UI_Car_1","UI_IntelligentSilo_PJ_1","UI_IntelligentSilo_DB_1","UI_IntelligentSilo_CC_1","UI_IntelligentSilo_ZZ_1","UI_IntelligentSilo_NG_1"],"children":{"cc_area":{"data":{"datas":{"calcuObject":"NVcGoq3BrIs","device":"1bZqy4rctadpmxYL93Pd","dataType":null,"dataName":null},"params":{"modelSrc":"model/IntelligentSilo_CC.json"},"type":"终端","uikey":"UI_IntelligentSilo_CC_1","id":"终端1723705279366"},"UItype":"UI_IntelligentSilo_CC_1","allowUI":{"UI_IntelligentSilo_CC_1":{"scale":{"x":1,"y":1,"z":1},"position":{"x":1128.022,"y":1149.206,"z":835.915},"rotation":{"x":0,"y":0,"z":0}}}},"db_area":{"data":{"datas":{"calcuObject":"NVcGoq3BrIs","device":"1bZqy4rctadpmxYL93Pd","dataType":null,"dataName":null},"params":{"modelSrc":"model/IntelligentSilo_DB.json"},"type":"终端","uikey":"UI_IntelligentSilo_DB_1","id":"终端1723705277672"},"UItype":"UI_IntelligentSilo_DB_1","allowUI":{"UI_IntelligentSilo_DB_1":{"scale":{"x":1,"y":1,"z":1},"position":{"x":1335.279,"y":1149.206,"z":-307.509},"rotation":{"x":0,"y":0,"z":0}}}},"zz_area":{"data":{"datas":{"calcuObject":"NVcGoq3BrIs","device":"1bZqy4rctadpmxYL93Pd","dataType":null,"dataName":null},"params":{"modelSrc":"model/IntelligentSilo_ZZ.json"},"type":"终端","uikey":"UI_IntelligentSilo_ZZ_1","id":"终端1723705281567"},"UItype":"UI_IntelligentSilo_ZZ_1","allowUI":{"UI_IntelligentSilo_ZZ_1":{"scale":{"x":1,"y":1,"z":1},"position":{"x":927.81,"y":1148.106,"z":-151.94},"rotation":{"x":0,"y":0,"z":0}}}},"pj_area":{"data":{"datas":{"calcuObject":"NVcGoq3BrIs","device":"1bZqy4rctadpmxYL93Pd","dataType":null,"dataName":null},"params":{"modelSrc":"model/IntelligentSilo_PJ.json"},"type":"终端","uikey":"UI_IntelligentSilo_PJ_1","id":"终端1723705275911"},"UItype":"UI_IntelligentSilo_PJ_1","allowUI":{"UI_IntelligentSilo_PJ_1":{"scale":{"x":1,"y":1,"z":1},"position":{"x":1009.239,"y":1148.629,"z":-335.422},"rotation":{"x":0,"y":0,"z":0}}}},"ng_area":{"data":{"datas":{"calcuObject":"NVcGoq3BrIs","device":"1bZqy4rctadpmxYL93Pd","dataType":null,"dataName":null},"params":{"modelSrc":"model/IntelligentSilo_NG.json"},"type":"终端","uikey":"UI_IntelligentSilo_NG_1","id":"终端1723705283510"},"UItype":"UI_IntelligentSilo_NG_1","allowUI":{"UI_IntelligentSilo_NG_1":{"scale":{"x":1,"y":1,"z":1},"position":{"x":273.974,"y":1148.282,"z":282.257},"rotation":{"x":0,"y":0,"z":0}}}},"car_area":{"data":{"datas":{"calcuObject":"qhWdmohxDsU","device":"6hjGE0x6TEDbZvmdVcyr","dataType":null,"dataName":null},"params":{"modelSrc":"model/Car.json"},"type":"终端","uikey":"UI_Car_1","id":"终端1723705273945"},"UItype":"UI_Car_1","allowUI":{"UI_Car_1":{"scale":{"x":1,"y":1,"z":1},"position":{"x":-788.212,"y":1152.375,"z":70.652},"rotation":{"x":0,"y":0,"z":0}}}},"fj_area":{"data":{"datas":{"calcuObject":"Bob7csV7uKW","device":"zkb5v7ERBZRMaoLcqiYw","dataType":null,"dataName":null},"params":{"modelSrc":"model/Sorting.json"},"type":"终端","uikey":"UI_Sorting_1","id":"终端1723705268090"},"UItype":"UI_Sorting_1","allowUI":{"UI_Sorting_1":{"scale":{"x":1,"y":1,"z":1},"position":{"x":-1096.898,"y":1140.841,"z":298.234},"rotation":{"x":0,"y":0,"z":0}}}},"jxb_area":{"data":{"datas":{"calcuObject":"OYbWW48tf14","device":"iYFKhzgNcSVSYcOmLhke","dataType":null,"dataName":null},"params":{"modelSrc":"model/Manipulator.json"},"type":"终端","uikey":"UI_Manipulator_1","id":"终端1723705265206"},"UItype":"UI_Manipulator_1","allowUI":{"UI_Manipulator_1":{"scale":{"x":1,"y":1,"z":1},"position":{"x":789.66,"y":1501.732,"z":181.824},"rotation":{"x":0,"y":0,"z":0}}}}},"left":960,"top":540,"width":1920,"height":1080,"backgroundColor":"rgba(6, 38, 74, 0.57)","borderColor":"#2eb9ff","borderStyle":"solid","borderWidth":2,"borderRadius":1}}],"控件":[{"id":"控件1728890744233","type":"控件","uikey":"UI_BASE_BUTTON_1","zIndex":3,"params":{"isButton":true,"left":614,"top":75,"width":202,"height":64,"rotateX":0,"rotateY":0,"rotateZ":0,"buttonColor":"rgba(0, 143, 255, 1)","borderWidth":2,"fontcolor":"#fff","fontsize":30,"fontweight":"normal","fontfamily":"serif","text":"停车点"},"datas":{"calcuObject":"qhWdmohxDsU","order":[{"device":"6hjGE0x6TEDbZvmdVcyr","orderType":"属性","propertyName":"agv_parting","serviceName":null,"orderValue":null,"deviceStr":"AGV智能小车1","propertyNameStr":"小车停车位置"}],"device":null,"dataType":null,"dataName":null}}]} | string | 是 | - |
| projectId | 113 | string | 是 | - |

**认证方式**

> 无需认证

**响应示例**

* 成功(200)

```javascript
暂无数据
```

* 失败(404)

```javascript
暂无数据
```

**请求Header参数**

| 参数名 | 示例值 | 参数类型 | 是否必填 | 参数描述 |
| --- | --- | ---- | ---- | ---- |
| Accept | application/json, text/plain, */* | string | 是 | - |
| Accept-Language | zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6 | string | 是 | - |
| Connection | keep-alive | string | 是 | - |
| Cookie | _clck=1bmvt0l%7C2%7Cflj%7C0%7C1587; _ga=GA1.1.91285543.1714988103; _ga_8NW26JNFDM=GS1.1.1714988103.1.1.1714988385.60.0.0; _pk_id.1.90a4=b03866383b65f9a1.1716126958.; ajs_anonymous_id=97e7e947-5798-41da-9b77-ccfdca4feb31 | string | 是 | - |
| Origin | http://172.18.18.19 | string | 是 | - |
| Referer | http://172.18.18.19/ | string | 是 | - |
| User-Agent | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36 Edg/129.0.0.0 | string | 是 | - |
| X-Requested-With | XMLHttpRequest | string | 是 | - |
| iotToken | 2abf8afe-82c8-49a8-8fc1-ae8f72154e5d | string | 是 | - |
| token | 2abf8afe-82c8-49a8-8fc1-ae8f72154e5d | string | 是 | - |

**Query**
