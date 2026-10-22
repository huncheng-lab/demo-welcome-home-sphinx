"""《欢迎回家》档案站 —— Sphinx 配置。

主题：pydata-sphinx-theme；配色贴近 React 原站的「暖纸米白 + 深墨字 + 琥珀金」。
"""

project = "欢迎回家 · WELCOME HOME"
copyright = "2026, 《欢迎回家》剧组档案"
author = "《欢迎回家》剧组档案"
release = "1.0"

extensions = ["myst_parser"]

source_suffix = {".md": "markdown", ".rst": "restructuredtext"}

master_doc = "index"
language = "zh_CN"

exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ---------------------------------------------------------------- 主题
html_theme = "pydata_sphinx_theme"
html_static_path = ["_static"]
html_css_files = ["welcome-home.css"]
html_title = "《欢迎回家》档案站"
html_short_title = "欢迎回家"

html_theme_options = {
    "logo": {"text": "ψ = ψ(ψ) · 欢迎回家"},
    "navbar_align": "left",
    "show_toc_level": 2,
    "footer_start": ["copyright"],
    "footer_center": [],
    "footer_end": [],
}

# MyST 设置
myst_enable_extensions = ["colon_fence", "deflist", "strikethrough", "tasklist"]
myst_heading_anchors = 3
