# demo-welcome-home-sphinx · .agents/

> 父级规范：[../../../AGENTS.md](../../../AGENTS.md)（huncheng-lab 工作区）
> 全局契约：[../../../../../AGENTS.md](../../../../../AGENTS.md)（SpecWeave）
> 本目录是 demo 的最小规范容器，不复制 SpecWeave 全量 `.agents/` 体系。

## 本目录结构

```
.agents/
└── README.md    # 本文件（唯一规范文件）
```

## 规范来源（单一可信源，只引用不复制）

| 层级 | 文件 | 作用 |
|---|---|---|
| SpecWeave | [../../../../../AGENTS.md](../../../../../AGENTS.md) | 全局契约与路由 |
| huncheng-lab | [../../../AGENTS.md](../../../AGENTS.md) | demo 硬约束：命名、状态、三件套、独立性 |
| 本 demo | [../AGENTS.md](../AGENTS.md) | 技术栈、运行方式、文件地图、改动纪律 |
| 使用说明 | [../README.md](../README.md) | 一句话说明、安装/构建命令、内容维护 |

## 本 demo 的落地约定

- 命名：`demo-welcome-home-sphinx`，符合 `demo-<主题>-<技术栈>`
- 依赖：`pyproject.toml` → `dependency-groups.docs`
- 构建：`python -m sphinx -M html docs build`
- 状态：以 `README.md` 顶部 `Status:` 徽章为准
