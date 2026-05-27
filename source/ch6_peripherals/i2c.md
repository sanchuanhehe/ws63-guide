(ch6-i2c)=

# I2C

## 概述

I2C 模块是 {term}`APB` 总线上的从设备，是 I2C 总线上的主设备。I2C 模块的作用是完成 {term}`CPU` 对 I2C 总线上从设备的数据读写，CPU 可以连续配置多个发送的数据和接收多个数据。I2C 总线上可挂载多个从设备，芯片支持 2 个 I2C 模块（I2C0 和 I2C1）。

## 功能描述

I2C 具有以下功能特点：

- 2.0 版本的 I2C 总线协议，只支持 Master 模式。

- I2C 模块在 APB 总线上执行 APB Slave 的功能，在 I2C 总线上作为 Master，支持多主设备时的总线仲裁。

- I2C 主机可以向从机写入数据，也可以接收从机发来的数据。

- 支持 Clock synchronization 和 Bit and Byte waiting。

- 支持中断或轮询操作。

- I2C 模块支持标准地址（7bit）和扩展地址（10bit）。

- 可以工作在两种速度模式下：标准模式（100Kbit/s）、快速模式（400Kbit/s）。

- I2C 模块支持 General Call 和 Start Byte 功能。

- I2C 总线上不支持 CBUS 器件。

- 对接收到的 SDA（Serial Data and Address）和 SCL（Serial Clock Line）信号进行滤波。

- 内部包含 1 个 32×8bit 的发送 FIFO 和 1 个 32×8bit 的接收 FIFO。

- 支持硬件检测 FIFO 数据深度并发出相应中断。

- 兼容不使用 FIFO 和使用 FIFO 两种工作方式。

## 工作方式

I2C 包含以下两种工作场景：

- 主机仅对单个数据发送和接收（不使用 FIFO）。
- 主机连续发送多个数据、连续接收多个数据（使用 FIFO）。

## 不使用 FIFO

### I2C 主机发送数据流程

I2C 主机发送数据流程如图 6-2 所示。

```{figure} ../images/fig-6-2-i2c-tx-no-fifo.jpg
:name: fig-6-2
I2C 主机发送数据（不使用 FIFO）流程图
```

### I2C 主机接收数据流程

I2C 主机接收数据流程如图 6-3 所示。

```{figure} ../images/fig-6-3-i2c-rx-no-fifo.jpg
:name: fig-6-3
I2C 主机接收数据（不使用 FIFO）流程图
```

## 使用 FIFO

### I2C 主机发送数据流程

I2C 主机发送数据流程图如图 6-4 所示。

```{figure} ../images/fig-6-4-i2c-tx-fifo.jpg
:name: fig-6-4
I2C 主机发送数据（使用 FIFO）流程图
```

### I2C 主机接收数据流程

I2C 主机接收数据流程如图 6-5 所示。

```{figure} ../images/fig-6-5-i2c-rx-fifo.jpg
:name: fig-6-5
I2C 主机接收数据（使用 FIFO）流程图
```

## 寄存器概览

I2C 寄存器概览如表 6-9 所示。

表6-9 I2C 寄存器概览（基址是 I2C0：0x44018000、I2C1：0x44008100）

| 偏移地址 | 名称 | 描述 |
| --- | --- | --- |
| 0x00 | I2C_CTRL | I2C 控制寄存器。 |
| 0x04 | I2C_COM | I2C 模块的命令寄存器。 |
| 0x08 | I2C_ICR | I2C 模块的中断清除寄存器。 |
| 0x0C | I2C_SR | I2C 模块状态寄存器。 |
| 0x10 | I2C_SCL_H | I2C 总线 SCL 信号高电平周期数寄存器。 |
| 0x14 | I2C_SCL_L | I2C 总线 SCL 信号低电平周期数寄存器。 |
| 0x18 | I2C_TXR | I2C 发送数据寄存器。 |
| 0x1C | I2C_RXR | I2C 接收数据寄存器。 |
| 0x20 | I2C_FIFOSTATUS | FIFO 状态寄存器。 |
| 0x24 | I2C_TXCOUNT | 发送 FIFO 数据个数寄存器。 |
| 0x28 | I2C_RXCOUNT | 接收 FIFO 数据个数寄存器。 |
| 0x2C | I2C_RXTIDE | 接收 FIFO 的溢出阈值寄存器。 |
| 0x30 | I2C_TXTIDE | 发送 FIFO 的溢出阈值寄存器。 |
| 0x34 | I2C_FTRPER | 毛刺过滤配置寄存器。 |


