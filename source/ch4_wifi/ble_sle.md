(ch4-ble-sle)=

# BLE/SLE

## 概述

{term}`BLE`/SLE 部分包含 MODEM 和 {term}`MAC`，MODEM 实现调制解调功能，MAC 部分实现调度、收发控制和组包解包功能。

## 功能描述

BLE 主要特性如表 4-1 所示。

表4-1 BLE 主要特性

```{list-table}
:header-rows: 1

* - 标题
  - 描述
* - 蓝牙协议版本
  - 支持蓝牙核心规范 5.4。
* - 蓝牙模式
  - 仅支持 Low Energy only。
* - BT4.0 特性
  - 支持蓝牙规范 4.0 特性。
* - Low Energy Physical
  - Low Energy Physical Layer。
* - Low Energy Link
  - Low Energy Link Layer。
* - Enhancements to HCI for Low Energy
  - 支持 BLE 模式相关的 HCI 功能。
* - Low Energy Direct Test Mode
  - 支持 BLE 直接测试模式。
* - AES Encryption
  - 支持对数据包进行 AES 加解密。
* - BT4.1 特性
  - 支持蓝牙规范 4.1 特性。
* - Low duty cycle directed advertising
  - 支持低占空比定向广播。
* - LE Dual mode topology
  - BLE 设备可同时为 master 和 Slave。
* - Fast Advertising interval
  - 支持高占空比定向广播。
* - LE privacy v1.1
  - 支持 LE 隐私策略 v1.1。
* - LE Ping
  - 支持 LE Ping 功能。
* - Private address changes
  - 支持私有地址变更功能。
* - BT4.2 特性
  - 支持蓝牙规范 4.2 特性。
* - LE Data Packet Length Extension
  - 支持数据包长度扩展,最大可支持 250Byte。
* - LE Secure Connections
  - 支持低功耗蓝牙安全连接。
* - Link Layer privacy
  - 支持低功耗蓝牙链路层隐私策略。
* - Link Layer Extended Scanner Filter policies
  - 支持扩展扫描过滤机制。
* - BT5.0 特性
  - 支持蓝牙规范 5.0 特性。
* - 2 Msym/s PHY for LE
  - 支持 2M 传输速率。
* - LE Channel Selection Algorithm #2
  - 支持自适应跳频算法 2。
* - High Duty Cycle Non-Connectable Advertising
  - 支持高占空比非连接广播。
* - LE Long Range
  - 支持 BLE Long Range。
* - BT5.2 特性
  - 支持蓝牙规范 5.2 特性。
* - BLE Power Control
  - 支持功率控制功能。
* - 连接个数
  - 支持 4 条 BLE 连接(可选 8 条)。
* - BLE dual mode
  - BLE 设备支持的角色。
* - Master
  - 支持 LE 的 Master role。
* - Slave
  - 支持 LE 的 Slave Role。
* - PHY Update
  - 支持选择 PHY 信道。
* - Data Length Update
  - 支持选择数据包的长度。
* - 白名单个数
  - 白名单个数最大支持 8 条。
* - BLE RPA 列表
  - Device 能支持的最大的 BLE RPA 名单数目到 4 个。
* - RPA 功能
  - 支持私有可解析地址功能。广播、扫描、Init 支持 RPA 功能。
* - RPA 名单个数
  - 最大支持 4 条 RPA 条目。
* - 快速信道干扰检测
  - 支持业务间隙扫描蓝牙信道所有频点,以判断空口的干扰程度。
* - Channel map update
  - 支持信道位图更新功能。
* - 信道扫描
  - 支持扫描所有的蓝牙信道,根据扫描结果评估信道干扰程度。
```

SLE 主要特性如表 4-2 所示。

表4-2 SLE 主要特性

```{list-table}
:header-rows: 1

* - 标题
  - 描述
* - SLE 协议 1.0
  - 支持 SLE1.0 协议核心规范内容。
* - SLE 链路管理
  - 支持 SLE 链路管理。
* - 时隙调度
  - 支持系统基础时隙按 125μs 调度。
* - SLE 广播业务
  - 支持 SLE 广播链路业务。
* - Channel Scan 业务
  - 支持对通信信道进行扫描,上报信道 rssi。
* - SLE 帧格式
  - 支持 SLE1.0 协议无线帧类型。支持 SLE1.0 协议无线帧类型 1。支持 SLE1.0 协议无线帧类型 2。
* - 白名单个数
  - 白名单个数最大支持 8 条。
* - SLE 调制模式和物理层带宽
  - 支持调制解调带宽 1M/2M/4M 三种速率。支持 SLE 调制方式 GFSK-1M/GFSK-2M/GFSK-4M 三种速率。支持 QPSK 调制方式 QPSK-1M/QPSK-2M/QPSK-4M 三种速率。支持 8PSK 调制方式 8PSK-1M/8PSK-2M/8PSK-4M 三种速率。
* - SLE 码率
  - 支持帧类型 2 下,QPSK 调制 Polar 码率为 3/4。支持帧类型 2 下,8PSK 调制 Polar 码率为 3/4、1。
* - SLE 导频插值比例
  - 支持帧类型 2 下,数据信息符号导频比为 4:1、16:1。
* - 信道干扰检测
  - 支持信道扫描业务进行干扰检测。
* - 连接个数
  - 支持默认最大支持 4 条 SLE link(可选 8 条,与 BLE 共享连接数)。
```

## 工作方式

## 中断

BLE&SLE {term}`CPU` 只有 2 个主中断源 ble_irq/SLE_irq，每个中断源由多个子中断源汇和而成，CPU 响应相应中断源，通过查询中断状态寄存器来查询子中断类型。

## 加密

BLE 支持 {term}`AES`-128 加密方式，SLE 支持 SM4 和 AES-128 加密。
