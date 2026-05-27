(ch6-peripherals)=

# 外围设备

## IO MUX

### 概述

芯片数字管脚数量有限，通过 IO 复用的方式丰富管脚功能。

### 软用管脚描述

```{important}
ADC 管脚：LSADC 通道与 GPIO 功能只支持其中 1 种功能，ADC 通道管脚与 GPIO 管脚的对应关系如表 6-2 所示。
```


表6-1 ADC 通道管脚与复用管脚对应关系

| 复用管脚名称 | ADC 管脚 |
| --- | --- |
| GPIO_07 | ADC0 |
| GPIO_08 | ADC1 |
| GPIO_09 | ADC2 |
| GPIO_10 | ADC3 |
| GPIO_11 | ADC4 |
| GPIO_12 | ADC5 |


软件复用管脚如表 6-2 所示。

表6-2 软件复用管脚

| Pin | Pad信号 | 复用控制寄存器 | 复用信号0 | 复用信号1 | 复用信号2 | 复用信号3 | 复用信号4 | 复用信号5 | 复用信号6 | 复用信号7 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 4 | GPIO_00 | GPIO_00_SEL | GPIO_00 | PWM0 | DIAG[0] | SPI1_CSN | JTAG_TDI | - | - | - |
| 5 | GPIO_01 | GPIO_01_SEL | GPIO_01 | PWM1 | DIAG[1] | SPI1_IO0 | JTAG_MODE | BT_SAMPLE | - | - |
| 6 | GPIO_02 | GPIO_02_SEL | GPIO_02 | PWM2 | DIAG[2] | SPI1_IO3 | WIFI_TSF_SYNC | WL_GLP_SYNC_PULSE | BLE&SLE_GLP_SYNC_PULSE | - |
| 7 | GPIO_03 | GPIO_03_SEL | GPIO_03 | PWM3 | PMU_32_K_TEST | SPI1_IO1 | HW_ID[0] | DIAG[3] | - | - |
| 8 | GPIO_04 | GPIO_04_SEL | SSI_CLK | PWM4 | GPIO_04 | SPI1_IO1 | JTAG_ENABLE | DFT_JTAG_TMS | - | - |
| 9 | GPIO_05 | GPIO_05_SEL | SSI_DATA | PWM5 | UART2_CTS | SPI1_IO2 | GPIO_05 | SPI0_IN | DFT_JTAG_TCK | - |
| 10 | GPIO_06 | GPIO_06_SEL | GPIO_06 | PWM6 | UART2_RTS | SPI1_SCK | REF_CLK_FREQ_STATUS | DIAG[4] | SPI0_OUT | DFT_JTAG_TDI |
| 11 | GPIO_07 | GPIO_07_SEL | GPIO_07 | PWM7 | UART2_RXD | SPI0_SCK | I2S_MCLK | DIAG[5] | - | - |
| 12 | GPIO_08 | GPIO_08_SEL | GPIO_08 | PWM0 | UART2_TXD | SPI0_CS1_N | DIAG[6] | - | - | - |
| 13 | GPIO_09 | GPIO_09_SEL | GPIO_09 | PWM1 | RADAR_ANT0_SW | SPI0_OUT | I2S_DO | HW_ID[1] | DIAG[7] | JTAG_TDO |
| 14 | GPIO_10 | GPIO_10_SEL | GPIO_10 | PWM2 | ANT0_SW | SPI0_CS0_N | I2S_SCLK | DIAG[0] | - | - |
| 15 | GPIO_11 | GPIO_11_SEL | GPIO_11 | PWM3 | RADAR_ANT1_SW | SPI0_IN | I2S_LRCLK | DIAG[1] | HW_ID[2] | - |
| 16 | GPIO_12 | GPIO_12_SEL | GPIO_12 | PWM4 | ANT1_SW | - | I2S_DI | DIAG[7] | HW_ID[3] | - |
| 24 | GPIO_13 | GPIO_13_SEL | GPIO_13 | UART1_CTS | RADAR_ANT0_SW | DFT_JTAG_TDO | JTAG_TMS | - | - | - |
| 25 | GPIO_14 | GPIO_14_SEL | GPIO_14 | UART1_RTS | RADAR_ANT1_SW | DFT_JTAG_TRSTN | JTAG_TCK | - | - | - |
| 26 | UART1_TXD | UART1_TXD_SEL | GPIO_15 | UART1_TXD | I2C1_SDA | - | - | - | - | - |
| 27 | UART1_RXD | UART1_RXD_SEL | GPIO_16 | UART1_RXD | I2C1_SCL | - | - | - | - | - |
| 28 | UART0_TXD | UART0_TXD_SEL | GPIO_17 | UART0_TXD | I2C0_SDA | - | - | - | - | - |
| 29 | UART0_RXD | UART0_RXD_SEL | GPIO_18 | UART0_RXD | I2C0_SCL | - | - | - | - | - |
|  |  |  |  |  |  |  |  |  |  |  |


GPIO 的软件复用管脚说明如表 6-3 所示。

表6-3 GPIO 的软件复用管脚说明

```{list-table}
:header-rows: 1

* - 信号名
  - 方向
  - 说明
* - REFCLK_FREQ_STATUS
  - I
  - 晶体时钟频率的指示信号:1'b0:40M。1'b1:24M。
* - JTAG_ENABLE
  - I
  - jtag 使能:1'b0:普通 IO。1'b1:jtag 使能。
* - JTAG_MODE
  - I
  - DFT 使能:1'b0:正常功能模式。• 1'b1:DFT (Design For Testability) 测试模式。
* - HW_ID
  - I
  - HW_ID(上电硬件控制字)
* - DFT_JTAG_TDI
  - I
  - DFT_JTAG 数据输入。
* - DFT_JTAG_TRSTN
  - I
  - DFT_JTAG 复位输入,低电平有效,默认状态为复位。
* - DFT_JTAG_TCK
  - I
  - DFT_JTAG 时钟输入。
* - DFT_JTAG_TMS
  - I
  - DFT_JTAG 模式选择输入。
* - DFT_JTAG_TDO
  - B
  - DFT_JTAG 数据输出。
* - JTAG_TDI
  - I
  - JTAG 数据输入。
* - JTAG_TCK
  - I
  - JTAG 时钟输入。
* - JTAG_TMS
  - B
  - JTAG 模式选择输入。
* - JTAG_TDO
  - B
  - JTAG 数据输出。
* - UART0_RXD
  - I
  - UART0 RX。
* - UART0_TXD
  - O
  - UART0 TX。
* - UART1_RXD
  - I
  - UART1 RX。
* - UART1_TXD
  - O
  - UART1 TX。
* - UART1_RTS
  - O
  - UART1 流控信号。
* - UART1_CTS
  - I
  - UART1 流控信号。
* - UART2_RXD
  - I
  - UART2 RX。
* - UART2_TXD
  - O
  - UART2 TX。
* - UART2_RTS
  - O
  - UART2 流控信号。
* - UART2_CTS
  - I
  - UART2 流控信号。
* - PWM0
  - B
  - PWM0 输出。
* - PWM1
  - B
  - PWM1 输出。
* - PWM2
  - B
  - PWM2 输出。
* - PWM3
  - B
  - PWM3 输出。
* - PWM4
  - B
  - PWM4 输出。
* - PWM5
  - B
  - PWM5 输出。
* - PWM6
  - B
  - PWM6 输出。
* - PWM7
  - B
  - PWM7 输出。
* - GPIO_00
  - B
  - GPIO
* - GPIO_01
  - B
  - GPIO
* - GPIO_02
  - B
  - GPIO
* - GPIO_03
  - B
  - GPIO
* - GPIO_04
  - B
  - GPIO
* - GPIO_05
  - B
  - GPIO
* - GPIO_06
  - B
  - GPIO
* - GPIO_07
  - B
  - GPIO
* - GPIO_08
  - B
  - GPIO
* - GPIO_09
  - B
  - GPIO
* - GPIO_10
  - B
  - GPIO
* - GPIO_11
  - B
  - GPIO
* - GPIO_12
  - B
  - GPIO
* - GPIO_13
  - B
  - GPIO
* - GPIO_14
  - B
  - GPIO
* - GPIO_15
  - B
  - GPIO
* - GPIO_16
  - B
  - GPIO
* - GPIO_17
  - B
  - GPIO
* - GPIO_18
  - B
  - GPIO
* - SSI_CLK
  - I
  - SSI 时钟
* - SSI_DATA
  - B
  - SSI 数据
* - SPI0_SCK
  - B
  - SPI0 时钟信号
* - SPI0_CS0_N
  - B
  - SPI0 片选信号 0 chip select0, active low
* - SPI0_CS1_N
  - B
  - SPI0 片选信号 1 chip select1, active low
* - SPI0_IN
  - I
  - SPI0 数据接收信号 data input
* - SPI0_OUT
  - B
  - SPI0 数据发送信号 data output, with tri-state output
* - SPI1_SCK
  - O
  - QSPI (SPI1 时钟信号)
* - SPI1_CSN
  - O
  - QSPI (SPI1 片选信号)
* - SPI1_IO0
  - B
  - QSPI (SPI1)数据 0。
* - SPI1_IO1
  - B
  - QSPI (SPI1)数据 1。
* - SPI1_IO2
  - B
  - QSPI (SPI1)数据 2。
* - SPI1_IO3
  - B
  - QSPI (SPI1)数据 3。
* - SFC_CLK
  - O
  - Flash 控制信号,不支持双沿。Flash 时钟范围:CMU 中 PLL 源头时钟二分频产生 96M 或 80M 的时钟。上电使用晶体时钟二分频:20M 或 12M。
* - SFC_CSN
  - O
  - Flash 控制信号,不支持双沿,默认上拉。
* - SFC_IO0
  - B
  - Flash 数据信号,不支持双沿,默认上拉。
* - SFC_IO1
  - B
  - Flash 数据信号,不支持双沿,默认上拉。
* - SFC_IO2
  - B
  - Flash 数据信号,不支持双沿,默认上拉。
* - SFC_IO3
  - B
  - Flash 数据信号,不支持双沿,默认上拉。
* - I2C0_SCL
  - B
  - I2C 时钟
* - I2C0_SDA
  - B
  - I2C 数据
* - I2C1_SCL
  - B
  - I2C 时钟
* - I2C1_SDA
  - B
  - I2C 数据
* - I2S_MCLK
  - O
  - I2S MCLK
* - I2S_SCLK
  - B
  - I2S CLK
* - I2S_LRCLK
  - B
  - I2S WS
* - I2S_DI
  - I
  - I2S RX
* - I2S_DO
  - O
  - I2S TX
* - WIFI_TSF_SYNC
  - O
  - WiFi 输出的音频同步信号。
* - WL_GLP_SYNC_PULSE
  - O
  - WiFi 输出的 GLP 同步信号。
* - BLE&SLE_GLP_SYNC_PULSE
  - O
  - BLE&SLE 输出的 GLP 同步信号。
* - BT_SAMPLE
  - I
  - BT 维测信号。
* - DIAG
  - O
  - 内部时钟、信号的维测,端口观测。
* - PMU_32K_TEST
  - O
  - PMU 32k 时钟观测。
* - ANT0_SW
  - O
  - WiFi 输出的物理天线选择信号 0。
* - ANT1_SW
  - O
  - WiFi 输出的物理天线选择信号 1。
* - RADAR_ANT0_SW
  - O
  - 雷达感知输出的物理天线选择信号 0。
* - RADAR_ANT1_SW
  - O
  - 雷达感知输出的物理天线选择信号 1。
```

### 寄存器概览

IO_CONFIG 寄存器概览如表 6-4 所示。

表6-4 IO_CONFIG 寄存器概览（基址是 0x4400_d000）

```{list-table}
:header-rows: 1

* - 偏移地址
  - 名称
  - 描述
* - 0x0
  - GPIO_00_SEL
  - GPIO_00 管脚复用控制寄存器。
* - 0x4
  - GPIO_01_SEL
  - GPIO_01 管脚复用控制寄存器。
* - 0x8
  - GPIO_02_SEL
  - GPIO_02 管脚复用控制寄存器。
* - 0xc
  - GPIO_03_SEL
  - GPIO_03 管脚复用控制寄存器。
* - 0x10
  - GPIO_04_SEL
  - GPIO_04 管脚复用控制寄存器。
* - 0x14
  - GPIO_05_SEL
  - GPIO_05 管脚复用控制寄存器。
* - 0x18
  - GPIO_06_SEL
  - GPIO_06 管脚复用控制寄存器。
* - 0x1c
  - GPIO_07_SEL
  - GPIO_07 管脚复用控制寄存器。
* - 0x20
  - GPIO_08_SEL
  - GPIO_08 管脚复用控制寄存器。
* - 0x24
  - GPIO_09_SEL
  - GPIO_09 管脚复用控制寄存器。
* - 0x28
  - GPIO_10_SEL
  - GPIO_10 管脚复用控制寄存器。
* - 0x2c
  - GPIO_11_SEL
  - GPIO_11 管脚复用控制寄存器。
* - 0x30
  - GPIO_12_SEL
  - GPIO_12 管脚复用控制寄存器。
* - 0x34
  - GPIO_13_SEL
  - GPIO_13 管脚复用控制寄存器。
* - 0x38
  - GPIO_14_SEL
  - GPIO_14 管脚复用控制寄存器。
* - 0x3c
  - UART1_TXD_SEL
  - UART1_TXD 管脚复用控制寄存器。
* - 0x40
  - UART1_RXD_SEL
  - UART1_RXD 管脚复用控制寄存器。
* - 0x44
  - UART0_TXD_SEL
  - UART0_TXD 管脚复用控制寄存器。
* - 0x48
  - UART0_RXD_SEL
  - UART0_RXD 管脚复用控制寄存器。
* - 0x800
  - PAD_GPIO_00_CTRL
  - GPIO_00 功能管脚控制寄存器。
* - 0x804
  - PAD_GPIO_01_CTRL
  - GPIO_01 功能管脚控制寄存器。
* - 0x808
  - PAD_GPIO_02_CTRL
  - GPIO_02 功能管脚控制寄存器。
* - 0x80c
  - PAD_GPIO_03_CTRL
  - GPIO_03 功能管脚控制寄存器。
* - 0x810
  - PAD_GPIO_04_CTRL
  - GPIO_04 功能管脚控制寄存器。
* - 0x814
  - PAD_GPIO_05_CTRL
  - GPIO_05 功能管脚控制寄存器。
* - 0x818
  - PAD_GPIO_06_CTRL
  - GPIO_06 功能管脚控制寄存器。
* - 0x81c
  - PAD_GPIO_07_CTRL
  - GPIO_07 功能管脚控制寄存器。
* - 0x820
  - PAD_GPIO_08_CTRL
  - GPIO_08 功能管脚控制寄存器。
* - 0x824
  - PAD_GPIO_09_CTRL
  - GPIO_09 功能管脚控制寄存器。
* - 0x828
  - PAD_GPIO_10_CTRL
  - GPIO_10 功能管脚控制寄存器。
* - 0x82c
  - PAD_GPIO_11_CTRL
  - GPIO_11 功能管脚控制寄存器。
* - 0x830
  - PAD_GPIO_12_CTRL
  - GPIO_12 功能管脚控制寄存器。
* - 0x834
  - PAD_GPIO_13_CTRL
  - GPIO_13 功能管脚控制寄存器。
* - 0x838
  - PAD_GPIO_14_CTRL
  - GPIO_14 功能管脚控制寄存器。
* - 0x83c
  - PAD_UART1_TXD_CTRL
  - UART1_TXD 功能管脚控制寄存器。
* - 0x840
  - PAD_UART1_RXD_CTRL
  - UART1_RXD 功能管脚控制寄存器。
* - 0x844
  - PAD_UART0_TXD_CTRL
  - UART0_TXD 功能管脚控制寄存器。
* - 0x848
  - PAD_UART0_RXD_CTRL
  - UART0_RXD 功能管脚控制寄存器。
* - 0x868
  - PAD_SFC_CLK_CTRL
  - SFC_CLK 功能管脚控制寄存器。
* - 0x86c
  - PAD_SFC_CSN_CTRL
  - SFC_CSN 功能管脚控制寄存器。
* - 0x870
  - PAD_SFC_IO0_CTRL
  - SFC_IO0 功能管脚控制寄存器。
* - 0x874
  - PAD_SFC_IO1_CTRL
  - SFC_IO1 功能管脚控制寄存器。
* - 0x878
  - PAD_SFC_IO2_CTRL
  - SFC_IO2 功能管脚控制寄存器。
* - 0x87c
  - PAD_SFC_IO3_CTRL
  - SFC_IO3 功能管脚控制寄存器。
```

