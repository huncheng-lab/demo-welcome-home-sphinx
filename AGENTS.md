# demo-welcome-home-sphinx 智能体入口

> 父级规范：[../../AGENTS.md](../../AGENTS.md)（huncheng-lab 工作区）
> 全局契约：[../../../../AGENTS.md](../../../../AGENTS.md)（SpecWeave）
> 状态：🚧 WIP

## 定位

《欢迎回家》档案站的 Sphinx 静态文档站 demo：Python 3.14 + Sphinx + MyST Markdown，
构建产物可直接发布到 GitHub Pages。本目录是独立 demo，不依赖 SpecWeave 主仓代码。

## 技术栈

| 项 | 值 |
|---|---|
| 语言 | Python 3.14+ |
| 文档引擎 | Sphinx + MyST Markdown |
| 主题 | pydata-sphinx-theme |
| 依赖声明 | `pyproject.toml` 的 `dependency-groups.docs`（无 `requirements.txt`） |
| 发布 | `.github/workflows/docs.yaml` → GitHub Pages |

## 如何运行（Windows PowerShell）

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install --group docs
python -m sphinx -M html docs build
python -m http.server 8000 --directory build/html
```

Linux / macOS 命令见 [README.md](README.md#本地构建)。

## 文件地图

| 路径 | 用途 | 改动注意 |
|---|---|---|
| `docs/conf.py` | Sphinx 唯一配置入口 | 主题、扩展、语言在此修改 |
| `docs/index.md` | 站点首页 | 增删页面时同步 toctree |
| `docs/cast/*.md` | 角色档案 | 直接改内容 |
| `docs/script/*.md` | 分幕剧本 | 直接改内容 |
| `docs/keyart.md`、`docs/relations.md`、`docs/timeline.md` | 剧照、关系、时间线 | 直接改内容 |
| `docs/assets/stills/*.png` | 剧照图片 | 替换同名文件即可，无需改引用 |
| `docs/_static/welcome-home.css` | 配色与样式 | 只改顶部 `--pst-*` 变量 |
| `pyproject.toml` | 依赖与工具配置 | 新依赖只加到 `dependency-groups.docs` |
| `.github/workflows/docs.yaml` | Pages 构建发布 | 改安装/构建命令须同步 README |

## 工作约束

- **独立性**：依赖一律走 PyPI，禁止引用 `apps/`、`projects/` 或 SpecWeave `.agents/` 内的代码。
- **依赖入口唯一**：安装统一用 `pip install --group docs`（pip ≥ 25.1），不再新增 `requirements.txt`。
- **构建产物**：`build/` 为生成目录，不手工编辑、不入库。
- **流程边界**：不新增测试/发版流程；GitHub Pages 发布工作流是唯一例外。
- **提交规范**：遵循 Conventional Commits（`type(scope): subject`），主体使用中文。
