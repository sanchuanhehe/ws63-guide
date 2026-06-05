(ch8-internals)=

# 底层实现补充（基于厂商 SDK 与仿真器实证）

```{note}
本章不属于原厂用户指南的公开内容，而是 **对芯片底层编程模型的实证补充**：信息来源为厂商
C SDK（`fbb_ws63`，被视为本未公开芯片的事实标准）、对其逐寄存器复核的独立 Rust HAL
（`ws63-hal`），以及一个开源 QEMU 机器模型（`ws63-qemu`，含自定义 ISA 与中断模型）。
三方一致的结论按「已核实」给出；仅由 QEMU 建模或由代码算术推得的，按 **[推断/QEMU 建模]** 标注。

它回答原厂手册留白的关键问题：**中断控制器到底怎么编程、CPU 上跑的到底是什么指令集、
eFuse/LSADC/SPI/DMA 等外设的寄存器位域与时序、时钟门控位、启动与镜像格式、Wi-Fi/BLE 子系统
的内存与掩膜 ROM 布局。** 第 {ref}`2 章 <ch2-system>` 给出官方层面的中断号表、地址映射与
复位源；本章给出与之配套的可编程细节。
```

## 处理器自定义本地中断控制器（LOCI\*）

第 {ref}`2 章 <ch2-system>` 表 2-5 列出了中断号（nmi、26～72），并说明「CPU 内部集成中断控制器、
3bit 优先级、7 级」。但官方手册未给出**如何用寄存器编程**这个控制器。实证结论如下。

WS63 应用核是一颗 HiSilicon 自研 riscv31 hart，**没有 PLIC**。中断分两层：

- **IRQ 26～31**：标准机器局部中断，由标准 `mie`/`mip` 的第 *n* 位门控。
- **IRQ ≥ 32**：HiSilicon 自定义局部中断，由下表的自定义 CSR（`LOCIEN*`/`LOCIPD*`/`LOCIPRI*`/`PRITHD`/`LOCIPCLR`）门控。

### 自定义 CSR 映射

表8-1 自定义中断控制器 CSR

```{list-table}
:header-rows: 1

* - CSR
  - 地址
  - 访问
  - 位宽用法
  - 功能
* - `LOCIPRI0`～`LOCIPRI15`
  - 0xBC0～0xBCF
  - RW
  - 32 位 = 8×4bit 字段
  - 每 IRQ 4bit 优先级，每寄存器 8 个 IRQ，优先级基号从 IRQ 26 起
* - `LOCIEN0`～`LOCIEN2`
  - 0xBE0～0xBE2
  - RW（用 `csrs`/`csrc` 置/清）
  - 每寄存器 32 个 IRQ
  - 使能掩码，基号从 IRQ 32 起
* - `LOCIPD0`～`LOCIPD2`
  - 0xBE8～0xBEA
  - RO
  - 每寄存器 32 个 IRQ
  - 挂起（pending）状态，基号从 IRQ 32 起
* - `LOCIPCLR`
  - 0xBF0
  - WO
  - 12bit IRQ 号
  - 写入 IRQ 号 → 清除该 IRQ 的挂起位
* - `PRITHD`
  - 0xBFE
  - RW
  - 3bit（0..7）
  - 全局优先级阈值
* - `CXCPTSC`（ccause）
  - 0xFC2
  - RO
  - —
  - 自定义扩展异常原因，保存在陷入帧
```

```{note}
LiteOS 头另声明了 `LOCIEN3`(0xBE3) 与 `LOCIPD3`～`LOCIPD6`(0xBEB～0xBEE)，对应 IRQ 96～191，
**WS63 上未使用**（实际只接 IRQ 32～91，共 60 个自定义局部中断；见表 2-5）。
```

同族还有缓存/MPU 自定义 CSR（非中断控制器，但同属厂商扩展）：`ICCTL 0x7C0`、`DCCTL 0x7C1`、
`ICMAINT 0x7C2`、`DCMAINT 0x7C3`、`ICINVA 0x7C4`、`DCINCVA 0x7C5`、`MEMATTRL 0x7D8`、
`MEMATTRH 0x7D9`。启动时通过 `csrwi 0x7C0/0x7C1, 0b11` 使能 I/D-Cache。

### IRQ 号 →（寄存器, 位）映射

模型常量（三方一致）：`SYS_VECTOR_CNT=26`、`MIE_IRQ_CNT=6`、`LOCAL_IRQ_CNT=32`、
`LOCIEN_IRQ_NUM=32`、`LOCIPRI_IRQ_NUM=8`、`LOCIPRI_IRQ_BITS=4`、`LOCIPRI 默认值=0x11111111`。

表8-2 IRQ 号到寄存器位的换算

```{list-table}
:header-rows: 1

* - 用途
  - 基号
  - 公式
* - 使能 `LOCIEN` / 挂起 `LOCIPD`
  - 32
  - `reg = (irq−32)/32`，`bit = (irq−32)%32`
* - 优先级 `LOCIPRI`
  - 26
  - `reg = (irq−26)/8`，`field = (irq−26)%8`，`shift = field×4`
* - 优先级字段宽度
  - —
  - 每 IRQ 4bit，有效取值 1..7
```

```{important}
注意**两个不同基号**：使能/挂起从 IRQ 32 计数（26～31 由 `mie` 覆盖），但优先级从 IRQ 26 计数
（26～31 也各有一个 `LOCIPRI` 半字节，IRQ 26 → `LOCIPRI0` 字段 0）。
```

### 挂起 / 清除 / 阈值语义

- **挂起**锁存在 `LOCIPD`（只读）。IRQ ≥ 32 读 `LOCIPD0-2`；IRQ 26～31 读标准 `mip` 第 *n* 位。
- **清除**：向 `LOCIPCLR (0xBF0)` 写入 IRQ 号，前后用 `fence`/`dsb` 围栏。由软件确认（SDK 的分组分发器清源，而非设备自清）。
- **投递规则**：当且仅当 **已使能 且 优先级严格大于 `PRITHD`** 时投递。复位默认优先级=1、阈值=0，
  故所有已使能（优先级≥1）的 IRQ 都被准入。
- **仲裁**：优先级高者胜；同优先级时 IRQ 号小者胜。
- **初始化**：`int_setup()` 先置 `mstatus.MIE`，再把 `LOCIPRI0-15` 全写 `0x11111111`（每个 IRQ 优先级=1），
  使没有任何 IRQ 落在优先级 0（即阈值之下）。

```{note}
两处 SDK 实现缺陷（独立 Rust HAL 已修正）：(1) SDK 的 `int_set_priority` 用裸 `csrs`（只能 OR 置位），
无法**降低**某 IRQ 的优先级字段；正确做法是「先清字段再写」的读改写。(2) SDK 的 `int_get_priority`
用 `0x3`（2bit）掩码读取，而字段是 4bit、取值 1～7，属潜在越界 bug，应使用 `0xF`。
```

### 陷入与向量化

- **mcause 编码**：被取的局部中断令 `mcause = irq`（IRQ 号即原因码），通过 `read_csr(mcause) & 0xFFF` 取回。
- **向量化 mtvec**：`mtvec` 工作在向量模式（`mtvec[1:0]=01`），向量基址 64 字节对齐。异步中断目标
  PC = `(mtvec & ~3) + 4×cause`——即每个 cause 占一个跳转槽。