## 寄存器描述

I2C_CTRL

I2C_CTRL 为 I2C 控制寄存器。

Offset Address: 0x00 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:13]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [12]
  - RW
  - int_txfifo_over_mask
  - 发送FIFO数据发送完成中断屏蔽。0:屏蔽;1:不屏蔽。
  - 0x0
* - [11]
  - RW
  - mode_ctrl
  - I2C工作模式选择。0:不使用FIFO传输模式;1:使用FIFO传输模式。
  - 0x0
* - [10]
  - RW
  - int_txtide_mask
  - 发送FIFO溢出中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [9]
  - RW
  - int_rxtide_mask
  - 接收 FIFO 溢出中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [8]
  - RW
  - i2c_en
  - I2C 使能。0: 禁止;1: 使能。
  - 0x0
* - [7]
  - RW
  - int_mask
  - I2C 中断总屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [6]
  - RW
  - int_start_mask
  - 主机开始条件发送结束中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [5]
  - RW
  - int_stop_mask
  - 主机停止条件发送结束中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [4]
  - RW
  - int_tx_mask
  - 主机发送中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [3]
  - RW
  - int_rx_mask
  - 主机接收中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [2]
  - RW
  - int_ack_err_mask
  - 从机 ACK 错误中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [1]
  - RW
  - int_arb_loss_mask
  - 总线仲裁失败中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
* - [0]
  - RW
  - int_done_mask
  - 总线传输完成中断屏蔽。0: 屏蔽;1: 不屏蔽。
  - 0x0
```

I2C_COM

I2C_COM 为 I2C 模块的命令寄存器。

<CH>在系统初始化时配置或配置前，需要清除对应中断标志。I2C_COM bit[3:0]在操作结后将自动清 0。

Offset Address: 0x04 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:5]
  - -
  - reserved
  - 保留。
  - 0x0000000
* - [4]
  - RW
  - op_ack
  - 主机作为接收器是否发送 ACK。0: 发送;1: 不发送。
  - 0x0
* - [3]
  - RW
  - op_start
  - 产生开始条件操作。0: 操作结束;1: 操作有效。
  - 0x0
* - [2]
  - RW
  - op_rd
  - 产生读操作。0: 操作结束;1: 操作有效。
  - 0x0
* - [1]
  - RW
  - op_we
  - 产生写操作。0: 操作结束;1: 操作有效。
  - 0x0
* - [0]
  - RW
  - op_stop
  - 产生停止条件操作。0: 操作结束;1: 操作有效。
  - 0x0
```

I2C_ICR

I2C_ICR 为 I2C 模块的中断清除寄存器。

```{note}
新中断到来时，I2C 模块会自动将 I2C_ICR 相应位清 0。
```

Offset Address: 0x08 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:10]
  - -
  - reserved
  - 保留。
  - 0x000000
* - [9]
  - WC
  - clr_int_txfifo_over
  - 发送FIFO数据发送完成中断标志清除。0:不清除;1:清除。
  - 0x0
* - [8]
  - WC
  - clr_int_txtide
  - 发送FIFO溢出中断标志清除。0:不清除;1:清除。
  - 0x0
* - [7]
  - WC
  - clr_int_rxtide
  - 接收FIFO溢出中断标志清除。0:不清除;1:清除。
  - 0x0
* - [6]
  - WC
  - clr_int_start
  - 主机开始条件发送结束中断标志清除。0:不清除;1: 清除。
  - 0x0
* - [5]
  - WC
  - clr_int_stop
  - 主机停止条件发送结束中断标志清除。0: 不清除;1: 清除。
  - 0x0
* - [4]
  - WC
  - clr_int_tx
  - 主机发送中断标志清除。0: 不清除;1: 清除。
  - 0x0
