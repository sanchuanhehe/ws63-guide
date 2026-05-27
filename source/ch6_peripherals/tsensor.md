(ch6-tsensor)=

# Tsensor

## 概述

Tsensor 是模拟温度检测 IP，检测芯片的节温并以二进制形式输出温度信息。检测温度范围：$-40^{\circ}C \sim +125^{\circ}C$，10bit SARADC 量化温度，分辨率 0.208℃/{term}`LSB`，IP 校准后温度精度在 $\pm 2^{\circ}C$ 以内。

## 功能描述

Tsensor 具有以下功能特点：

- 支持 Tsensor 三种测温模式：单次 16 点平均测温模式、周期 16 点平均测温模式、单点测温模式。
- 支持 Tsensor 测温完成中断上报。
- 支持 Tsensor 测温过温（overtemp）中断上报。
- 支持高温低温门限的使用。
- 支持软件分别可配高温门限和低温门限。
- 支持周期采样温度上报。
- 支持软件可配周期采样间隔。
- 支持 Tsensor 测温门限中断上报。

## 工作方式

Tsensor 模块的工作模式分为以下 3 种：

- 正常检测温度模式
- 高低温门限中断模式
- 过温保护中断模式

```{note}
以上 3 种模式均在检测温度值基础上进行，检测温度的模式有多种，此处检测温度的模式均为周期采样配合 16 次单点平均计算。
```

## 正常检测温度模式

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

## 高低温门限中断模式

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



## 过温保护中断模式

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



## 寄存器概览

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


## 寄存器描述

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

### TSENSOR_REG0

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

### TSENSOR_REG1

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

### TSENSOR_REG2

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

### TSENSOR_REG3

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

### TSENSOR_START

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

### TSENSOR_CTRL

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

### TSENSOR_STS

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

### TSENSOR_CTRL1

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

### TSENSOR_TEMP_HIGH_LIMIT

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

### TSENSOR_TEMP_LOW_LIMIT

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

### TSENSOR_OVER_TEMP

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

### TSENSOR_TEMP_INT_EN

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

### TSENSOR_TEMP_INT_CLR

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

### TSENSOR_TEMP_INT_STS

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

### TSENSOR_AUTO_REFRESH_PERIOD

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

### TSENSOR_AUTO_REFRESH_CFG

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

