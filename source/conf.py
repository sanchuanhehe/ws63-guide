# Configuration file for the Sphinx documentation builder.
# -- WS63 系列 SoC 用户指南

import os
import sys

# -- Project information -----------------------------------------------------
project = 'WS63 系列 SoC 用户指南'
copyright = '2024, HiSilicon'
author = 'HiSilicon'
version = '01'
release = '01'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinxcontrib.mermaid',
]

# MyST Parser settings
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "dollarmath",
]

myst_number_code_blocks = ["json"]
myst_heading_anchors = 4
myst_title_to_header = True

# Suppress warnings for unknown mime types
myst_fence_as_directive = ["mermaid"]

# Source settings
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

root_doc = 'index'

# Templates path
templates_path = ['_templates']

# Exclude patterns
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_language = 'zh_CN'
html_permalinks_icon = '#'

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    'fontpkg': r'''
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage{booktabs}
\usepackage{longtable}
\usepackage{graphicx}
\usepackage{xcolor}
\usepackage{tabularx}
\usepackage{array}
\usepackage{colortbl}
\usepackage{multirow}
\usepackage{hyperref}

% CJK support via fontspec (xeCJK requires ctexhook which is not available)
\usepackage{xeCJK}
\setCJKmainfont{Droid Sans Fallback}
\setCJKsansfont{Droid Sans Fallback}
\setCJKmonofont{Droid Sans Fallback}

% Custom colors
\definecolor{headerblue}{RGB}{51, 102, 153}
\definecolor{lightgray}{RGB}{240, 240, 240}

% Table header style
\newcommand{\tableheader}{\rowcolor{headerblue}\textcolor{white}}

% Set default figure placement
\makeatletter
\def\fps@figure{htbp}
\makeatother

% Better table support
\setlength{\tabcolsep}{4pt}
\renewcommand{\arraystretch}{1.2}
''',
    'sphinxsetup': r'''
hmargin={2cm,2cm},
vmargin={2.5cm,2.5cm},
''',
    'tableofcontents': r'''
\pagenumbering{Roman}
\sphinxtableofcontents
\clearpage
\pagenumbering{arabic}
''',
    'maketitle': r'''
\begin{titlepage}
\centering
\vspace*{5cm}
{\Huge \textbf{WS63 系列 SoC \\ Wi-Fi、BLE 和 SLE Combo 芯片}}\\[1cm]
{\LARGE \textbf{用户指南}}\\[2cm]
{\Large 文档版本 01}\\[0.5cm]
{\Large 发布日期 2024-04-10}\\[3cm]
\end{titlepage}
''',
}

# Latex documents
latex_documents = [
    (root_doc, 'ws63_user_guide.tex', 'WS63 系列 SoC 用户指南', 'HiSilicon', 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    (root_doc, 'ws63-user-guide', 'WS63 系列 SoC 用户指南', [author], 1),
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
    (root_doc, 'WS63UserGuide', 'WS63 系列 SoC 用户指南',
     author, 'WS63UserGuide', 'WS63 系列 SoC Wi-Fi、BLE 和 SLE Combo 芯片用户指南',
     'Miscellaneous'),
]

# -- Figure numbering --------------------------------------------------------
numfig = True
numfig_secnum_depth = 3
numfig_format = {
    'figure': '图 %s',
    'table': '表 %s',
    'code-block': '代码 %s',
    'section': '第 %s 节',
}

# -- Smart quotes ------------------------------------------------------------
smartquotes = False

# -- Internationalization ----------------------------------------------------
language = 'zh_CN'
locale_dirs = ['locale/']
gettext_compact = False

# -- MyST specific -----------------------------------------------------------
myst_url_schemes = ("http", "https", "mailto")
