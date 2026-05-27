(ch7-jtag)=

# JTAG

## 概述

芯片内部集成一个自研 CPU，在内部集成 Coresight 调试架构，支持基于 Coresight 的 JTAG 和 SWD（Serial Wire Debug）调试接口，通过 Coresight 的 JTAG 或 SWD 调试接口实现调试，支持 Lauterbach 仿真器和 JLINK 仿真器。

## 调试接口

### 须知

芯片调试接口默认复用为其他功能，如果需要使用调试功能，则管脚 GPIO_04 在上电 时置高电平，系统复位解除后，对应管脚即可复位为调试接口，此后 GPIO_04 管脚功 能不受影响，可以作为正常管脚使用。

调试管脚与 PAD 名字的对应关系请参见《WS63V100 SoC WiFi、BLE 和 SLE 和 SLE Combo 芯片 硬件用户指南》。