### 寄存器描述

GPIO_00_SEL

GPIO_00_SEL 为 GPIO_00 复用关系配置。

Offset Address: 0x0 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_00_sel
  - GPIO_00 管脚复用:0: GPIO_00;1: PWM0;2: DIAG[0];3: SPI1_CSN;4: JTAG_TDI;其他: 保留。
  - 0x0
```

### GPIO_01_SEL

GPIO_01_SEL 为 GPIO_01 复用关系配置。

Offset Address: 0x4 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_01_sel
  - GPIO_01 管脚复用:0: GPIO_01;1: PWM1;2: DIAG[1];3: SPI1_IO0;4: JTAG_MODE;5: BT_SAMPLE;其他: 保留。
  - 0x0
```

### GPIO_02_SEL

GPIO_02_SEL 为 GPIO_02 复用关系配置。

Offset Address: 0x8 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_02_sel
  - GPIO_02 管脚复用:0: GPIO_02;1: PWM2;2: DIAG[2];3: SPI1_IO3;4: WIFI_TSF_SYNC;5: WL_GLP_SYNC_PULSE;6:BSLE_GLP_SYNC_PULSE;其他: 保留。
  - 0x0
```

GPIO_03_SEL

GPIO_03_SEL 为 GPIO_03 复用关系配置。

Offset Address: 0xc Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_03_sel
  - GPIO_03 管脚复用:0: GPIO_03;1: PWM3;2: PMU_32K_TEST;3: SPI1_IO1;4: HW_ID[0];5: DIAG[3];其他: 保留。
  - 0x0
```

### GPIO_04_SEL

GPIO_04_SEL 为 GPIO_04 复用关系配置。

Offset Address: 0x10 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_04_sel
  - GPIO_04 管脚复用:0: SSI_CLK;1: PWM4;2: GPIO_04;3: SPI1_IO1;4: JTAG_ENABLE;5: DFT_JTAG_TMS;其他: 保留。
  - 0x0
```

### GPIO_05_SEL

GPIO_05_SEL 为 GPIO_05 复用关系配置。

Offset Address: 0x14 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_05_sel
  - GPIO_05 管脚复用:0: SSI_DATA;1: PWM5;2: UART2_CTS;3: SPI1_IO2;4: GPIO_05;5: SPI0_IN;6: DFT_JTAG_TCK;其他: 保留。
  - 0x0
```

### GPIO_06_SEL

GPIO_06_SEL 为 GPIO_06 复用关系配置。

Offset Address: 0x18 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_06_sel
  - GPIO_06 管脚复用:0: GPIO_06;1: PWM6;2: UART2_RTS;3: SPI1_SCK;4:REFCLK_FREQ_STATUS;5: DIAG[4];6: SPI0_OUT;7: DFT_JTAG_TDI;其他: 保留。
  - 0x0
```

### GPIO_07_SEL

GPIO_07_SEL 为 GPIO_07 复用关系配置。

Offset Address: 0x1c Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_07_sel
  - GPIO_07 管脚复用:0: GPIO_07;1: PWM7;2: UART2_RXD;3: SPI0_SCK;4: I2S_MCLK;5: DIAG[5];其他:保留。
  - 0x0
```

GPIO_08_SEL

GPIO_08_SEL 为 GPIO_08 复用关系配置。

Offset Address: 0x20 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_08_sel
  - GPIO_08 管脚复用:0: GPIO_08;1: PWM0;2: UART2_TXD;3: SPI0_CS1_N;4: DIAG[6];其他: 保留。
  - 0x0
```

GPIO_09_SEL

GPIO_09_SEL 为 GPIO_09 复用关系配置

Offset Address: 0x24 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_09_sel
  - GPIO_09 管脚复用:0: GPIO_09;1: PWM1;2: RADAR_ANT0_SW;3: SPI0_OUT;4: I2S_DO;5: HW_ID[1];6: DIAG[7];7: JTAG_TDO;其他:保留。
  - 0x0
```

### GPIO_10_SEL

GPIO_10_SEL 为 GPIO_10 复用关系配置。

Offset Address: 0x28 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_10_sel
  - GPIO_10 管脚复用:0: GPIO_10;1: PWM2;2: ANT0_SW;3: SPI0_CS0_N;4: I2S_SCLK;5: DIAG[0];其他: 保留。
  - 0x0
```

### GPIO_11_SEL

GPIO_11_SEL 为 GPIO_11 复用关系配置。

Offset Address: 0x2c Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_11_sel
  - GPIO_11 管脚复用:0: GPIO_11;1: PWM3;2: RADAR_ANT1_SW;3: SPI0_IN;4: I2S_LRCLK;5: DIAG[1];6: HW_ID[2];其他:保留。
  - 0x0
```

### GPIO_12_SEL

GPIO_12_SEL 为 GPIO_12 复用关系配置。

Offset Address: 0x30 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_12_sel
  - GPIO_12 管脚复用:0: GPIO_12;1: PWM4;2: ANT1_SW;4: I2S_DI;6: HW_ID[3];其他: 保留。
  - 0x0
```

### GPIO_13_SEL

GPIO_13_SEL 为 GPIO_13 复用关系配置。

Offset Address: 0x34 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_13_sel
  - GPIO_13 管脚复用:0: GPIO_13;1: UART1_CTS;2: RADAR_ANT0_SW;3: DFT_JTAG_TDO;4: JTAG_TMS;其他:保留。
  - 0x0
```

### GPIO_14_SEL

GPIO_14_SEL 为 GPIO_14 复用关系配置。

Offset Address: 0x38 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:3]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [2:0]
  - RW
  - gpio_14_sel
  - GPIO_14 管脚复用:0: GPIO_14;1: UART1_RTS;2: RADAR_ANT1_SW;3: DFT_JTAG_TRSTN;4: JTAG_TCK;其他: 保留。
  - 0x0
```

### UART1_TXD_SEL

UART1_TXD_SEL 为 UART1_TXD 复用关系配置。

Offset Address: 0x3c Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:2]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [1:0]
  - RW
  - uart1_txd_sel
  - UART1_TXD 管脚复用:0: GPIO_15;1: UART1_TXD;2: I2C1_SDA;其他:保留。
  - 0x0
```

### UART1_RXD_SEL

UART1_RXD_SEL 为 UART1_RXD 复用关系配置。

Offset Address: 0x40 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:2]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [1:0]
  - RW
  - uart1_rxd_sel
  - UART1_RXD 管脚复用:0: GPIO_16;1: UART1_RXD;2: I2C1_SCL;其他: 保留。
  - 0x0
```

### UART0_TXD_SEL

UART0_TXD_SEL 为 UART0_TXD 复用关系配置。

Offset Address: 0x44 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:2]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [1:0]
  - RW
  - uart0_txd_sel
  - UART0_TXD 管脚复用:0: GPIO_17;1: UART0_TXD;2: I2C0_SDA;其他: 保留。
  - 0x0
```

### UART0_RXD_SEL

UART0_RXD_SEL 为 UART0_RXD 复用关系配置。

Offset Address: 0x48 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:2]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [1:0]
  - RW
  - uart0_rxd_sel
  - UART0_RXD 管脚复用:0: GPIO_18;1: UART0_RXD;2: I2C0_SCL;其他: 保留。
  - 0x0
