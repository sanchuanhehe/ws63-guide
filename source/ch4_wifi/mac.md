(ch4-mac)=

# WiFi MAC

## 概述

DBB（Digital Baseband） MAC 主要完成 WiFi MAC 层的硬件处理，包括信道接入、 组解帧、数据收发、加解密、节能控制等功能。

## 功能描述

WiFi MAC 具有以下功能特点：

- 支持 IEEE802.11b/g/n/ax 无线局域网络通信协议。

- 支持 STA 模式和 AP 模式。

- 支持 2.4G Band、802.11b/a/g 20MHz；802.11n 20MHz/40MHz；802.11ax 20MHz。最大支持 1 流、1 天线。

- 支持 WPA、WPA2、AES 加解密。

- 支持 WPS2.0。

- 支持协议低功耗：PSM（Power Saving Mode）、UAPSD（Unscheduled Automatic Power Save Delivery）、P2P（Peer-to-Peer） Power Save。

## 工作方式

### AP 模式

在一个基础 BSS（Basic Service Set）网络中提供所有接入点的基本功能，包括：

- 发送 Beacon 帧声明 BSS 的存在和能力
- 为 BSS 中的客户端提供无线关联和认证服务
- 管理 BSS 网络中与之关联的客户端

芯片支持 1 个 AP。

### STA 模式

在一个基础 BSS 网络中提供扫描发现网络、加入网络并管理与 AP 的连接以提供数据收发服务的功能。

芯片支持 2 个 STA。

### Monitor 模式

芯片进入 Monitor 模式，实现网卡的功能，MAC 将接收到的所有帧上报软件。

### AP 与 STA 共存

芯片支持 1 个 AP 和 1 个 STA 同时工作。

芯片支持 2.4G 下 AP/STA 在相同或不同信道的并发，分别对应同频共存和异频共存。

```{important}
STA 上电后会进行信道扫描，导致信道切换，因此开启 AP/STA 动态共存时，需要先创建 STA，再创建 AP，否则将会影响 AP 的工作信道。
```

### CSI 模式

CSI（Channel State Information）模式支持将 PHY 上报的信道状态信息过滤后上报软件：

- 支持 11g/11n/11ax 的 CSI 信息上报，不支持 11b
- 支持对将提取 CSI 的帧进行源地址过滤，源地址过滤列表（白名单）共 6 个（关联设备使用 LUT（Lookup Table）中的地址内容）
- 支持 6 个 CSI 采样周期，CSI 采样周期与白名单绑定，一个白名单对应一个采集周期
- 支持白名单、采样周期、特定帧类型等匹配条件，满足匹配条件才上报 CSI 信息
- 支持带宽（20MHz、40MHz）、帧格式（NON-HT、HT-MF）、RSSI（Received Signal Strength Indicator）、SNR（Signal Noise Ratio）随 CSI 信息上报（不支持 STBC 帧上报），上报 L-LTF H 矩阵数据