- **运行时向量表**（`ws63-rt` 的 `trap_vector`）：槽 0 = 全异常入口；槽 12 = NMI；槽 26～31 = 六个专用
  `mie` 中断处理；槽 32～91 = 60 个 `local_interrupt_handler`。局部处理器保存 32 个寄存器、切到 IRQ 栈、
  调用弱符号 `local_isr_dispatch`、恢复后 `mret`。
- **异常分发**：另有 `.rodata` 中按 `mcause` 索引的 `excp_vect_table`（0～15：misaligned/fault/illegal/
  breakpoint/ecall/page-fault），M 态 ecall 令 `mepc += 4`。

## 自定义指令集扩展 "xlinx"

第 {ref}`2 章 <ch2-system>` 给出 ISA = `RV32IMFC_Zicsr`。但真实硅片与厂商工具链在此之上叠加了
HiSilicon 私有的 **"xlinx" 指令扩展**：厂商 `gcc` 默认以
`-march=rv32imfcxlinxma_xlinxmb_xlinxmc` 编译，整套 `fbb_ws63` 固件都用到这些指令——所以官方那行
ISA 描述对真实硅片是**不完整**的。三个子扩展：`xlinxma`/`xlinxmb`/`xlinxmc`。

```{note}
xlinx 指令编码为逆向所得的事实（厂商汇编器往返 + 逐字段差分扫描），语义经厂商 `gcc -S` 代码生成
与 13 项单元自检确认；本节标注 **[QEMU 建模]** 的部分指 QEMU 的实现细节。
```

**编码空间**：占用 RV32 保留 / RV64 专用主操作码 `0x1b`、`0x3b`；自定义操作码 `0x0b`、`0x5b`、`0x7b`；
一种 48 位形式（`bits[5:0]==0x1f` 标记）；以及复用的压缩槽（quadrant-0 funct3=100，及空置的
C.FLD/C.FSD 双精度浮点槽 funct3=001/101）。在真正的 RV32 核上，标准译码器总会落空到这些扩展。

表8-3 xlinx 指令一览

```{list-table}
:header-rows: 1

* - 助记符
  - 形式 / 操作码
  - 语义
* - `{add,sub,or,xor,and}shf rd,rs1,rs2,mode,shamt`
  - 32 位，op `0x1b`
  - `rd = rs1 OP (rs2<<移位)`；f3 0..4=add/sub/or/xor/and；bits[31:30]=sll/srl/sra/ror；shamt=bits[29:25]
* - `muliadd rd,rs1,rs2,imm6`
  - 32 位，op `0x5b`，bits[13:12]=01
  - `rd = rs1 + rs2*imm6`
* - `{beq,bne,blt,bge,bltu,bgeu}i rs1,imm8,off`
  - 32 位，op `0x3b`
  - rs1 与有符号 imm8 比较；10bit 有符号分支偏移（±1KB）
* - `jal16 / j16 target`
  - 32 位，op `0x7b`
  - `pc += off`；bit7=0→`ra=pc+4`(jal16)，=1→x0(j16)；25bit 有符号偏移（±16 MiB）
* - `ldmia/stmia {ra,s0-s11},(base)`
  - 32 位，op `0x0b`
  - 多寄存器加载/存储，升序，base 不回写；bit12=ld/st
* - `l.li rd, imm32`
  - **48 位**，半字 0 `&0x3f==0x1f`
  - `rd = imm32`（后随 4 字节小端立即数）
* - `push/pop/popret {ra,s0-sN},spimm`
  - 16 位，funct3=100 Q0
  - Zcmp 风格多寄存器保存/恢复（popret 末尾 ret）
* - `uxtb/uxth rd'`
  - 16 位
  - rd'（x8..x15）原地零扩展 8/16 位
* - 压缩 `lbu/lhu rd',imm(rs1')`
  - 16 位 funct3=001（复用 C.FLD 槽）
  - 无符号字节/半字加载
* - 压缩 `sb/sh rs2',imm(rs1')`
  - 16 位 funct3=101（复用 C.FSD 槽）
  - 字节/半字存储
```

```{important}
**[QEMU 建模]** 由于 xlinx 复用了 quadrant-0 funct3=100 与双精度浮点压缩槽，标准的
Zcb/Zcmp/Zcmt 压缩扩展会与之**冲突**，必须关闭，否则误译码；Zcf（单精度浮点压缩）保留。
QEMU 把 `MAX_INSN_LEN` 由 4 提到 6，`insn_len()` 在首半字 `&0x3f==0x1f` 时返回 6，并在标准译码落空后
依次尝试 `decode_xlinx16/32/48`。13/13 指令自检通过，真实厂商固件（flashboot、ws63-liteos-app）
可在该模型上启动。
```

## eFuse 控制器（v151）

基址见第 2 章地址映射（`EFUSE_CTL` = `0x4400_8000`～`0x4400_BFFF`）。控制块与数据窗如下。

表8-4 eFuse 地址与窗口

```{list-table}
:header-rows: 1

* - 项
  - 值
* - eFuse0 基址
  - 0x4400_8000
* - 控制块基址（寄存器组）
  - 基址 + 0x30 = 0x4400_8030
* - boot-done 状态
  - 基址 + 0x2C = 0x4400_802C
* - 读/写数据窗
  - 基址 + 0x800 = 0x4400_8800
* - 单区容量
  - 2048 bit = 256 字节
```

**数据窗（基址+0x800）**：128 个 32 位字，每字打包 2 个 eFuse 字节。字地址 = `0x4400_8800 + (byte_addr/2)*4`；
偶字节 → 低字节 `[7:0]`，奇字节 → 高字节 `[15:8]`。整窗跨 `0x4400_8800`～`0x4400_89FC`。

表8-5 eFuse 控制寄存器（相对控制块基址 0x4400_8030）

```{list-table}
:header-rows: 1

* - 寄存器
  - 绝对地址
  - 关键字段
  - 用途
* - `EFUSE_STS`
  - 0x4400_802C
  - `man_sts[1:0]`、`boot0/1/2_done[2:4]`
  - 状态/boot-done（RO）
* - `EFUSE_CTL_DATA`
  - 0x4400_8030
  - `efuse_wr_rd[15:0]`
  - 模式 arm：读=0x5A5A，写=0xA5A5
* - `EFUSE_CLK_PERIOD`
  - 0x4400_8034
  - `clock_period[7:0]`
  - 时钟周期（24MHz→0x29，40MHz→0x19）
* - `EFUSE_AVDD_CTL`
  - 0x4400_803C
  - `efuse_avdd_sw[0]`
  - 编程电压开关