```

### PAD_GPIO_00_CTRL

PAD_GPIO_00_CTRL 为 GPIO_00 控制寄存器。

Offset Address: 0x800 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_00_ctrl_ie
  - GPIO_00.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_00_ctrl_ps
  - GPIO_00.PS 管脚控制:需与 GPIO_00.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_00_ctrl_pe
  - GPIO_00.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_00_ctrl_ds2
  - GPIO_00.DS2 管脚控制:需与GPIO_00.DS1/GPIO_00.DS0管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_00_ctrl_ds1
  - GPIO_00.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_00_ctrl_ds0
  - GPIO_00.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_00_ctrl_st
  - GPIO_00.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_01_CTRL

PAD_GPIO_01_CTRL 为 GPIO_01 控制寄存器。

Offset Address: 0x804 Total Reset Value: 0x0000_0A00

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_01_ctrl_ie
  - GPIO_01.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_01_ctrl_ps
  - GPIO_01.PS 管脚控制:需与 GPIO_01.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_01_ctrl_pe
  - GPIO_01.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_01_ctrl_ds2
  - GPIO_01.DS2 管脚控制:需与GPIO_01.DS1/GPIO_01.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111 至 000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_01_ctrl_ds1
  - GPIO_01.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_01_ctrl_ds0
  - GPIO_01.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_01_ctrl_st
  - GPIO_01.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

PAD_GPIO_02_CTRL

PAD_GPIO_02_CTRL 为 GPIO_02 控制寄存器。

Offset Address: 0x808 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_02_ctrl_ie
  - GPIO_02.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_02_ctrl_ps
  - GPIO_02.PS 管脚控制:需与 GPIO_02.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_02_ctrl_pe
  - GPIO_02.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_02_ctrl_ds2
  - GPIO_02.DS2 管脚控制:需与GPIO_02.DS1/GPIO_02.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_02_ctrl_ds1
  - GPIO_02.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_02_ctrl_ds0
  - GPIO_02.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_02_ctrl_st
  - GPIO_02.ST 管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_03_CTRL

PAD_GPIO_03_CTRL 为 GPIO_03 控制寄存器。

Offset Address: 0x80c Total Reset Value: 0x0000_0A00

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_03_ctrl_ie
  - GPIO_03.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_03_ctrl_ps
  - GPIO_03.PS 管脚控制:需与 GPIO_03.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_03_ctrl_pe
  - GPIO_03.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_03_ctrl_ds2
  - GPIO_03.DS2 管脚控制:需与GPIO_03.DS1/GPIO_03.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111 至 000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_03_ctrl_ds1
  - GPIO_03.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_03_ctrl_ds0
  - GPIO_03.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_03_ctrl_st
  - GPIO_03.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_04_CTRL

PAD_GPIO_04_CTRL 为 GPIO_04 控制寄存器。

Offset Address: 0x810 Total Reset Value: 0x0000_0A00

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_04_ctrl_ie
  - GPIO_04.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_04_ctrl_ps
  - GPIO_04.PS 管脚控制:需与 GPIO_04.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_04_ctrl_pe
  - GPIO_04.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_04_ctrl_ds2
  - GPIO_04.DS2 管脚控制:需与GPIO_04.DS1/GPIO_04.DS0管脚控制结合使用。DS2~DS0对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_04_ctrl_ds1
  - GPIO_04.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_04_ctrl_ds0
  - GPIO_04.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_04_ctrl_st
  - GPIO_04.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_05_CTRL

PAD_GPIO_05_CTRL 为 GPIO_05 控制寄存器。

Offset Address: 0x814 Total Reset Value: 0x0000_0820

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_05_ctrl_ie
  - GPIO_05.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_05_ctrl_ps
  - GPIO_05.PS 管脚控制:需与 GPIO_05.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01: 强上拉;10: 下拉;11: 上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_05_ctrl_pe
  - GPIO_05.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_05_ctrl_ds2
  - GPIO_05.DS2 管脚控制:需与GPIO_05.DS1/GPIO_05.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000, 驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_05_ctrl_ds1
  - GPIO_05.DS1 管脚控制。
  - 0x1
* - [4]
  - RW
  - pad_gpio_05_ctrl_ds0
  - GPIO_05.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_05_ctrl_st
  - GPIO_05.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

PAD_GPIO_06_CTRL

PAD_GPIO_06_CTRL 为 GPIO_06 控制寄存器。

Offset Address: 0x818 Total Reset Value: 0x0000_0A00

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_06_ctrl_ie
  - GPIO_06.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_06_ctrl_ps
  - GPIO_06.PS 管脚控制:需与 GPIO_06.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_06_ctrl_pe
  - GPIO_06.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_06_ctrl_ds2
  - GPIO_06.DS2 管脚控制:需与GPIO_06.DS1/GPIO_06.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_06_ctrl_ds1
  - GPIO_06.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_06_ctrl_ds0
  - GPIO_06.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_06_ctrl_st
  - GPIO_06.ST 管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

PAD_GPIO_07_CTRL

PAD_GPIO_07_CTRL 为 GPIO_07 控制寄存器。

Offset Address: 0x81c Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_07_ctrl_ie
  - GPIO_07.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_07_ctrl_ps
  - GPIO_07.PS 管脚控制:需与 GPIO_07.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_07_ctrl_pe
  - GPIO_07.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_07_ctrl_ds2
  - GPIO_07.DS2 管脚控制:需与GPIO_07.DS1/GPIO_07.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_07_ctrl_ds1
  - GPIO_07.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_07_ctrl_ds0
  - GPIO_07.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_07_ctrl_st
  - GPIO_07.ST 管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_08_CTRL

PAD_GPIO_08_CTRL 为 GPIO_08 控制寄存器。

Offset Address: 0x820 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_08_ctrl_ie
  - GPIO_08.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_08_ctrl_ps
  - GPIO_08.PS 管脚控制:需与 GPIO_08.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_08_ctrl_pe
  - GPIO_08.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_08_ctrl_ds2
  - GPIO_08.DS2 管脚控制:需与 GPIO_08.DS1/GPIO_08.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_08_ctrl_ds1
  - GPIO_08.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_08_ctrl_ds0
  - GPIO_08.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_08_ctrl_st
  - GPIO_08.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_09_CTRL

PAD_GPIO_09_CTRL 为 GPIO_09 控制寄存器。

Offset Address: 0x824 Total Reset Value: 0x0000_0A00

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_09_ctrl_ie
  - GPIO_09.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_09_ctrl_ps
  - GPIO_09.PS 管脚控制:需与 GPIO_09.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_09_ctrl_pe
  - GPIO_09.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_09_ctrl_ds2
  - GPIO_09.DS2 管脚控制:需与GPIO_09.DS1/GPIO_09.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_09_ctrl_ds1
  - GPIO_09.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_09_ctrl_ds0
  - GPIO_09.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_09_ctrl_st
  - GPIO_09.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_10_CTRL

PAD_GPIO_10_CTRL 为 GPIO_10 控制寄存器。

Offset Address: 0x828 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_10_ctrl_ie
  - GPIO_10.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_10_ctrl_ps
  - GPIO_10.PS 管脚控制:需与 GPIO_10.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_10_ctrl_pe
  - GPIO_10.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_10_ctrl_ds2
  - GPIO_10.DS2 管脚控制:需与GPIO_10.DS1/GPIO_10.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_10_ctrl_ds1
  - GPIO_10.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_10_ctrl_ds0
  - GPIO_10.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_10_ctrl_st
  - GPIO_10.ST 管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_11_CTRL

PAD_GPIO_11_CTRL 为 GPIO_11 控制寄存器。

Offset Address: 0x82c Total Reset Value: 0x0000_0A00

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_11_ctrl_ie
  - GPIO_11.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_11_ctrl_ps
  - GPIO_11.PS 管脚控制:需与 GPIO_11.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_11_ctrl_pe
  - GPIO_11.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_11_ctrl_ds2
  - GPIO_11.DS2 管脚控制:需与GPIO_11.DS1/GPIO_11.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_11_ctrl_ds1
  - GPIO_11.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_11_ctrl_ds0
  - GPIO_11.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_11_ctrl_st
  - GPIO_11.ST 管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_12_CTRL

PAD_GPIO_12_CTRL 为 GPIO_12 控制寄存器。

Offset Address: 0x830 Total Reset Value: 0x0000_0A00

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_12_ctrl_ie
  - GPIO_12.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_12_ctrl_ps
  - GPIO_12.PS 管脚控制:需与 GPIO_12.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_12_ctrl_pe
  - GPIO_12.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_12_ctrl_ds2
  - GPIO_12.DS2 管脚控制:需与 GPIO_12.DS1/GPIO_12.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_12_ctrl_ds1
  - GPIO_12.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_12_ctrl_ds0
  - GPIO_12.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_12_ctrl_st
  - GPIO_12.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_13_CTRL

PAD_GPIO_13_CTRL 为 GPIO_13 控制寄存器。

Offset Address: 0x834 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_13_ctrl_ie
  - GPIO_13.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_13_ctrl_ps
  - GPIO_13.PS 管脚控制:需与 GPIO_13.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_13_ctrl_pe
  - GPIO_13.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_13_ctrl_ds2
  - GPIO_13.DS2 管脚控制:需与GPIO_13.DS1/GPIO_13.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_13_ctrl_ds1
  - GPIO_13.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_13_ctrl_ds0
  - GPIO_13.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_13_ctrl_st
  - GPIO_13.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_GPIO_14_CTRL

PAD_GPIO_14_CTRL 为 GPIO_14 控制寄存器。

Offset Address: 0x838 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_gpio_14_ctrl_ie
  - GPIO_14.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_gpio_14_ctrl_ps
  - GPIO_14.PS 管脚控制:需与 GPIO_14.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_gpio_14_ctrl_pe
  - GPIO_14.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_gpio_14_ctrl_ds2
  - GPIO_14.DS2 管脚控制:需与GPIO_14.DS1/GPIO_14.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_gpio_14_ctrl_ds1
  - GPIO_14.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_gpio_14_ctrl_ds0
  - GPIO_14.DS0 管脚控制。
  - 0x0
* - [3]
  - RW
  - pad_gpio_14_ctrl_st
  - GPIO_14.ST 管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_UART1_TXD_CTRL

PAD_UART1_TXD_CTRL 为 UART1_TXD 控制寄存器。

Offset Address: 0x83c Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_uart1_txd_ctrl_ie
  - UART1_TXD.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10:4]
  - -
  - reserved
  - 保留。
  - 0x00
* - [3]
  - RW
  - pad_uart1_txd_ctrl_st
  - UART1_TXD.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_UART1_RXD_CTRL

PAD_UART1_RXD_CTRL 为 UART1_RXD 控制寄存器。

Offset Address: 0x840 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_uart1_rxd_ctrl_ie
  - UART1_RXD.IE 管脚控制:default: 10:禁止;1:使能。
  - 0x1
* - [10:4]
  - -
  - reserved
  - 保留。
  - 0x00
* - [3]
  - RW
  - pad_uart1_rxd_ctrl_st
  - UART1_RXD.ST 管脚控
  - 0x0
* -
  -
  -
  - 制:0: No Schmitt;1: Schmitt Enable。
  -
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_UART0_TXD_CTRL

PAD_UART0_TXD_CTRL 为 UART0_TXD 控制寄存器。

Offset Address: 0x844 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_uart0_txd_ctrl_ie
  - UART0_TXD.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10:4]
  - -
  - reserved
  - 保留。
  - 0x00
* - [3]
  - RW
  - pad_uart0_txd_ctrl_st
  - UART0_TXD.ST 管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_UART0_RXD_CTRL

PAD_UART0_RXD_CTRL 为 UART0_RXD 控制寄存器。

Offset Address: 0x848 Total Reset Value: 0x0000_0800

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_uart0_rxd_ctrl_ie
  - UART0_RXD.IE 管脚控制:0: 输入禁止;1: 输入使能。
  - 0x1
* - [10:4]
  - -
  - reserved
  - 保留。
  - 0x00
* - [3]
  - RW
  - pad_uart0_rxd_ctrl_st
  - UART0_RXD.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

#### PAD_SFC_CLK_CTRL

PAD_SFC_CLK_CTRL 为 SFC_CLK 控制寄存器。

Offset Address: 0x868 Total Reset Value: 0x0000_0810

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_sfc_clk_ctrl_ie
  - SFC_CLK.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_sfc_clk_ctrl_ps
  - SFC_CLK.PS 管脚控制:需与 SFC_CLK.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x0
* - [9]
  - RW
  - pad_sfc_clk_ctrl_pe
  - SFC_CLK.PE 管脚控制。
  - 0x0
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_sfc_clk_ctrl_ds2
  - SFC_CLK.DS2 管脚控制:需与SFC_CLK.DS1/SFC_CLK.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_sfc_clk_ctrl_ds1
  - SFC_CLK.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_sfc_clk_ctrl_ds0
  - SFC_CLK.DS0 管脚控制。
  - 0x1
* - [3]
  - RW
  - pad_sfc_clk_ctrl_st
  - SFC_CLK.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

#### PAD_SFC_CSN_CTRL

PAD_SFC_CSN_CTRL 为 SFC_CSN 控制寄存器。

Offset Address: 0x86c Total Reset Value: 0x0000_0E10

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_sfc_csn_ctrl_ie
  - SFC_CSN.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_sfc_csn_ctrl_ps
  - SFC_CSN.PS 管脚控制:需与SFC_CSN.PE管脚控制结合使用。PE/PS对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x1
* - [9]
  - RW
  - pad_sfc_csn_ctrl_pe
  - SFC_CSN.PE管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_sfc_csn_ctrl_ds2
  - SFC_CSN.DS2管脚控制:需与SFC_CSN.DS1/SFC_CSN.DS0管脚控制结合使用。DS2~DS0对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_sfc_csn_ctrl_ds1
  - SFC_CSN.DS1管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_sfc_csn_ctrl_ds0
  - SFC_CSN.DS0管脚控制。
  - 0x1
* - [3]
  - RW
  - pad_sfc_csn_ctrl_st
  - SFC_CSN.ST管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_SFC_IO0_CTRL

PAD_SFC_IO0_CTRL 为 SFC_IO0 控制寄存器。

Offset Address: 0x870 Total Reset Value: 0x0000_0E10

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_sfc_io0_ctrl_ie
  - SFC_IO0.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_sfc_io0_ctrl_ps
  - SFC_IO0.PS 管脚控制:需与 SFC_IO0.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x1
* - [9]
  - RW
  - pad_sfc_io0_ctrl_pe
  - SFC_IO0.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_sfc_io0_ctrl_ds2
  - SFC_IO0.DS2 管脚控制:需与SFC_IO0.DS1/SFC_IO0.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_sfc_io0_ctrl_ds 1
  - SFC_IO0.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_sfc_io0_ctrl_ds 0
  - SFC_IO0.DS0 管脚控制。
  - 0x1
* - [3]
  - RW
  - pad_sfc_io0_ctrl_st
  - SFC_IO0.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_SFC_IO1_CTRL

PAD_SFC_IO1_CTRL 为 SFC_IO1 控制寄存器。

Offset Address: 0x874 Total Reset Value: 0x0000_0E10

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_sfc_io1_ctrl_ie
  - SFC_IO1.IE 管脚控制:0: 输入禁止;1: 输入使能。
  - 0x1
* - [10]
  - RW
  - pad_sfc_io1_ctrl_ps
  - SFC_IO1.PS 管脚控制:需与 SFC_IO1.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00: 无上下拉;01: 强上拉;10: 下拉;11: 上拉。
  - 0x1
* - [9]
  - RW
  - pad_sfc_io1_ctrl_pe
  - SFC_IO1.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_sfc_io1_ctrl_ds2
  - SFC_IO1.DS2 管脚控制:需与SFC_IO1.DS1/SFC_IO1.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_sfc_io1_ctrl_ds1
  - SFC_IO1.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_sfc_io1_ctrl_ds0
  - SFC_IO1.DS0 管脚控制。
  - 0x1
* - [3]
  - RW
  - pad_sfc_io1_ctrl_st
  - SFC_IO1.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_SFC_IO2_CTRL

PAD_SFC_IO2_CTRL 为 SFC_IO2 控制寄存器。

Offset Address: 0x878 Total Reset Value: 0x0000_0E10

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_sfc_io2_ctrl_ie
  - SFC_IO2.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_sfc_io2_ctrl_ps
  - SFC_IO2.PS 管脚控制:需与SFC_IO2.PE管脚控制结合使用。PE/PS对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x1
* - [9]
  - RW
  - pad_sfc_io2_ctrl_pe
  - SFC_IO2.PE管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_sfc_io2_ctrl_ds2
  - SFC_IO2.DS2管脚控制:需与SFC_IO2.DS1/SFC_IO2.DS0管脚控制结合使用。DS2~DS0对应驱动能力调节:111至000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_sfc_io2_ctrl_ds1
  - SFC_IO2.DS1管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_sfc_io2_ctrl_ds0
  - SFC_IO2.DS0管脚控制。
  - 0x1
* - [3]
  - RW
  - pad_sfc_io2_ctrl_st
  - SFC_IO2.ST管脚控制:0:No Schmitt;1:Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

### PAD_SFC_IO3_CTRL

PAD_SFC_IO3_CTRL 为 SFC_IO3 控制寄存器。

Offset Address: 0x87c Total Reset Value: 0x0000_0E10

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:12]
  - -
  - reserved
  - 保留。
  - 0x00000
* - [11]
  - RW
  - pad_sfc_io3_ctrl_ie
  - SFC_IO3.IE 管脚控制:0:输入禁止;1:输入使能。
  - 0x1
* - [10]
  - RW
  - pad_sfc_io3_ctrl_ps
  - SFC_IO3.PS 管脚控制:需与 SFC_IO3.PE 管脚控制结合使用。PE/PS 对应上下拉能力控制如下:00:无上下拉;01:强上拉;10:下拉;11:上拉。
  - 0x1
* - [9]
  - RW
  - pad_sfc_io3_ctrl_pe
  - SFC_IO3.PE 管脚控制。
  - 0x1
* - [8:7]
  - -
  - reserved
  - 保留。
  - 0x0
* - [6]
  - RW
  - pad_sfc_io3_ctrl_ds2
  - SFC_IO3.DS2 管脚控制:需与SFC_IO3.DS1/SFC_IO3.DS0 管脚控制结合使用。DS2~DS0 对应驱动能力调节:111~000,驱动能力依次减弱。
  - 0x0
* - [5]
  - RW
  - pad_sfc_io3_ctrl_ds1
  - SFC_IO3.DS1 管脚控制。
  - 0x0
* - [4]
  - RW
  - pad_sfc_io3_ctrl_ds0
  - SFC_IO3.DS0 管脚控制。
  - 0x1
* - [3]
  - RW
  - pad_sfc_io3_ctrl_st
  - SFC_IO3.ST 管脚控制:0: No Schmitt;1: Schmitt Enable。
  - 0x0
* - [2:0]
  - -
  - reserved
  - 保留。
  - 0x0
```

## GPIO

### 概述

GPIO（General Purpose Programable Input/Output）为通用可编程输入输出外设， 用于生成和采集特定应用的输入或输出信号，实现系统和外设之间的通信，方便系统对外设的控制。

### 功能描述

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

- 每组 GPIO 上报一个中断，共三个中断号，CPU 查询上报的 GPIO 编号。每个中断支持独立屏蔽功能，边沿中断支持可清除功能。

### 工作方式

### 初始化配置

每个 GPIO 可以单独配置为输入或者输出，具体步骤如下：

步骤 1 配置 GPIO_SW_OEN`n`数据方向寄存器，数据方向按 bit 单独控制，写入值为 1 表示该 bit 对应的数据方向是输入，写入值为 0 表示该 bit 对应的数据方向是输出；

步骤 2 写 GPIO_SW_OUT`n`数据寄存器，如果对应的 bit 数据方向是输出，写入该 bit 的值是对应 I/O 信号的输出，回读值等于最后一次写入的值。如果对应的 bit 数据方向是输入，写入值不起作用；

步骤 3 读 GPIO_SW_OUT`n`数据寄存器，如果对应的 bit 数据方向是输入，读该寄存器为外部端口的输入值，软件写入值无效。

 

```{important}
当 GPIO 用作输出时，建议禁止 GPIO 控制器的中断功能，否则当输出信号符合中断产生条件时，会产生 GPIO 中断。
```


### 边沿中断配置

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

### 电平中断配置

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

### 寄存器概览

GPIO 寄存器概览如表 6-5 所示。

表6-5 GPIO 寄存器概览（基址是 GPIO0:0x44028000、GPIO1:0x44029000、

GPIO2:0x4402A000）

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


### 寄存器描述

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

#### GPIO_SW_OEN

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

#### GPIO_INT_EN

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

#### GPIO_INT_MASK

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

#### GPIO_INT_TYPE

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

#### GPIO_INT_POLARITY

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

#### GPIO_INT_DEDGE

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

#### GPIO_INT_DEBOUNCE

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

#### GPIO_INT_RAW

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

#### GPIO_INTR

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

#### GPIO_INT_EOI

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

#### GPIO_DATA_SET

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

#### GPIO_DATA_CLR

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

## UART

### 概述

通用异步收发器 UART（universal asynchronous receiver/transmitter）是一个异步串行的通信接口，UART 主要用于和外部芯片的 UART 进行对接，实现两芯片间的通信。

芯片提供 3 个 UART 单元（UART0/1/2），UART0 仅支持两线模式，UART1/2 支持流控功能。

### 功能描述

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

- 支持 DMA 方式。

- 支持中断方式。

- 支持软件查询方式。

### 工作方式

### 接口信号

UART 接口信号描述如表 UART 接口信号描述所示。

表6-6UART 接口信号描述

| 信号名 | 宽度(bit) | 方向 | 功能描述 |
| --- | --- | --- | --- |
| RXD | 1 | I | 输入数据。 |
| TXD | 1 | O | 输出数据。 |
| CTS | 1 | I | 清除发送信号,用于硬件流控,低有效。 |
| RTS | 1 | O | 请求发送信号,用于硬件流控,低有效。 |


#### UART 数据格式

```{important}
整数波特率寄存器和小数波特率寄存器的值必须等到当前数据发送和接收完毕才更新。
```


UART 的数据帧格式如图 6-1 所示。其中数据帧长度、停止位位数和奇偶检验可配置。

```{figure} images/fig-6-1-uart-data-format.jpg
:name: fig-6-1
UART 数据帧格式
```

### 中断或查询方式下的数据传输

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

表6-7自动流控配置参考

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

步骤 1 将发送数据写入 DATA`data`步骤，启动数据发送。若为查询模式则跳转至步骤 2，若为中断模式则跳转至步骤 3。

