(ch6-i2s)=

# I2S

## 概述

I2S 模块是 {term}`APB` 总线上的从设备、I2S 总线上的主/从设备。

## 功能描述

I2S 具有以下功能特点：

- 支持 Master/Slave 模式。
- 支持 TRX 的左右声道各自独立 FIFO，FIFO 规格为 32x8。
- 支持 8kHz/16kHz/32kHz/44.1kHz/48kHz/96kHz/128kHz。
- 支持 16/24/32 位的传输工作模式。
- 支持 I2S 协议/PCM-TDM 协议（PCM-TDM 只支持 RX 方向的 16 位传输工作模式）。

## 寄存器概览

I2S 寄存器概览如表 6-20 所示。

表6-20 I2S 寄存器概览（基址 0x4402_5000）

| Offset | Register | Description |
| --- | --- | --- |
| 0x3C | VERSION | 版本与环回测试寄存器。 |
| 0x40 | MODE | I2S / PCM 模式寄存器。 |
| 0x44 | INTSTATUS | 中断状态寄存器。 |
| 0x48 | INTCLR | 中断清除寄存器。 |
| 0x4C/0x50 | LEFT_TX / RIGHT_TX | TX 左/右声道数据。 |
| 0x54/0x58 | LEFT_RX / RIGHT_RX | RX 左/右声道数据。 |
| 0x5C/0x60 | CT_SET / CT_CLR | 控制置位 / 控制清除寄存器。 |
| 0x64 | FIFO_THRESHOLD | FIFO 水线寄存器。 |
| 0x68/0x6C | RX_STA / TX_STA | RX / TX 状态寄存器。 |
| 0x78 | DATA_WIDTH_SET | 数据位宽寄存器（16/24/32 位）。 |
| 0x84 | SIGNED_EXT | 符号扩展使能。 |
| 0x8C | INTMASK | 中断屏蔽寄存器。 |
| 0x90 | I2S_CRG | I2S 时钟/复位生成。 |
| 0x94 | I2S_BCLK_DIV_NUM | BCLK 分频值。 |
| 0x98 | I2S_FS_DIV_NUM | FS（帧同步/采样率）分频值。 |
| 0x9C | I2S_FS_DIV_RATIO_NUM | FS 分频比值。 |

## 关键寄存器

- **MODE（0x40）**：选择 I2S 还是 PCM-TDM 协议、Master/Slave。
- **CT_SET / CT_CLR（0x5C/0x60）**：分别置位 / 清除控制位（TX/RX 使能、左右声道使能等），写 1 生效。
- **DATA_WIDTH_SET（0x78）**：传输位宽 16/24/32。**INTSTATUS/INTMASK/INTCLR**：FIFO 水线等中断的查询/屏蔽/清除。
- **时钟**：MCLK 由 480 MHz WDBB 抽头经 `I2S_CRG`/`RST_I2S_DIV_CFG` 分得（约 12.288 MHz），再由
  `I2S_BCLK_DIV_NUM` / `I2S_FS_DIV_NUM` 分出 BCLK 与采样率 FS（8k～128kHz）。完整时钟链见
  {ref}`ch8 时钟树 <ch8-internals>`。

