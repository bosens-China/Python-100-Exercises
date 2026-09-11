# Python 100 在线练习前端

桌面端学习工作区：分类导航、Markdown 题目与提示、多文件 Python 编辑、示例检查、完整提交、错误反馈，以及浏览器草稿和进度。课程唯一来源为根目录 `curriculum/`，判题逻辑复用 `tools/grader.py`。

## 开发

维护者需要 Node.js 24、pnpm 11.17 和 Python 3.12+。学习者只需浏览器。

```bash
pnpm --dir web install
pnpm --dir web dev
```

`dev` 和 `build` 自动导出题库，并从锁定的 Pyodide 包复制执行资源至 `public/runtime/`。网站图标复用根目录 `image.png`，启动或构建时复制到 `public/favicon.png`。这些生成文件不提交 Git。更新题库或判题内核后重新执行上述命令。没有 CDN 或业务 API 依赖；首次运行按需下载同站点约 15 MB 的 Python 资源，后续使用浏览器 HTTP 缓存。

技术栈：Vite、React、TypeScript、React Compiler、Ant Design、少量 UnoCSS、CodeMirror、Pyodide。Compiler 通过 Vite React 官方模板的 Babel preset 启用；UnoCSS 插件在 React 插件之前。浅色和深色主题默认跟随系统。

## 验证

```bash
pnpm --dir web lint
pnpm --dir web format:check
pnpm --dir web test
pnpm --dir web build
pnpm --dir web exec playwright install chromium
pnpm --dir web test:browser
```

浏览器测试在真实 Worker 中验证 100 道参考实现、100 道起始代码，并通过构建产物验证仓库子路径、编辑、保存、导入导出、重置与异常恢复。参考答案只由测试进程读取，不放入站点导出文件。已有 Chrome 时可以使用 `PLAYWRIGHT_CHANNEL=chrome pnpm --dir web test:browser`。

## 目录职责与 CI

- `curriculum/`：题库唯一来源，每题包含说明、起始文件、参考实现和行为测试。
- `tools/`：课程校验、导出、Python 判题内核与工具回归测试。
- `web/src/`：`pages` 组合页面，`components` 呈现交互，`hooks` 管理 React 状态，`services` 处理课程与进度数据，`runtime` 管理 Worker 和 Python 执行。
- `web/scripts/`：构建前资源准备与子路径验收服务器；`web/test/`：端到端验收。
- `web/public/course.json`、`web/public/runtime/` 和 `web/dist/` 为生成内容，不手动维护、不提交。
- `legacy/` 只用于历史归档，不进入当前构建和默认检查；`docs/` 管理现行决策、未来计划与进行中的发布验收。

`.github/workflows/ci.yml` 在提交到 `main`、向 `main` 发起或更新 PR 时检查 Python 工具回归、100 题参考/起始实现、前端格式和 Lint、Vitest、TypeScript/构建及浏览器验收。固定 Node 24、Python 3.12 和 pnpm 11.17，使用冻结的前端锁文件；失败时保留浏览器诊断产物。

Pages 手动发布复用同一套 CI，只发布这次检查通过的构建产物。普通 CI 仅有仓库读取权限；Pages 写入权限仅授予部署任务。不使用路径过滤，避免文档 PR 的必需检查一直等待。

当前配置已在本地验证，尚未在 GitHub 执行。配置推送后应先确认远端 CI 成功，再把 `Quality checks` 设为 `main` 的必需状态检查。分支保护属于仓库设置，工作流文件本身不会启用它。

工作流复用方式见 [GitHub 官方说明](https://docs.github.com/en/actions/how-tos/reuse-automations/reuse-workflows)。

## GitHub Pages

构建产物是 `web/dist/`。使用相对资源路径和 `#/exercises/001` 哈希路由，可部署在仓库子路径，题目直达链接刷新无需服务器回退规则。

仓库已经提供手动部署工作流 `.github/workflows/pages.yml`。首次发布需由维护者：

1. 将改动推送到 GitHub 默认分支。
2. 在仓库 Settings → Pages 中将 Source 设为 GitHub Actions。
3. 在 Actions 中运行「Deploy Python 100 to Pages」。工作流通过验证后再发布。
4. 用部署返回的地址验收第 001、100 题及直接链接刷新。

当前仅完成本地构建与子路径测试，尚未发布到真实 Pages 地址。

## 执行与保存约定

- 每项测试使用独立临时目录，并清理练习模块；文件与 SQLite 均位于浏览器 Python 工作区。
- 「运行示例」只运行题目的首个行为测试，包含其所需夹具，不记录通关；「提交检查」运行全部测试。逐项展开可查看标准输出与错误位置。
- Python 首次初始化最多等待 90 秒；执行最多 10 秒。停止或超时直接销毁 Worker，下次运行重建。
- 每项标准输出与错误输出分别限 32,000 字符。执行单元用于自学反馈，不承诺恶意代码安全隔离或防作弊。
- 草稿按课程版本保存在 localStorage，输入后 300 毫秒保存，关闭或刷新前尝试立即保存。通过状态绑定实际提交的源码；修改后显示待检查。
- 导入严格校验课程和文件清单，替换前确认。读写存储异常会提示导出备份，不能保证无痕模式或被清理的数据可恢复。
- 当前只验收桌面 Chrome；移动端、账号同步和可信考试不在首版范围内。

实现参考：[React Compiler](https://zh-hans.react.dev/learn/react-compiler/installation)、[Vite Pages 部署](https://vite.dev/guide/static-deploy#github-pages)、[Ant Design](https://ant.design/docs/react/introduce/)、[UnoCSS Vite](https://unocss.dev/integrations/vite)、[Pyodide](https://pyodide.org/en/stable/usage/quickstart.html)。