步骤 2 查询方式下，如果进行连续数据发送，需要通过读取 FIFO_STATUS`tx_fifo_full`检测 TX FIFO 状态。如果 FIFO_STATUS`tx_fifo_full`为 0，即 TX FIFO 未满，则可以向 TX FIFO 中发送数据。直到无数据需要发送，跳转至步骤 4。

步骤 3 中断方式下，在中断服务程序中查询 INTR_STATUS`thre_intr_status`发送中断状态位，决定是否向 TX FIFO 中发送数据。当 INTR_STATUS`thre_intr_status`置 1，此时 TX FIFO 内数据量小于发送数据水线，可以向 TX FIFO 中发送数据。直到无数据需要发送，跳转至步骤 4。

步骤 4 通过检测 INTR_STATUS`tx_fifo_empty`是否为 1，判断 UART 是否完成全部数据发送。

数据接收的处理方式如下：

步骤 1 等待数据接收，若为查询模式则跳转至步骤 2。若为中断模式则跳转至步骤 3。

步骤 2 查询方式下，进行数据接收时通过读取 INTR_STATUS`rx_fifo_empty`检测 RX_FIFO 状态，如果 INTR_STATUS`rx_fifo_empty`为 0，则 RX_FIFO 非空，可以读取 RX_FIFO 中的数据，跳转至步骤 4。

步骤 3 中断方式下，则检测 INTR_STATUS`data_avail_intr_status`接收中断状态位，决定是否读取 RX_FIFO 中的数据。当 INTR_STATUS`data_avail_intr_status`置 1，此时 RX_FIFO 内数据量大于接收 FIFO 水线，可以读取 RX_FIFO 中数据，跳转至步骤 4。

步骤 4 回读 DATA`data`，读出数据即为 RX 数据。

### 寄存器概览

UART 寄存器概览如表 6-8 所示。

表6-8 UART 寄存器概览（基址是 UART0：0x44010000、UART1：0x44011000、 UART2：0x44012000）

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


### 寄存器描述

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

#### DATA

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

#### UART_CTL

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

#### INTR_EN

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

#### INTR_STATUS

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

#### FAR

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

#### MODEM_CTL

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

#### MODEM_STATUS

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

#### LINE_STATUS

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

#### UART_GP_REG

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

#### TX_FIFO_READ

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

#### RX_FIFO_WRITE

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

#### FIFO_STATUS

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

#### TX_FIFO_CNT

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

#### RX_FIFO_CNT

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

#### HALT_TX

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

#### DMA_SW_ACK

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

#### UART_PARAMETER

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

## I2C

### 概述

I2C 模块是 APB 总线上的从设备，是 I2C 总线上的主设备。I2C 模块的作用是完成 CPU 对 I2C 总线上从设备的数据读写，CPU 可以连续配置多个发送的数据和接收多个数据。I2C 总线上可挂载多个从设备，芯片支持 2 个 I2C 模块（I2C0 和 I2C1）。

### 功能描述

### I2C 具有以下功能特点：

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

兼容不使用 FIFO 和使用 FIFO 两种工作方式

### 工作方式

### I2C 包含以下两种工作场景：

主机仅对单个数据发送和接收（不使用 FIFO）。

主机连续发送多个数据、连续接收多个数据（使用 FIFO）。

### 不使用 FIFO

### I2C 主机发送数据流程

I2C 主机发送数据流程如图 6-2 所示。

```{figure} images/fig-6-2-i2c-tx-no-fifo.jpg
:name: fig-6-2
I2C 主机发送数据（不使用 FIFO）流程图
```

### I2C 主机接收数据流程

I2C 主机接收数据流程如图 6-3 所示。

```{figure} images/fig-6-3-i2c-rx-no-fifo.jpg
:name: fig-6-3
I2C 主机接收数据（不使用 FIFO）流程图
```

### 使用 FIFO

### I2C 主机发送数据流程

I2C 主机发送数据流程图如图 6-4 所示。

```{figure} images/fig-6-4-i2c-tx-fifo.jpg
:name: fig-6-4
I2C 主机发送数据（使用 FIFO）流程图
```

### I2C 主机接收数据流程

I2C 主机接收数据流程如图 6-5 所示。

```{figure} images/fig-6-5-i2c-rx-fifo.jpg
:name: fig-6-5
I2C 主机接收数据（使用 FIFO）流程图
```

### 寄存器概览

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


### 寄存器描述

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

### 说明

新中断到来时，I2C 模块会自动将 I2C_ICR 相应位清 0。

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

### 说明

I2C_SR bit[1]表示 I2C 总线仲裁失败。当 I2C_SR bit[1]有效时，当前操作失败。在清 I2C_SR bit[1]之前，需要清除其他中断标志，然后清除 I2C_COM 或向 I2C_COM 写入新的操作命令， 最后清除 I2C_SR bit[1]。

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

### 说明

在系统初始化时配置或配置前使 I2C_CTRL bit[7]=0。

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

### 说明

在系统初始化时配置或配置前使 I2C_CTRL bit[7]=0。

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

### 说明

不使用 FIFO模式下，发送结束后，I2C模块不会修改 I2C_TXR内容；使用FIFO 模式下，写入的数据会自动载入到发送 FIFO 中保存直到该数据发送结束。

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

### 说明

不使用 FIFO 模式下，I2C_RXR 数据在 I2C_SR bit[3]=1 时，数据有效。同时数据将保持到下一个读操作前。使用 FIFO 模式下，读取 I2C_RXR 会直接从接收 FIFO 中取数据。

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

## SPI

### 概述

SPI实现数据的串并、并串转换，可以作为 Master 或 Slave 与外部设备进行同步串行通信（外围设备必须支持 SPI 帧格式）。芯片的 SPI 工作参考时钟为 240MHz。

### 功能描述

SPI具有以下功能特点：

- 支持接口时钟频率可编程。

- 作为主设备：最大支持 10M 接口频率工作。

- 作为从设备：最大支持 32M 接口频率工作；。

- 支持 SPI 帧格式，分为以下三种：

Motorola 帧格式

TI（Texas Instruments）帧格式

National Microwire 帧格式

串行数据帧长度可编程：4bit～16bit。

支持发送 FIFO 中断、接收 FIFO 中断独立屏蔽。

内部提供环回测试模式。

支持 DMA 操作，但不支持作为 DMA 的流控设备。

## PWM

### 概述

PWM模块用于生成 PWM信号。

### 功能描述

PWM模式具有以下功能特点：

- 支持 8 路 PWM。

- 支持将 PWM 分组绑定，实现互补输出，最多支持 4 组分组。

- 支持 PWM 输出恒为 0、1 或高阻。

- PWM 占空比支持 0~100%（256 档）。

- 支持 PWM不同配置间的平滑切换。

### 工作方式

PWM0~7 模块支持 2 个时钟源：晶振时钟；PLL 时钟。

以配置 PWM0 信号对 80M 时钟分频、分频倍数为 25 倍、占空比为 1/5 为例，配置步骤如下：

步骤 1 写 CLDO_CRG_CLK_SEL`pwm_cksel`为 0x1，将 PWM 时钟置为 80M。

步骤 2 写 PWM_ABNOR_STATE_CLR0`pwm_abnor_state_clr0`为 0xFFFF，写

PWM_ABNOR_STATE_CLR1`pwm_abnor_state_clr1`为 0xFFFF，清除异常状态。

步骤 3 写 PWM_EN`pwm_en_0`为 1，使能 PWM0。

步骤 4 写 PWM_FREQ_L`pwm_freq_l_0`为 0x19，配置分频倍数为 25。

步骤 5 写 PWM_DUTY_L`pwm_duty_l_0`为 0x5，配出占空比 1/5。

步骤 6 写 PWM_PORTITY`pwm_poarity_0`为 0，PWM 输出极性为正向极性。

步骤 7 写 PWM_SEL`pwm_sel_0`为 0x1，配置第一组使用的 PWM0。

步骤 8 写 PWM_STARTCLRCNT_EN`pwm_startclrcnt_en_0`为 1，在 start 时刻对 PWM 内部寄存器载入配置并清零计数器。

步骤 9 写 PWM_START`pwm_start_0`为 1，配置 PWM0 新配置生效。

 

### 寄存器概览

PWM 寄存器概览如表 6-12 所示。

表6-10 PWM 寄存器概览（基址是 0x4402_4000）

| 偏移地址 | 名称 | 描述 |
| --- | --- | --- |
| 0x000 + 0x10×i | PWM_SEL | pwm 分组选择控制寄存器。 |
| 0x004 + | PWM_STARTCLRCN T_EN | pwm 配置生效计数清零使能寄存器。 |
| 0x10×i |  |  |
| 0x008 + 0x10×i | PWM_START | PWM 配置生效寄存器。 |
| 0x0100 + 0x40×j | PWM_EN | PWM 使能寄存器。 |
| 0x0104 + 0x40×j | PWM_PORTITY | PWM 的输出极性配置寄存器。 |
| 0x0108 + 0x40×j | PWM_OEN_CFG | Pwm 无效电平高阻使能配置寄存器。 |
| 0x010C + 0x40×j | PWM_OFFSET_L | PWM_START 为 PWM 相位控制计数值低 16bit 寄存器。 |
| 0x0110 + 0x40×j | PWM_OFFSET_H | PWM_START 为 PWM 相位控制计数值高 16bit 寄存器。 |
| 0x0114 + 0x40×j | PWM_FREQ_L | PWM_FREQ 为 PWM 频率控制计数值低 16bit 寄存器。 |
| 0x0118 + 0x40×j | PWM_FREQ_H | PWM_FREQ 为 PWM 频率控制计数值高 16bit 寄存器。 |
| 0x011C + 0x40×j | PWM_DUTY_L | PWM_DUTY 为 PWM 占空比计数值寄存器。 |
| 0x0120 + 0x40×j | PWM_DUTY_H | PWM_DUTY 为 PWM 占空比计数值寄存器。 |
| 0x0124 + 0x40×j | PWM_PERIODLOAD_FLAG | PWM 周期配置允许标志寄存器。 |
| 0x0128 + 0x40×j | PWM_PERIOD_VAL | PWM 周期脉冲周期值寄存器。 |
| 0x012C + 0x40×j | PWM_PERIODCNT | PWM 周期脉冲周期值寄存器。 |
| 0x500 | PWM_ABNOR_STATE0 | pwm 异常状态寄存器 0。 |
| 0x504 | PWM_ABNOR_STATE1 | pwm 异常状态寄存器 1。 |
| 0x508 | PWM_ABNOR_STATE_CLR0 | pwm 异常状态清除寄存器 0。 |
| 0x50C | PWM_ABNOR_STATE_CLR1 | pwm 异常状态清除寄存器 1。 |
| 0x510 | PWM_INT_MASK | pwm 中断屏蔽寄存器。 |
| 0x0514 | PWM_DMA_EN | pwm dma 使能寄存器。 |
| 0x0518 | PWM_CFG_INT_CLR0 | pwm 步进模式循环结束中断清除。 |


PWM 寄存器偏移地址中变量的取值范围和含义如表 6-13 所示。

表6-11PWM寄存器偏移地址变量表

| 变量名称 | 取值范围 | 描述 |
| --- | --- | --- |
| i | 0~3 | PWM 分组 |
| j | 0~7 | pwm 个数 |


### 寄存器描述

PWM_SEL

PWM_SEL 为 pwm 分组选择控制寄存器。

### 说明

本 IP 仅支持 8 个 PWM，最大可以支持分组数为 4；

即下述寄存器i 支持0~3，j支持0~7

Offset Address: 0x000＋0x10×i Total Reset Value: 0x0000_0000

| Bits | Access | Name | Description | Reset |
| --- | --- | --- | --- | --- |
| [31:16] | - | reserved | 保留。 | 0x0000 |
| [15:0] | RW | pwm_sel_i | 分组 pwm 选择信号,最多支持 | 0x0000 |
|  | 4 组,每组对应 8bitpwm_sel,每 bit 对应一路pwm。 |  |  |  |


#### PWM_STARTCLRCNT_EN

PWM_STARTCLRCNT_EN 为 pwm 配置生效计数清零使能寄存器。

Offset Address: 0x004＋0x10×i Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:1]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [0]
  - RW
  - pwm_startclrcnt_en_i
  - star 时刻对 pwm 内部寄存器清零使能。每组对应 1bitpwm_startclrcnt_en。
  - 0x0
```

#### PWM_START

PWM_START 为 PWM 配置生效寄存器。

Offset Address: 0x008＋0x10×i Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:1]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [0]
  - W1_PULSE
  - pwm_start_i
  - pwm 配置生效寄存器。配成 1时,此前赋值的 pwm 相关寄存器生效。每组对应 1bitpwm_start。注意:因逻辑内部模块需要对相关寄存器配置值进行同步和处理,建议该寄存器的配置间隔时间至少 10μs 以上。
  - 0x0
```

#### PWM_EN

PWM_EN 为 PWM 使能寄存器。

Offset Address: 0x0100＋0x40×j Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:1]
  - -
  - reserved
  - 保留
  - 0x00000000
* - [0]
  - RW
  - pwm_en_j
  - pwm 功能使能,每路 pwm 对应一个 pwm_en。0: pwm 关闭,pwm_out 输出持续为 0;1: pwm 使能打开。
  - 0x0
```

#### PWM_PORTITY

PWM_PORTITY 为 PWM 的输出极性配置寄存器。

Offset Address: 0x0104＋0x40×j Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:1]
  - -
  - reserved
  - 保留
  - 0x00000000
* - [0]
  - RW
  - pwm_poarity_j
  - Pwm 输出极性配置:0: 正向极性;1: 反向极性。
  - 0x0
```

#### PWM_OEN_CFG

PWM_OEN_CFG 为 Pwm 无效电平高阻使能配置寄存器。

Offset Address: 0x0108＋0x40×j Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:1]
  - -
  - reserved
  - 保留
  - 0x00000000
* - [0]
  - RW
  - pwm_oen_cfg_j
  - Pwm 无效电平高阻使能配置:0:无效电平跟随极性等其他配置;1:无效电平时 Pwm 输出高阻。
  - 0x0
```

#### PWM_OFFSET_L

PWM_OFFSET_L 为 PWM_START 为 PWM 相位控制计数值低 16bit 寄存器。

Offset Address: 0x010C＋0x40×j Total Reset Value: 0x0000_0000

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
  - pwm_offset_l_j
  - Pwm 相位控制计数值的低 16bit,控制 pwm 在一个周期内为 1 的位置,对 PWM,取值范围 1~65535。每路 pwm 对应一个 offset 参数。
  - 0x0000
```

#### PWM_OFFSET_H

PWM_OFFSET_H 为 PWM_START 为 PWM 相位控制计数值高 16bit 寄存器。

Offset Address: 0x0110＋0x40×j Total Reset Value: 0x0000_0000

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
  - pwm_offset_h_j
  - Pwm 相位控制计数值的高 16bit,在 pwm_offset_l 计满后+1,控制 pwm 在一个周期内为 1 的位置,对 PWM,取值范围 1~65535。每路 pwm 对应一个 offset 参数。
  - 0x0000
```

#### PWM_FREQ_L

PWM_FREQ_L 为 PWM_FREQ 为 PWM 频率控制计数值低 16bit 寄存器。

Offset Address: 0x0114＋0x40×j Total Reset Value: 0x0000_0000

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
  - pwm_freq_l_j
  - pwm 频率控制计数值的低 16bit,含义为对 PWM 时钟的分频倍数,取值范围 1~65535。每路 pwm 对应一个 freq 参数。
  - 0x0000
```

