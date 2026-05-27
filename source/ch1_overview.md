(ch1-overview)=

# 产品概述

## 概述

Q353333N1100 系列芯片是一款高度集成的 2.4GHz {term}`SoC` Wi-Fi、{term}`BLE` 和 SLE 的 Combo 芯片，集成 {term}`IEEE` 802.11b/g/n/ax 基带和 RF 电路，RF 电路包括功率放大器 PA、低噪声放大器 {term}`LNA`、RF balun、天线开关以及电源管理等模块；支持 HT 20MHz/40MHz、HE 20MHz 标准带宽，提供最大 150Mbit/s 物理层速率。

Q353333N1100 系列芯片 Wi-Fi 基带支持正交频分多址（OFDMA）技术，正交频分复用（{term}`OFDM`）技术，并向下兼容直接序列扩频（{term}`DSSS`）和补码键控（{term}`CCK`）技术，支持 IEEE 802.11b/g/n 协议的各种数据速率，支持 IEEE 802.11ax 协议的 MCS0~MCS9 速率。

Q353333N1100 系列芯片支持 BLE 1MHz/2MHz 频宽，支持 BLE 5.4 协议，支持 BLE Mesh 和 BLE 网关功能，最大空口速率 2Mbps。

Q353333N1100 系列芯片支持 SLE 1MHz/2MHz/4MHz 频宽，支持 SLE1.0 协议，支持 SLE 网关功能，Q353333N1100 最大空口速率 4Mbps，Q353333N1100E 最大空口速率 12Mbps。

Q353333N1100 系列芯片集成高性能 32bit 微处理器、硬件安全引擎以及丰富的外设接口，外设接口包括 {term}`SPI`、QSPI、UART、I2C、PWM、{term}`GPIO` 和多路 {term}`ADC`；芯片内置 SRAM 和 Flash，可独立运行，并支持在 Flash 上运行程序。

Q353333N11001E 支持雷达感知功能，智能感知房间内是否有人。

Q353333N1100 系列芯片支持 OpenHarmony 和第三方组件，并配套提供开放、易用的开发和调试运行环境。

Q353333N1100 系列芯片适应于智能家电等物联网智能终端领域。

## 功能描述

### Wi-Fi

- 1×1 2.4GHz 频段
- {term}`PHY` 支持 IEEE 802.11b/g/n/ax
- {term}`MAC` 支持 IEEE 802.11d/e/i/k/v/r/w
- 支持 802.11n 20MHz/40MHz 频宽，支持 802.11ax 20MHz 频宽
- 支持最大速率：150Mbit/s@HT40 MCS7，114.7Mbit/s@HE20 MCS9
- 内置 PA 和 LNA，集成 TX/RX Switch、Balun 等
- 支持 {term}`STA` 和 SoftAP 形态，作为 SoftAP 时最大支持 6 个 STA 接入
- 支持 {term}`A-MPDU`、A-MSDU
- 支持 Block-{term}`ACK`
- 支持 QoS，满足不同业务服务质量需求
- 支持 {term}`WPA`/WPA2/WPA3 Personal、WPS2.0、WAPI
- 支持 RF 自校准方案
- 支持 {term}`STBC` 和 LDPC
- 支持雷达感知功能（仅 Q353333N11001E 芯片支持）

### 蓝牙

- 低功耗蓝牙 Bluetooth Low Energy（BLE）
- 支持 BLE 5.4
- 支持 125Kbit/s、500Kbit/s、1Mbit/s、2Mbit/s 速率
- 支持多路广播
- 支持 Class 1
- 支持高功率 20dBm
- 支持 BLE Mesh，支持 BLE 网关

### 星闪

- 星闪低功耗接入技术 Sparklink Low Energy（SLE）
- 支持 SLE 1.0
- 支持 SLE 1MHz/2MHz/4MHz，最大空口速率 12Mbit/s
- 支持 Polar 信道编码
- 支持 SLE 网关

### CPU 子系统

- 高性能 32bit 微处理器，最大工作频率 240MHz
- 内嵌 {term}`SRAM` 606KB、{term}`ROM` 300KB
- 内嵌 4MB Flash

### 外围接口

- 1 个 SPI 接口、1 个 QSPI 接口、2 个 I2C 接口、1 个 I2S 接口、3 个 {term}`UART` 接口、19 个 GPIO 接口、6 路 ADC 输入、8 路 PWM（注：上述接口通过复用实现）
- 外部晶体时钟频率 24MHz、40MHz

### 其他信息

- 电源电压输入：典型值 3.3V/5V
- IO 电源电压支持 1.8V/3.3V，外接 {term}`MCU` 和调试的 UART 支持 5V tolerant
- 封装：{term}`QFN`-40，5mm×5mm
- 工作温度：-40℃～+85℃

### 遵从的标准与协议

Q353333N1100 系列芯片支持以下标准协议：

- 802.11-2020 Wireless LAN Medium Access Control (MAC) and Physical Layer (PHY) Specifications
- Bluetooth Core Specification Version 5.4
- Sparklink Wireless Communication Low Energy Air-interface Technical Requirements V01.00

## 逻辑框图

Q353333N1100 系列芯片逻辑框图如图 1-1 所示。

```{figure} images/fig-1-1-chip-block-diagram.jpg
:name: fig-1-1
Q353333N1100 系列芯片逻辑框图
```

其中，图中的各模块功能描述如表 1-1 所示。

表1-1 模块功能描述

```{list-table}
:header-rows: 1

* - 模块名
  - 功能描述
* - PMU
  - 电源管理单元。
* - REF
  - 电压参考。
* - UVLO/OVP/PWR RESET
  - 欠压/过压保护、电源复位。
* - LDO
  - 低压差线性稳压器。
* - PWRON DET
  - 上电检测。
* - CMU
  - 时钟管理单元。
* - XO
  - 晶体振荡器。
* - Clock Divider
  - 时钟分频器。
* - PLL
  - 锁相环。
* - Clock Driver
  - 时钟驱动器。
* - CPU
  - 中央处理单元。
* - DMA
  - 直接存储器访问单元。
* - SEC SUBSYS
  - 安全子系统。
* - RAM
  - 随机存取存储器。
* - ROM
  - 只读存储器。
* - QSPI
  - 4线SPI。
* - WDT
  - 看门狗单元。
* - Timer
  - 定时器。
* - RTC
  - 实时时钟单元。
* - EFUSE
  - 加解密和芯片ID存储。
* - TSENSOR
  - 温度传感器。
* - HPM
  - 工艺监视单元。
* - Wi-Fi
  - WiFi通信模块。
* - BLE
  - 低功耗蓝牙通信模块。
* - SLE
  - SLE通信模块。
* - PHY
  - 信道调制、解调。
* - MAC
  - MAC层业务处理。
* - RF&ABB
  - 射频&模拟模块。
* - GPIO
  - 通用输入输出接口。
* - UART
  - 通用异步串行接口控制器。
* - SPI
  - 串行外设接口控制器。
* - PWM
  - 脉冲宽度调制单元。
* - LSADC
  - 低速 ADC。
* - I2C
  - 集成电路互连总线控制器。
* - I2S
  - 集成电路内置音频总线控制器。
* - FLASH
  - 闪存。
* - PSRAM
  - 伪静态存储器。
```

## 应用场景

Q353333N1100 系列芯片适应于智能家电等物联网智能终端领域，典型应用框图如图 1-2 所示。

```{figure} images/fig-1-2-typical-application.jpg
:name: fig-1-2
Q353333N1100 系列芯片典型应用框图
```