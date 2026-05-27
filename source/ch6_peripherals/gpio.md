(ch6-gpio)=

# GPIO

## 概述

{term}`GPIO`（General Purpose Programmable Input/Output）为通用可编程输入输出外设，用于生成和采集特定应用的输入或输出信号，实现系统和外设之间的通信，方便系统对外设的控制。

## 功能描述

GPIO 接口具有以下功能特点：

- 共 3 组 GPIO（GPIO0/1/2），其中 GPIO0/1 各有 8 个独立的可配置管脚，GPIO2 有 3 个独立的可配置管脚，总共 19 个独立的可配置管脚。第一组 GPIO0 对应管脚为 7:0，第二组 GPIO1 对应管脚为 15:8，第三组 GPIO2 对应管脚为 18:16。

- 每个 GPIO 管脚都可单独控制传输方向。

- 每个 GPIO 可以被配置为外部中断源。

- GPIO 用作中断时有 5 种中断触发方式，中断触发方式可配：

  - 上升沿触发
  - 下降沿触发
  - 高电平触发
  - 低电平触发
  - 双沿触发

- 每组 GPIO 上报一个中断，共三个中断号，{term}`CPU` 查询上报的 GPIO 编号。每个中断支持独立屏蔽功能，边沿中断支持可清除功能。

## 工作方式

## 初始化配置

每个 GPIO 可以单独配置为输入或者输出，具体步骤如下：

步骤 1 配置 GPIO_SW_OEN`n`数据方向寄存器，数据方向按 bit 单独控制，写入值为 1 表示该 bit 对应的数据方向是输入，写入值为 0 表示该 bit 对应的数据方向是输出；

步骤 2 写 GPIO_SW_OUT`n`数据寄存器，如果对应的 bit 数据方向是输出，写入该 bit 的值是对应 I/O 信号的输出，回读值等于最后一次写入的值。如果对应的 bit 数据方向是输入，写入值不起作用；

步骤 3 读 GPIO_SW_OUT`n`数据寄存器，如果对应的 bit 数据方向是输入，读该寄存器为外部端口的输入值，软件写入值无效。



```{important}
当 GPIO 用作输出时，建议禁止 GPIO 控制器的中断功能，否则当输出信号符合中断产生条件时，会产生 GPIO 中断。
```


## 边沿中断配置

假设低 8bit GPIO 输入中断，中断类型均为上升沿有效，并且输入中断需要去毛刺。

步骤 1 写中断使能寄存器 GPIO_INT_EN[7:0]=8'h0，配置 8 个 GPIO 中断禁止。

步骤 2 写双沿中断使能寄存器 GPIO_INT_DEDGE[7:0]=8'h0，配置不使能双沿中断。

步骤 3 写中断类型寄存器 GPIO_INT_TYPE[7:0]=8'hFF，配置 8 个输入中断为边沿有效。

步骤 4 写中断极性寄存器 GPIO_INT_POLARITY[7:0]=8'hFF，配置为 8 个输入中断上升沿有效。

步骤 5 写中断屏蔽寄存器 GPIO_INT_MASK[7:0]=8'h0，配置不屏蔽中断。

步骤 6 写中断去毛刺控制寄存器 GPIO_INT_DEBOUNCE[7:0]=8'hFF，配置为去毛刺使能。

步骤 7 写中断使能寄存器 GPIO_INT_EN[7:0]=8'hFF，使能 8 个输入端口的中断功能。

步骤 8 当有上升沿有效（经过去毛刺）的中断发生后，CPU 收到 GPIO 中断，可以通过查询中断状态寄存器 GPIO_INTR 来判断哪个端口发生了中断。

步骤 9 写中断清除寄存器 GPIO_INT_EOI 对应 bit 为 1，可以清除掉相应的中断状态。

```{note}
- 中断相关寄存器的配置均独立生效，建议先取消中断使能，再配置相应的中断相关寄存器，最后配置中断使能。
- 当配置的是边沿中断时，可以通过写中断清除寄存器 GPIO_INT_EOI 来清中断，如果是电平中断写此寄存器无效。
- 当配置双沿中断使能寄存器 GPIO_INT_DEDGE 后，双沿中断有效时，配置中断类型寄存器和中断极性寄存器均无效。
- 对于边沿中断（包括双沿或单沿），同步功能是默认有效的，不能配置。
- 双沿中断使能后，建议软件配置中断去毛刺控制寄存器 GPIO_INT_DEBOUNCE 为不使能。
```