#### PWM_FREQ_H

PWM_FREQ_H 为 PWM_FREQ 为 PWM 频率控制计数值高 16bit 寄存器。

Offset Address: 0x0118＋0x40×j Total Reset Value: 0x0000_0000

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
  - pwm_freq_h_j
  - pwm 频率控制计数值的高 16bit,在 pwm_freq_l 计满后 +1,含义为对 PWM 时钟的分频倍数,取值范围 1~65535。每路 pwm 对应一个 freq 参数。
  - 0x0000
```

#### PWM_DUTY_L

PWM_DUTY_L 为 PWM_DUTY 为 PWM 占空比计数值寄存器。

Offset Address: 0x011C＋0x40×j Total Reset Value: 0x0000_0000

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
  - pwm_duty_l_j
  - pwm 占空比控制计数值的低 16bit,取值范围 1~65535。pwm_duty 与 pwm_freq 的比值为占空比。每路 pwm 对应一个 duty 参数。
  - 0x0000
```

#### PWM_DUTY_H

PWM_DUTY_H 为 PWM_DUTY 为 PWM 占空比计数值寄存器。

Offset Address: 0x0120＋0x40×j Total Reset Value: 0x0000_0000

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
  - pwm_duty_h_j
  - pwm 占空比控制计数值的高 16bit,在 pwm_duty_l 计满后 +1,取值范围 1~65535。pwm_duty 与 pwm_freq 的比值为占空比。每路 pwm 对应一个 duty 参数。
  - 0x0000
```

#### PWM_PERIODLOAD_FLAG

PWM_PERIODLOAD_FLAG 为 PWM 周期配置允许标志寄存器。

Offset Address: 0x0124＋0x40×j Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:1]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [0]
  - RO
  - pwm_periodload_flag_j
  - pwm 平滑切换周期结束,可进行新参数配置标志寄存器。周期计数结束产生。配置 start 清除/或者配置 pwm_cfg_int_clr0 寄存可清除。
  - 0x0
```

#### PWM_PERIOD_VAL

PWM_PERIOD_VAL 为 PWM 周期脉冲周期值寄存器。

Offset Address: 0x0128＋0x40×j Total Reset Value: 0x0000_0000

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
  - pwm_period_val_j
  - Pwm 输出脉冲数值,非零时触发 pwm 输出脉冲计数功能,输出脉冲个数大于该值时会加载新参数继续计数。
  - 0x0000
```

#### PWM_PERIODCNT

PWM_PERIODCNT 为 PWM 周期脉冲周期值寄存器。

Offset Address: 0x012C＋0x40×j Total Reset Value: 0x0000_0000

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
  - RO
  - pwm_periodcnt_j
  - Pwm 输出脉冲计数值。
  - 0x0000
```

#### PWM_ABNOR_STATE0

PWM_ABNOR_STATE0 为 pwm 异常状态寄存器 0。

Offset Address: 0x500 Total Reset Value: 0x0000_0000

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
  - RO
  - pwm_abnor_state0
  - bit[15:0]为 Pwm 多路使用配置异常,每路 pwm 对应1bit。
  - 0x0000
```

#### PWM_ABNOR_STATE1

PWM_ABNOR_STATE1 为 pwm 异常状态寄存器 1。

Offset Address: 0x504 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:16]
  - RO
  - reserved
  - 保留。
  - 0x0000
* - [15:0]
  - RO
  - pwm_abnor_state1
  - bit[15:0]为 Pwm 计数值配置异常,每路 pwm 对应 1bit。
  - 0x0000
```

#### PWM_ABNOR_STATE_CLR0

PWM_ABNOR_STATE_CLR0 为 pwm 异常状态清除寄存器 0。

Offset Address: 0x508 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:16]
  - RO
  - reserved
  - 保留。
  - 0x0000
* - [15:0]
  - W1_PULSE
  - pwm_abnor_state_clr0
  - Pwm 异常清除寄存器 0,对应寄存器pwm_abnor_state0。
  - 0x0000
```

#### PWM_ABNOR_STATE_CLR1

PWM_ABNOR_STATE_CLR1 为 pwm 异常状态清除寄存器 1。

Offset Address: 0x50C Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:16]
  - RO
  - reserved
  - 保留。
  - 0x0000
* - [15:0]
  - W1_PULSE
  - pwm_abnor_state_clr1
  - Pwm 异常清除寄存器,对应寄存器pwm_abnor_state1。
  - 0x0000
```

#### PWM_INT_MASK

PWM_INT_MASK 为 pwm 中断屏蔽寄存器。

Offset Address: 0x510 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:2]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [1:0]
  - RW
  - pwm_int_mask
  - pwm 中断屏蔽寄存器,0: 屏蔽;1: 不屏蔽,默认屏蔽:bit[1]: 步进模式一轮周期循环结束中断屏蔽;bit[0]: 异常中断屏蔽。
  - 0x0
```

#### PWM_DMA_EN

PWM_DMA_EN 为 pwm dma 使能寄存器。

Offset Address: 0x0514 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:1]
  - -
  - reserved
  - 保留。
  - 0x00000000
* - [0]
  - RW
  - pwm_dma_en
  - dma 功能使能:0:禁止。1:使能;
  - 0x0
```

#### PWM_CFG_INT_CLR0

PWM_CFG_INT_CLR0 为 pwm 步进模式循环结束中断清除。

Offset Address: 0x0518 Total Reset Value: 0x0000_0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:16]
  - RO
  - reserved
  - 保留。
  - 0x0000
* - [15:0]
  - W1_PULSE
  - pwm_cfg_int_clr0
  - Pwmpwm 步进模式循环结束中断清除寄存器。对应 pwm_cfg_int 的中断和pwm_periodload_flag_j 寄存器。
  - 0x0000
```

## Tsensor

### 概述

Tsensor 是模拟温度检测 IP，检测芯片的节温并以二进制形式输出温度信息。

检查温度范围： $- 4 0 ^ { \circ } C \sim + 1 2 5 ^ { \circ } C$ 的温度检测，10bit SARADC 量化温度，分辨率 0.208℃/LSB。

支持 IP 校准后温度精度在 $\pm 2 ^ { \circ } C$ 以内。

### 功能描述

支持 Tsensor 三种测温模式：单次 16 点平均测温模式，周期 16 点平均测温模式，单点测温模式。

支持 Tsensor 测温完成中断上报。

支持 Tsensor 测温 overtemp 中断上报。

支持高温低温门限的使用。

支持软件分别可配高温门限和低温门限。

支持周期采样温度上报。

支持软件可配周期采样间隔。

支持 Tsensor 测温门限中断上报。

### 工作方式

Tsensor 模块的工作模式分为以下 3 种：

正常检测温度模式。

高低温门限中断模式。

过温保护中断模式。

### 说明

以上 3 种模式均为在检测温度值基础上进行，检测温度的模式有多种，此处检测温度的模式均为周期采样配合 16 次单点平均计算。

### 正常检测温度模式

正常检测温度模式配置步骤如下：

步骤 1 写 TSENSOR_STS`tsensor_clr`为 0x1，清除所有模式的状态信息。

步骤 2 写 TSENSOR_TEMP_INT_CLR`tsensor_int_clr`为 0x1，清除 Tsensor 中断信号。

步骤 3 写 TSENSOR_TEMP_INT_EN`tsensor_done_int_en`为 0x1，打开 Tsensor 的采集温度完成中断使能。

步骤 4 写 TSENSOR_CTRL`tsensor_mode`为 0x0，选择 16 次平均值的单次上报方式。

步骤 5 写 TSENSOR_CTRL`tsensor_enable`为 0x1，开启 Tsensor 的使能信号。

步骤 6 写 TSENSOR_AUTO_REFRESH_PERIOD`tsensor_auto_refresh_period`，设置合适的周期采样的时间间隔。

步骤 7 写 TSENSOR_AUTO_REFRESH_CFG`tsensor_auto_refresh_enable`为 0x1，开启周期采样的使能信号。

步骤 8 读 TSENSOR_TEMP_INT_STS`tsensor_done_int_sts`为 0x1，等待 16 点平均计算温度模式下的中断信号的产生。

步骤 9 读 TSENSOR_STS`tsensor_data`，获取 16 点平均单次上报模式下的温度值。

### 高低温门限中断模式

高低温门限中断模式配置步骤如下：

步骤 1 写 TSENSOR_STS`tsensor_clr`为 0x1，清除自动模式下产生的 rdy 信号。

步骤 2 写 TSENSOR_TEMP_INT_CLR`tsensor_int_clr`为 0x1，清除 Tsensor 中断信号。

步骤 3 写 TSENSOR_TEMP_INT_EN`tsensor_out_thresh_int_en`为 0x1，打开 Tsensor 的超门限范围中断使能。

步骤 4 写 TSENSOR_TEMP_HIGH_LIMIT`tsensor_temp_high_limit`、 TSENSOR_TEMP_LOW_LIMIT`tsensor_temp_low_limit`，设置合适的高低温门限值。

步骤 5 写 TSENSOR_CTRL`tsensor_mode`为 0x0，选择 16 次平均值的单次上报方式。

步骤 6 写 TSENSOR_CTRL`tsensor_enable`为 0x1，开启 Tsensor 的使能信号。

步骤 7 写 TSENSOR_AUTO_REFRESH_PERIOD`tsensor_auto_refresh_period`，设置合适的周期采样的时间间隔。

步骤 8 写 TSENSOR_AUTO_REFRESH_CFG`tsensor_auto_refresh_enable`为 0x1，开启周期采样的使能信号。

步骤 9 读 TSENSOR_TEMP_INT_STS`tsensor_out_thresh_int_sts`是否为 1，如果为 1，则当前的温度值高于高温门限或低于低温门限。

 

### 过温保护中断模式

过温保护中断模式配置步骤如下：

步骤 1 写 TSENSOR_STS`tsensor_clr`为 0x1，清除自动模式下产生的 rdy 信号。

步骤 2 写 TSENSOR_TEMP_INT_CLR`tsensor_int_clr`为 0x1，清除 Tsensor 中断信号。

步骤 3 写 TSENSOR_TEMP_INT_EN`tsensor_overtemp_int_en`为 0x1，打开 Tsensor 的过温中断使能。

步骤 4 写 TSENSOR_OVER_TEMP`tsensor_overtemp_thresh`，设置合适的过温门限值。

步骤 5 写 TSENSOR_OVER_TEMP`tsensor_overtemp_thresh_en`为 0x1，打开过温保护使能信号。

步骤 6 写 TSENSOR_CTRL`tsensor_mode`为 0x0，选择 16 次平均值的单次上报方式。

步骤 7 写 TSENSOR_CTRL`tsensor_enable`为 0x1，开启 Tsensor 的使能信号。

步骤 8 写 TSENSOR_AUTO_REFRESH_PERIOD`tsensor_auto_refresh_period`，设置合适的周期采样的时间间隔。

步骤 9 写 TSENSOR_AUTO_REFRESH_CFG`tsensor_auto_refresh_enable`为 0x1，开启周期采样的使能信号。

读 TSENSOR_TEMP_INT_STS`tsensor_overtemp_int_sts`是否为 1，如果为 1，则当前的温度值超过了设置的过温门限值。

 

### 寄存器概览

Tsensor 寄存器概览如表 1-1 所示。

表6-12 Tsensor 寄存器概览（基址是 0x4000_0000）

| 偏移地址 | 名称 | 描述 |
| --- | --- | --- |
| 0x0000 + 0x1000×CH_NUM | TSENSOR_CTL_ID | TSENSOR CTL ID 寄存器。 |
| 0x0010 + 0x1000×CH_NUM | TSENSOR_REG0 | 通用寄存器。 |
| 0x0014 + 0x1000×CH_NUM | TSENSOR_REG1 | 通用寄存器。 |
| 0x0018 + 0x1000×CH_NUM | TSENSOR_REG2 | 通用寄存器。 |
| 0x001C + 0x1000×CH_NUM | TSENSOR_REG3 | 通用寄存器。 |
| 0x0300 + 0x1000×CH_NUM | TSENSOR_START | TSENSOR 启动寄存器。 |
| 0x0304 + 0x1000×CH_NUM | TSENSOR_CTRL | TSENSOR 控制寄存器。 |
| 0x0308 + 0x1000×CH_NUM | TSENSOR_STS | TSENSOR 状态寄存器。 |
| 0x0310 + 0x1000×CH_NUM | TSENSOR_CTRL1 | TSENSOR 控制寄存器1。 |
| 0x0314 + 0x1000×CH_NUM | TSENSOR_TEMP_HIGH_LIMIT | TSENSOR 温度门限上限。 |
| 0x0318 + 0x1000×CH_NUM | TSENSOR_TEMP_LOW_LIMIT | TSENSOR 温度门限下限。 |
| 0x031C + 0x1000×CH_NUM | TSENSOR_OVER_TEMP | TSENSOR 过温控制寄存器。 |
| 0x0320 + 0x1000×CH_NUM | TSENSOR_TEMP_INT_EN | TSENSOR 中断控制寄存器。 |
| 0x0324 + 0x1000×CH_NUM | TSENSOR_TEMP_INT_CLR | TSENSOR 中断控制寄存器。 |
| 0x0328 + 0x1000×CH_NUM | TSENSOR_TEMP_INT_STS | TSENSOR 中断控制寄存器。 |
| 0x0330 + 0x1000×CH_NUM | TSENSOR_AUTO_REFRESH_PERIOD | TSENSOR 自动检测控制寄存器。 |
| 0x0334 + 0x1000×CH_NUM | TSENSOR_AUTO_REFRESH_CFG | TSENSOR 自动检测控制寄存器。 |


Tsensor 寄存器偏移地址中变量的取值范围和含义如表 6-15 所示。

表6-13 Tsensor 寄存器偏移地址变量表

| 变量名称 | 取值范围 | 描述 |
| --- | --- | --- |
| CH_NUM | 0 | Tsensor 组数 |


### 寄存器描述

TSENSOR_CTL_ID

TSENSOR_CTL_ID 为 TSENSOR CTL ID 寄存器

Offset Address：0x0000＋0x1000×CH_NUM Total Reset Value：0x0106

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:0]
  - RO
  - tsensor_ctl_id
  - TSENSOR CTL ID 寄存器。
  - 0x0106
```

#### TSENSOR_REG0

TSENSOR_REG0 为通用寄存器。

Offset Address：0x0010＋0x1000×CH_NUM Total Reset Value：0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:0]
  - RW
  - tsensor_reg0
  - Tsensor 通用寄存器 0。
  - 0x0000
```

#### TSENSOR_REG1

TSENSOR_REG1 为通用寄存器。

Offset Address：0x0014＋0x1000×CH_NUM Total Reset Value：0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:0]
  - RW
  - tsensor_reg1
  - Tsensor 通用寄存器 1。
  - 0x0000
```

#### TSENSOR_REG2

TSENSOR_REG2 为通用寄存器。

Offset Address：0x0018＋0x1000×CH_NUM Total Reset Value：0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:0]
  - RW
  - tsensor_reg2
  - Tsensor 通用寄存器 2。
  - 0x0000
```

#### TSENSOR_REG3

TSENSOR_REG3 为通用寄存器。

Offset Address：0x001C＋0x1000×CH_NUM Total Reset Value：0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:0]
  - RW
  - tsensor_reg3
  - Tsensor 通用寄存器 3。
  - 0x0000
```

#### TSENSOR_START

TSENSOR_START 为 TSENSOR 启动寄存器。

