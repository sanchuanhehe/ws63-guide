(ch6-uart)=

# UART

## 概述

通用异步收发器 {term}`UART`（universal asynchronous receiver/transmitter）是一个异步串行的通信接口，UART 主要用于和外部芯片的 UART 进行对接，实现两芯片间的通信。

芯片提供 3 个 UART 单元（UART0/1/2），UART0 仅支持两线模式，UART1/2 支持流控功能。

## 功能描述

UART 具有以下功能特点：

- 支持 64x8bit 的发送 FIFO 和 64x10bit 的接收 FIFO（First In First Out）。

- 支持可编程数据位宽 5/6/7/8 bit。

- 支持可编程停止位宽 1/1.5/2 bit。

- 支持奇/偶校验或者无校验位，支持校验位为软件设定值。

- 支持波特率可编程（整数分频和小数分频，小数分频的参数 DLF_SIZE 为 6）。

- 支持接收 FIFO 中断、发送 FIFO 中断、接收超时中断、错误中断。

- 支持中断状态查询。

- UART0 不支持硬件流控，UART1 和 UART2 支持硬件流控。

- 支持三种数据搬运方式：

  - {term}`DMA` 方式
  - 中断方式
  - 软件查询方式

## 工作方式

## 接口信号

UART 接口信号描述如表 UART 接口信号描述所示。

表6-6 UART 接口信号描述

| 信号名 | 宽度(bit) | 方向 | 功能描述 |
| --- | --- | --- | --- |
| RXD | 1 | I | 输入数据。 |
| TXD | 1 | O | 输出数据。 |
| CTS | 1 | I | 清除发送信号,用于硬件流控,低有效。 |
| RTS | 1 | O | 请求发送信号,用于硬件流控,低有效。 |


### UART 数据格式

```{important}
整数波特率寄存器和小数波特率寄存器的值必须等到当前数据发送和接收完毕才更新。
```


UART 的数据帧格式如图 6-1 所示。其中数据帧长度、停止位位数和奇偶检验可配置。

```{figure} ../images/fig-6-1-uart-data-format.jpg
:name: fig-6-1
UART 数据帧格式
```

## 中断或查询方式下的数据传输

初始化步骤如下：

步骤 1 配置 IO 复用关系，IO 暂不复用为 UART，防止初始化过程中 UART 被对端影响。

步骤 2 配置 HALT_TX`halt_tx`=1，停止 TX 功能，防止初始化过程中触发 TX。

步骤 3 配置 INTR_EN=0，屏蔽 UART 所有中断。

步骤 4 向 FIFO_CTL`rx_fifo_rst`和 FIFO_CTL`tx_fifo_rst`写 1，分别复位 RX FIFO 和 TX FIFO。

步骤 5 配置 BAUD_CTL`baud_div`，根据需要配置波特率过采样倍数。

步骤 6 配置 UART_CTL`div_en`=1，准备开始配置波特率。

步骤 7 配置 DIV_H、DIV_L、DIV_FRA，确定波特率。配置值计算方法为：分频值=工作时钟频率/（波特率×波特率过采样倍数），{DIV_H, DIV_L}组成分频值的整数部分， DIV_FRA = 分频率的小数部分×64。

步骤 8 配置 UART_CTL`stp`、UART_CTL`pen`、UART_CTL`eps`、UART_CTL`dlen`，根据需要配置帧格式， 以上寄存器分别控制停止位位宽，奇偶校验使能，奇偶校验选择和数据位长度。

步骤 9 配置 MODEM_CTL`afc_en`和 MODEM_CTLL`rts`，根据需要配置自动流控。

表6-7 自动流控配置参考

| 场景 | MODEM_CTL`afc_en`配置值 | MODEM_CTL`rts`配置值 |
| --- | --- | --- |
| 打开自动流控 | 1 | 1 |
| 关闭自动流控,反压对端 | 0 | 0 |
| 关闭自动流控,正常 RX | 0 | 1 |


步骤 10 配置 FIFO_CTL`rx_empty_trig`和 FIFO_CTL`tx_empty_trig`，设定发送及接收 FIFO 水线。

步骤 11 配置 FIFO_CTL`fifo_en`=1，使能 TX FIFO 和 RX FIFO。

步骤 12 配置 INTR_EN=0x1f，恢复中断使能。

步骤 13 恢复 IO 复用，将 IO 复用为 UART。