```

**读时序**：① 越界检查（`addr<256`）；② 算窗字指针；③ 写 `0x5A5A` arm 读；④ 读锁存的 32 位字；
⑤ 取字节（奇 `>>8`、偶 `&0xFF`）。读无需延时/轮询。

**写（烧写）时序**：① 越界检查；② 写 `0xA5A5` arm 写；③ `efuse_avdd_sw=1` 升压；
④ 延时 **100 µs**；⑤ 把打包字节写入窗字；⑥ `efuse_avdd_sw=0` 降压；⑦ 再延时 **100 µs**。
eFuse 位只能 0→1，不可逆。

## LSADC 寄存器映射（v154）

LSADC 基址 `0x4400_C000`（见第 2 章），中断 `LSADC_INTR` = IRQ 72，6 个通道（CH0～CH5）。
寄存器组 `adc_regs_t` 连续排布（命名跳过 CTRL_5/CTRL_10，但地址不留空）。

表8-6 LSADC 寄存器映射（偏移相对基址）

```{list-table}
:header-rows: 1

* - 寄存器
  - 偏移
  - 关键字段
* - `LSADC_CTRL_0`
  - 0x00
  - `channel[5:0]`、`equ_model_sel[7:6]`、`sample_cnt[12:8]`、`satrt_cnt[20:13]`、`cast_cnt[27:21]`
* - `LSADC_CTRL_1`
  - 0x04
  - `rxintsize[2:0]`、`rne[3]`、`rff[4]`、`bsy[5]`（FIFO 状态 + 水线）
* - `LSADC_CTRL_2`
  - 0x08
  - 中断屏蔽/状态：`rorim[0]`、`rxim[1]`、`rormis[2]`、`rxmis[3]`、`rorris[4]`、`rxris[5]`
* - `LSADC_CTRL_8`
  - 0x1C
  - `lsadc_start[0]`、`lsadc_stop[1]`（扫描启停）
* - `LSADC_CTRL_9`
  - 0x20
  - FIFO 读：`data[13:0]`、`channel[16:14]`
* - `LSADC_CTRL_11`
  - 0x24
  - `da_lsadc_en[15:0]`、`da_lsadc_rstn[16]`（模拟使能 + 复位）
* - `CFG_DATA_SEL`
  - 0xDC
  - `data_sel`（1=处理后，0=原始）
* - `CFG_OFFSET`
  - 0xE0
  - `offset`（16bit 偏移校正）
* - `CFG_GAIN`
  - 0xE4
  - `gain`（16bit 增益校正）
* - `CFG_CIC_FILTER_EN` / `CFG_CIC_OSR`
  - 0xE8 / 0xEC
  - CIC 滤波器使能 / 过采样率
```

（CTRL_3/4/6/7/12 为模拟相关保留字段；偏移 0x2C～0xD8 为保留间隙。）

**扫描模式默认值**（`hal_adc_auto_scan_mode_set`）：`equ_model_sel=3`（8× 平均）、`sample_cnt=0x8`、
`satrt_cnt=0x18`、`cast_cnt=0x0`；按通道在 `LSADC_CTRL_0.channel` 置位使能。
**FIFO 读格式**：`data = raw & 0x3FFF`（14bit 码）、`channel = (raw>>14) & 0x07`。
**使能/复位**：`da_lsadc_rstn=1` 释放模拟复位（低有效），`rne` 位指示数据就绪。

## SPI / I2C 控制器寄存器

### SPI（Synopsys DesignWare SSI v151）

经 `spi_id` 寄存器确认是 DesignWare SSI 衍生。基址：SPI0 = `0x4402_0000`，SPI1（QSPI0）= `0x4402_1000`。

表8-7 SPI 关键寄存器（偏移相对实例基址）

```{list-table}
:header-rows: 1

* - 寄存器
  - 偏移
  - 功能
* - `SPI_ER`
  - 0x00
  - 使能（`start_en` bit0）
* - `SPI_CTRA`
  - 0x04
  - 控制 0：模式/帧/传输方向（trsm）
* - `SPI_CTRB`
  - 0x08
  - 数据帧数 `nrdf[15:0]`
* - `SPI_BRS`
  - 0x14
  - 时钟分频 `frdv[15:0]`（= SCKDV）
* - `SPI_DRNM`
  - 0x2C
  - TX/RX FIFO 数据寄存器
* - `SPI_SLENR`
  - 0xC8
  - 从选使能 `ssef[15:0]`
* - `SPI_WSR`
  - 0xE4
  - 传输/FIFO 状态
```

**CTRA 关键位**：`scph`(bit3 时钟相位)、`scpol`(bit4 时钟极性)、**`trsm`（传输模式，2bit）**。

```{important}
`trsm` 语义（关键，易错）：**`0b00` = 收发全双工（TX&RX）**；`0b01` = 仅发；`0b10` = 仅收；
**`0b11` = EEPROM Read（不是 TX+RX）**。全双工应保持 `trsm=0`。其数值语义已确证；
位偏移 18:19 取自 HAL 注释，随 SoC 的 `SPI_MAX_XFER_SIZE` 编译宏而定 **[推断]**。
```

**SCKDV 分频**：`Fsclk_out = Fssi_clk / SCKDV`，SCKDV 取偶数，范围 2..65534。`Fssi_clk` 为 **PLL 衍生的 160 MHz**
（ch2 表 2-3；**非** 240 MHz CPU 时钟）。注：厂商实为两级分频——480 MHz PLL 经 CLDO_CRG 分频得 SSI_CLK，再经 SCKDV 得 SCK。
**SPI_WSR 状态位**（按 SVD 显式 bitRange，PAC/HAL 即用此布局）：`busy`(bit0 忙)、`txfnf`(bit1 TX 不满)、
`txfe`(bit2 TX 空)、`rxfne`(bit3 RX 非空)、`rxfo`/`txfo`(bit4/5 溢出)。

### I2C（hal_i2c_v150）

基址：I2C0 = `0x4401_8000`，I2C1 = `0x4401_8100`。

表8-8 I2C 寄存器映射

```{list-table}
:header-rows: 1

* - 寄存器
  - 偏移
  - 寄存器
  - 偏移
* - `I2C_CTRL`
  - 0x00
  - `I2C_RXR`
  - 0x1C
* - `I2C_COM`
  - 0x04
  - `I2C_FIFOSTATUS`
  - 0x20
* - `I2C_ICR`
  - 0x08
  - `I2C_TXCOUNT`
  - 0x24
* - `I2C_SR`
  - 0x0C
  - `I2C_RXCOUNT`
  - 0x28
* - `I2C_SCL_H` / `I2C_SCL_L`
  - 0x10 / 0x14
  - `I2C_RXTIDE` / `I2C_TXTIDE`
  - 0x2C / 0x30
* - `I2C_TXR`
  - 0x18
  - `I2C_FTRPER`
  - 0x34
```

**I2C_SR 状态位**：`int_done`(0)、`int_arb_loss`(1)、`int_ack_err`(2 NACK)、`int_rx`(3)、`int_tx`(4)、
`int_stop`(5)、`int_start`(6)、`bus_busy`(7)、`int_rxtide`(8)、`int_txtide`(9)、`int_txfifo_over`(10)。
**I2C_COM 命令位**：`op_stop`(0)、`op_we`(1 写)、`op_rd`(2 读)、`op_start`(3)、`op_ack`(4，0=ACK/1=NACK)；
[3:0] 在操作后自动清。**时钟**：`scl_h`/`scl_l` 写入值 ×2 = SCL 高/低电平计数；分频基准为 **24 MHz TCXO 晶体**
——与 UART/SPI 不同，`clock_init` 不把 I2C 切到 PLL，而是 `i2c_port_set_clock_value(REQ_24M)` 留在晶体上
（ch2 表 2-3 的「I2C 80 MHz」是总线能力标称值，非 SDK 实际用于 SCL 分频的时钟）。

```{note}
**超时模型**：C SDK 的 `hal_i2c_v150_wait` 每次轮询 `osal_udelay(1)` 并 `time_out++`，
`time_out ≥ timeout_us`（ws63 配置 `CONFIG_I2C_WAIT_CONDITION_TIMEOUT = 3000`，即 3 ms）时返回
`ERRCODE_I2C_TIMEOUT`；超时后若 `int_ack_err` 置位则返回 `ERRCODE_I2C_ACK_ERR`。
```

## DMA 控制器与外设握手 ID

两个 DMA 控制器共享寄存器块结构，每个 4 通道。

表8-9 DMA 控制器

```{list-table}
:header-rows: 1

