# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

Chinese-language Sphinx + MyST documentation for the WS63 series SoC (Wi-Fi/BLE/SLE combo chip by HiSilicon). 9 chapters + appendix covering product overview, system architecture, QSPI, WiFi/BLE/SLE, security, peripherals, and JTAG.

## Commands

```bash
# Install dependencies (pin to lock file)
uv sync --locked

# Build HTML
uv run sphinx-build -b html -c source source _build/html

# Build PDF (requires XeLaTeX)
uv run sphinx-build -M latexpdf -c source source _build/pdf

# Link check (non-blocking warnings)
uv run sphinx-build -b linkcheck -c source source _build/linkcheck

# Lint Markdown
npx markdownlint-cli2 "source/**/*.md"
```

## Architecture

- **Sphinx config** is `source/conf.py` (not at repo root). The `-c source` flag is required.
- **Root toctree** is `source/index.rst` (RST). All individual chapters are `.md` files in `source/` and use MyST Markdown syntax.
- **PDF generation** uses `xeCJK` with Droid Sans Fallback for Chinese character support. CI installs the full TeX Live suite for this.
- **`uv.lock`** is committed — always use `uv sync --locked` to respect pinned versions.
- **Images** live in `source/images/` (19 JPEGs). All are diagrams, icons, or safety-symbol illustrations.
- **`_build/`** is gitignored and safe to delete — it's the local build output.

## CI/CD

`.github/workflows/docs.yml` runs on push to `main`, PRs, and manual dispatch:
- **Build HTML** → upload artifact, also prepare Pages artifact (non-PR)
- **Build PDF** → installs TeX Live, builds, uploads PDF artifact
- **Deploy Pages** → deploys to GitHub Pages (push to `main` only)
- **Link Check** → `continue-on-error: true`, non-blocking

Concurrency is `cancel-in-progress: true` grouped by ref.

## Content guidelines

- All prose is Simplified Chinese (`zh_CN`).
- Mermaid diagrams use ````{mermaid}` fence blocks.
- MyST extensions enabled: `colon_fence`, `deflist`, `html_image`, `dollarmath`, `substitution`, `replacements`, `smartquotes`.
- Line length ≤ 200 chars (tables and code blocks exempt).