步骤 14 配置 HALT_TX`halt_tx`=0，使能 TX 功能。

数据发送步骤如下：

步骤 1 将发送数据写入 DATA`data`，启动数据发送。若为查询模式则跳转至步骤 2，若为中断模式则跳转至步骤 3。

步骤 2 查询方式下，如果进行连续数据发送，需要通过读取 FIFO_STATUS`tx_fifo_full`检测 TX FIFO 状态。如果 FIFO_STATUS`tx_fifo_full`为 0，即 TX FIFO 未满，则可以向 TX FIFO 中发送数据。直到无数据需要发送，跳转至步骤 4。

步骤 3 中断方式下，在中断服务程序中查询 INTR_STATUS`thre_intr_status`发送中断状态位，决定是否向 TX FIFO 中发送数据。当 INTR_STATUS`thre_intr_status`置 1，此时 TX FIFO 内数据量小于发送数据水线，可以向 TX FIFO 中发送数据。直到无数据需要发送，跳转至步骤 4。

步骤 4 通过检测 INTR_STATUS`tx_fifo_empty`是否为 1，判断 UART 是否完成全部数据发送。

数据接收的处理方式如下：

步骤 1 等待数据接收，若为查询模式则跳转至步骤 2。若为中断模式则跳转至步骤 3。

步骤 2 查询方式下，进行数据接收时通过读取 INTR_STATUS`rx_fifo_empty`检测 RX_FIFO 状态，如果 INTR_STATUS`rx_fifo_empty`为 0，则 RX_FIFO 非空，可以读取 RX_FIFO 中的数据，跳转至步骤 4。

步骤 3 中断方式下，则检测 INTR_STATUS`data_avail_intr_status`接收中断状态位，决定是否读取 RX_FIFO 中的数据。当 INTR_STATUS`data_avail_intr_status`置 1，此时 RX_FIFO 内数据量大于接收 FIFO 水线，可以读取 RX_FIFO 中数据，跳转至步骤 4。

步骤 4 回读 DATA`data`，读出数据即为 RX 数据。

## 寄存器概览

UART 寄存器概览如表 6-8 所示。

表6-8 UART 寄存器概览（基址是 UART0：0x44010000、UART1：0x44011000、UART2：0x44012000）

| 偏移地址 | 名称 | 描述 |
| --- | --- | --- |
| 0x00 | INTR_ID | 中断 ID 寄存器。 |
| 0x4 | DATA | 数据寄存器。 |
| 0x8 | UART_CTL | UART 控制寄存器。 |
| 0xC | DIV_H | 分频系数(高位)寄存器。 |
| 0x10 | DIV_L | 分频系数(低位)寄存器。 |
| 0x14 | DIV_FRA | 分频系数(小数部分)寄存器。 |
| 0x18 | INTR_EN | 中断使能寄存器。 |
| 0x1C | INTR_STATUS | 中断状态寄存器。 |
| 0x24 | FIFO_CTL | FIFO 控制寄存器。 |
| 0x28 | FAR | FIFO 存取模式使能寄存器。 |
| 0x2C | MODEM_CTL | Modem 控制寄存器。 |
| 0x30 | MODEM_STATUS | Modem 状态寄存器。 |
| 0x34 | LINE_STATUS | Line 状态寄存器。 |
| 0x38 | UART_GP_REG | Uart 通用寄存器。 |
| 0x3C | TX_FIFO_READ | 发送 FIFO 读取寄存器。 |
| 0x40 | RX_FIFO_WRITE | 接收 FIFO 写入寄存器。 |
| 0x44 | FIFO_STATUS | FIFO 状态寄存器。 |
| 0x48 | TX_FIFO_CNT | 发送 FIFO 数据计数器。 |
| 0x4C | RX_FIFO_CNT | 接收 FIFO 数据计数器。 |
| 0x50 | HALT_TX | 传输挂起寄存器。 |
| 0x54 | DMA_SW_ACK | DMA 应答寄存器。 |
| 0x58 | BAUD_CTL | 波特率控制寄存器。 |
| 0x5C | STP_CTL | 停止位控制寄存器。 |
| 0x60 | UART_PARAMETER | UART 参数寄存器。 |


## 寄存器描述

INTR_ID

INTR_ID 为中断 ID 寄存器。

Offset Address：0x00 Total Reset Value：0x0001

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:5]
  - -
  - reserved
  - 保留。
  - 0x000