Offset Address：0x0300＋0x1000×CH_NUM Total Reset Value：0x0000

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
  - W1_PULSE
  - tsensor_start
  - 自动模式下,写1刷新一次温度码,回读tsensor_data_auto获取当前温度值,当tsensor_rdy_auto为1时,表明温度值有效。写0无效。
  - 0x0
```

#### TSENSOR_CTRL

TSENSOR_CTRL 为 TSENSOR 控制寄存器。

Offset Address：0x0304＋0x1000×CH_NUM Total Reset Value：0x0000

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
* - [2:1]
  - RW
  - tsensor_mode
  - 模式选择2'b00: 16 点平均单次上报模式;2'b01: 16 点平均循环上报模式;2'b10、2'b11: 单点循环上报模式(该模式不比较阈值,仅上报温度码)。
  - 0x0
* - [0]
  - RW
  - tsensor_enable
  - TSENSOR_CTRL 开关0: 关闭 TENSOR_CTRL;1: 打开 TENSOR_CTRL。
  - 0x0
```

#### TSENSOR_STS

TSENSOR_STS 为 TSENSOR 状态寄存器。

Offset Address：0x0308＋0x1000×CH_NUM Total Reset Value：0x0000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:12]
  - -
  - reserved
  - 保留。
  - 0x0
* - [11:2]
  - RO
  - tsensor_data
  - 所有模式下获取到的温度值。10bit 温度区间码值输出,线性分布;-40C~dec'114125C~dec'896即是 tsensor 直接输出码值对温度°C单位换算公式 T °C=[BIN2DEC(temp_out )-114]/(896-114)*[125-(-40)]+(-40)
  - 0x000
* - [1]
  - RO
  - tsensor_rdy
  - 所有模式下。0:检测未启动或手动检测中;1: tsensor_data 值为有效的温度值。
  - 0x0
* - [0]
  - W1_PULSE
  - tsensor_clr
  - 清除所有模式的状态。0:无效;1:清除。
  - 0x0
```

#### TSENSOR_CTRL1

TSENSOR_CTRL1 为 TSENSOR 控制寄存器 1。

Offset Address：0x0310＋0x1000×CH_NUM Total Reset Value：0x0000

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
  - temp_scan_dft
  - DFT使能0:功能输出;1:DFT输出。
  - 0x0
* - [3]
  - RW
  - temp_set
  - 0:功能模式下 temp_out 正常输出(默认);1:功能模式下 temp_out 可以通过数模接口输入来配置输出值。
  - 0x0
* - [2:1]
  - RW
  - temp_ct_sel
  - 对于输入 1M 精准时钟情况下:00:0.512ms;01:0.256ms;10:1.024ms;11:2.048ms。
  - 0x0
* - [0]
  - RW
  - temp_calib
  - 0:选择开启校准算法(默认);1.:不开启校准算法。
  - 0x0
```

#### TSENSOR_TEMP_HIGH_LIMIT

TSENSOR_TEMP_HIGH_LIMIT 为 TSENSOR 温度门限上限。

Offset Address：0x0314＋0x1000×CH_NUM Total Reset Value：0x0000

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
* - [9:0]
  - RW
  - tsensor_temp_high_limit
  - 过高温度阈值门限。
  - 0x000
```

#### TSENSOR_TEMP_LOW_LIMIT

TSENSOR_TEMP_LOW_LIMIT 为 TSENSOR 温度门限下限。

Offset Address：0x0318＋0x1000×CH_NUM Total Reset Value：0x0000

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
* - [9:0]
  - RW
  - tsensor_temp_low_limit
  - 过低温度阈值门限。
  - 0x000
```

#### TSENSOR_OVER_TEMP

TSENSOR_OVER_TEMP 为 TSENSOR 过温控制寄存器

Offset Address：0x031C＋0x1000×CH_NUM Total Reset Value：0x03FF

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:11]
  - -
  - reserved
  - 保留。
  - 0x00
* - [10]
  - RW
  - tsensor_overtemp_thresh_en
  - 16 点平均单次上报模式或16 点平均循环上报模式下过温 PA 保护使能。0: PA 保护使能关闭;1: PA 保护使能打开。
  - 0x0
* - [9:0]
  - RW
  - tsensor_overtemp_thresh
  - 过温保护阈值门限。
  - 0x3FF
```

#### TSENSOR_TEMP_INT_EN

TSENSOR_TEMP_INT_EN 为 TSENSOR 中断控制寄存器

Offset Address：0x0320＋0x1000×CH_NUM Total Reset Value：0x0000

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
  - tsensor_overemp_int_en
  - TSENSOR 过温保护中断使能。
  - 0x0
* - [1]
  - RW
  - tsensor_out_thresh_int_en
  - TSENSOR 温度超门限范围中断使能。0:禁止;1:使能。
  - 0x0
* - [0]
  - RW
  - tsensor_done_int_en
  - TSENSOR 温度采集完毕中断使能。0:禁止;1:使能。
  - 0x0
```

#### TSENSOR_TEMP_INT_CLR

TSENSOR_TEMP_INT_CLR 为 TSENSOR 中断控制寄存器。

Offset Address：0x0324＋0x1000×CH_NUM Total Reset Value：0x0000

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
  - W1_PULSE
  - tsensor_int_clr
  - 0:无效;1:清除中断。
  - 0x0
```

#### TSENSOR_TEMP_INT_STS

TSENSOR_TEMP_INT_STS 为 TSENSOR 中断控制寄存器。

Offset Address：0x0328＋0x1000×CH_NUM Total Reset Value：0x0000

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
  - RO
  - tsensor_overtemp_int_sts
  - TSENSOR 过温保护中断状态。
  - 0x0
* - [1]
  - RO
  - tsensor_out_thresh_int_sts
  - TSENSOR 温度超门限范围中断状态。
  - 0x0
* - [0]
  - RO
  - tsensor_done_int_sts
  - TSENSOR 温度采集完毕中断状态。
  - 0x0
```

#### TSENSOR_AUTO_REFRESH_PERIOD

TSENSOR_AUTO_REFRESH_PERIOD 为 TSENSOR 自动检测控制寄存器。

Offset Address：0x0330＋0x1000×CH_NUM Total Reset Value：0xFFFF

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [15:0]
  - RW
  - tsensor_auto_refresh_period
  - TSENSOR 自动检测周期,32k 时钟周期数。
  - 0xFFFF
```

#### TSENSOR_AUTO_REFRESH_CFG

TSENSOR_AUTO_REFRESH_CFG 为 TSENSOR 自动检测控制寄存器。

Offset Address：0x0334＋0x1000×CH_NUM Total Reset Value：0x0000

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
  - tsensor_auto_refresh_enable
  - 16 点平均单次上报模式下周期检测使能。0:定时周期检测关闭;1:定时周期检测打开。
  - 0x0
```

## I2S

### 概述

I2S 模块是 APB 总线上的从设备、I2S 总线上的主/从设备。

### 功能描述

支持 Master/Slave 模式；

支持 TRX 的左右声道各自独立 FIFO，FIFO 规格为 32X8；

支持 8kHz/16kHz/32kHz/44.1kHz/48kHz/96kHz/128kHz；

支持 16/24/32 位的传输工作模式；

支持 I2S 协议/PCM-TDM 协议（PCM-TDM 只支持 RX 方向的 16 位传输工作模式）。

## QSPI

### 概述

QSPI 是 Quad SPI 的简写，一共有 6 线组成

（SPI_CLK/SPI_CSN/SPI_D0/SPI_D1/SPI_D2/SPI_D3），常用来对接

FLASH/PSRAM 等器件。

### 功能描述

QSPI 具有以下功能特点：

- 仅支持 Master 模式。

- 支持 1 线/4 线模式。

1 线模式下，支持三种帧格式：

Motorola 帧格式。

TI（Texas Instruments）帧格式。

National Microwire 帧格式。

1 线模式下，支持串行帧长度可编程。

支持 DMA 搬移操作。

支持接口时钟频率可编程：

1 线模式下，最大支持 10M 的接口频率工作。

4 线模式下，最大支持 32M的接口频率工作。

## DMA

### 概述

直接存储器访问（DMA）方式，是一种完全由硬件执行 I/O 交换的工作方式。在这种方式中，直接存储器访问控制器（DMAC）直接在存储器和外设、外设和外设、存储器和存储器之间进行数据传输，减少处理器的干涉和开销。

DMA（Directory Memory Access）方式一般用于高速传输成组的数据。DMAC （Directory Memory Access Controller）在收到 DMA 传输请求后根据 CPU 对通道的配置启动总线主控制器，向存储器和外设发出地址和控制信号，对传输数据的个数计数，并且以中断方式向 CPU 报告传输操作的结束或错误。

### 功能描述

DMA 控制器有如下特点：

支持单 MASTER，支持 4 通道，每个通道可配置用于一种单向传输。

支持 UART0/UART1/UART2/SPI/QSPI/I2S 硬握手通道，可通过配置设为传输的源端请求或目的端请求。

支持四种方向的搬移场景：

MEMORY 到 MEMORY。

外设到外设。

外设到 MEMORY。

MEMORY 到外设。

DMA 通道优先级固定，优先级从高到低对应的通道号依次为 0～3。

DMAC 通道 0～通道 3 中各包含 1 个 16×32bit 的 FIFO。

支持总线位宽为 32bit 的 AHB 总线接口；支持一组 AHB SLAVE 接口和一组 AHB MASTER 接口。

外设可使用单次传输（single）和连续传输（burst）2 种 DMA 请求。

支持软件控制的 DMA 请求。

支持源地址和目的地址可分别配置为自动递增或不递增，递增步长取决于传输位宽。

支持分别配置源端和目的端的传输位宽：8/16/32bit。

支持链表 DMA 传输。

提供 1 个可屏蔽电平中断输出，中断可清除。

支持 DMA 错误和 DMA 传输完成中断屏蔽前后状态查询，及两者的组合中断状态查询。

### 工作方式

DMA 初始化配置步骤如下：

步骤 1 读 DMAC_EN_CHNS`en_chns`，获取空闲的通道编号 ch_num，以通道 0 为例。

步骤 2 写 DMAC_CONFIG`dmac_en`为 0x1，使能 DMAC。

步骤 3 写 DMAC_CHN_CONTROL_0`dmac_chn_en_0`为 0x0，关闭通道 0 使能。

步骤 4 如果需要通过软请求方式进行 DMA 搬数，则需要根据表 1 中的保留编号配置 DMAC_BURST_REQ`burst_req`、DMAC_SINGLE_REQ`single_req`。

### 说明

如果通过硬请求方式进行 DMA 搬数或传输方向为 MEMORY 到 MEMORY，则忽略此步骤。

表6-14 DMA 请求接口信号描述

| 外设编号 | 外设端口 | 功能描述 |
| --- | --- | --- |
| 0 | reserved | 保留。 |
| 1 | uart0_tx | UART0 的发送信号。 |
| 2 | uart0_rx | UART0 的接收信号。 |
| 3 | uart1_tx | UART1 的发送信号。 |
| 4 | uart1_rx | UART1 的接收信号。 |
| 5 | uart2_tx | UART2 的发送信号。 |
| 6 | uart2_rx | UART2 的接收信号。 |
| 7 | spi_tx | SPI 的发送信号。 |
| 8 | spi_rx | SPI 的接收信号。 |
| 9 | qspi_tx | QSPI 的发送信号。 |
| 10 | qspi_rx | QSPI 的接收信号。 |
| 11 | i2s_tx | I2S 的发送信号。 |
| 12 | i2s_rx | I2S 的接收信号。 |
| 13~15 | reserved | 保留。 |


步骤 5 配置通道 0 的源地址 DMAC_S_ADDR_0`dmac_s_addr_0`和目的地址 DMAC_D_ADDR_0`dmac_d_addr_0`。

步骤 6 根据具体需求配置 DMA 通道 0 控制寄存器 DMAC_CHN_CONTROL_0，例如传输位宽、传输长度、Burst 长度等。

步骤 7 如果需要进行链表传输，则配置链式地址 DMAC_LLI_0`dmac_lli_0`。

步骤 8 根据具体需求配置 DMA 通道 0 配置寄存器 DMAC_CHN_CONTROL_0：

写`dmac_flow_ctl_0`，配置流控和传输类型。

写`dmac_d_peripheral_0`，配置目的设备，配置值为表 1 中的外设编号。

写`dmac_s_peripheral_0`，配置源设备，配置值为表 1 中的外设编号。

写`dmac_int_tc_0`，配置完成中断屏蔽位。

写`dmac_int_en_0`，配置错误中断屏蔽位。

写`dmac_chn_en_0`为 0x1，启动通道 0。

步骤 9 若 DMAC_CHN_CONTROL_0`dmac_int_tc_0`未屏蔽，则当 DMA 通道 0 传输完成后上报完成中断，或轮询读取 DMAC_ORI_INT_ST`ori_int_trans_st`查询完成状态。

 

### 寄存器概览

AHB_DMA_RB 寄存器概览如表 6-18 所示。

表6-15 AHB_DMA_RB 寄存器概览（基址是 0x4A000000）

| 偏移地址 | 名称 | 描述 |
| --- | --- | --- |
| 0x0004 | DMAC_INT_ST | 中断状态寄存器。 |
| 0x0008 | DMAC_INT_CLR | 传输中断寄存器。 |
| 0x000C | DMAC_ORI_INT_ST | 原始中断状态寄存器。 |
| 0x0010 | DMAC_EN_CHNS | 通道使能查询寄存器。 |
| 0x0014 | DMAC_BURST_REQ | BURST 软件配置寄存器。 |
| 0x0018 | DMAC_SINGLE_REQ | SINGLE 软件配置寄存器。 |
| 0x001C | DMAC_CONFIG | 配置寄存器。 |
| 0x0020 | DMAC_SYNC | 同步寄存器。 |
| 0x0100 | DMAC_LLI_0 | 通道 0 链表寄存器。 |
| 0x0120 | DMAC_LLI_1 | 通道 1 链表寄存器。 |
| 0x0140 | DMAC_LLI_2 | 通道 2 链表寄存器。 |
| 0x0160 | DMAC_LLI_3 | 通道 3 链表寄存器。 |
| 0x0110 | DMAC_S_ADDR_0 | 通道 0 源地址寄存器。 |
| 0x0130 | DMAC_S_ADDR_1 | 通道 1 源地址寄存器。 |
| 0x0150 | DMAC_S_ADDR_2 | 通道 2 源地址寄存器。 |
| 0x0170 | DMAC_S_ADDR_3 | 通道 3 源地址寄存器。 |
| 0x0104 | DMAC_D_ADDR_0 | 通道 0 目的地址寄存器。 |
| 0x0124 | DMAC_D_ADDR_1 | 通道 1 目的地址寄存器。 |
| 0x0144 | DMAC_D_ADDR_2 | 通道 2 目的地址寄存器。 |
| 0x0164 | DMAC_D_ADDR_3 | 通道 3 目的地址寄存器。 |
| 0x0114 | DMAC_CHN_CONTR OL_0 | 通道 0 控制寄存器。 |
| 0x0134 | DMAC_CHN_CONTR OL_1 | 通道 1 控制寄存器。 |
| 0x0154 | DMAC_CHN_CONTR OL_2 | 通道 2 控制寄存器。 |
| 0x0174 | DMAC_CHN_CONTR OL_3 | 通道 3 控制寄存器。 |
| 0x0108 | DMAC_CHN_CONFIG_0 | 通道 0 配置寄存器。 |
| 0x0128 | DMAC_CHN_CONFIG_1 | 通道 1 配置寄存器。 |
| 0x0148 | DMAC_CHN_CONFIG_2 | 通道 2 配置寄存器。 |
| 0x0168 | DMAC_CHN_CONFIG_3 | 通道 3 配置寄存器。 |


