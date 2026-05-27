(ch7-jtag)=

# JTAG

## 概述

芯片内部集成自研 {term}`CPU`，内部集成 Coresight 调试架构，支持基于 Coresight 的 {term}`JTAG` 和 SWD（Serial Wire Debug）调试接口，支持 Lauterbach 仿真器和 JLINK 仿真器。

## 调试接口

```{important}
芯片调试接口默认复用为其他功能，如果需要使用调试功能，则管脚 GPIO_04 在上电时置高电平，系统复位解除后，对应管脚即可复位为调试接口，此后 GPIO_04 管脚功能不受影响，可以作为正常管脚使用。
```


调试管脚与 PAD 名字的对应关系请参见《WS63V100 {term}`SoC` WiFi、{term}`BLE` 和 SLE Combo 芯片硬件用户指南》。