* - [4]
  - RO
  - fifo_en_s
  - FIFO 使能控制。0: FIFO 禁用;1: FIFO 使能。
  - 0x0
* - [3:0]
  - RO
  - intr_id
  - 中断 ID。0x0: modem 状态;0x1: 无中断请求;0x2: THR 空标志;0x4: 接收数据到达;0x6: 接收数据线状态;0x7: busy 状态;0xc: 字符超时;others: 未定义。
  - 0x1
```

### DATA

DATA 为数据寄存器。

Offset Address：0x4 Total Reset Value：0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7:0]
  - RW
  - data
  - 寄存器写入:若使能FIFO_CTL`fifo_en`,写入该寄存器的数据将被发送至txfifo;若未使能FIFO_CTL`fifo_en`,写入该寄存器的数据将被存储于transmitter holding寄存器(简称thr,tx fifo的底端存储位置)。寄存器读取:该寄存器包含从串行输入端口(sin)接收的数据。若FIFO_CTL`fifo_en`未使能,当前数据必须在下一个接收数据到来前读取,否则将被覆盖,并产生over-run错误;若使能FIFO_CTL`fifo_en`,通过该寄存器可访问rx fifo。若rx fifo已满,且在下一接收数据到来前没有读取该寄存器,虽然rx fifo内已有的数据不受影响,但后续到来的数据将丢失,并产生over-run错误。
  - 0x00
```

### UART_CTL

UART_CTL 为 UART 控制寄存器。

Offset Address：0x8 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7]
  - RW
  - stp
  - 停止位宽。0: 1bit 停止位;1: UART_CTL`dlen`为零时 1.5bit 停止位,否则 2bit 停止位。注意: 只有当STP_CTL`stp_mode`==0 时,该寄存器才生效。
  - 0x0
* - [6]
  - RW
  - sps
  - 粘性奇偶校验位选择。0: 禁用粘性奇偶校验;1: 使能粘性就校验。
  - 0x0
* - [5]
  - RW
  - pen
  - 奇偶校验使能。0: 禁用奇偶校验;1: 使能奇偶校验。
  - 0x0
* - [4]
  - RW
  - eps
  - 奇偶校验模式选择。0: 选择奇校验模式;1: 选择偶校验模式。
  - 0x0
* - [3:2]
  - RW
  - dlen
  - 数据长度。00: 每个字符 5bit 数据;01: 每个字符 6bit 数据;10: 每个字符 7bit 数据;11: 每个字符 8bit 数据。
  - 0x0
* - [1]
  - RW
  - xbreak
  - Break 控制位。0: 串行输出已经释放可用于数据传输;1: 串行输出强制置于空白状态。
  - 0x0
* - [0]
  - RW
  - div_en
  - UART 分频器使能寄存器。0: DIV_L 与 DIV_H 两寄存器仅在UART 非 Busy 状态可写入;1:DIV_L 与 DIV_H 两寄存器可在任意时刻读写。注意:本芯片 UART 始终处于非Busy 状态。
  - 0x0
```

DIV_H

DIV_H 为分频系数(高位)寄存器。

Offset Address: 0xC Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7:0]
  - RW
  - div_h
  - 分频器分频系数整数部分高 8bit。该寄存器仅在 UART_CTL`div_en`置位且 UART 非忙状态下可以存取。
  - 0x00
```

DIV_L

DIV_L 为分频系数(低位）寄存器。

Offset Address: 0x10 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7:0]
  - RW
  - div_l
  - 分频器分频系数整数部分低 8bit。该寄存器仅在 UART_CTL`div_en`置位且 UART 非忙状态下可以存取。
  - 0x00
```

DIV_FRA

DIV_FRA 为分频系数（小数部分）寄存器。

Offset Address: 0x14 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:6]
  - -
  - reserved
  - 保留。
  - 0x000
* - [5:0]
  - RW
  - div_fra
  - 分频器分频系数小数部分。分频器所用实际分频系数的小数部分为该值除以2^6。
  - 0x00
```

### INTR_EN

INTR_EN 为中断使能寄存器。

Offset Address: 0x18 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:5]
  - -
  - reserved
  - 保留。
  - 0x000
* - [4]
  - RW
  - ptim_en
  - 可编程THRE中断模式使能。0:禁用可编程THRE中断模式;1:使能可编程THRE中断模式。
  - 0x0
