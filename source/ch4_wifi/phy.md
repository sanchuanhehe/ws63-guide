(ch4-phy)=

# WiFi PHY

## 概述

WLAN PHY 实现 802.11 协议定义的物理层功能，包括：

- 802.11b 协议定义的 DSSS、CCK 调制解调
- 802.11g、802.11n、802.11ax 协议定义的 OFDM 调制解调：发送方向包括加扰、交织、编码、OFDM 调制等处理；接收方向包括 OFDM 解调、Viterbi 译码、解交织、解扰等处理；同时实现 AGC（Automatic Gain Control）、CCA（Clear Channel Assessment）、RSSI（Receive Signal Strength Indicator）功能
- RF/ABB 校准功能

## 功能描述

WiFi PHY 具有以下功能特点：

- 支持 IEEE802.11b/g/n/ax 无线局域网络通信协议，其中 ax 支持 su/ersu 的收发、 tb 帧的发送、mu 帧的接收。

- 支持 802.11b 的 DSSS、CCK，802.11g/n/ax 的 BCC(Binary Convolutional Code) 编解码，802.11n/ax 的 LDPC(Low Density Parity Check)的编码。

- 支持 2.4G Band， 802.11b/g/n/ax 支持 20MHz 信号带宽， 802.11n 支持 40MHz 信号带宽， 802.11ax（tb/mu）支持 20MHz-only 信号带宽。

- 支持 4 选 1 多天线分集，最大支持 1 个空间流；802.11n/ax 支持 STBC(Space-Time Block Code)接收; 802.11n/ax 支持 4x1 TxBF； 802.11ax 最多支持 4 用户识别并支持配置其中任一个用户接收。

- 支持雷达感知(Radar Sensing)。

- 支持 GLP(Green-tooth Low-energy Positioning)辅助同步。

- 支持 PSD(Power Spectral Desity)上报。

- 支持 CSI(Channel State Infomation)上报。

- 支持 ABB/RF 校准功能。

## 工作方式

PHY 模式初始化配置支持物理带宽为 20MHz 的 WiFi 业务收发，在业务模式下可以根据与 AP 的交互完成不同物理带宽的切换，也可以在测试模式下配置不同的物理带宽用于性能测试或问题定位。PHY 会根据不同的带宽自适应驱动配置，完成基带数据发送或接收。根据上层业务的需求，PHY 主要支持以下几种工作模式。

### 校准模式

在上电时对 ABB/RF 进行离线校准，RF 配置校准模式，复用 PHY 中部分逻辑通路进行校准计算，校准项主要包括 TXDC、TXIQ、TXPWR、RXDC、RXIQ、RXRC 等。校准完成后将结果存储在 PHY 对应配置寄存器中，在测试或业务模式下自动线控调用，优化 ABB/RF 性能。

### 测试模式

测试模式主要是常发、常收测试。常发测试指基于描述符或配置寄存器下发 TXVECTOR 来启动 RF 线控及 PHY 内部编码调制等，最终将数字 DAC 数据送给 ABB/RF 输出，多帧连续输出，配合仪器用于测试发送时各种性能指标或基本问题定位；常收测试将经过 ABB/RF 的数字 ADC 数据送给 PHY 进行解调，并将解调后的数据送给 MAC 进行 FCS（Frame Check Sequence）校验，来统计接收数据是否正确，多帧连续输入，配合仪器用于测试接收时各种性能指标或基本问题定位。

### 业务模式

业务模式下，PHY 受上层 MAC 主控，与 AP 进行收发通信。业务发送时，PHY 接收来自 MAC 的 TXVECTOR，启动 RF 线控及 PHY 编码调制等，最终将数字 DAC 送给 ABB/RF 数采。业务接收时，PHY 将来自 ABB/RF 的数字 ADC 数据经过 AGC 控制后进行解调译码，并将解析后数据送给上层 MAC 进一步处理。

### 雷达感知模式

雷达感知模式下，PHY 受上层 MAC 主控，根据业务需求启动雷达感知使能。PHY 从 PKTRAM 中读取 DAC 采样率下的雷达数据，经过校准后送给 ABB/RF；同时将经过 ABB/RF 的数字 ADC 数据经过固定增益控制后进行校准处理，校准后的 ADC 数据储存在 PKTRAM 中，并给出中断信息，CPU 收到中断信息后对存储在 PKTRAM 中的雷达数据做进一步处理，满足雷达感知业务需求。

### PSD 模式

PSD 模式下，PHY将来自 ABB/RF 的数字 ADC 数据经过 AGC 控制后进行 FFT 计算等统计，最终将 PSD 存储在内部存储空间，并以中断形式上报 CPU，CPU 收到中断后顺序将 PSD 信息读出。可以通过配置不同信道多次统计，收集数据用于再次开发利用。

### GLP 联合测距模式

支持与 GLP 联合测距，WiFi 业务下生成发送/接收初始化同步脉冲，给 GLP 提供精确的脉冲定时以及频偏估计值上报。