* - 控制器
  - 基址
  - 通道（物理 / 逻辑）
* - `Dma0`（M_DMA）
  - 0x4A00_0000
  - 0-3 / 0-3
* - `Sdma0`（S_DMA，安全）
  - 0x520A_0000
  - 0-3 / 8-11
```

外设触发 DMA 时需配置握手请求 ID（`hal_dma_handshaking_source_t` 枚举序号）。

表8-10 DMA 外设握手 ID（节选）

```{list-table}
:header-rows: 1

* - ID
  - 名称
  - 外设
* - 0
  - `TIE0`
  - 内存↔内存（tie-off）
* - 1 / 2
  - `UART_L_TX/RX`
  - UART0 发 / 收
* - 3 / 4
  - `UART_H0_TX/RX`
  - UART1 发 / 收
* - 5 / 6
  - `UART_H1_TX/RX`
  - UART2 发 / 收
* - 7 / 8
  - `SPI_MS0_TX/RX`
  - SPI0 发 / 收
* - 9 / 10
  - `QSPI0_2CS_TX/RX`
  - QSPI0 发 / 收
* - 11 / 12
  - `I2S_TX/RX`
  - I2S 发 / 收
* - 13 / 14
  - `SPI_MS1_TX/RX`
  - SPI1 发 / 收
* - 29+
  - `I2C0/1_TX/RX`、`IR_TX/RX` 等
  - I2C/IR（属 SDMA 组，ID ≥ 29）
```

```{note}
通道配置里的 `src/dst_peripheral` 字段为 4bit，故只有 ID ≤ 15 能直接编码；I2C/IR 等 ID ≥ 29 的握手
归 SDMA 组。UART 总线命名映射：UART0=UART_L、UART1=UART_H0、UART2=UART_H1。
```

## 时钟树（FNPLL 2880 MHz + CLDO_CRG，实证重建）

第 2 章表 2-3 给出各模块的标称时钟频率，本节据厂商 SDK 重建**完整的产生路径**：单一锁相环
（FNPLL）+ CLDO_CRG 的源选择（CLK_SEL）/ 分频（DIV_CTL）/ 门控（CKEN）。

**关键事实：全片只有一个 FNPLL，VCO 固定 2880 MHz。** `CMU_FBDIV` 按晶体取值——24 MHz 晶体写
`0x78`(=120)、40 MHz 晶体写 `0x48`(=72)——两者都得 `晶体 × FBDIV = 2880 MHz`（`CMU_FRAC=0`，整数模式）。
所有「PLL」外设时钟都是 2880 MHz 的**整数分频**，这把表 2-3 里看似零散的频率统一了起来：

| 分频 | 频率 | 去向 |
| --- | --- | --- |
| ÷12 | **240 MHz** | CPU / CPU 总线 |
| ÷18 | **160 MHz** | UART、SPI（标称） |
| ÷24 | **120 MHz** | GPIO、WiFi MAC |
| ÷9 | **320 MHz** | WiFi PHY |
| ÷6 | **480 MHz** | SPI/QSPI/I2S 根（再经 DIV_CTL 二级分频） |

```{mermaid}
graph LR
    XTAL["TCXO 晶体<br/>24 / 40 MHz<br/>HW_CTL bit0"]
    OSC32["32.768 kHz OSC<br/>(AON)"]
    XTAL --> FNPLL["FNPLL VCO<br/>2880 MHz<br/>FBDIV 0x78@24M / 0x48@40M"]
    FNPLL -->|÷12| C240["240 MHz"]
    FNPLL -->|÷18| C160["160 MHz"]
    FNPLL -->|÷24| C120["120 MHz"]
    FNPLL -->|÷9| C320["320 MHz"]
    FNPLL -->|÷6| C480["480 MHz"]
    C240 --> CPU["CPU / 总线"]
    C160 --> UART["UART0/1/2"]
    C120 --> WMAC["WiFi MAC / GPIO"]
    C320 --> WPHY["WiFi PHY"]
    C480 --> SPIROOT["SPI / QSPI / I2S 根<br/>(DIV_CTL3/RST_I2S 二级分频)"]
    XTAL --> XCLK["Timer / WDT / eFuse / I2C<br/>24 / 40 MHz 直挂晶体"]
    XTAL -->|÷2 / ÷4| TRNG["TRNG 12 / 10 MHz"]
    XTAL -->|÷24 / ÷40| TS["Tsensor ~1 MHz"]
    OSC32 --> RTC["RTC / PMU OSC<br/>32.768 kHz"]

    classDef pll fill:#d5e8ff,stroke:#36c;
    classDef xtal fill:#d5f5d5,stroke:#2a2;
    class FNPLL,C240,C160,C120,C320,C480 pll;
    class XTAL,OSC32 xtal;
```

### 时钟源（根）

表8-11 时钟源

```{list-table}
:header-rows: 1

* - 时钟源
  - 频率
  - 选择 / 寄存器
* - TCXO 晶体
  - 24 或 40 MHz
  - `HW_CTL`(0x4000_0014) bit0：1=24 MHz（`CLK24M_TCXO`）、0=40 MHz；硬件检测、只读
* - FNPLL VCO
  - **2880 MHz**（固定）
  - `CMU_FBDIV`(0x4000_3430)=0x78@24M / 0x48@40M；`CFG0..5`@0x4000_340C–0x3420；锁定查询 `EXCEP_RO_RG`(0x4000_319C) bit12
* - FNPLL 命名抽头
  - 320 / 480 / 24 MHz
  - `CMU_CLK_320M_WDBB`(0x4000_3448)、`CMU_CLK_480M_WDBB`(0x4000_344C)、`CMU_CLK_24M_USB`(0x4000_3454)
* - 低功耗振荡
  - 32.768 kHz
  - AON 域，供 RTC / PMU OSC
* - RFPLL 基准
  - —
  - `DBG_CMU_XO_PD`(0x4000_3400) 写 0x5 使能；仅供射频，非系统时钟源
```

### 源选择 CLK_SEL（0x4400_1134，1=PLL / 0=TCXO）

表8-12 CLK_SEL 位映射

```{list-table}
:header-rows: 1

* - 位
  - 域
  - 位
  - 域
* - 0
  - RF_CTL
  - 17
  - CPU / 总线 PLL 选择
* - 1 / 2 / 3
  - UART0 / 1 / 2
  - 18
  - Flash / SFC
* - 6
  - SPI
  - 19
  - WiFi PHY