* - [3]
  - RW
  - tran_em_intr_en
  - 发送数据为空中断使能。0:禁用发送为空中断;1:使能发送为空中断。
  - 0x0
* - [2]
  - RW
  - rece_data_intr_en
  - 接收数据到达中断使能。0:禁用接收数据到达中断;1:使能接收数据到达中断。
  - 0x0
* - [1]
  - RW
  - modem_intr_en
  - Modem状态中断使能。0(DISABLED):禁用Modem状态中断;1(ENABLED):使能Modem状态中断。
  - 0x0
* - [0]
  - RW
  - rece_line_stat_intr_en
  - 接收数据线状态中断使能。0:禁用接收数据线状态中断;1:使能接收数据线状态中断。
  - 0x0
```

### INTR_STATUS

INTR_STATUS 为中断状态寄存器。

Offset Address: 0x1C Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:6]
  - -
  - reserved
  - 保留。
  - 0x000
* - [5]
  - RO
  - line_intr_status
  - 接收数据线中断。1: 中断有效;0: 无中断。注意: 需要使能INTR_EN`rece_line_stat_intr_en`, 否则本中断保持为0。
  - 0x0
* - [4]
  - RO
  - data_avail_intr_status
  - 接收数据到达中断。1: 中断有效;0: 无中断。注意: 需要使能INTR_EN`rece_data_intr_en`, 否则本中断保持为0。
  - 0x0
* - [3]
  - RO
  - char_to_intr_status
  - 字符超时中断。1: 中断有效;0: 无中断。注意: 需要使能FIFO_CTL`fifo_en`和INTR_EN`rece_data_intr_en`, 否则本中断保持为0。
  - 0x0
* - [2]
  - RO
  - thre_intr_status
  - THR 空中断。1: 中断有效;0: 无中断。注意:需要使能INTR_EN`tran_em_intr_en`,否则本中断保持为0。
  - 0x0
* - [1]
  - RO
  - modem_intr_status
  - Modem状态中断。1:中断有效;0:无中断。注意:需要使能INTR_EN`modem_intr_en`,否则本中断保持为0。
  - 0x0
* - [0]
  - RO
  - busy_det_intr
  - 忙状态监测中断。1:中断有效;0:无中断。注意:本芯片UART始终处于非Busy状态,即该寄存器保持0。
  - 0x0
```

FIFO_CTL

FIFO_CTL 为 FIFO 控制寄存器。

Offset Address: 0x24 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:7]
  - -
  - reserved
  - 保留。
  - 0x000
* - [6]
  - WO
  - rx_fifo_rst
  - 接收FIFO复位请求。0:不复位;1:复位。
  - 0x0
* - [5]
  - WO
  - tx_fifo_rst
  - 发送FIFO复位请求。0:不复位;1:复位。
  - 0x0
* - [4]
  - WO
  - fifo_en
  - FIFO使能。0:禁用FIFO;1:使能FIFO。
  - 0x0
* - [3:2]
  - WO
  - rx_empty_trig
  - 接收空中断触发条件设置。00:FIFO 内存在 1 个字符;01:FIFO 1/4 满;10:FIFO 1/2 满;11:距 FIFO 满状态少 2 个字符以内。
  - 0x0
* - [1:0]
  - WO
  - tx_empty_trig
  - 发送空中断触发条件设置。00:FIFO 为空;01:FIFO 内存在 2 个字符;10:FIFO 1/4 满;11:FIFO 1/2 满。
  - 0x0
```

### FAR

FAR 为 FIFO 存取模式使能寄存器。

Offset Address: 0x28 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:1]
  - -
  - reserved
  - 保留。
  - 0x0000
* - [0]
  - RW
  - far
  - 使能 FIFO 存取模式。出于测试目的,FIFO 存取模式允许 Master 写入接收 FIFO、读取发送 FIFO。0:禁用;1:使能。
  - 0x0
```

### MODEM_CTL

MODEM_CTL 为 Modem 控制寄存器。

Offset Address: 0x2C Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:6]
  - -
  - reserved
  - 保留。
  - 0x000
* - [5]
  - RW
  - out2
  - 可编程接口 OUT2。0: out2_n 端口撤离;1: out2_n 端口有效。注意:该寄存器无用。
  - 0x0
