# WS63 系列 SoC 用户指南

基于 Sphinx + MyST 构建的 WS63 系列 SoC 芯片用户指南文档。

## 项目概述

本仓库包含 WS63 系列 SoC（Wi-Fi、BLE 和 SLE Combo 芯片）的用户指南文档源码，
使用 [Sphinx](https://www.sphinx-doc.org/) 和 [MyST Parser](https://myst-parser.readthedocs.io/)
将 Markdown 文件构建为 HTML 和 PDF 格式。

## 前置条件

- Python ≥ 3.10
- [uv](https://docs.astral.sh/uv/) — Python 包管理器
- PDF 构建需要 XeLaTeX（见下文）

## 快速开始

```bash
# 克隆仓库
git clone <repo-url>
cd ws63-guide

# 安装依赖
uv sync

# 构建 HTML
uv run sphinx-build -b html -c source source _build/html
# 浏览器打开 _build/html/index.html
```

## 构建命令

### HTML

```bash
uv run sphinx-build -b html -c source source _build/html
```

### PDF

需要安装 TeX Live（含 XeLaTeX）：

```bash
# macOS
brew install --cask mactex

# Ubuntu/Debian
sudo apt-get install -y latexmk texlive-xetex texlive-latex-recommended texlive-fonts-recommended texlive-latex-extra

# 构建
uv run sphinx-build -M latexpdf -c source source _build/pdf
# 输出: _build/pdf/ws63_user_guide.pdf
```

### 链接检查

```bash
uv run sphinx-build -b linkcheck -c source source _build/linkcheck
```

## 仓库结构

```
ws63-guide/
├── .github/workflows/docs.yml  # CI/CD 流水线
├── .markdownlint.json          # Markdown 规范配置
├── source/                     # 文档源码
│   ├── conf.py                 # Sphinx 配置
│   ├── index.rst               # 目录入口
│   ├── preface.md              # 前言
│   ├── ch1_overview.md         # 产品概述
│   ├── ch2_system.md           # 系统
│   ├── ch3_qspi.md             # QSPI Flash 控制器
│   ├── ch4_wifi.md             # WiFi/BLE & SLE 系统
│   ├── ch5_security.md         # 安全系统
│   ├── ch6_peripherals.md      # 外围设备
│   ├── ch7_jtag.md             # JTAG
│   ├── appendix.md             # 缩略语
│   └── images/                 # 图片资源
├── pyproject.toml              # 项目/依赖配置
├── uv.lock                     # 依赖锁文件
└── README.md
```

## CI/CD

本仓库使用 GitHub Actions 自动构建和部署文档。

### 工作流说明

| 任务 | 触发条件 | 说明 |
|------|----------|------|
| **Build HTML** | push / PR | 构建 HTML 版本，上传为构建产物 |
| **Build PDF** | push / PR | 安装 TeX Live，构建 PDF 版本 |
| **Deploy Pages** | push main | 部署 HTML 到 GitHub Pages |
| **Link Check** | push / PR | 检查文档中的外部链接（仅告警，不阻断） |

### 构建产物

- **HTML**: 每次构建上传，可在 Actions → 具体构建 → Artifacts 下载
- **PDF**: 每次构建上传 `ws63_user_guide.pdf`
- **Pages**: 推送到 main 分支后自动部署到 GitHub Pages

## 格式规范

本项目使用 [markdownlint](https://github.com/DavidAnson/markdownlint) 检查格式，
配置见 `.markdownlint.json`。主要规则：

- 行长度 ≤ 200 字符（表格和代码块除外）
- 允许中文标点结尾的标题
- 允许多层标题重复（跨文件场景）

## 技术栈

- [Sphinx](https://www.sphinx-doc.org/) — 文档构建引擎
- [MyST Parser](https://myst-parser.readthedocs.io/) — Markdown 解析
- [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/) — Read the Docs 主题
- [sphinxcontrib-mermaid](https://github.com/mgaitan/sphinxcontrib-mermaid) — Mermaid 图表支持
- [uv](https://docs.astral.sh/uv/) — Python 依赖管理

## 贡献

1. 编辑 `source/` 目录下的 Markdown 文件
2. 本地构建验证：`uv run sphinx-build -b html -c source source _build/html`
3. 提交 Pull Request
4. CI 会自动构建并检查链接