* - 7
  - PWM（高频=PLL）
  - 20
  - WiFi MAC
```

### 分频 DIV_CTL（CLDO_CRG）

表8-13 时钟分频寄存器

```{list-table}
:header-rows: 1

* - 寄存器.字段
  - 外设
  - 分频值
* - `DIV_CTL0`(0x4400_1108)[7:4]，load bit8
  - CPU / 总线
  - 正常 0x1；低功耗 24M→4M=0x6、40M→4M=0xA
* - `DIV_CTL3`(0x4400_1114)[9:5]，load bit10
  - SPI
  - 主：`480 / 目标MHz`；从：默认 2（→240 MHz）
* - `DIV_CTL3/4/5` PWM 字段
  - PWM0–7
  - 6（24M）或 10（40M）
* - `DIV_CTL7`(0x4400_1124)[11:6]，en bit18
  - Tsensor
  - 0x18（24M）/ 0x28（40M）→ ~1 MHz
* - `DIV_CTL9`(0x4400_112C)[8:6]，en bit9
  - TRNG
  - ÷2（24M）/ ÷4（40M）
* - `RST_I2S_DIV_CFG`(0x4400_1144)
  - I2S MCLK
  - → 12.288 MHz
```

门控寄存器 `CKEN_CTL0/1` 的逐外设位见下一节表 8-15。

### 各外设时钟产生

表8-14 外设时钟派生（SDK 实证；与 ch2 表 2-3 对照）

```{list-table}
:header-rows: 1

* - 外设
  - 源
  - 选择 / 分频
  - SDK 实际频率
  - ch2 标称
* - CPU / 总线
  - FNPLL
  - CLK_SEL 17 + DIV_CTL0=1
  - 240 MHz
  - 240
* - Timer / WDT
  - **TCXO**
  - 直挂晶体
  - **24 / 40 MHz**
  - 晶体分频
* - RTC
  - 32.768 kHz
  - AON
  - 32768 Hz
  - 0.032
* - UART0/1/2
  - FNPLL
  - CLK_SEL 1/2/3；门控 CKEN1 18/19/20
  - **160 MHz**
  - 160
* - SPI
  - FNPLL（480 根）
  - CLK_SEL 6；DIV_CTL3[9:5]；门控 CKEN1 25
  - 主 ≤480/N；从 240
  - 160
* - QSPI
  - FNPLL（480 根）
  - 同 SPI 链（`lpm_dev_get_freq(DEV_SPI)`）
  - 480 根再分
  - 64
* - I2C
  - **TCXO**
  - 无 PLL mux
  - **24 / 40 MHz** ⚠
  - 80
* - I2S
  - FNPLL（480 WDBB）
  - `RST_I2S_DIV_CFG`；门控 CKEN0 11/12
  - MCLK 12.288 MHz
  - 8.192 等
* - GPIO
  - FNPLL
  - CRG
  - 120 MHz
  - 120
* - eFuse
  - **TCXO**
  - 周期寄存器（非分频）
  - 晶体；周期 0x29/0x19
  - 晶体
* - TRNG
  - TCXO
  - DIV_CTL9
  - 12 / 10 MHz
  - —
* - Tsensor
  - TCXO
  - DIV_CTL7
  - ~1 MHz
  - —
* - SFC / Flash
  - FNPLL
  - CLK_SEL 18；`CMU_NEW_CFG1`(0x4000_34A4)
  - PLL 派生
  - （QSPI 64）
* - WiFi MAC
  - FNPLL
  - CLK_SEL 20；CKEN1 13 入口门控
  - 120 MHz
  - 120
* - WiFi PHY
  - FNPLL（320 抽头）
  - CLK_SEL 19；`CMU_CLK_320M_WDBB`
  - 320 MHz
  - 320
* - BT/BLE MAC·PHY
  - FNPLL
  - CKEN1 8–12；`CMU_CLK_BT_TX/RX`(0x4000_3444/343C)
  - 32 MHz
  - 32
* - RF_CTL
  - FNPLL
  - CLK_SEL 0
  - PLL
  - —
```

```{important}
**SDK 与 ch2 标称的差异（以 SDK 为准）**：
- **I2C = 24/40 MHz（晶体），ch2 写 80**。与 UART/SPI 不同，I2C **不切 PLL**——`clock_init` 用
  `i2c_port_set_clock_value(REQ_24M/40M)` 把分频基准设为晶体；ch2 的 80 是总线能力标称值。
- **SPI 根 = 480 MHz（`PLL_CLK480M`），ch2 写 160**。SPI 分频链由 480 MHz 抽头喂入再二级分频；ch2 的 160 是标称。
- **I2S MCLK = 12.288 MHz，ch2 写「8.192 等」**——8.192 kHz 类采样率的 bclk 由 12.288 MHz 再分得。
- **CPU 240 / GPIO 120**：取自 ch2 + FBDIV 算术（2880÷12 / 2880÷24）；porting 代码做门控/分频但无字面常量。
```

### 启动时钟序列（自举 → 锁 PLL → 切换外设）

1. **flashboot**：关 CMU dummy load（`CMU_CFG0`[5:3]=0x7）；`boot_clock_adapt()` 检测晶体，先把 UART/Timer/WDT 置为**晶体**频率（UART 此时仍在 TCXO）。
2. **Flash 切 PLL**：`switch_flash_clock_to_pll()` 写 `CMU_NEW_CFG1`=0x1→0x3，再置 `CLK_SEL` bit18 → Flash/SFC 由 TCXO 切 PLL。
3. **应用 `open_rf_power()`**：按序上电 PLL/RF 各 LDO（120/10 µs 延时），解除 ADDA 隔离。
4. **`switch_clock()`**：使能 RFPLL 基准（`DBG_CMU_XO_PD`=0x5）→ WiFi MAC(`CLK_SEL`20)/PHY(19)/RF_CTL(0) 切 PLL →
   **UART 走「关门→切源→开门」**（清 `CKEN1` 18/19/20，置 `CLK_SEL` 1/2/3，再置 `CKEN1` 18/19/20）→ 设 TRNG/Tsensor 分频。
5. **`set_uart_tcxo_clock_period()`**：把 Timer / WDT / I2C0/1 / LiteOS sysclock 的软件 `clock_value` 设为**晶体**频率，把 **UART 设为 160 MHz**（此处唯一的 PLL 值）。
6. **驱动懒初始化**：SPI(`DIV_CTL3`+`CLK_SEL`6)、PWM(`CLK_SEL`7+门控+`DIV_CTL3/4/5`)、I2S(`RST_I2S_DIV_CFG`+`CKEN0` 11/12) 在各自 init 时切源/分频/开门控。
7. **低功耗 suspend/resume**：suspend 把 Flash/UART/总线/PHY 的 `CLK_SEL` 切回 TCXO、总线降到 4 MHz、关 FNPLL；resume **重编 FNPLL**（FBDIV 0x78/0x48）、轮询 bit12 锁定（失败则重启）、使能 480M WDBB、再把各域切回 PLL。

## 时钟门控映射与复位原因

### CLDO_CRG 时钟门控

时钟使能寄存器 `CKEN_CTL0` = `0x4400_1100`（索引 0）、`CKEN_CTL1` = `0x4400_1104`（索引 1）。
各外设时钟门控位如下（复位默认**已使能**，多数驱动不主动门控）。

表8-15 SDK 确认的时钟门控位（经 fbb_ws63 porting + SVD 逐一核对）

```{list-table}
:header-rows: 1

