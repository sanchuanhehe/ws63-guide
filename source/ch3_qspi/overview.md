(ch3-qspi-overview)=

# 概述

SFC 是一个 {term}`SPI` Flash 控制器。业务侧提供一个 AHB（Advanced High Performance Bus） Slave 接口，主要完成 AHB 通道对 SPI Flash 的访问控制功能；提供一个 AHB Master 接口，用于 {term}`DMA` 方式读写 Flash。

```{figure} ../images/fig-3-1-sfc-block-diagram.jpg
:name: fig-3-1
SFC 应用框图
```

```{note}
IF（Interface）。
```

# 功能描述

## AHB Slave 接口

AHB Slave 接口具有以下特点：

- 提供一个 AHB Slave 接口，可以根据不同的选择信号访问内部配置寄存器或直接访问 SPI Flash Memory。
- 支持 AMBA2.0 协议。
- 仅支持小端（Little-Endian）。

## AHB Master 接口

AHB Master 接口具有以下特点：

- 提供一个 AHB Master 接口，用于 DMA 方式在内存和 Flash 之间搬运数据。
- 支持 AMBA2.0 协议。
- 只支持小端。
- 支持 Single、INCR、INCR4、INCR8、INCR16 传输类型。
- 不支持 Early Termination。
- 支持总线 Lock 传输。

## 存储器接口

存储器接口具有以下特点：

- 片选的存储空间最大支持到 64Mbit（3Byte 地址模式），片选映射基地址可配置，只支持片选 1，不支持片选 0。
- 支持 Standard SPI、Dual-Output/Dual-Input SPI、Quad-Output/Quad-Input SPI、Dual-I/O SPI、Quad-I/O SPI 五种接口类型。上电后默认支持 Standard SPI 接口类型，可通过寄存器配置切换接口类型。
- 支持 {term}`XIP`（Executed In Place）。
- SPI Flash 读写操作支持总线直接读写、寄存器编程读写、DMA 读写三种方式。
- 支持多种写保护操作。
- SFC 模块支持 SPI Mode0 和 Mode3，按协议要求，支持 SPI Mode0 和 Mode3 的 SPI Flash 器件在时钟的上升沿采样数据，在时钟的下降沿输出数据。
- XIP 实现地址 remap，为了软件只编译一个 XIP 镜像，升级镜像时主镜像和备份镜像使用相同地址。

## Flash 数据在线解密

Flash 数据在线解密具有以下特点：

- 解密算法为 {term}`AES`-128-CTR，仅支持 1 个 IV，秘钥来源于 KM 派生。
- 支持 4 个解密区域，配置粒度为 256Byte；每个区域支持单独的 IV 解密起始地址可配，配置粒度同为 256Byte，4 个解密区域配置不能存在交叉地址。

```{note}
支持 AES 在线解密，解密时读取数据量没有 16Byte 的倍数与对齐的约束。
```

# 工作方式

## 读写 Flash

有三种方式读写 Flash：

- 通过寄存器配置方式发送 SPI Flash Program、Read 等命令来读写 Flash。例如：对寄存器 CMD_CONFIG 写 0x0000_7F8B，对寄存器 CMD_INS 写 0x03，表示通过 Standard SPI 方式发起读 64Byte Flash 数据的操作。此方式直接控制需要发送的 Flash 命令。
- 通过 AHB Slave 接口以类似读写普通 Memory 的方式读写 Flash，SFC 模块会自动将 AHB 总线的读写操作时序映射为 SPI Flash 读写命令。
- 通过 DMA 方式在 Flash 和外部 Memory 之间搬移数据。

## 其他操作

对 Flash 的其他操作如 Erase、进入 Deep Power Down、读 Device ID 等必须通过寄存器访问来实现。需要配置 CMD_INS[REG_INS]为相应的命令，具体请参见 Flash 器件手册。

例如：对寄存器 CMD_CONFIG 写 0x0000_0583，对寄存器 CMD_INS 写 0x0000_009F，表示读器件 ID 的操作。

## 初始化流程

```{important}
注意以下初始化流程仅做参考，请根据器件差异进行调整。
```


