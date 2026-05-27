(ch4-rf)=

# WiFi / BLE & SLE RF

## 概述

RF 部分包含 2.4G RX、TX、{term}`PLL` 三个模块，支持 {term}`IEEE` 802.11b/g/n/ax 20M 模式。RF 电路主要功能包括：

- 集成 TX/RX Switch
- RX 通路：{term}`LNA`、Mixer、LPF（Low Pass Filter）、{term}`VGA`（Variable Gain Amplifier）
- TX 通路：{term}`LPF`、UPC（UP Converter）、PA（Power Amplifier）
- 集成 PLL/LO（Local Oscillator）通路，为信号通路提供本振
- 集成 Radar 功能

```{figure} ../images/fig-4-1-rf-arch.jpg
:name: fig-4-1
RF 电路模块架构
```

## 功能描述

{term}`WiFi` RF 具有以下功能特点：

- RF 电路提供稳定的 LO 信号，支持收发信号的上下变频功能。

- 支持校准功能，包含：RX DC（Direct Current）校准、TX LO Leakage 校准、 TX Power 校准、TRX IQ 校准等。

## RF 性能

芯片集成 2.4G WiFi/{term}`BLE`/SLE 收发机，支持雷达功能。除雷达在 RFI 口接收外，其他功能均在 RFIO 口测试。