* - 外设
  - 寄存器
  - 位
  - 依据
* - PWM（9 门控 [10:2]）
  - CKEN0
  - 基位 2
  - `pwm_porting.c`
* - I2S 总线
  - CKEN0
  - 11
  - `sio_porting.c`
* - I2S 时钟
  - CKEN0
  - 12
  - `sio_porting.c`
* - UART0 / 1 / 2
  - CKEN1
  - 18 / 19 / 20
  - `clock_init.c` + SVD `uart_cken[20:18]`
* - SPI
  - CKEN1
  - 25
  - `spi_porting.c` + SVD `spi_cken[25]`
* - WiFi 入口总时钟
  - CKEN1
  - 13
  - `clock_init.c`
* - BT/BLE 硬件组
  - CKEN1
  - 8–12 / 14:13 / 29
  - `pm_porting.c`
```

```{important}
**校正（经 SDK 核对）**：上表是 SDK porting 代码**实际写门控位**的全部外设。其余外设——**I2C、Timer、
LSADC、Tsensor、TRNG、安全子系统、DMA、SDMA、SFC、SPI1**——SDK **不单独门控**（依赖复位默认开），SVD 也
未给出其 cken 字段，故无权威门控位来源。早期把它们标到 CKEN0 18–26 / CKEN1 22–24、并把 **I2S 误标为
CKEN0 bit24**（实为 bit 11 总线 + bit 12 时钟）均不可靠；这些未证实位已在 `ws63-hal/src/clock.rs` 显式标注为占位。
```

完整的时钟产生路径（FNPLL 2880 MHz、CLK_SEL 源选择、DIV_CTL 分频、各外设派生频率与启动序列）见上一节
**「时钟树（FNPLL 2880 MHz + CLDO_CRG，实证重建）」**。本表（8-15）只列门控位。

### 复位与复位原因

表8-16 软复位与复位原因寄存器

```{list-table}
:header-rows: 1

* - 项
  - 地址
  - 说明
* - 全芯片软复位寄存器
  - 0x4000_2110
  - 置 **bit2** 触发全芯片复位（GLB_CTL_M + 0x110）
* - `SYS_RST_RECORD_0`
  - 0x4000_00A0
  - 复位原因记录
* - `SYS_DIAG_CLR_1`
  - 0x4000_00A4
  - 复位原因清除（把命中位写回此处）
```

复位原因解码（按优先级；命中位写回 `SYS_DIAG_CLR_1` 清除）：

表8-17 复位原因位

```{list-table}
:header-rows: 1

* - 位
  - 掩码
  - 原因
* - 0
  - 0x1（`SYS_WDT_RST_HIS`）
  - 看门狗复位（最高优先级）
* - 1
  - 0x2（`SYS_SOFT_RST_HIS`）
  - 软件复位
* - 3
  - 0x8（`POR_RST_FILTER_HIS`）
  - 上电复位
```

```{note}
同一 SDK 文件中另有一处 `REG_SYS_RST_RECORD = 0x4000_0098`（位编码 HARD=1<<2/SOFT=1<<1/WDT=1<<0），
但 `reboot_port_get_rst_reason` 实际走的是 `0x4000_00A0` 路径（位 0/1/3）——以 **`0x4000_00A0` 为准**，
`0x4000_0098` 块在该函数中未使用。
```

## SFC 与启动流程

SFC（串行 Flash 控制器）基址 `0x4800_0000`（见第 2 章），外接 SPI NOR Flash 经 XIP 映射到
`0x0020_0000`（8 MB，越界读地址卷绕）。

表8-18 SFC 寄存器（flashboot 使用，绝对地址）

```{list-table}
:header-rows: 1

* - 寄存器
  - 地址
  - 功能
* - `SFC_GLOBAL_CONFIG`
  - 0x4800_0100
  - 全局配置（SPI 模式、地址字节数）
* - `SFC_TIMING`
  - 0x4800_0110
  - tshsl/tcss/tcsh 时序
* - `SFC_INT_STATUS` / `SFC_INT_CLEAR`
  - 0x4800_0124 / 0x012C
  - 命令完成 / 中断清除
* - `SFC_BUS_CONFIG1`
  - 0x4800_0200
  - XIP 读写模式
* - `SFC_CMD_CONFIG`
  - 0x4800_0300
  - start/addr_en/data_en/rw + data_len[14:9]
* - `SFC_CMD_INS` / `SFC_CMD_ADDR`
  - 0x4800_0308 / 0x030C
  - 指令（0xEB Quad 读） / 地址
* - `SFC_CMD_DATABUF`
  - 0x4800_0400
  - 16 字（64 字节）数据缓冲
```

**总线配置**：读 = Quad I/O（`rd_ins=0xEB`，dummy=4），写 = Dual I/O（`wr_ins=0x02` Page Program）。

**启动流程**（掩膜 ROM → SFC/Flash → 二级引导）：掩膜 ROM（厂商，不在仓库）加载二级引导
→ 检测 TCXO（24/40 MHz）→ eFuse init → Flash/UART 时钟切 PLL → UART 初始化 115200 → WDT 65 s
→ `sfc_init`（Quad-SPI）→ FAMA 重映射 Flash 应用窗 → 定位应用 → 校验镜像头 + SHA256 完整性
→ `mie=0` 后跳转 `addr + 0x300`。

**镜像头布局**（`ImageHeader` = 0x300：`KeyArea` 0x100 + `CodeInfo` 0x200）。`CodeInfo` 关键字段：
`image_id`@+0x00、`structure_version`@+0x04（=0x0001_0000）、`structure_length`@+0x08（ECC/SM2=0x200）、
`signature_length`@+0x0C（ECC=64）、`code_area_addr`@+0x20、`code_area_len`@+0x24、
`code_area_hash`@+0x28（SHA256[32]）。

```{important}
仓库内的 Rust `flashboot` 仅做**完整性**校验（SHA256 与头内 `code_area_hash` 比对），
**非真实性验签**（头本身未签名）——这不是 secure boot。厂商 flashboot 才用 ECC-bp256/SM2 签名 +
eFuse 根密钥验签。
```

## 定时器（Timer）寄存器

第 2 章给出 3 个可独立配置的 32 位定时器及其三种模式（one-shot/periodic/free-running），本节给出寄存器编程模型。
基址 `0x4400_2000`；每个定时器占 **0x100 步进**的子块：Timer0 @ +0x100、Timer1 @ +0x200、Timer2 @ +0x300；
另有 +0x00..0x88 的**公共窗**（VMID 权限校验、锁、异常中断聚合）。中断 `TIMER_INT0/1/2` = 26/27/28，
共享异常线 `TIMER_ABNOR` = 60（见表 2-5）。计数器为**递减计数**，硬件最高支持 64 位（load/current 各有 0/1 两字）。

表8-19 单个 Timer 寄存器（偏移相对该定时器子块基址）

```{list-table}
:header-rows: 1

* - 偏移
  - 名称
  - 访问
  - 说明
