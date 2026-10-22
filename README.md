# 《欢迎回家》档案站 · Sphinx 版

Status: 🚧 WIP

45 分钟短剧《欢迎回家》(WELCOME HOME, ψ = ψ(ψ)) 的配套档案站，从 React 单页应用迁移为
**Python + Sphinx + MyST Markdown** 静态文档站，可直接发布到 GitHub Pages。

## 本地构建

环境要求：Python 3.14+、pip 25.1+（依赖组 `--group` 支持）。

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install --group docs    # 依赖声明见 pyproject.toml
make html                   # 产物在 build/html/
make serve                  # 构建并在 8000 端口预览
```

### Windows（PowerShell）

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install --group docs    # 依赖声明见 pyproject.toml
python -m sphinx -M html docs build        # 产物在 build/html/
python -m http.server 8000 --directory build/html   # 本地预览
```

## 发布到 GitHub Pages

1. 本仓库 push 到 main 分支（源码进 main）。
2. 仓库 Settings → Pages → Build and deployment 选 **GitHub Actions**。
3. push 到 main 后，`.github/workflows/docs.yaml` 自动用 Python 3.14 构建并把
   `build/html` 发布为站点。

## 内容维护

- 依赖声明在 `pyproject.toml` 的 `dependency-groups.docs`（不再维护 `requirements.txt`）。
- 角色档案改 `docs/cast/*.md`；拍摄脚本改 `docs/script/*.md`。
- 剧照替换 `docs/assets/stills/*.png`，文件名不变则无需改引用。
- 配色只动 `docs/_static/welcome-home.css` 顶部的 `--pst-*` 变量。

## 与原 React 站的差异（已知降级）

- key art 悬停标注 ↔ 侧栏滚动 spy 的联动交互无法还原，Sphinx 静态版为图文阅读式呈现。
- 强调色由 Tailwind class 映射改为 CSS 变量 + 内联色值。
- 关系网图谱由 SVG 画布改为表格 + 列表呈现。