* - [4]
  - RW
  - out1
  - 可编程接口 OUT1。0: out1_n 端口撤离;1: out1_n 端口有效。注意:该寄存器无用。
  - 0x0
* - [3]
  - RW
  - dtr
  - 数据终端 ready。0: dtr_n 端口撤离;1: dtr_n 端口有效。注意:该寄存器无用。
  - 0x0
* - [2]
  - RW
  - rts
  - 自动流控 RTS 软控信号。0: 反压对端, rts_n=1;1: 自动流控 RTS 软控信号。注意:当MODEL_CTL`afc_en`==1 且FIFO_CTL`fifo_en`==1 时, 自动流控 RTS 由硬件逻辑接管, 此时本寄存器无效。
  - 0x0
* - [1]
  - RW
  - lb_mode
  - 环回模式控制。0: 禁用;1: 使能。
  - 0x0
* - [0]
  - RW
  - afc_en
  - 自动流控模式使能。0: 禁用;1: 使能。
  - 0x0
```

### MODEM_STATUS

MODEM_STATUS 为 Modem 状态寄存器。

Offset Address: 0x30 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7]
  - RO
  - dsr
  - 数据已准备指示寄存器。用于指示调制解调器控制线 dsr_n 的当前状态。在环回模式(MODEM_CTL[lb_mode==1])下,本寄存器值取自与MODEM_CTL`dtr`。0: dsr_n 信号线高电平;1: dsr_n 信号线为低电平。注意:本芯片 UART 的 dsr_n 恒为 1。
  - 0x0
* - [6]
  - RO
  - ddsr
  - dsr_n 跳变指示寄存器,指示 dsr 是否有跳变。0: dsr_n 信号线无变化;1: dsr_n 信号线存在变化。
  - 0x0
* - [5]
  - RO
  - ri
  - 响铃指示寄存器。用于指示调制解调器控制线 ri_n 的当前状态。在环回模式(MODEM_CTL[lb_mode==1])下,本寄存器值取自MODEM_CTL`out1`。0: ri_n 信号线为高电平;1: ri_n 信号线为低电平。注意:本芯片 UART 的 ri_n 恒为 1。
  - 0x0
* - [4]
  - RO
  - teri
  - ri_n 上升沿指示寄存器。0: 未检测到 ri_n 上升沿;1:检测到ri_n的上升沿。
  - 0x0
* - [3]
  - RO
  - dcd
  - 数据载波检测寄存器。用于指示modem控制线 dcd_n 的当前状态。在环回模式(MODEM_CTL[lb_mode==1])下,本寄存器值取自MODEL_CTL`out2`。0:dcd_n 信号线为高电平;1:dcd_n 信号线为低电平。注意:本芯片 UART 的 dcd_n 恒为 1。
  - 0x0
* - [2]
  - RO
  - ddcd
  - dcd_n 跳变指示寄存器,指示 dcd 是否有跳变。0:dcd_n 信号线无变化;1:dcd_n 信号线存在变化。
  - 0x0
* - [1]
  - RO
  - cts
  - CTS 信号状态。0:cts_n 信号线为高电平;1:cts_n 信号线为低电平。
  - 0x0
* - [0]
  - RO
  - dcts
  - 该 bit 位用于指示 Modem 的CTS_N 数据线从上一次读取MODEM_STATUS 寄存器后是否发生过变化。0:无变化;1:存在变化。
  - 0x0
```

### LINE_STATUS

LINE_STATUS 为 Line 状态寄存器。

Offset Address: 0x34 Total Reset Value: 0x00C0

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7]
  - RO
  - tx_empty_s
  - 发射器空标志。若FIFO使能,该bit在发送器的移位寄存器与发送FIFO同时为空时置位;当FIFO禁用时,该bit在thr寄存器与移位寄存器同时位空时置位。0:发送器非空;1:发送器为空。
  - 0x1
* - [6]
  - RO
  - thre_s
  - thr寄存器为空标志。在INTR_EN`ptim_en`使能的前提下,如果FIFO_CTL`fifo_en`也使能,该bit位在发送FIFO位满时置位;当FIFO_CTL`fifo_en`未使能,该bit位在thr寄存器为空时置位。0:THRE中断控制禁用;1:THRE中断控制使能。
  - 0x1
* - [5]
  - RO
  - data_available
  - 指示RBR或接收FIFO内至少存在1个字符。非FIFO模式下该bit位在RBR倍读取后清零,在FIFO模式下该bit位在接收FIFO为空时清零。0:数据未准备好;1:数据已准备好。
  - 0x0