* - 0x00
  - `LOAD_COUNT0`
  - RW
  - 装载/重载值，低 32 位
* - 0x04
  - `LOAD_COUNT1`
  - RW
  - 装载值高 32 位（64 位定时器）
* - 0x08
  - `CURRENT_VALUE0`
  - RO
  - 当前递减计数，低 32 位
* - 0x0C
  - `CURRENT_VALUE1`
  - RO
  - 当前计数高 32 位
* - 0x10
  - `CONTROL`
  - RW
  - 控制（位域见下）
* - 0x14
  - `EOI`
  - RO
  - 读清中断（end-of-interrupt）
* - 0x18
  - `RAW_INTR`
  - RO
  - 原始（未屏蔽）中断状态
* - 0x1C
  - `INTR`
  - RO
  - 屏蔽后中断状态
```

**CONTROL（0x10）位域**：`enable`(0)、`mode`[2:1]、`int_mask`(3)、`rstfsm`(4 复位 FSM)、
`cnt_req`(5 置位锁存当前值以相干读取)、`cnt_lock`(6 RO 锁存就绪)。
**模式 `mode`[2:1]**：0 = one-shot、1 = periodic、2 = one-shot（别名）、3 = free-running。
**计数时钟为 TCXO 晶体**（24 MHz；40 MHz 晶体板为 40 MHz）：硅片上由 `clock_init` 经
`timer_porting_clock_value_set(REQ_24M)` 设定，`CONFIG_TIMER_CLOCK_VALUE` 的 32 MHz 仅为 Kconfig 占位默认。
故 1 µs = 24 拍；无内置预分频器。当前值的相干读取走 `cnt_req` → 轮询 `cnt_lock` 握手。

```{note}
**[校正]** PAC 的 `Mode` 枚举文档把编码写反（标 0=free-run/1=one-shot/2=periodic）；**以厂商 SDK 为准**
（0 = one-shot、1 = periodic、3 = free-run）。另：timer 计数时钟是 **TCXO 晶体（24/40 MHz）**，**不是**系统
240 MHz CPU/PLL 时钟——换算定时值勿混用（32 MHz 是 Kconfig 占位，被 `clock_init` 的晶体路径覆盖）。
```

## RTC 与 48 位系统计数器

官方地址映射表里的 **RTC（0x4000_5000）** 实为一个 **48 位自由运行递加计数器**（厂商 SDK 内部名 `SYSTICK`），
即第 2 章 RTC 小节描述的「48bit free running 递加计数器、32 kHz、上电即计数、支持阈值中断」，中断 `RTC_IRQ` = 29。

表8-20 系统计数器寄存器（基址 0x4000_5000）

```{list-table}
:header-rows: 1

* - 偏移
  - 名称
  - 位
  - 说明
* - 0x18
  - `RTC_TIME_OUT_H`
  - [15:0]
  - 计数高 16 位
* - 0x1C
  - `RTC_TIME_OUT_L`
  - [31:0]
  - 计数低 32 位
```

读取：先读低 32 位、再读高 16 位拼成 48 位值（双读取保证相干）；自由运行、无使能位、无装载值；时钟 32 kHz。

```{note}
厂商 SDK 另有一个独立的 RTC IP（`rtc_unified`，porting 与 PAC 给出基址 **`0x5702_4000`**，位于官方简表范围之外），
含 4 个 **32 位**实例（步进 0x14），每实例寄存器：`LOAD_COUNT`(0x00)、`CURRENT_VALUE`(0x04)、
`CONTROL`(0x08，位 `enable`(0)/`mode`(1，0=自由运行/1=周期)/`int_mask`(2))、`EOI`(0x0C 读清)、`INT_STATUS`(0x10)，
用作可编程周期/阈值中断。该 IP 的基址超出官方地址映射表，标注为 **[推断/超出官方映射]**。
```

## 看门狗（WDT）寄存器

WDT 基址 `0x4000_6000`，Synopsys DesignWare 风格，32 位递减计数（装载值 24 位）。对应第 2 章看门狗的两种工作方式。

表8-21 WDT 寄存器（偏移相对基址）

```{list-table}
:header-rows: 1

* - 偏移
  - 名称
  - 说明
* - 0x00
  - `WDT_LOCK`
  - 锁/解锁：写 `0x5A5A5A5A` 解锁；读 0=已解锁、1=锁定
* - 0x04
  - `WDT_LOAD`
  - 装载值（[31:8] = 24bit 计数；[7:0] 保留）
* - 0x08
  - `WDT_RESTART`
  - 喂狗/重启（写入即重载计数器）
* - 0x0C
  - `WDT_EOI`
  - 中断清除（读清）
* - 0x10
  - `WDT_CR`
  - 控制（位域见下）
* - 0x14
  - `WDT_CNT`
  - 当前 32 位递减计数
* - 0x18 / 0x1C
  - `WDT_RAW_INTR` / `WDT_INTR`
  - 原始 / 屏蔽后中断状态（bit0）
* - 0x28
  - `WDT_CCVR_EN`
  - 计数锁存：`ccvr_req`(0 置位锁存) / `ccvr_lock`(1 锁存就绪)
```

**WDT_CR（0x10）位域**：`wdt_en`(0)、`rst_en`(2 允许产生系统复位)、`rst_pl`[5:3]（复位脉冲长度 2/4/8/…/256 时钟）、
`wdt_imsk`(6 中断屏蔽)、`wdt_mode`(7：0=一次中断后复位、1=两次中断后复位)。
**喂狗时序**：解锁(`0x5A5A5A5A`) → 写 `WDT_RESTART` → 重新锁定。

```{important}
WS63 的解锁魔数是 **`0x5A5A5A5A`**，不是 DesignWare 经典的 `0x1ACCE551`。WDT 中断**不在** IRQ ≥ 26 的外部中断表内，
而是经专用处理走 **NMI 类**通路（与第 2 章「NMI 由 WDOG 中断触发」一致）；超时按 `rst_en` 触发**全芯片复位**，
脉冲长度由 `rst_pl` 决定。**计数时钟为 TCXO 晶体**（24 MHz；硅片上 `clock_init` 经
`watchdog_port_set_clock(REQ_24M)` 设定，与 `CONFIG_WDT_CLOCK` 的 24 MHz 一致；40 MHz 晶体板为 40 MHz）。
24 位 `WDT_LOAD` 位于 [31:8]，装载值 = `(timeout × clock) >> 8`，故最大超时 ≈ `(0xFFFFFF << 8) / 24 MHz ≈ 178 s`。
```

## TCXO 时间基准

TCXO 计数器是芯片的**单调时间基准**，基址 `0x4400_04C0`，**64 位**自由运行计数（由 4 个 16 位 COUNT 寄存器拼成），
tick 速率 **24 MHz**。它是 ws63-rs 的 embassy 时间驱动 `now()` 的时钟源（与定时器闹钟配合实现 `Timer::after`）。

表8-22 TCXO 寄存器（偏移相对 0x4400_04C0）

```{list-table}
:header-rows: 1

* - 偏移
  - 名称
  - 位
  - 说明
* - 0x00
  - `TCXO_STATUS`
  - —
  - 控制/状态：`refresh`(0 写 1 锁存当前计数)、`clear`(1 清零)、`enable`(2)、`valid`(4 锁存有效，refresh 后轮询)