* - [3]
  - WC
  - clr_int_rx
  - 主机接收中断标志清除。0: 不清除;1: 清除。
  - 0x0
* - [2]
  - WC
  - clr_int_ack_err
  - 从机 ACK 错误中断标志清除。0: 不清除;1: 清除。
  - 0x0
* - [1]
  - WC
  - clr_int_arb_loss
  - 总线仲裁失败中断标志清除。0: 不清除;1: 清除。
  - 0x0
* - [0]
  - WC
  - clr_int_done
  - 总线传输完成中断标志清除。0: 不清除;1: 清除。
  - 0x0
```

I2C_SR

I2C_SR 为 I2C 模块状态寄存器。

```{note}
I2C_SR bit[1]表示 I2C 总线仲裁失败。当 I2C_SR bit[1]有效时，当前操作失败。在清 I2C_SR bit[1]之前，需要清除其他中断标志，然后清除 I2C_COM 或向 I2C_COM 写入新的操作命令，最后清除 I2C_SR bit[1]。
```

Offset Address: 0x0C Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:11]
  - -
  - reserved
  - 保留。
  - 0x000000
* - [10]
  - RO
  - int_txfifo_over
  - 发送FIFO数据发送完成中断标志。0:无中断标志产生;1:中断标志产生。
  - 0x0
* - [9]
  - RO
  - int_txtide
  - 发送FIFO溢出中断标志。0:无中断标志产生;1:中断标志产生。
  - 0x0
* - [8]
  - RO
  - int_rxtide
  - 接收FIFO溢出中断标志。0:无中断标志产生;1:中断标志产生。
  - 0x0
* - [7]
  - RO
  - bus_busy
  - 总线忙。0:空闲;1:忙。
  - 0x0
* - [6]
  - RO
  - int_start
  - 主机开始条件发送结束中断标志。0:无中断标志产生;1:中断标志产生。
  - 0x0
* - [5]
  - RO
  - int_stop
  - 主机停止条件发送结束中断标志。0:无中断标志产生;1:中断标志产生。
  - 0x0
* - [4]
  - RO
  - int_tx
  - 主机发送中断标志。0:无中断标志产生;1: 中断标志产生。
  - 0x0
* - [3]
  - RO
  - int_rx
  - 主机接收中断标志。0: 无中断标志产生;1: 中断标志产生。
  - 0x0
* - [2]
  - RO
  - int_ack_err
  - 从机 ACK 错误中断标志。0: 无中断标志产生;1: 中断标志产生。
  - 0x0
* - [1]
  - RO
  - int_arb_loss
  - 总线仲裁失败中断标志。0: 无中断标志产生;1: 中断标志产生。
  - 0x0
* - [0]
  - RO
  - int_done
  - 总线传输完成中断标志。0: 无中断标志产生;1: 中断标志产生。
  - 0x0
```

I2C_SCL_H

I2C_SCL_H 为 I2C 总线 SCL 信号高电平周期数寄存器。

```{note}
在系统初始化时配置或配置前使 I2C_CTRL bit[7]=0。
```

Offset Address: 0x10 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:16]
  - -
  - reserved
  - 保留。
  - 0x0000
* - [15:0]
  - RW
  - scl_h
  - I2C 总线 SCL 信号高电平周期数寄存器。用于配置 I2C 模块工作时 SCL 高电平周期数,配置数值乘 2 等于 SCL 高电平周期数。
  - 0x0000
```

I2C_SCL_L

I2C_SCL_L 为 I2C 总线 SCL 信号低电平周期数寄存器。

```{note}
在系统初始化时配置或配置前使 I2C_CTRL bit[7]=0。
```

Offset Address: 0x14 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:16]
  - -
  - reserved
  - 保留。
  - 0x0000
* - [15:0]
  - RW
  - scl_I
  - I2C 总线 SCL 信号低电平周期数寄存器。用于配置 I2C 模块工作时SCL 低电平周期数,配置数值乘 2等于 SCL 低电平周期数。
  - 0x0000
```

I2C_TXR

I2C_TXR 为 I2C 发送数据寄存器。