* - [4]
  - RO
  - break_intr
  - 指示串行输入数据中是否检测到break序列。0:无break序列;1:检测到break序列。
  - 0x0
* - [3]
  - RO
  - overrun_err
  - Overrun错误,读取LINE_STATUS寄存器清零该bit位。0:无 overrun 错误;1:发送 overrun 错误。
  - 0x0
* - [2]
  - RO
  - parity_err
  - 奇偶校验错误,读取LINE_STATUS 寄存器清零该 bit 位。0:无奇偶校验错误;1:奇偶校验报错。
  - 0x0
* - [1]
  - RO
  - frame_err
  - 帧错误,读取 LINE_STATUS 寄存器清零该 bit 位。0:无帧错误;1:帧错误。
  - 0x0
* - [0]
  - RO
  - rx_fifo_err
  - 接收 FIFO 错误状态指示。该 bit 位仅在 FIFO 使能时生效。当存在错误的字符位于接收 FIFO 顶部且后续数据无错误,那么在读取 LSR 后该 bit 位清零。0:接收 FIFO 无错误;1:接收 FIFO 报错。
  - 0x0
```

### UART_GP_REG

UART_GP_REG 为 Uart 通用寄存器。

Offset Address: 0x38 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7:0]
  - RW
  - uart_gp_reg
  - 为开发者提供临时存储空间,在UART ip内无明确定义。
  - 0x00
```

### TX_FIFO_READ

TX_FIFO_READ 为发送 FIFO 读取寄存器。

Offset Address: 0x3C Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7:0]
  - RO
  - tx_fifo_read
  - tx fifo 读数据寄存器。当FIFO_CTL`fifo_en`被使能,读取该寄存器将返回 tx fifo 顶部数据,每个连续的读取会对 tx fifo 进行 POP 操作,并返回当前在 tx fifo 顶部的数据;当 FIFO_CTL`fifo_en`未被使能,读取该寄存器将返回 DR 中的数据。
  - 0x00
```

### RX_FIFO_WRITE

RX_FIFO_WRITE 为接收 FIFO 写入寄存器。

Offset Address: 0x40 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:10]
  - -
  - reserved
  - 保留。
  - 0x00
* - [9]
  - WO
  - rx_fifo_fe
  - 接收FIFO帧错误。0:无错误;1:帧错误。
  - 0x0
* - [8]
  - WO
  - rx_fifo_pe
  - 接收FIFO奇偶校验错误。0:校验位错误;1:无错误。
  - 0x0
* - [7:0]
  - RW
  - rx_fifo_write
  - 写操作:向rx fifo写数据。该寄存器仅在FIFO存取模式使能(FAR`far`==1)时生效。当FIFO_CTL`fifo_en`使能时,写入该寄存器的数据将被压入rx fifo。每个连续的写操作会连续压入新数据至 rx fifo 的下一写入位置;当FIFO_CTL`fifo_en`未被使能,写入该寄存器的数据将被压入 DR。读操作:返回 rx_fifo_level[6:0],指示 rx fifo 内的数据量。
  - 0x00
```

### FIFO_STATUS

FIFO_STATUS 为 FIFO 状态寄存器。

Offset Address: 0x44 Total Reset Value: 0x0002

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:4]
  - -
  - reserved
  - 保留。
  - 0x000
* - [3]
  - RO
  - rx_fifo_empty
  - rx fifo 空标志。0: 接收 FIFO 非空;1: 接收 FIFO 为空。
  - 0x1
* - [2]
  - RO
  - rx_fifo_full
  - rx fifo 满标志。0: 接收 FIFO 非满;1: 接收 FIFO 为满。
  - 0x0
* - [1]
  - RO
  - tx_fifo_empty
  - tx fifo 空标志。0: 发送 FIFO 非空;1: 发送 FIFO 为空状态。
  - 0x1
* - [0]
  - RO
  - tx_fifo_full
  - tx fifo 满标志。0: 发送 FIFO 非满;1: 发送 FIFO 为满。
  - 0x0
```

### TX_FIFO_CNT

TX_FIFO_CNT 为发送 FIFO 数据计数器。

Offset Address: 0x48 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:7]
  - -
  - reserved
  - 保留。
  - 0x000
* - [6:0]
  - RO
  - tx_fifo_level
  - tx fifo 数据计数器。用于指示 tx fifo 内数据量。
  - 0x00
```

