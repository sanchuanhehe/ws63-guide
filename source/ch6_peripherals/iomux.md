(ch6-iomux)=

# IO MUX

## 概述

芯片数字管脚数量有限，通过 IO 复用的方式丰富管脚功能。

## 软用管脚描述

```{important}
ADC 管脚：LSADC 通道与 GPIO 功能只支持其中 1 种功能，ADC 通道管脚与 GPIO 管脚的对应关系如表 6-2 所示。
```


表6-1 {term}`ADC` 通道管脚与复用管脚对应关系

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
| 6 | GPIO_02 | GPIO_02_SEL | GPIO_02 | PWM2 | DIAG[2] | SPI1_IO3 | WIFI_TSF_SYNC | WL_GLP_SYNC_PULSE | {term}`BLE`&SLE_GLP_SYNC_PULSE | - |
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


{term}`GPIO` 的软件复用管脚说明如表 6-3 所示。

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

## 寄存器概览

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

## 寄存器描述

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

### PAD_SFC_CLK_CTRL

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

### PAD_SFC_CSN_CTRL

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