初始化流程如下：

1. （如果需要调整 Timing 参数）配置 TIMING 寄存器。
2. 配置总线操作方式寄存器。
   - 根据实际 Flash 大小配置 BUS_FLASH_SIZE`flash_size_cs1`（直接获知器件大小或可通过发 Read ID 命令给 Flash 查询获得）。
   - 有些器件要求进入非 Standard SPI 读写时序，需要预先以特殊命令配置 Flash。根据器件需要，对寄存器 CMD_INS 进行写操作，发特定命令配置 Flash。
   - 通过 BUS_CONFIG1/BUS_CONFIG2 配置总线读写操作指令和参数。例如：对寄存器 BUS_CONFIG1 写 0xCC85_EB1E 表示配置的参数为写指令 32h，写方式为 Quad-Input SPI，读指令 EBh、读方式为 Quad I/O SPI。
   - 如果需要开启总线写操作，配置 BUS_CONFIG1`wr_enable`为 1，使能总线写。默认关闭总线写功能。

## 通过寄存器方式读 Flash 操作流程

通过寄存器读取 Flash 的操作流程（查询方式），如图 3-2 所示。

```{figure} ../images/fig-3-2-sfc-reg-read-flow.jpg
:name: fig-3-2
通过寄存器读取 Flash 的操作流程（查询方式）
```

## 通过寄存器方式写 Flash 操作流程

```{important}
- 通过寄存器方式写 Flash 数据时，总线和 DMA 不得访问 Flash。
```

- 单次写 Flash 不能跨越 Page 边界（寄存器写方式没有跨越 Page 边界保护，需要软件保证，如果跨越 256Byte 边界，将会 Wrap 到该 Page 的起始地址，覆盖原来的内容）。

通过寄存器写 Flash 的操作流程（中断方式），如图 3-3 所示。

```{figure} ../images/fig-3-3-sfc-reg-write-flow.jpg
:name: fig-3-3
通过寄存器写 Flash 的操作流程（中断方式）
```

```{note}
WREN（Write Read Enable），PP（Page Program），RDSR（Read Status Register）。
```

## 通过寄存器方式其他操作流程

通过寄存器方式其他操作流程如图 3-4 所示。

```{figure} ../images/fig-3-4-sfc-other-op-flow.jpg
:name: fig-3-4
通过寄存器方式其他操作流程
```

```{note}
SFC 控制器不支持发出”OPCODE（1byte）+ DUMMY（3byte 全 0）”组合 SPI 时序，某些 Flash 指令需要这种组合时序时，可以采用”OPCODE（1byte）+ ADDR（3byte 全 0）”组合代替。
```

## 通过 AHB Slave 直接读写 Flash 操作流程

- 上电复位后，默认配置为 Standard SPI 时序模式，不需要额外配置，可直接读 Flash。
- 默认通过 AHB Slave 写 Flash 是禁止的，需要配置 BUS_CONFIG1`wr_enable`为 1，使能总线写操作。
- 如果需要调整默认配置，请参见”3.3.3 初始化流程”。

## 通过 DMA 方式读写 Flash 操作流程

DMA 操作流程如下：

1. 如需调整总线操作方式时序配置，请参见”3.3.3 初始化流程”。
2. 写 BUS_DMA_MEM_SADDR，配置 DMA 操作的内存端起始地址；写 BUS_DMA_FLASH_SADDR，配置 Flash 端起始地址（Flash 偏移地址）；写 BUS_DMA_LEN，配置数据长度。
3. 写 BUS_DMA_CTRL，配置读写方向，选择 Flash 片选 1。
4. 写 BUS_DMA_CTRL`start`为 1，使能 DMA 操作。
5. 等待 dma_done 中断触发（中断方式）或轮询 DMA 操作完成（BUS_DMA_CTRL`start`变为 0）。

```{note}
- DMA 操作时可以同时进行 Flash 寄存器读命令操作。
- DMA 操作时可以同时通过 AHB Slave 直接访问 Flash，但需保证中间不修改总线操作相关配置。
- DMA 操作时需要保证首地址 4Byte 对齐。
```