* - 0x04
  - `COUNT0`
  - [15:0]
  - 计数 [15:0]
* - 0x08
  - `COUNT1`
  - [15:0]
  - 计数 [31:16]
* - 0x0C
  - `COUNT2`
  - [15:0]
  - 计数 [47:32]
* - 0x10
  - `COUNT3`
  - [15:0]
  - 计数 [63:48]
```

**读取序列**：写 `refresh` → 轮询 `valid` → 读 `COUNT0..3` 拼成 64 位计数。**闹钟映射**：embassy 时间驱动以
**TIMER 通道 0**（IRQ `TIMER_INT0` = 26）作一次性闹钟——`set_alarm` 算出 `delta` 写入 `Timer0 LOAD_COUNT0` 并使能，
触发后 `on_alarm_interrupt` 唤醒到期任务并按下一个截止时间重装。

## Wi-Fi/BLE 子系统：内存区、掩膜 ROM 与单核架构

第 {ref}`4 章 <ch4-wifi>` 描述 Wi-Fi/BLE/SLE 的射频与协议。本节补充**把闭源协议栈链接进固件**所需的
底层事实（来自对厂商 blob 与符号表的实证分析）。

### 连接性内存区

闭源 blob 期望固件链接脚本提供以下区段（均为 `extern` 链接符号）。

表8-23 Wi-Fi/BLE 内存区

```{list-table}
:header-rows: 1

* - 区段
  - 大小
  - 用途
  - 链接符号
* - Wi-Fi Packet RAM
  - 48 KB
  - DMA 缓冲、netbuf 池、描述符环
  - `__wifi_pkt_ram_begin__/end__`
* - ROM Data
  - ~4 KB
  - 已初始化 ROM 变量（启动时 flash→RAM 拷贝）
  - `__rom_data_begin__/load__/size__`
* - ROM BSS
  - ~1 KB
  - 零初始化 ROM 变量
  - `__rom_bss_begin__/end__`
* - TCM Text / Data
  - 各 16–64 KB
  - 延迟敏感的 Wi-Fi/BT 代码/数据（ITCM/DTCM，可选）
  - `__tcm_text_*` / `__tcm_data_*`
* - SRAM Text
  - ~128 KB
  - Wi-Fi 协议代码
  - `__sram_text_begin__/end__/load__`
* - SRAM Data / BSS
  - ~256 KB
  - Wi-Fi 协议运行时状态
  - `__data_*` / `__bss_*`
```

全 Wi-Fi+BLE 运行**最小 RAM ≈ 500 KB**。物理映射与第 2 章地址表一致：ITCM `0x0010_0000`、
DTCM `0x0018_0000`、SHARE_RAM/SRAM `0x00A0_0000`、NOR_FLASH `0x0020_0000`。

### 掩膜 ROM 符号表

WS63 的 RF 前端与底层 MAC 例程固化在片内掩膜 ROM 里，C SDK 通过一张**符号地址表**解析它们。

- **符号数：3752**，地址跨 `0x10_9000`～`0x18_2884`（实测最大符号超出 SDK 注释里 `0x14C000` 的上界）。
- 这些是**真实硅片地址**：不填充掩膜 ROM 的仿真器无法执行它们（连接性因此是硬件在环）。
- 类别（前缀计数与示例）：`dmac_*` 709、`hal_*` 472（如 `hal_sfc_regs_init=0x10_9478`）、`oal_*` 66、
  `frw_*` 56、`ble_*` 29、`hal_btcoex_*` 25、`fe_*` RF 前端 14（如 `fe_initialize_rf_dev=0x12_825e`）、
  `hal_al_rx_*` 2 等。

**符号闭合分析**：`libwifi_driver_dmac.a` 有约 1080 个未定义符号，分布为——约 422 个掩膜 ROM 函数
（由 ROM 符号表 `.lds` 解析）、约 618 个由其余厂商 `.a`（hmac/tcm/alg）提供、约 40 个属运行时职责
（porting 契约 + 编译器 rt builtin + `__wifi_pkt_ram_*` + ROM 数据全局 `g_dmac_alg_main`/`g_mac_res_etc`）。
凑齐 ROM 表 + 完整 Wi-Fi `.a` 集 + porting 层后，可达路径残留恰好 40 个（23 OSAL/OAL + 10 平台 + 7 rt + 2 链接符号）。

### 单核架构与 HMAC/DMAC/HCC

```{important}
WS63 是**单核** —— 一颗自研 RISC-V 应用核（带 32 KB I-Cache + 4 KB D-Cache）。证据：原厂手册第 2 章
「系统提供一个自研 RISC-V 处理器作为主控 CPU」；`platform_core.h` 标题 *Application Core*；SDK 只有
`acore` 的 rom_config（无 `dcore`）；app/loaderboot/flashboot 三套构建均 `-DCORE=acore`。
```

Wi-Fi 的 **HMAC（host MAC）与 DMAC（device MAC）是链接进同一应用镜像的软件库**
（`libwifi_driver_hmac.a` / `libwifi_driver_dmac.a` 同在 `ws63-liteos-app/`），都跑在这一颗核上。
**HCC** 是 host↔device 传输抽象，有两种拓扑：(a) 外接主控 MCU 经 SDIO/SPI 驱动 WS63 模组——这才是「两颗 CPU」；
(b) WS63 独立运行——HMAC/DMAC 退化为同一核上的软件分层，HCC 是片内消息通路，**没有第二颗核**。
（早期文档把 HMAC/DMAC 写成「ACORE/DCORE 双核」，不准确，已更正。）

### 厂商库目录

表8-24 闭源库目录（`ws63-RF/lib/`，共 14 个 `.a`，约 44 MB）

```{list-table}
:header-rows: 1

* - 库
  - 大小
  - 用途
* - `libwifi_driver_dmac.a`
  - 614 KB
  - Wi-Fi device MAC + HAL + RF 前端控制
* - `libwifi_driver_hmac.a`
  - ~32 MB
  - Wi-Fi host MAC + 公开 Wi-Fi API（`wifi_*`）
* - `libwifi_driver_tcm.a`
  - ~6 MB
  - TCM 驻留的 Wi-Fi 驱动代码
* - `libwifi_alg_*.a`（5 个）
  - ~2.5 MB
  - 抗干扰 / CCA / EDCA / 温度保护 / TxBF 算法
* - `libwifi_rom_data.a`
  - ~2 KB
  - Wi-Fi ROM 数据段（配置全局）
* - `libbt_host.a`
  - ~1.1 MB
  - BLE host 协议栈（GAP/GATT/SMP/L2CAP）
* - `libbt_app.a`
  - ~279 KB
  - BLE 应用层
* - `libbth_gle.a`
  - ~801 KB
  - SLE/GLE（星闪）host 协议栈
* - `libbth_sdk.a`
  - ~87 KB
  - BT host SDK 工具
* - `libbg_common.a`
  - ~213 KB
  - BT 公共工具
```

```{note}
开源的 `libwpa_supplicant.a`（WPA 认证，hostap）**未**打包进 `ws63-RF/lib/`：它非专有、且 MAC 驱动对其 0 引用。
```
