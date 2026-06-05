(ch6-qspi)=

# QSPI

## 概述

QSPI 是 Quad {term}`SPI` 的简写，一共有 6 线组成（SPI_CLK/SPI_CSN/SPI_D0/SPI_D1/SPI_D2/SPI_D3），常用来对接 FLASH/PSRAM 等器件。

## 功能描述

QSPI 具有以下功能特点：

- 仅支持 Master 模式。

- 支持 1 线/4 线模式。1 线模式下，支持三种帧格式：

  - Motorola 帧格式
  - TI（Texas Instruments）帧格式
  - National Microwire 帧格式

- 1 线模式下，支持串行帧长度可编程。

- 支持 {term}`DMA` 搬移操作。

- 支持接口时钟频率可编程：1 线模式下最大支持 10M 的接口频率工作，4 线模式下最大支持 32M 的接口频率工作。

## 寄存器

QSPI 即 **SPI1**，与 {ref}`SPI <ch6-spi>` 共用同一套 DesignWare SSI（v151）寄存器，基址为 **0x4402_1000**。
完整寄存器概览见 {ref}`SPI 章 <ch6-spi>` 表 6-17；QSPI 特有的多线模式由 `SPI_ENHCTL`（offset 0x0C）控制：

表6-19 SPI_ENHCTL 多线模式位（QSPI）

| 位 | 名称 | 说明 |
| --- | --- | --- |
| 0 | spi_dual_en | 双线（2 线）模式使能 |
| 1 | spi_quad_en | **四线（Quad）模式使能** —— QSPI 的核心 |
| 2 | spi_oct_en | 八线（Octal）模式使能 |

1 线模式下行为与标准 SPI 一致（帧格式、SCKDV 分频见 SPI 章）；4 线模式下 `SPI_D0~D3` 并行收发，常用于对接
NOR Flash / PSRAM。`SPI_BRS` 的 SCKDV 分频与时钟链同 SPI（见 {ref}`ch8 时钟树 <ch8-internals>`）。

