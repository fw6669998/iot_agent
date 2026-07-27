## 电脑

创建一个"电脑"产品,创建一个"家用笔记本电脑"设备  
支持属性: 查看锁屏状态, 获取系统名,获取主机名  
支持服务: 锁屏, 开启远程软件  

将家用笔记本电脑接入到物联网平台,
工作目录: C:\Users\fw666\OneDrive\project\research\iot_agent\devices\computer

## 打印机

创建"打印机"产品, 并创建一个"打印机1"设备,  
支持服务: 打印.  

将打印机接入云平台, 工作目录: C:\Users\fw666\OneDrive\project\research\iot_agent\devices\printter

## 企业微信机器人

创建一个"企业微信机器人"产品, 并创建一个设备"企业微信机器人_AI通知"设置  
支持属性: 联系人(字符串,只读)  
支持服务: 添加联系人(字段:userId,name), 发送通知(字段:消息,userId(非必须))  

将企业微信机器人接入平台, 工作目录: C:\Users\fw666\OneDrive\project\research\iot_agent\devices\wechat

## 手机

创建产品"手机", 创建一个设备"我的手机"  
支持属性: 当前连接wifi名称, 当前电池电量  
支持服务: 发送系统通知, 发送语言, 控制闪光灯  

将我的手机接入到平台
手机连接信息: u0_a506@192.168.0.199, 工作代码目录: ~/phone, 通过termux-api完成动作