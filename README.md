# Python 100：从零到项目

面向零基础与转行学习者的 Python 练习课程。通过 **10 个章节、100 道渐进练习**，从第一条返回语句学到多文件任务清单项目。

在浏览器里读题、写代码、查看检查结果，逐步练习初级开发中的业务实现、数据处理、测试与调试。

[课程目录](./curriculum/README.md) · [贡献指南](./docs/authoring.md) · [开发与部署](./web/README.md) · [反馈问题](https://github.com/bosens-China/Python-100-Exercises/issues/new/choose)

## 开始学习

**当前状态：题库和桌面端在线工作区已实现，GitHub Pages 待发布。** 现在可以从[课程目录](./curriculum/README.md)阅读题目。网站发布后，学习者打开浏览器即可做题，无需安装 Python 或使用终端。

- 仓库地址：[bosens-China/Python-100-Exercises](https://github.com/bosens-China/Python-100-Exercises)
- 网站预留地址：[Python 100 在线练习](https://bosens-china.github.io/Python-100-Exercises/)（待发布）

## 你可以在这里做什么

- **循序渐进地学**：每题都有知识铺垫、明确约定、示例和两层提示。
- **在线编写 Python**：语法高亮、基础代码补全、自动缩进和多文件编辑。
- **获得具体反馈**：运行示例、提交完整检查，查看逐项结果和错误位置。
- **保留学习进度**：自动保存当前浏览器中的代码，支持导入导出和重置。
- **完成一个小项目**：逐步实现任务清单的校验、存储、查询和接口逻辑。

首版面向桌面浏览器，支持深浅色主题。学习记录保存在当前浏览器中；清理数据或更换设备前，请先导出备份。

## 学习路线

题目按知识依赖排列，建议从第 001 题开始。

| 题号 | 章节 | 学习目标 |
| --- | --- | --- |
| 001–012 | [基础语法与数据类型](./curriculum/01-basics/README.md) | 读懂数值、字符串和布尔值，用表达式返回计算结果。 |
| 013–024 | [条件判断与循环](./curriculum/02-control-flow/README.md) | 把业务规则写成分支，使用循环处理重复任务。 |
| 025–038 | [常用数据结构](./curriculum/03-collections/README.md) | 用列表、字典和集合组织、查询和汇总数据。 |
| 039–050 | [函数与代码组织](./curriculum/04-functions/README.md) | 设计函数契约、复用逻辑，并拆分简单模块。 |
| 051–060 | [文件与数据处理](./curriculum/05-files/README.md) | 在练习工作区处理文本、JSON 和 CSV。 |
| 061–068 | [异常处理与调试](./curriculum/06-errors/README.md) | 识别错误边界、阅读失败信息并修复业务缺陷。 |
| 069–076 | [类与对象](./curriculum/07-objects/README.md) | 封装独立状态，通过组合与基本继承复用行为。 |
| 077–084 | [数据库基础](./curriculum/08-database/README.md) | 在内存 SQLite 中练习 SQL、约束和事务。 |
| 085–092 | [HTTP 与接口逻辑](./curriculum/09-http/README.md) | 通过模拟请求响应练习接口业务，不启动真实服务器。 |
| 093–100 | [综合项目：任务清单](./curriculum/10-project/README.md) | 逐步实现任务清单的数据校验、存储、查询和接口。 |

文件题使用独立练习工作区，数据库题使用内存 SQLite。HTTP 题通过模拟请求响应练习业务逻辑。后期项目每题都有独立起始文件，可以单独学习和检查。

## 每道题怎么练

1. 阅读「先学一点」和「任务与约定」，弄清输入和预期结果。
2. 在起始代码中完成实现，先运行示例，再提交完整检查。
3. 根据失败反馈修改代码；遇到困难时逐层展开提示。
4. 通过后继续下一题，尝试说明自己的解法为什么成立。

运行示例只检查部分行为；提交全部通过后才记录完成。修改已通过的代码后，当前版本需要重新检查。

每题的 `solution/` 提供参考实现。测试按行为验收，允许不同解法。完成课程表示通过了已覆盖的要求，不等同于就业或职业资格保证。

## 实现方式

前端使用 **Vite + React + TypeScript**，开启 React Compiler。组件以 Ant Design 为主，配合少量 UnoCSS；编辑器使用 CodeMirror。

Python 通过 **Pyodide 在 Web Worker 中运行**，复用仓库的判题内核。全部题型支持浏览器检查，可用 GitHub Pages 静态托管，无需判题后端。运行支持停止、超时处理和失败重试。

100 道参考实现已通过浏览器内的 329 项检查，100 份起始代码均未被误判通过。实时语法错误标记与中文错误解释属于[后续计划](./docs/plans/editor-feedback/PRD.md)。

## 参与开发

以下命令面向维护者。需要 Node.js 24、pnpm 11.17 和 Python 3.12+。

```bash
# 安装依赖并启动前端
pnpm --dir web install
pnpm --dir web dev
```

```bash
# 校验题库结构与参考实现
python -m tools.course validate
python -m tools.course check

# 运行判题工具的回归测试
python -m pip install -r requirements.txt
python -m pytest -q
```

完整的前端检查、浏览器测试和部署步骤见[前端说明](./web/README.md)。CI 已配置为检查 PR 与 main 推送；远端首次执行和 Pages 发布待完成。

| 目录 | 内容 |
| --- | --- |
| [`curriculum/`](./curriculum/README.md) | 课程目录、题目、起始代码、参考实现与测试 |
| [`tools/`](./tools/) | 题库校验、导出和 Python 判题内核 |
| [`web/`](./web/README.md) | 在线练习前端与浏览器验收 |
| [`docs/`](./docs/index.md) | 产品决策、贡献规范和后续计划 |
| [`legacy/`](./legacy/README.md) | 旧版题库归档，不参与当前构建和默认检查 |

## 贡献与反馈

欢迎改进题目说明、补充行为测试，或报告编辑器和判题问题。开始前请阅读[题库作者说明](./docs/authoring.md)。

提交 Issue 时，请注明课程版本、题号、相关代码与实际结果。当前课程版本为 `python-100-v2`；旧版为 `legacy-v1`，同号题的内容可能不同。

## 许可证

本项目采用 [MIT License](./LICENSE)。
