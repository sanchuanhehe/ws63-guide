(ch6-spi)=

# SPI

## 概述

SPI 实现数据的串并、并串转换，可以作为 Master 或 Slave 与外部设备进行同步串行通信（外围设备必须支持 SPI 帧格式）。芯片的 SPI 工作参考时钟为 240MHz。

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

- 支持 DMA 操作，但不支持作为 DMA 的流控设备。

