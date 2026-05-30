# ws63-guide 架构

本仓库是 [ws63-rs](https://github.com/sanchuanhehe/ws63-rs) monorepo 的子模块。

`ws63-guide` 是 WS63 芯片的**中文硬件手册**（Sphinx + MyST），逆向自 vendor 文档，覆盖系统/内存图/中断表/
QSPI/Wi-Fi/RF/安全/外设寄存器等。它是有价值的逆向 IP，与 Rust 代码架构文档（`docs/`）互补——
本手册讲**硬件**，`docs/` 讲**代码**，两者不重叠。

代码侧的架构与评审（集中维护于主仓库）：
- 总体架构：<https://github.com/sanchuanhehe/ws63-rs/blob/main/docs/architecture/overview.md>
- 组件文档：<https://github.com/sanchuanhehe/ws63-rs/blob/main/docs/architecture/ws63-guide.md>
- 整改排期：<https://github.com/sanchuanhehe/ws63-rs/blob/main/ROADMAP.md>