### 寄存器描述

DMAC_INT_ST

DMAC_INT_ST 为中断状态寄存器。

### 说明

本 IP 仅支持 4 通道，i=0'3 有效，i=4'7 无效。

Offset Address：0x0004 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:24]
  - RO
  - reserved
  - 保留。
  - 0x00
* - [23:16]
  - RO
  - int_err_st
  - i=0~7int_err_st`i`=1'b0:通道i未产生错误中断(经过中断屏蔽);int_err_st`i`=1'b1:通道i产生错误中断(经过中断屏蔽)。
  - 0x00
* - [15:8]
  - RO
  - int_trans_st
  - i=0~7int_trans_st`i`=1'b0:通道i未产生传输中断(经过中断屏蔽);int_trans_st`i`=1'b1:通道i产生传输中断(经过中断屏蔽)。
  - 0x00
* - [7:0]
  - RO
  - int_st
  - i=0~7int_st`i`=1'b0:通道i未产生中断(经过中断屏蔽);int_st`i`=1'b1:通道i产生中断(经过中断屏蔽)。
  - 0x00
```

DMAC_INT_CLR

DMAC_INT_CLR 为传输中断寄存器。

### 说明

本 IP 仅支持 4 通道，i=0'3 有效，i=4'7 无效。

Offset Address：0x0008 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - [31:16]
  - RO
  - reserved
  - 保留。
  - 0x0000
* - [15:8]
  - RW
  - int_err_clr
  - i=0~7int_err_clr`i`=1'b0:不清除通道i的错误中断;int_err_clr`i`=1'b1:清除通道i的错误中断。
  - 0x00
* - [7:0]
  - RW
  - int_trans_clr
  - i=0~7int_trans_clr`i`=1'b0:不清除通道i的传输中断;int_trans_clr`i`=1'b1:清除通道i的传输中断。
  - 0x00
```

DMAC_ORI_INT_ST

DMAC_ORI_INT_ST 为原始中断状态寄存器。

### 说明

本 IP 仅支持 4 通道，i=0'3 有效，i=4'7 无效。

Offset Address：0x000C Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:16
  - RO
  - reserved
  - 保留。
  - 0x0000
* - 15:8
  - RO
  - ori_int_err_st
  - i=0~7ori_int_err_st`i`=1'b0:通道i未产生错误中断(未经中断屏蔽);ori_int_err_st`i`=1'b1:通道i产生错误中断(未经中断屏蔽)。
  - 0x00
* - 7:0
  - RO
  - ori_int_trans_st
  - i=0~7ori_int_trans_st`i`=1'b0:通道i未产生传输中断(未经中断屏蔽);ori_int_trans_st`i`=1'b1:通道i产生传输中断(未经中断屏蔽)。
  - 0x00
```

#### DMAC_EN_CHNS

DMAC_EN_CHNS 为通道使能查询寄存器。

### 说明

本 IP 仅支持 4 通道，i=0'3 有效，i=4'7 无效。

Offset Address：0x0010 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:8
  - RO
  - reserved
  - 保留。
  - 0x000000
* - 7:0
  - RO
  - en_chns
  - i=0~7en_chns`i`=1'b0:通道i未使能;en_chns`i`=1'b1:通道i使能。
  - 0x00
```

#### DMAC_BURST_REQ

DMAC_BURST_REQ 为 BURST 软件配置寄存器。

Offset Address：0x0014 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:16
  - RW
  - burst_req
  - i=0~15burst_req`i`=1'b0:无影响;burst_req`i`=1'b1:产生DMA burst传输请求,当传输结束时该寄存器中的相应位被清零。
  - 0x0000
* - 15:0
  - RW
  - last_burst_req
  - i=0~15last_burst_req`i`=1'b0:无影响;last_burst_req`i`=1'b1:产生DMA last burst传输请求,当传输结束时该寄存器中的相应位被清零。
  - 0x0000
```

#### DMAC_SINGLE_REQ

DMAC_SINGLE_REQ 为 SINGLE 软件配置寄存器。

Offset Address：0x0018 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:16
  - RW
  - single_req
  - i=0~15single_req`i`=1'b0:无影响single_req`i`=1'b1:产生DMA single传输请求,当传输结束时该寄存器中的相应位被清零
  - 0x0000
* - 15:0
  - RW
  - last_single_req
  - i=0~15last_single_req`i`=1'b0:无影响last_single_req`i`=1'b1:产生DMA last single传输请求,当传输结束时该寄存器中的相应位被清零
  - 0x0000
```

#### DMAC_CONFIG

DMAC_CONFIG 为配置寄存器。

### 说明

本 IP 仅支持单 master，master2 配置无效。

Offset Address：0x001C Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:3
  - RO
  - reserved
  - 保留。
  - 0x00000000
* - 2
  - RW
  - dmac_m2
  - Master 2 endianness 配置位。0: little endian 模式;1: big endian 模式。
  - 0x0
* - 1
  - RW
  - dmac_m1
  - Master 1 endianness 配置位。0: little endian 模式;1: big endian 模式。
  - 0x0
* - 0
  - RW
  - dmac_en
  - DMAC 使能。0: 禁止 DMAC;1: 使能 DMAC。
  - 0x0
```

#### DMAC_SYNC

DMAC_SYNC 为同步寄存器。

Offset Address：0x0020 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:16
  - RO
  - reserved
  - 保留。
  - 0x0000
* - 15:0
  - RW
  - damc_sync
  - 控制是否需要对请求线进行同步。0:使能对应外设的DMA请求信号同步逻辑;1:禁止对应外设的DMA请求信号同步逻辑。
  - 0x0000
```

#### DMAC_LLI_0

DMAC_LLI_0 为通道 0 链表寄存器。

### 说明

本 IP 仅支持单 master，master2 相关配置无效。

Offset Address：0x0100 Total Reset Value：0x00000000

表6-16 Table9 DMAC_LLI_0 Register Field Description

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:2
  - RW
  - dmac_lli_0
  - 链式地址[31:2]
  - 0x00000000
* - 1
  - RO
  - reserved
  - 保留。
  - 0x0
* - 0
  - RW
  - dmac_lm_0
  - 用于载入下一个链表结点的Master。0: Master1;1: Master2。
  - 0x0
```

#### DMAC_LLI_1

DMAC_LLI_为通道 1 链表寄存器。

### 说明

本 IP 仅支持单 master，master2 相关配置无效。

Offset Address：0x0120 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:2
  - RW
  - dmac_lli_1
  - 链式地址[31:2]
  - 0x00000000
* - 1
  - RO
  - reserved
  - 保留。
  - 0x0
* - 0
  - RW
  - dmac_lm_1
  - 用于载入下一个链表结点的 Master。0: Master1;1: Master2。
  - 0x0
```

#### DMAC_LLI_2

DMAC_LLI_2 为通道 2 链表寄存器。

### 说明

本 IP 仅支持单 master，master2 相关配置无效。

Offset Address：0x0140 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:2
  - RW
  - dmac_lli_2
  - 链式地址[31:2]
  - 0x00000000
* - 1
  - RO
  - reserved
  - 保留。
  - 0x0
* - 0
  - RW
  - dmac_lm_2
  - 用于载入下一个链表结点的 Master。0:Master1;1:Master2。
  - 0x0
```

#### DMAC_LLI_3

DMAC_LLI_3 为通道 3 链表寄存器。

### 说明

本 IP 仅支持单 master，master2 相关配置无效。

Offset Address：0x0160 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:2
  - RW
  - dmac_lli_3
  - 链式地址[31:2]
  - 0x00000000
* - 1
  - RO
  - reserved
  - 保留。
  - 0x0
* - 0
  - RW
  - dmac_lm_3
  - 用于载入下一个链表结点的 Master。0: Master1;1: Master2。
  - 0x0
```

#### DMAC_S_ADDR_0

DMAC_S_ADDR_0 为通道 0 源地址寄存器。

Offset Address：0x0110 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:0
  - RW
  - dmac_s_addr_0
  - DMAC 通道 0 源地址寄存器
  - 0x00000000
```

#### DMAC_S_ADDR_1

DMAC_S_ADDR_1 为通道 1 源地址寄存器。

Offset Address：0x0130 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:0
  - RW
  - dmac_s_addr_1
  - DMAC 通道 1 源地址寄存器
  - 0x00000000
```

#### DMAC_S_ADDR_2

DMAC_S_ADDR_2 为通道 2 源地址寄存器。

Offset Address：0x0150 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:0
  - RW
  - dmac_s_addr_2
  - DMAC 通道 2 源地址寄存器
  - 0x00000000
```

#### DMAC_S_ADDR_3

DMAC_S_ADDR_3 为通道 3 源地址寄存器。

Offset Address：0x0170 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:0
  - RW
  - dmac_s_addr_3
  - DMAC 通道 3 源地址寄存器
  - 0x00000000
```

#### DMAC_D_ADDR_0

DMAC_D_ADDR_0 为通道 0 目的地址寄存器。

Offset Address：0x0104 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:0
  - RW
  - dmac_d_addr_0
  - DMAC 通道 0 目的地址寄存器
  - 0x00000000
```

#### DMAC_D_ADDR_1

DMAC_D_ADDR_1 为通道 1 目的地址寄存器。

Offset Address：0x0124 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:0
  - RW
  - dmac_d_addr_1
  - DMAC 通道 1 目的地址寄存器
  - 0x00000000
```

#### DMAC_D_ADDR_2

DMAC_D_ADDR_2 为通道 2 目的地址寄存器。

Offset Address：0x0144 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:0
  - RW
  - dmac_d_addr_2
  - DMAC 通道 2 目的地址寄存器。
  - 0x00000000
```

#### DMAC_D_ADDR_3

DMAC_D_ADDR_3 为通道 3 目的地址寄存器。

Offset Address：0x0164 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:0
  - RW
  - dmac_d_addr_3
  - DMAC 通道 3 目的地址寄存器。
  - 0x00000000
```

#### DMAC_CHN_CONTROL_0

DMAC_CHN_CONTROL_0 为通道 0 控制寄存器。

### 说明

本 IP 仅支持单 master，master2 相关配置无效。

Offset Address：0x0114 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31
  - RW
  - dmac_trans_int_0
  - 传输完成中断使能位。该位用于决定当前链表结点是否触发传输完成中断。0:当前链表结点不触发传输完成中断;1:当前链表结点触发传输完成中断。
  - 0x0
* - 30:28
  - RW
  - dmac_prot_0
  - master 发出的访问保护HPROT[2:0]信号。
  - 0x0
* - 27
  - RW
  - dmac_d_inc_0
  - 目的地址递增。0:目的地址不递增;1:目的地址每传一个数就递增一次。目的设备为外设时目的地址不递增;目的设备为存储器时目的地址递增。
  - 0x0
* - 26
  - RW
  - dmac_s_inc_0
  - 源地址递增。0:源地址不递增;1:源地址每传一个数就递增一次。源设备为外设时源地址不递增;源设备为存储器时源地址递增。
  - 0x0
* - 25
  - RW
  - dmac_d_master_0
  - 设置访问目的设备的 master。0:使用 Master1 作为目的设备传输;1: 使用 Master2 作为目的设备传输。
  - 0x0
* - 24
  - RW
  - dmac_s_master_0
  - 设置访问源设备的 master。0: 使用 Master1 作为源设备传输;1: 使用 Master2 作为源设备传输。
  - 0x0
* - 23:21
  - RW
  - dmac_d_width_0
  - 目的设备传输位宽。000: Byte (8bit)001: Halfword (16bit)010: Word (32bit)
  - 0x0
* - 20:18
  - RW
  - dmac_s_width_0
  - 源设备传输位宽。000: Byte (8bit)001: Halfword (16bit)010: Word (32bit)
  - 0x0
* - 17:15
  - RW
  - dmac_d_bsize_0
  - 目的设备 burst 长度。000: 1001: 4010: 8011: 16100: 32101: 64110: 128111: 256
  - 0x0
* - 14:12
  - RW
  - dmac_s_bsize_0
  - 源设备 burst 长度。000: 1001: 4010: 8011: 16100: 32101: 64110: 128111: 256
  - 0x0
* - 11:0
  - RW
  - dmac_trans_size_0
  - 当 DMAC 是流控制器时,通过写该寄存器可设定 DMA 传输的长度。
  - 0x000
```

#### DMAC_CHN_CONTROL_1

DMAC_CHN_CONTROL_1 为通道 1 控制寄存器。

### 说明

本 IP 仅支持单 master，master2 相关配置无效。

Offset Address：0x0134 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31
  - RW
  - dmac_trans_int_1
  - 传输完成中断使能位。该位用于决定当前链表结点是否触发传输完成中断。0:当前链表结点不触发传输完成中断;1:当前链表结点触发传输完成中断。
  - 0x0
* - 30:28
  - RW
  - dmac_prot_1
  - master 发出的访问保护 HPROT[2:0]信号。
  - 0x0
* - 27
  - RW
  - dmac_d_inc_1
  - 目的地址递增。0:目的地址不递增;1:目的地址每传一个数就递增一次。目的设备为外设时目的地址不递增;目的设备为存储器时目的地址递增。
  - 0x0
* - 26
  - RW
  - dmac_s_inc_1
  - 源地址递增。0:源地址不递增;1:源地址每传一个数就递增一次。源设备为外设时源地址不递增;源设备为存储器时源地址递增。
  - 0x0
* - 25
  - RW
  - dmac_d_master_1
  - 设置访问目的设备的 master。0:使用 Master1 作为目的设备传输;1:使用 Master2 作为目的设备传输。
  - 0x0
* - 24
  - RW
  - dmac_s_master_1
  - 设置访问源设备的 master。0:使用 Master1 作为源设备传输;1:使用 Master2 作为源设备传输。
  - 0x0
* - 23:21
  - RW
  - dmac_d_width_1
  - 目的设备传输位宽。000:Byte (8bit)001:Halfword (16bit)010:Word (32bit)
  - 0x0
* - 20:18
  - RW
  - dmac_s_width_1
  - 源设备传输位宽。000:Byte (8bit)001:Halfword (16bit)010:Word (32bit)
  - 0x0
* - 17:15
  - RW
  - dmac_d_bsize_1
  - 目的设备 burst 长度。000:1001: 4010: 8011: 16100: 32101: 64110: 128111: 256
  - 0x0
* - 14:12
  - RW
  - dmac_s_bsize_1
  - 源设备 burst 长度。000: 1001: 4010: 8011: 16100: 32101: 64110: 128111: 256
  - 0x0
* - 11:0
  - RW
  - dmac_trans_size_1
  - 当 DMAC 是流控制器时,通过写该寄存器可设定 DMA 传输的长度。
  - 0x000
```

#### DMAC_CHN_CONTROL_2

DMAC_CHN_CONTROL_2 为通道 2 控制寄存器。

### 说明

本 IP 仅支持单 master，master2 相关配置无效。

Offset Address：0x0154 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31
  - RW
  - dmac_trans_int_2
  - 传输完成中断使能位。该位用于决定当前链表结点是否触发传输完成中断。0:当前链表结点不触发传输完成中断;1:当前链表结点触发传输完成中断。
  - 0x0
* - 30:28
  - RW
  - dmac_prot_2
  - master 发出的访问保护 HPROT[2:0]信号。
  - 0x0