### RX_FIFO_CNT

RX_FIFO_CNT 为接收 FIFO 数据计数器。

Offset Address: 0x4C Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:7]
  - -
  - reserved
  - 保留。
  - 0x000
* - [6:0]
  - RO
  - reserved
  - 保留。
  - 0x00
```

### HALT_TX

HALT_TX 为传输挂起寄存器。

Offset Address: 0x50 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:1]
  - -
  - reserved
  - 保留。
  - 0x0000
* - [0]
  - RW
  - halt_tx
  - TX 功能挂起使能。0:禁用传输挂起功能;1:使能传输挂起功能。
  - 0x0
```

### DMA_SW_ACK

DMA_SW_ACK 为 DMA 应答寄存器。

Offset Address: 0x54 Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:1]
  - -
  - reserved
  - 保留。
  - 0x0000
* - [0]
  - WC
  - dma_sw_ack
  - DMA 软件应答。0: 未应答;1: DMA 软件应答。
  - 0x0
```

BAUD_CTL

BAUD_CTL 为波特率控制寄存器。

Offset Address: 0x58 Total Reset Value: 0x007F

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:8]
  - -
  - reserved
  - 保留。
  - 0x00
* - [7:4]
  - RW
  - sample_phase
  - 接收采样相位。
  - 0x7
* - [3:0]
  - RW
  - baud_div
  - 波特率过采样倍数。0x7: 8 倍波特率采样;0xF: 16 倍波特率采样;其他: 不支持。
  - 0xF
```

STP_CTL

STP_CTL 为停止位控制寄存器。

Offset Address: 0x5C Total Reset Value: 0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:3]
  - -
  - reserved
  - 保留。
  - 0x0000
* - [2]
  - RW
  - stp_mode
  - 停止位控制模式。0: 接收与发送的停止位位宽由UART_CTL`stp`控制;1: 发送停止位位宽受STP_CTL`tx_sp`控制,接收停止位位宽受 STP_CTL`rx_sp`控制。
  - 0x0
* - [1]
  - RW
  - tx_sp
  - 发送停止位位宽。0: 1bit 停止位;1: 当 UART_CTL`dlen`为零,1.5bit 停止位,否则 2bit 停止位。注意: 只有当 stp_mode 置位,STP_CTL`tx_sp`才生效。
  - 0x0
* - [0]
  - RW
  - rx_sp
  - 接收停止位位宽。0: 1bit 停止位;1: 当 UART_CTL`dlen`为零,1.5bit 停止位,否则 2bit 停止位。注意: 只有当 stp_mode 置位,STP_CTL`rx_sp`才生效。
  - 0x0
```

### UART_PARAMETER

UART_PARAMETER 为 UART 参数寄存器。

Offset Address: 0x60 Total Reset Value: 0x0D04

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:13]
  - -
  - reserved
  - 保留。
  - 0x0
* - [12]
  - RO
  - shadow
  - SHADOW 功能使能。0:禁用;1:使能。
  - 0x0
* - [11]
  - RO
  - dma_mode
  - DMA 模式查询。0: DMA_EXTRA 禁用;1: DMA_EXTRA 使能。
  - 0x1
* - [10]
  - RO
  - afce_mode
  - AFCE 模式查询。0: AFCE 模式禁用;1: AFCE 模式使能。
  - 0x1
* - [9:8]
  - RO
  - apb_data_width
  - 总线接口宽度查询寄存器。00: APB 数据位宽 8bit;01: APB 数据位宽 16bit;10: APB 数据位宽 32bit;11: 未定义。注意:本芯片 UART APB 数据位宽固定为 16bit,故该寄存器值固定为 0x1。
  - 0x1
* - [7:0]
  - RO
  - fifo_depth
  - UART 接收发送 FIFO 深度。0x0: FIFO 深度为 0;0x1: FIFO 深度为 16;0x2: FIFO 深度为 32;0x4: FIFO 深度为 64;0x8: FIFO 深度为 128;0x10: FIFO 深度为 256;0x20: FIFO 深度为 512;0x40: FIFO 深度为 1024;0x80: FIFO 深度为 2048;其他:未定义。注意:本芯片 UART FIFO 深度固定为 64,故该寄存器值固定为 0x4。
  - 0x04
```

