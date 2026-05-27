(ch4-abb)=

# WiFi/BLE & SLE ABB

## 概述

ABB IP 用于 Connectivity {term}`SoC` 芯片，是支持 WiFi 802.11b/g/n/ax（2.4G mode）系统的模拟数字接口模块，根据功能分为以下 2 个功能模块：

{term}`WiFi` IQ-{term}`ADC`

WiFi IQ DAC

完成发送时的数模转换及接收时的模数转换功能。

WiFi ADC（1 个通道，通道有 IQ）、WiFi {term}`DAC`（1 个通道，通道有 IQ），以及时钟 buf 模块和 {term}`LDO`，共同包括在 Q353333N1100 WL ABB 中，时钟 buf 和 LDO 不作为独立功能模块，不在行为模型中独立体现。

```{figure} ../images/fig-4-2-abb-block.jpg
:name: fig-4-2
ABB 模块组成
```

注：{term}`WADC`（WiFi Analog Digital Converter），{term}`WDAC`（WiFi Digital Analog Converter）。

## 功能描述

ABB IP 具有以下功能特点：

- 提供 1 路 WiFi IQ ADC、1 路 WiFi IQ DAC。

- 支持 WiFi 802.11b/g/n（2.4G mode）。

## 工作方式

业务模式寄存器配置为固定一次性配置，业务工作期间无需重复配置，仅在逻辑电源掉电重新上电时需要重新配置；校正算法在温度、电压漂移下受影响，如果温度、电压变化较大，需要重新运行算法并刷新寄存器，除此情况之外无需重复配置。

校准包括：

{term}`WLAN`（Wireless Local Area Network）的 ADC 比较器校准。

WLAN DC Offset 校准。

WLAN 电容校准。

校准步骤：

步骤 1 比较器校准。

步骤 2 电容校准。

步骤 3 DC Offset 校准。