## 电平中断配置

假设低 2 个 GPIO 输入中断，中断类型均为高电平有效，并且输入中断需要去毛刺。

步骤 1 写中断使能寄存器 GPIO_INT_EN[1:0]=2'h0，配置低 2 个 GPIO 中断不使能。

步骤 2 写双沿中断使能寄存器 GPIO_INT_DEDGE[1:0]=2'h0，配置不使能双沿中断。

步骤 3 写中断类型寄存器 GPIO_INT_TYPE[1:0]=2'h0，配置低 2 个输入中断为电平有效。

步骤 4 写中断极性寄存器 GPIO_INT_POLARITY[1:0]=2'h3，配置为低 2 个输入中断高电平有效。

步骤 5 写中断屏蔽寄存器 GPIO_INT_MASK[1:0]=2'h0，配置不屏蔽中断。

步骤 6 写中断去毛刺控制寄存器 GPIO_INT_DEBOUNCE[1:0]=2'h3，配置低 2 个输入中断为去毛刺使能。

步骤 7 写中断使能寄存器 GPIO_INT_EN[1:0]=2'h3，使能低 2 个输入端口的中断功能。

步骤 8 当有高电平有效的中断发生后，经过去毛刺处理，CPU 收到 GPIO 中断，可以通过查询中断状态寄存器 GPIO_INTR 来判断哪个端口发生了中断。

```{note}
- 当设置电平中断时，中断同步功能默认有效，不可配置。
- 电平中断无法通过写 GPIO_INT_EOI 中断清除寄存器来清除。
- 由于需要同步，因此电平中断必须在 GPIO 有时钟时才能输出。
```

## 寄存器概览

GPIO 寄存器概览如表 6-5 所示。

表6-5 GPIO 寄存器概览（基址是 GPIO0:0x44028000、GPIO1:0x44029000、GPIO2:0x4402A000）

| 偏移地址 | 名称 | 描述 |
| --- | --- | --- |
| 0x0000 | GPIO_SW_OUT | GPIO 数据寄存器。 |
| 0x0004 | GPIO_SW_OEN | GPIO 数据方向寄存器。 |
| 0x000C | GPIO_INT_EN | GPIO 中断使能寄存器。 |
| 0x0010 | GPIO_INT_MASK | GPIO 中断屏蔽寄存器。 |
| 0x0014 | GPIO_INT_TYPE | GPIO 中断类型寄存器。 |
| 0x0018 | GPIO_INT_POLARITY | GPIO 中断极性寄存器。 |
| 0x001C | GPIO_INT_DEDGE | GPIO 双沿中断使能寄存器。 |
| 0x0020 | GPIO_INT_DEBOUNCE | GPIO 中断去毛刺控制寄存器。 |
| 0x0024 | GPIO_INT_RAW | GPIO 原始中断状态寄存器。 |
| 0x0028 | GPIO_INTR | GPIO 中断状态寄存器。 |
| 0x002C | GPIO_INT_EOI | GPIO 中断清除寄存器。 |
| 0x0030 | GPIO_DATA_SET | GPIO 数据设置寄存器。 |
| 0x0034 | GPIO_DATA_CLR | GPIO 数据清除寄存器。 |


## 寄存器描述

GPIO_SW_OUT

GPIO_SW_OUT 为 GPIO 数据寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0000 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - gpio_sw_out
  - GPIO 信号的数据配置。软件模式输出:写入该寄存器的值是该端口 I/O 信号的输出,回读值等于最后一次写入寄存器的值。软件模式输入:读该寄存器为外部端口的输入值,写该寄存器无效。硬件模式:写无意义,读回为写入值。注意:由于端口可以独立控制,因此,上述描述是针对该寄存器的每一 bit 而言。
  - 0x00
```

### GPIO_SW_OEN

GPIO_SW_OEN 为 GPIO 数据方向寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0004 Total Reset Value: 0x0000_00FF

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - gpio_sw_oen
  - GPIO 信号的数据方向控制。写入寄存器的值独立控制相应端口的方向:0: output;1: input（默认值）。读回表示各端口的输入输出属性:0: output;1: input。
  - 0xFF
```

### GPIO_INT_EN

