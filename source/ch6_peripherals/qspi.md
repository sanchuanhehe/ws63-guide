(ch6-qspi)=

# QSPI

## 概述

QSPI 是 Quad SPI 的简写，一共有 6 线组成（SPI_CLK/SPI_CSN/SPI_D0/SPI_D1/SPI_D2/SPI_D3），常用来对接 FLASH/PSRAM 等器件。

## 功能描述

QSPI 具有以下功能特点：

- 仅支持 Master 模式。

- 支持 1 线/4 线模式。1 线模式下，支持三种帧格式：

  - Motorola 帧格式
  - TI（Texas Instruments）帧格式
  - National Microwire 帧格式

- 1 线模式下，支持串行帧长度可编程。

- 支持 DMA 搬移操作。

- 支持接口时钟频率可编程：1 线模式下最大支持 10M 的接口频率工作，4 线模式下最大支持 32M 的接口频率工作。

