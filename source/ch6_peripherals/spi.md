(ch6-spi)=

# SPI

## 概述

{term}`SPI` 实现数据的串并、并串转换，可以作为 Master 或 Slave 与外部设备进行同步串行通信（外围设备必须支持 SPI 帧格式）。芯片的 SPI 工作参考时钟为 240MHz。

## 功能描述

SPI 具有以下功能特点：

- 支持接口时钟频率可编程。

- 作为主设备：最大支持 10M 接口频率工作。

- 作为从设备：最大支持 32M 接口频率工作。

- 支持 SPI 帧格式，分为以下三种：

  - Motorola 帧格式
  - TI（Texas Instruments）帧格式
  - National Microwire 帧格式

- 串行数据帧长度可编程：4bit～16bit。

- 支持发送 FIFO 中断、接收 FIFO 中断独立屏蔽。

- 内部提供环回测试模式。

- 支持 {term}`DMA` 操作，但不支持作为 DMA 的流控设备。

## 寄存器概览

SPI 是 Synopsys DesignWare SSI（v151）衍生控制器。SPI0 与 SPI1（即 {ref}`QSPI <ch6-qspi>`）共用同一套寄存器，
仅基址不同。寄存器概览如表 6-17 所示。

表6-17 SPI 寄存器概览（基址 SPI0：0x4402_0000、SPI1/QSPI：0x4402_1000）

| Offset | Register | Description |
| --- | --- | --- |
| 0x00 | SPI_ER | SPI 使能寄存器（`spi_en`）。 |
| 0x04 | SPI_CTRA | 控制寄存器 0（相位/极性/帧长/传输方向）。 |
| 0x08 | SPI_CTRB | 控制寄存器 1（主模式数据帧数 `nrdf`）。 |
| 0x0C | SPI_ENHCTL | 增强控制（Dual/Quad/Octal 使能）。 |
| 0x14 | SPI_BRS | 波特率分频寄存器（SCKDV）。 |
| 0x18 | SPI_DCR | DMA 控制寄存器。 |
| 0x1C/0x20 | SPI_DRDL / SPI_DTDL | DMA 接收/发送数据水线。 |
| 0x60 | SPI_DR | 数据寄存器（TX/RX FIFO 读写）。 |
| 0xBC/0xC0 | SPI_RAINSR / SPI_INSR | 原始 / 屏蔽后中断状态。 |
| 0xC4/0xF8 | SPI_INMAR / SPI_ICR | 中断屏蔽 / 中断清除。 |
| 0xC8 | SPI_SLENR | 从选使能（主模式）。 |
| 0xCC/0xD0 | SPI_TWLR / SPI_TLR | TX FIFO 水线阈值 / 当前水线。 |
| 0xD8/0xDC | SPI_RWLR / SPI_RLR | RX FIFO 水线阈值 / 当前水线。 |
| 0xE4 | SPI_WSR | 状态寄存器（FIFO/忙）。 |

## 关键寄存器位域

表6-18 SPI_CTRA / SPI_ENHCTL / SPI_WSR 关键位域

```{list-table}
:header-rows: 1

* - 寄存器
  - 位
  - 名称
  - 说明
* - SPI_CTRA
  - 0
  - soe
  - 从输出使能
* - SPI_CTRA
  - 3
  - scph
  - 时钟相位（SCPH）
* - SPI_CTRA
  - 4
  - scpol
  - 时钟极性（SCPOL）
* - SPI_CTRA
  - 17:13
  - dfs32
  - 数据帧长度 −1（4～16bit）
* - SPI_CTRA
  - 19:18
  - trsm
  - 传输方向：**0b00=收发全双工**、01=仅发、10=仅收、**0b11=EEPROM 读**
* - SPI_ENHCTL
  - 0 / 1 / 2
  - spi_dual_en / quad_en / oct_en
  - 双线 / 四线（QSPI）/ 八线模式使能
* - SPI_WSR
  - 0
  - busy
  - 1=传输进行中
* - SPI_WSR
  - 1
  - txfnf
  - TX FIFO 不满（1=有空间）
* - SPI_WSR
  - 2
  - txfe
  - TX FIFO 空
* - SPI_WSR
  - 3
  - rxfne
  - RX FIFO 非空（1=有数据）
* - SPI_WSR
  - 4 / 5
  - rxfo / txfo
  - RX / TX FIFO 溢出
```

**波特率（SPI_BRS）**：`SCK = SSI_CLK / SCKDV`，SCKDV 取偶数、最小 2。SSI_CLK 为 PLL 衍生时钟，完整两级时钟链
（480 MHz PLL → CLDO_CRG 分频 → SSI_CLK → SCKDV）见 {ref}`ch8 时钟树 <ch8-internals>` 与表 8-7（SDK 实证视图）。

```{note}
`trsm = 0b11` 是 **EEPROM 读**、不是收发——全双工应保持 `trsm = 0`。这是易错点，详见第 8 章。
```