```{list-table}
:header-rows: 1

* - 参数
  - Sub-Item
  - 最小值
  - 典型值
  - 最大值
  - 单位
  - 测试条件
* - RF 工作频率段
  - -
  - 2400
  - -
  - 2500
  - MHz
  - 2401MHz 以下和2483.5MHz 以上频点无法满足无委会辐射要求。信道频率的选择需要遵循协议和法规要求。
* - **WiFi RX 11b 灵敏度**
  -
  -
  -
  -
  -
  -
* - 1 Mbps DSSS
  - -
  - -99
  - -98
  - dBm
  -
  -
* - 2 Mbps DSSS
  - -
  - -96
  - -95
  - dBm
  -
  -
* - 5.5 Mbps DSSS/CCK
  - -
  - -94
  - -93
  - dBm
  -
  -
* - 11 Mbps DSSS/CCK
  - -
  - -91
  - -90
  - dBm
  -
  -
* - **WiFi RX 11g 灵敏度**
  -
  -
  -
  -
  -
  -
* - BPSK, R=1/2 (6Mbps OFDM)
  - -
  - -96
  - -95
  - dBm
  -
  -
* - BPSK, R=3/4 (9Mbps OFDM)
  - -
  - -94
  - -92
  - dBm
  -
  -
* - QPSK, R=1/2 (12Mbps OFDM)
  - -
  - -93
  - -91
  - dBm
  -
  -
* - QPSK, R=3/4 (18Mbps OFDM)
  - -
  - -90
  - -89
  - dBm
  -
  -
* - 16-QAM, R=1/2 (24Mbps OFDM)
  - -
  - -87
  - -86
  - dBm
  -
  -
* - 16-QAM, R=3/4 (36Mbps OFDM)
  - -
  - -84
  - -82
  - dBm
  -
  -
* - 16-QAM, R=1/2 (48Mbps OFDM)
  - -
  - -80
  - -78
  - dBm
  -
  -
* - 64-QAM, R=3/4 (54Mbps OFDM)
  - -
  - -78
  - -76
  - dBm
  -
  -
* - **WiFi RX 11n HT20-MF 灵敏度**
  -
  -
  -
  -
  -
  -
* - HT20 MCS0
  - -
  - -95
  - -94
  - dBm
  - BCC Long PER 10%, 4096
  -
* - HT20 MCS1
  - -
  - -92
  - -91
  - dBm
  -
  -
* - HT20 MCS2
  - -
  - -90
  - -88
  - dBm
  -
  -
* - HT20 MCS3
  - -
  - -87
  - -85
  - dBm
  -
  -
* - HT20 MCS4
  - -
  - -83
  - -82
  - dBm
  -
  -
* - HT20 MCS5
  - -
  - -79
  - -78
  - dBm
  -
  -
* - HT20 MCS6
  - -
  - -77
  - -75
  - dBm
  -
  -
* - HT20 MCS7
  - -
  - -76
  - -74
  - dBm
  -
  -
* - **WiFi RX 11n HT40-MF 灵敏度**
  -
  -
  -
  -
  -
  -
* - HT40 MCS0
  - -
  - -93
  - -92
  - dBm
  -
  -
* - HT40 MCS1
  - -
  - -90
  - -88
  - dBm
  -
  -
* - HT40 MCS2
  - -
  - -87
  - -86
  - dBm
  -
  -
* - HT40 MCS3
  - -
  - -84
  - -83
  - dBm
  -
  -
* - HT40 MCS4
  - -
  - -81
  - -79
  - dBm
  -
  -
* - HT40 MCS5
  - -
  - -76
  - -75
  - dBm
  -
  -
* - HT40 MCS6
  - -
  - -74
  - -73
  - dBm
  -
  -
* - HT40 MCS7
  - -
  - -73
  - -72
  - dBm
  -
  -
* - **WiFi RX 11ax HE20 灵敏度**
  -
  -
  -
  -
  -
  -
* - HE20 MCS0
  - -
  - -96
  - -95
  - dBm
  -
  -
* - HE20 MCS1
  - -
  - -93
  - -92
  - dBm
  -
  -
* - HE20 MCS2
  - -
  - -91
  - -89
  - dBm
  -
  -
* - HE20 MCS3
  - -
  - -88
  - -87
  - dBm
  -
  -
* - HE20 MCS4
  - -
  - -84
  - -83
  - dBm
  -
  -
* - HE20 MCS5
  - -
  - -80
  - -79
  - dBm
  -
  -
* - HE20 MCS6
  - -
  - -79
  - -77
  - dBm
  -
  -
* - HE20 MCS7
  - -
  - -77
  - -75
  - dBm
  -
  -
* - HE20 MCS8
  - -
  - -73
  - -72
  - dBm
  -
  -
* - HE20 MCS9
  - -
  - -71
  - -70
  - dBm
  -
  -
* - **WiFi RX 11b 最大解调电平**
  -
  -
  -
  -
  -
  -
* - 1 Mbps DSSS
  - -
  - 0
  - -
  - dBm
  -
  -
* - 2 Mbps DSSS
  - -
  - 0
  - -
  - dBm
  -
  -
* - 5.5 Mbps DSSS/CCK
  - -
  - 0
  - -
  - dBm
  -
  -
* - 11 Mbps DSSS/CCK
  - -
  - 0
  - -
  - dBm
  -
  -
* - WiFi RX 11g 最大解调电平
  - 64-QAM, R=3/4 (54Mbps OFDM)
  - -
  - 0
  - -
  - dBm
  - PER 8%, 1000 octets PPDU
* - WiFi RX 11n HT20 最大解调电平
  - HT20 MCS7
  - -
  - 0
  - -
  - dBm
  - PER 10%, 4096 octets PPDU
* - **WiFi RX 11b 邻道抑制比**
  -
  -
  -
  -
  -
  -
* - 1Mbps DSSS
  - -
  - 48
  - -
  - dB
  - 有用信号-74dBm, PER 8%, 1024 octets PPDU
  -
* - 2Mbps DSSS
  - -
  - 59
  - -
  - dB
  - 有用信号-74dBm, PER 8%, 1024 octets PPDU
  -
* - 5.5Mbps DSSS/CCK
  - -
  - 44
  - -
  - dB
  - 有用信号-70dBm, PER 8%, 1024 octets PPDU
  -
* - 11Mbps DSSS/CCK
  - -
  - 44
  - -
  - dB
  - 有用信号-70dBm, PER 8%, 1024 octets PPDU
  -
* - **WiFi RX 11g 邻道抑制比**
  -
  -
  -
  -
  -
  -
* - BPSK, R=1/2 (6Mbps OFDM)
  - -
  - 34
  - -
  - dB
  - 有用信号-79dBm, PER 8%, 1000 octets PPDU
  -
* - BPSK, R=3/4 (9Mbps OFDM)
  - -
  - 30
  - -
  - dB
  - 有用信号-78dBm, PER 8%, 1000 octets PPDU
  -
* - QPSK, R=1/2 (12Mbps OFDM)
  - -
  - 31
  - -
  - dB
  - 有用信号-76dBm, PER 8%, 1000 octets PPDU
  -
* - QPSK, R=3/4 (18Mbps OFDM)
  - -
  - 27
  - -
  - dB
  - 有用信号-74dBm, PER 8%, 1000 octets PPDU
  -
* - 16-QAM, R=1/2 (24Mbps OFDM)
  - -
  - 27
  - -
  - dB
  - 有用信号-71dBm, PER 8%, 1000 octets PPDU
  -
* - 16-QAM, R=3/4 (36Mbps OFDM)
  - -
  - 22
  - -
  - dB
  - 有用信号-67dBm, PER 8%, 1000 octets PPDU
  -
* - 16-QAM, R=1/2 (48Mbps OFDM)
  - -
  - 19
  - -
  - dB
  - 有用信号-63dBm, PER 8%, 1000 octets PPDU
  -
* - 64-QAM, R=3/4 (54Mbps OFDM)
  - -
  - 20
  - -
  - dB
  - 有用信号-62dBm, PER 8%, 1000 octets PPDU
  -
* - **WiFi RX 11n HT20 邻道抑制比**
  -
  -
  -
  -
  -
  -
* - HT20 MCS0
  - -
  - 30
  - -
  - dB
  - 有用信号-79dBm,PER 10%, 4096octets PPDU
  -
* - HT20 MCS1
  - -
  - 29
  - -
  - dB
  - 有用信号-76dBm,PER 10%, 4096octets PPDU
  -
* - HT20 MCS2
  - -
  - 26
  - -
  - dB
  - 有用信号-74dBm,PER 10%, 4096octets PPDU
  -
* - HT20 MCS3
  - -
  - 24
  - -
  - dB
  - 有用信号-71dBm,PER 10%, 4096octets PPDU
  -
* - HT20 MCS4
  - -
  - 19
  - -
  - dB
  - 有用信号-67dBm,PER 10%, 4096octets PPDU
  -
* - HT20 MCS5
  - -
  - 17
  - -
  - dB
  - 有用信号-63dBm,PER 10%, 4096octets PPDU
  -
* - HT20 MCS6
  - -
  - 15
  - -
  - dB
  - 有用信号-62dBm,PER 10%, 4096octets PPDU
  -
* - HT20 MCS7
  - -
  - 13
  - -
  - dB
  - 有用信号-61dBm,PER 10%, 4096octets PPDU
  -
* - **WiFi RX 11n HT40 邻道抑制比**
  -
  -
  -
  -
  -
  -
* - HT40 MCS0
  - -
  - 29
  - -
  - dB
  - 有用信号-76dBm,PER 10%, 4096octets PPDU
  -
* - HT40 MCS1
  - -
  - 27
  - -
  - dB
  - 有用信号-73dBm,PER 10%, 4096octets PPDU
  -
* - HT40 MCS2
  - -
  - 24
  - -
  - dB
  - 有用信号-71dBm,PER 10%, 4096octets PPDU
  -
* - HT40 MCS3
  - -
  - 21
  - -
  - dB
  - 有用信号-68dBm,PER 10%, 4096octets PPDU
  -
* - HT40 MCS4
  - -
  - 17
  - -
  - dB
  - 有用信号-64dBm, PER 10%, 4096 octets PPDU
  -
* - HT40 MCS5
  - -
  - 13
  - -
  - dB
  - 有用信号-60dBm, PER 10%, 4096 octets PPDU
  -
* - HT40 MCS6
  - -
  - 14
  - -
  - dB
  - 有用信号-59dBm, PER 10%, 4096 octets PPDU
  -
* - HT40 MCS7
  - -
  - 10
  - -
  - dB
  - 有用信号-58dBm, PER 10%, 4096 octets PPDU
  -
* - **WIFI TX 11b 最大发射功率**
  -
  -
  -
  -
  -
  -
* - 1Mbps DSSS
  - -
  - 23
  - -
  - dBm
  -
  -
* - 2Mbps DSSS
  - -
  - 23
  - -
  - dBm
  -
  -
* - 5.5Mbps DSSS/CCK
  - -
  - 23
  - -
  - dBm
  -
  -
* - 11Mbps DSSS/CCK
  - -
  - 23
  - -
  - dBm
  -
  -
* - **WIFI TX 11g 最大发射功率**
  -
  -
  -
  -
  -
  -
* - BPSK, R=1/2 (6Mbps OFDM)
  - -
  - 21
  - -
  - dBm
  -
  -
* - BPSK, R=3/4 (9Mbps OFDM)
  - -
  - 21
  - -
  - dBm
  -
  -
* - QPSK, R=1/2 (12Mbps OFDM)
  - -
  - 21
  - -
  - dBm
  -
  -
* - QPSK, R=3/4 (18Mbps OFDM)
  - -
  - 21
  - -
  - dBm
  -
  -
* - 16-QAM, R=1/2 (24Mbps OFDM)
  - -
  - 21
  - -
  - dBm
  -
  -
* - 16-QAM, R=3/4 (36Mbps OFDM)
  - -
  - 21
  - -
  - dBm
  -
  -
* - 16-QAM, R=1/2 (48Mbps OFDM)
  - -
  - 20
  - -
  - dBm
  -
  -
* - 64-QAM, R=3/4 (54Mbps OFDM)
  - -
  - 19
  - -
  - dBm
  -
  -
* - **WIFI TX HT20-MF 最大发射功率**
  -
  -
  -
  -
  -
  -
* - MCS0
  - -
  - 20
  - -
  - dBm
  -
  -
* - MCS1
  - -
  - 20
  - -
  - dBm
  -
  -
* - MCS2
  - -
  - 20
  - -
  - dBm
  -
  -
* - MCS3
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS4
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS5
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS6
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS7
  - -
  - 18
  - -
  - dBm
  -
  -
* - **WIFI TX HT40-MF 最大发射功率**
  -
  -
  -
  -
  -
  -
* - MCS0
  - -
  - 20
  - -
  - dBm
  -
  -
* - MCS1
  - -
  - 20
  - -
  - dBm
  -
  -
* - MCS2
  - -
  - 20
  - -
  - dBm
  -
  -
* - MCS3
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS4
  - -
  - 19
  - -
  - dBm
  -
  -
* - **HE20 最大发射功率**
  -
  -
  -
  -
  -
  -
* - MCS1
  - -
  - 20
  - -
  - dBm
  -
  -
* - MCS2
  - -
  - 20
  - -
  - dBm
  -
  -
* - MCS3
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS4
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS5
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS6
  - -
  - 19
  - -
  - dBm
  -
  -
* - MCS7
  - -
  - 18
  - -
  - dBm
  -
  -
* - MCS8
  - -
  - 17
  - -
  - dBm
  -
  -
* - MCS9
  - -
  - 15
  - -
  - dBm
  -
  -
* - **LE RX 灵敏度**
  -
  -
  -
  -
  -
  -
* - LE 1M
  - -
  - -99
  - -98
  - dBm
  -
  -
* - LE 2M
  - -
  - -96
  - -95
  - dBm
  -
  -
* - LR S2 255byte
  - -
  - -100
  - -99
  - dBm
  -
  -
* - LR S8 255byte
  - -
  - -105
  - -103
  - dBm
  -
  -
* - LR S2 37byte
  - -
  - -101
  - -100
  - dBm
  -
  -
* - LR S8 37byte
  - -
  - -105
  - -104
  - dBm
  -
  -
* - **SLE RX 灵敏度**
  -
  -
  -
  -
  -
  -
* - SLE_1M GFSK
  - -
  - -99
  - -97
  - dBm
  -
  -
* - SLE_2M GFSK
  - -
  - -96
  - -94
  - dBm
  -
  -
* - SLE_4M GFSK
  - -
  - -93
  - -91
  - dBm
  -
  -
* - 1M QPSK shortHD pilot16:1 polar3/4
  - -
  - -101
  - -100
  - dBm
  -
  -
* - 2M QPSK shortHD pilot16:1 polar3/4
  - -
  - -98
  - -96
  - dBm
  -
  -
* - 4M QPSK shortHDpilot16:1polar3/4
  - -
  - -95
  - -93
  - dBm
  -
  -
* - 1M 8PSKshortHDPilot16:1polar3/4
  - -
  - -96
  - -94
  - dBm
  -
  -
* - 2M 8PSKshortHDPilot16:1polar3/4
  - -
  - -93
  - -91
  - dBm
  -
  -
* - 4M 8PSKshortHDPilot16:1polar3/4
  - -
  - -90
  - -88
  - dBm
  -
  -
* - 1M QPSKshortHDPilot_nopolar1/1
  - -
  - -96
  - -94
  - dBm
  -
  -
* - 2M QPSKshortHDPilot_nopolar1/1
  - -
  - -93
  - -92
  - dBm
  -
  -
* - 4M QPSKshortHDPilot_nopolar1/1
  - -
  - -89
  - -88
  - dBm
  -
  -
* - 1M 8PSKshortHDPilot_nopolar1/1
  - -
  - -90
  - -88
  - dBm
  -
  -
* - 2M 8PSKshortHDPilot_nopolar1/1
  - -
  - -87
  - -86
  - dBm
  -
  -
* - 4M 8PSKshortHDPilot_nopolar1/1
  - -
  - -82
  - -81
  - dBm
  -
  -
* - **LE TX 最大发射功率**
  -
  -
  -
  -
  -
  -
* - LE 1M
  - -
  - 20
  - -
  - dBm
  -
  -
* - LE 2M
  - -
  - 20
  - -
  - dBm
  -
  -
* - LR S2500K
  - -
  - 20
  - -
  - dBm
  -
  -
* -
  - LR S8125K
  - -
  - 20
  - -
  - dBm
  -
* - **SLE TX 最大发射功率**
  -
  -
  -
  -
  -
  -
* - SLE_1MGFSK
  - -
  - 20
  - -
  - dBm
  -
  -
* - SLE_2MGFSK
  - -
  - 20
  - -
  - dBm
  -
  -
* - SLE_4MGFSK
  - -
  - 20
  - -
  - dBm
  -
  -
* - 1M QPSKshortHDPilot16:1polar3/4
  - -
  - 14
  - -
  - dBm
  -
  -
* - 2M QPSKshortHDPilot16:1polar3/4
  - -
  - 14
  - -
  - dBm
  -
  -
* - 4M QPSKshortHDPilot16:1polar3/4
  - -
  - 14
  - -
  - dBm
  -
  -
* - 1M 8PSKshortHDPilot16:1polar3/4
  - -
  - 14
  - -
  - dBm
  -
  -
* - 2M 8PSKshortHDPilot16:1polar3/4
  - -
  - 14
  - -
  - dBm
  -
  -
* - 4M 8PSKshortHDPilot16:1polar3/4
  - -
  - 14
  - -
  - dBm
  -
  -
* - 1M QPSKshortHDPilot_no polar1/1
  - -
  - 14
  - -
  - dBm
  -
  -
* - 2M QPSKshortHDPilot_nopolar1/1
  - -
  - 14
  - -
  - dBm
  -
  -
* - 4M QPSK shortHD pilot_no polar1/1
  - -
  - 14
  - -
  - dBm
  -
  -
* - 1M 8PSK shortHD pilot_no polar1/1
  - -
  - 14
  - -
  - dBm
  -
  -
* - 2M 8PSK shortHD pilot_no polar1/1
  - -
  - 14
  - -
  - dBm
  -
  -
* - 4M 8PSK shortHD pilot_no polar1/1
  - -
  - 14
  - -
  - dBm
  -
  -
* - TX 输出功率精度
  - -
  - -2
  - -
  - 2
  - dB
  - -
* - TX 输出功率分辨率
  - -
  - -
  - 1
  - -
  - dB
  - BT 只能发送固定功率
```

## 说明

以上数据仿真条件为 VBAT=3.3V。