GPIO_INT_EN 为 GPIO 中断使能寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x000C Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - gpio_int_en
  - GPIO 信号的中断使能配置。写入寄存器的值可以独立控制相应端口的中断使能:0:普通 GPIO 端口（默认值）;1:中断端口。读回表示各端口的中断使能状态:0:普通 GPIO 端口;1:中断端口。注意:中断功能必须在对应端口为输入属性下才会有效。
  - 0x00
```

### GPIO_INT_MASK

GPIO_INT_MASK 为 GPIO 中断屏蔽寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0010 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - gpio_int_mask
  - GPIO 信号的中断屏蔽控制。写入寄存器的值可以独立控制相应端口的中断屏蔽:0:不屏蔽（默认值）;1:屏蔽。读回表示各端口的中断屏蔽状态:0:不屏蔽;1:屏蔽。
  - 0x00
```

### GPIO_INT_TYPE

GPIO_INT_TYPE 为 GPIO 中断类型寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0014 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - gpio_int_type
  - GPIO 信号的中断类型配置。写入寄存器的值可以独立控制相应端口的中断类型:0:电平中断（默认值）;1:边沿中断。读回表示各端口的中断类型属性:0:电平中断,1:边沿中断。
  - 0x00
```

### GPIO_INT_POLARITY

GPIO_INT_POLARITY 为 GPIO 中断极性寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0018 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - gpio_int_polarity
  - GPIO 信号的中断极性配置。写入寄存器的值可以独立控制相应端口的中断极性:0:低电平或者下降沿（默认值）;1:高电平或者上升沿。读回表示各端口的中断极性属性:0:低电平或者下降沿;1:高电平或者上升沿。
  - 0x00
```

### GPIO_INT_DEDGE

GPIO_INT_DEDGE 为 GPIO 双沿中断使能寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x001C Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - gpio_int_dedge
  - GPIO 信号的双沿中断使能配置。写入寄存器的值可以独立控制相应端口的双沿中断使能:0:禁止双沿中断;1:使能双沿中断。读回表示各端口的双沿中断使能状态:0:未使能双沿中断;1:已使能双沿中断。
  - 0x00
```

### GPIO_INT_DEBOUNCE

GPIO_INT_DEBOUNCE 为 GPIO 中断去毛刺控制寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0020 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RW
  - gpio_int_debounce
  - GPIO 信号的中断输入去毛刺控制配置。写入寄存器的值可以独立控制相应端口是否使能中断输入去毛刺功能:0:禁止去毛刺（默认值）;1:使能去毛刺。读回表示各端口的 Debounce 属性:0:禁止去毛刺;1:使能去毛刺。
  - 0x00
```

### GPIO_INT_RAW

GPIO_INT_RAW 为 GPIO 原始中断状态寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0024 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RO
  - gpio_int_raw
  - GPIO 信号的原始中断状态查询。屏蔽之前的中断状态:0:未产生中断;1:产生中断。
  - 0x00
```

### GPIO_INTR

GPIO_INTR 为 GPIO 中断状态寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0028 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RO
  - gpio_intr
  - GPIO 信号的中断状态查询。屏蔽之后的中断状态:0:未产生中断;1:产生中断。
  - 0x00
```

### GPIO_INT_EOI

GPIO_INT_EOI 为 GPIO 中断清除寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x002C Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - RO
  - gpio_int_eoi
  - GPIO 信号的中断清除控制。写入寄存器的值可以独立控制相应边沿中断端口的中断清除:0:不清除中断（默认值）;1:清除中断。
  - 0x00
```

### GPIO_DATA_SET

GPIO_DATA_SET 为 GPIO 数据设置寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0030 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - WO
  - gpio_data_set
  - 写 GPIO 数据请求,高有效。软件模式输出时,写入寄存器的值可以将GPIO_SW_OUT`gpio_sw_out`相应 bit 位置 1。
  - 0x00
```

### GPIO_DATA_CLR

GPIO_DATA_CLR 为 GPIO 数据清除寄存器。

```{note}
GPIO2 的 BIT[7:3]未使用。
```

Offset Address: 0x0034 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:8]
  - RO
  - reserved
  - 保留。
  - 0x000000
* - [7:0]
  - WO
  - gpio_data_clr
  - 清 GPIO 数据请求,高有效。软件模式输出时,写入寄存器的值可以将GPIO_SW_OUT`gpio_sw_out`相应 bit 位清零。
  - 0x00
```