```{note}
不使用 FIFO 模式下，发送结束后，I2C 模块不会修改 I2C_TXR 内容；使用 FIFO 模式下，写入的数据会自动载入到发送 FIFO 中保存直到该数据发送结束。
```

Offset Address: 0x18 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - -
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - i2c_txr
  - 主机发送数据。用于配置 I2C 模块工作时发送数据。
  - 0x00
```

I2C_RXR

I2C_RXR 为 I2C 接收数据寄存器。

```{note}
不使用 FIFO 模式下，I2C_RXR 数据在 I2C_SR bit[3]=1 时数据有效，同时数据将保持到下一个读操作前。使用 FIFO 模式下，读取 I2C_RXR 会直接从接收 FIFO 中取数据。
```

Offset Address: 0x1C Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - -
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RO
  - i2c_rxr
  - 主机接收数据。用于主机接收从机数据。
  - 0x00
```

### I2C_FIFOSTATUS

I2C_FIFOSTATUS 为 FIFO 状态寄存器。

Offset Address: 0x20 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:4]
  - -
  - reserved
  - 保留。
  - 0x0000000
* - [3]
  - RO
  - rxfe
  - 接收FIFO空状态。0:非空;1:空。
  - 0x0
* - [2]
  - RO
  - rxff
  - 接收FIFO满状态。0:未满;1:满。
  - 0x0
* - [1]
  - RO
  - txfe
  - 发送FIFO空状态。0:非空;1:空。
  - 0x0
* - [0]
  - RO
  - txff
  - 发送FIFO满状态。0:未满;1:满。
  - 0x0
```

### I2C_TXCOUNT

I2C_TXCOUNT 为发送 FIFO 数据个数寄存器。

Offset Address: 0x24 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:6]
  - -
  - reserved
  - 保留。
  - 0x0000000
* - [5:0]
  - WC
  - txcount
  - 读该寄存器返回发送 FIFO 中的字符数,写该寄存器(任意值)将清空发送 FIFO。
  - 0x00
```

### I2C_RXCOUNT

I2C_RXCOUNT 为接收 FIFO 数据个数寄存器。

Offset Address: 0x28 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:6]
  - -
  - reserved
  - 保留。
  - 0x0000000
* - [5:0]
  - WC
  - rxcount
  - 读该寄存器返回接收FIFO中的字符数,写该寄存器(任意值)将清空接收FIFO。
  - 0x00
```

### I2C_RXTIDE

I2C_RXTIDE 为接收 FIFO 的溢出阈值寄存器。

Offset Address: 0x2C Total Reset Value: 0x0000_0001

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:6]
  - -
  - reserved
  - 保留。
  - 0x0000000
* - [5:0]
  - RW
  - rxtide
  - 设置 int_rxtide 中断的触发值。RXFIFO 中的字符个数≥I2C_RXTIDE`rxtide`时会触发接收FIFO 溢出中断。
  - 0x01
```

### I2C_TXTIDE

I2C_TXTIDE 为发送 FIFO 的溢出阈值寄存器。

<CH>TXFIFO 中的字符只有在成功发送后才会被移除。

Offset Address: 0x30 Total Reset Value: 0x0000_0001

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:6]
  - -
  - reserved
  - 保留。
  - 0x0000000
* - [5:0]
  - RW
  - txtide
  - 设置 int_txtide 中断的触发值。TXFIFO 中的字符个数≤I2C_TXTIDE`txtide`时会触发发送 FIFO 溢出中断。
  - 0x01
```

### I2C_FTRPER

I2C_FTRPER 为毛刺过滤配置寄存器。

Offset Address: 0x34 Total Reset Value: 0x0000_000F

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:4]
  - -
  - reserved
  - 保留。
  - 0x0000000
* - [3:0]
  - RW
  - ftrper
  - 毛刺过滤配置寄存器。默认 15 个时钟周期,需要 SDA 需要再 SCL为高时,电平保持的时间。scl 为高时,判断 sda 电平持续时间,单位为 ic_clk 的时钟个数,持续时间大于该值才认为该电平为接收值。注意:配置值需要≤((fic_clk/(8*fscl))-2),其中 fic_clk为 I2C 工作时钟频率,fscl 为 I2C总线传输速率。
  - 0xF
```