* - 27
  - RW
  - dmac_d_inc_2
  - 目的地址递增。0:目的地址不递增;1:目的地址每传一个数就递增一次。目的设备为外设时目的地址不递增;目的设备为存储器时目的地址递增。
  - 0x0
* - 26
  - RW
  - dmac_s_inc_2
  - 源地址递增。0:源地址不递增;1:源地址每传一个数就递增一次。源设备为外设时源地址不递增;源设备为存储器时源地址递增。
  - 0x0
* - 25
  - RW
  - dmac_d_master_2
  - 设置访问目的设备的 master。0:使用 Master1 作为目的设备传输;1:使用 Master2 作为目的设备传输。
  - 0x0
* - 24
  - RW
  - dmac_s_master_2
  - 设置访问源设备的 master。0:使用 Master1 作为源设备传输;1:使用 Master2 作为源设备传输。
  - 0x0
* - 23:21
  - RW
  - dmac_d_width_2
  - 目的设备传输位宽。000: Byte (8bit)001: Halfword (16bit)010: Word (32bit)
  - 0x0
* - 20:18
  - RW
  - dmac_s_width_2
  - 源设备传输位宽。000: Byte (8bit)001: Halfword (16bit)010: Word (32bit)
  - 0x0
* - 17:15
  - RW
  - dmac_d_bsize_2
  - 目的设备 burst 长度。000: 1001: 4010: 8011: 16100: 32101: 64110: 128111: 256
  - 0x0
* - 14:12
  - RW
  - dmac_s_bsize_2
  - 源设备 burst 长度。000: 1001: 4010: 8011: 16100: 32101: 64110: 128111: 256
  - 0x0
* - 11:0
  - RW
  - dmac_trans_size_2
  - 当 DMAC 是流控制器时,通过写该寄存器可设定 DMA 传输的长度。
  - 0x000
```

#### DMAC_CHN_CONTROL_3

DMAC_CHN_CONTROL_3 为通道 3 控制寄存器。

### 说明

本 IP 仅支持单 master，master2 相关配置无效。

Offset Address：0x0174 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31
  - RW
  - dmac_trans_int_3
  - 传输完成中断使能位。该位用于决定当前链表结点是否触发传输完成中断。0:当前链表结点不触发传输完成中断;1:当前链表结点触发传输完成中断。
  - 0x0
* - 30:28
  - RW
  - dmac_prot_3
  - master 发出的访问保护HPROT[2:0]信号。
  - 0x0
* - 27
  - RW
  - dmac_d_inc_3
  - 目的地址递增。0:目的地址不递增;1:目的地址每传一个数就递增一次。目的设备为外设时目的地址不递增;目的设备为存储器时目的地址递增。
  - 0x0
* - 26
  - RW
  - dmac_s_inc_3
  - 源地址递增。0:源地址不递增;1:源地址每传一个数就递增一次。源设备为外设时源地址不递增;源设备为存储器时源地址递增。
  - 0x0
* - 25
  - RW
  - dmac_d_master_3
  - 设置访问目的设备的 master。0: 使用 Master1 作为目的设备传输;1: 使用 Master2 作为目的设备传输。
  - 0x0
* - 24
  - RW
  - dmac_s_master_3
  - 设置访问源设备的 master。0: 使用 Master1 作为源设备传输;1: 使用 Master2 作为源设备传输。
  - 0x0
* - 23:21
  - RW
  - dmac_d_width_3
  - 目的设备传输位宽。000: Byte (8bit)001: Halfword (16bit)010: Word (32bit)
  - 0x0
* - 20:18
  - RW
  - dmac_s_width_3
  - 源设备传输位宽。000: Byte (8bit)001: Halfword (16bit)010: Word (32bit)
  - 0x0
* - 17:15
  - RW
  - dmac_d_bsize_3
  - 目的设备 burst 长度。000: 1001: 4010: 8011: 16100: 32101: 64110: 128111: 256
  - 0x0
* - 14:12
  - RW
  - dmac_s_bsize_3
  - 源设备 burst 长度000: 1001: 4010: 8011: 16100: 32101: 64110: 128111: 256
  - 0x0
* - 11:0
  - RW
  - dmac_trans_size_3
  - 当 DMAC 是流控制器时,通过写该寄存器可设定 DMA 传输的长度。
  - 0x000
```

#### DMAC_CHN_CONFIG_0

DMAC_CHN_CONFIG_0 为通道 0 配置寄存器。

Offset Address：0x0108 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:17
  - RO
  - reserved
  - 保留。
  - 0x0000
* - 16
  - RW
  - dmac_halt_0
  - Halt 位。0: 允许 DMA 请求;1: 忽略后来的 DMA 请求,通道 FIFO 中的内容都被传完。
  - 0x0
* - 15
  - RO
  - dmac_active_0
  - Active 位。0: 通道 FIFO 中没有数据;1: 通道 FIFO 中有数据。
  - 0x0
* - 14
  - RW
  - dmac_lock_0
  - Lock 位。0:禁止总线上 lock 传输;1:使能总线上 lock 传输。
  - 0x0
* - 13
  - RW
  - dmac_int_tc_0
  - 传输完成中断屏蔽位。0:屏蔽本通道的传输完成中断;1:不屏蔽本通道的传输完成中断。
  - 0x0
* - 12
  - RW
  - dmac_int_en_0
  - 错误中断屏蔽位。0:屏蔽本通道的错误中断;1:不屏蔽本通道的错误中断。
  - 0x0
* - 11:9
  - RW
  - dmac_flow_ctl_0
  - 流控及传输类型字段。000:存储器至存储器DMAC;001:存储器至外设 DMAC;010:外设至存储器 DMAC;011:源设备至目的设备DMAC;100:源设备至目的设备目的设备;101:存储器至外设目的设备;110:外设至存储器源设备;111:源设备至目的设备源设备。
  - 0x0
* - 8:5
  - RW
  - dmac_d_peripheral_0
  - 目的设备。该字段用于选择一个外设请求信号作为本通道的DMA 目的设备的请求信号。如果 DMA 传输的目的设备是存储器则该字段被忽略。
  - 0x0
* - 4:1
  - RW
  - dmac_s_peripheral_0
  - 源设备。该字段用于选择一个外设请求信号作为本通道的DMA源设备的请求信号。如果DMA传输的源设备是存储器则该字段被忽略。
  - 0x0
* - 0
  - RW
  - dmac_chn_en_0
  - 通道使能位。0:关闭通道;1:启动通道。
  - 0x0
```

#### DMAC_CHN_CONFIG_1

DMAC_CHN_CONFIG_1 为通道 1 配置寄存器。

Offset Address：0x0128 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:17
  - RO
  - reserved
  - 保留。
  - 0x0000
* - 16
  - RW
  - dmac_halt_1
  - Halt 位。0: 允许 DMA 请求;1: 忽略后来的 DMA 请求,通道 FIFO 中的内容都被传完。
  - 0x0
* - 15
  - RO
  - dmac_active_1
  - Active 位。0: 通道 FIFO 中没有数据;1: 通道 FIFO 中有数据。
  - 0x0
* - 14
  - RW
  - dmac_lock_1
  - Lock 位。0: 禁止总线上 lock 传输;1: 使能总线上 lock 传输。
  - 0x0
* - 13
  - RW
  - dmac_int_tc_1
  - 传输完成中断屏蔽位。0: 屏蔽本通道的传输完成中断;1:不屏蔽本通道的传输完成中断。
  - 0x0
* - 12
  - RW
  - dmac_int_en_1
  - 错误中断屏蔽位。0:屏蔽本通道的错误中断;1:不屏蔽本通道的错误中断。
  - 0x0
* - 11:9
  - RW
  - dmac_flow_ctl_1
  - 流控及传输类型字段。000:存储器至存储器DMAC;001:存储器至外设DMAC;010:外设至存储器DMAC;011:源设备至目的设备DMAC;100:源设备至目的设备目的设备;101:存储器至外设目的设备;110:外设至存储器源设备;111:源设备至目的设备源设备。
  - 0x0
* - 8:5
  - RW
  - dmac_d_peripheral_1
  - 目的设备。该字段用于选择一个外设请求信号作为本通道的DMA目的设备的请求信号。如果DMA传输的目的设备是存储器则该字段被忽略。
  - 0x0
* - 4:1
  - RW
  - dmac_s_peripheral_1
  - 源设备。该字段用于选择一个外设请求信号作为本通道的 DMA 源设备的请求信号。如果 DMA 传输的源设备是存储器则该字段被忽略。
  - 0x0
* - 0
  - RW
  - dmac_chn_en_1
  - 通道使能位0:关闭通道;1:启动通道。
  - 0x0
```

#### DMAC_CHN_CONFIG_2

DMAC_CHN_CONFIG_2 为通道 2 配置寄存器。

Offset Address：0x0148 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:17
  - RO
  - reserved
  - 保留。
  - 0x0000
* - 16
  - RW
  - dmac_halt_2
  - Halt 位。0: 允许 DMA 请求;1: 忽略后来的 DMA 请求,通道 FIFO 中的内容都被传完。
  - 0x0
* - 15
  - RO
  - dmac_active_2
  - Active 位。0: 通道 FIFO 中没有数据;1: 通道 FIFO 中有数据。
  - 0x0
* - 14
  - RW
  - dmac_lock_2
  - Lock 位。0: 禁止总线上 lock 传输;1: 使能总线上 lock 传输。
  - 0x0
* - 13
  - RW
  - dmac_int_tc_2
  - 传输完成中断屏蔽位。0: 屏蔽本通道的传输完成中断;1:不屏蔽本通道的传输完成中断。
  - 0x0
* - 12
  - RW
  - dmac_int_en_2
  - 错误中断屏蔽位。0:屏蔽本通道的错误中断;1:不屏蔽本通道的错误中断。
  - 0x0
* - 11:9
  - RW
  - dmac_flow_ctl_2
  - 流控及传输类型字段000:存储器至存储器DMAC;001:存储器至外设DMAC;010:外设至存储器DMAC;011:源设备至目的设备DMAC;100:源设备至目的设备目的设备;101:存储器至外设目的设备;110:外设至存储器源设备;111:源设备至目的设备源设备。
  - 0x0
* - 8:5
  - RW
  - dmac_d_peripheral_2
  - 目的设备。该字段用于选择一个外设请求信号作为本通道的DMA目的设备的请求信号。如果DMA传输的目的设备是存储器则该字段被忽略。
  - 0x0
* - 4:1
  - RW
  - dmac_s_peripheral_2
  - 源设备。该字段用于选择一个外设请求信号作为本通道的 DMA 源设备的请求信号。如果 DMA 传输的源设备是存储器则该字段被忽略。
  - 0x0
* - 0
  - RW
  - dmac_chn_en_2
  - 通道使能位0:关闭通道;1:启动通道。
  - 0x0
```

#### DMAC_CHN_CONFIG_3

DMAC_CHN_CONFIG_3 为通道 3 配置寄存器。

Offset Address：0x0168 Total Reset Value：0x00000000

```{list-table}
:header-rows: 1

* - Bits
  - Access
  - Name
  - Description
  - Reset
* - 31:17
  - RO
  - reserved
  - 保留。
  - 0x0000
* - 16
  - RW
  - dmac_halt_3
  - Halt位。0:允许DMA请求;1:忽略后来的DMA请求,通道FIFO中的内容都被传完。
  - 0x0
* - 15
  - RO
  - dmac_active_3
  - Active位。0:通道FIFO中没有数据;1:通道FIFO中有数据。
  - 0x0
* - 14
  - RW
  - dmac_lock_3
  - Lock位。0:禁止总线上lock传输;1:使能总线上lock传输。
  - 0x0
* - 13
  - RW
  - dmac_int_tc_3
  - 传输完成中断屏蔽位。0:屏蔽本通道的传输完成中断;1:不屏蔽本通道的传输完成中断。
  - 0x0
* - 12
  - RW
  - dmac_int_en_3
  - 错误中断屏蔽位。0:屏蔽本通道的错误中断;1:不屏蔽本通道的错误中断。
  - 0x0
* - 11:9
  - RW
  - dmac_flow_ctl_3
  - 流控及传输类型字段000:存储器至存储器DMAC;001:存储器至外设DMAC;010:外设至存储器DMAC;011:源设备至目的设备DMAC;100:源设备至目的设备目的设备;101:存储器至外设目的设备;110:外设至存储器源设备;111:源设备至目的设备源设备。
  - 0x0
* - 8:5
  - RW
  - dmac_d_peripheral_3
  - 目的设备。该字段用于选择一个外设请求信号作为本通道的DMA目的设备的请求信号。如果DMA传输的目的设备是存储器则该字段被忽略。
  - 0x0
* - 4:1
  - RW
  - dmac_s_peripheral_3
  - 源设备。该字段用于选择一个外设请求信号作为本通道的DMA源设备的请求信号。如果DMA传输的源设备是存储器则该字段被忽略。
  - 0x0
* - 0
  - RW
  - dmac_chn_en_3
  - 通道使能位。0:关闭通道;1:启动通道。
  - 0x0
```

## ADC

### 概述

LSADC 为一款 SAR（Successive Approximations Register） ADC（逐次逼近型数模转换设备），实现将模拟信号转变成数字信号的功能。

```{list-table}
:header-rows: 1

* - 参数
  - 最小值
  - 典型值
  - 最大值
  - 单位
  - 描述
* -
  -
  -
  -
  -
  -
* - AVDD18
  - 1.71
  - 1.8
  - 1.89
  - V
  - 模拟 1.8V 电压
* - AVDD3P3
  - 2.97
  - 3.3
  - 3.63
  - V
  - 模拟 3.3V 电压
* - DVDD
  - 0.99
  - 1.1
  - 1.21
  - V
  - 数字电源电压
* -
  -
  -
  -
  -
  -
* - Full Scale Input
  - 0.3
  - -
  - 3.3
  - V
  - ADC 输入范围
* - DNL
  - -
  - ±1.5
  - ±3
  - LSB
  - 差分非线性
* - INL
  - -
  - ±2
  - ±4
  - LSB
  - 积分非线性
* - Resolution
  - -
  - 12
  - -
  - bit
  - 精度
* - -
  - 1.3
  - 1.5
  - mA
  - 工作时功耗
  -
* - -
  - 32
  - 500
  - μA
  - 关机时功耗(DVDD,AVDD33及 AVDD18 均在位)
  -
* - -
  - 3.6
  - 4.32
  - μA
  - 关机时功耗(DVDD 掉电,AVDD33 及 AVDD18 在位)
  -
* -
  -
  -
  -
  -
  -
* - f_{CLK}
  - -
  - -
  - 32
  - MHz
  - 输入时钟频率
* - Duty-Cycle
  - 45
  - 50
  - 55
  - %
  - 占空比
* - f_S
  - -
  - -
  - 1000
  - Ksps
  - 采样率
```

### 功能描述

LSADC 模块具有以下功能特点：

- 输入时钟 32MHz，12bit 分辨率，单通道采样率最大为 1Msps。

- 共 6 个通道，支持软件配置 0～5 任意通道使能，逻辑按通道编号先低后高发起切换，完成单通道采样并完成平均值滤波后自动进行通道切换。。

- 支持 128×17bit FIFO 用于数据缓存，数据存储格式：高 3bit 为通道编号，低 14bit 为有效数据。

- 支持对 ADC 采样数据进行平均滤波处理，平均次数支持 1（不进行平均）、2、 4、8；多通道时，每个通道接收 N 个数据（平均滤波个数）再切换通道。

- 支持 FIFO 水线中断、满中断上报,ADC 忙状态、控制器 FIFO 空满状态查询。
