---
name: git-step-commit
description: Review Git changes, organize and create coherent commits, manage explicit and learned commit preferences, and safely synchronize and push branches. Use for 提交、按推荐提交、审查提交计划、提交并推送、设置或个性化提交偏好、指定提交语言, or closing supplied GitHub issues through commits.
---

# Git Step Commit

把当前 Git 更改整理成清晰、可审查、可回滚的提交；只有用户要求时才推送。

## 偏好与优先级

提交模式按以下优先级解析：

1. 当前对话中用户最近一次明确指定
2. 当前仓库配置
3. 全局 Git 配置
4. 当前项目的个性化记忆
5. 内置默认

消息语言不使用个性化记忆，优先级仍为当前对话、当前仓库配置、全局 Git 配置、内置默认。

对话偏好在后续请求中继续生效，但不写入 Git 配置；用户重新指定时覆盖。只有用户明确说“仅这次”时才不延续。不要把一次确认某个计划误记为长期偏好。

配置键：

- `git-step-commit.mode`：`default`、`review`、`direct`
- `git-step-commit.language`：`auto` 或合法 BCP 47 标识，如 `zh-CN`、`en`、`ja`

模式含义：

- `review`：先输出审查报告并等待确认
- `direct`：按推荐方案直接提交
- `default`：普通提交走 `review`；用户说“按推荐提交”“直接提交”“无需确认”时走 `direct`

“提交并推送”本身不算用户明确指定模式，也不形成对话偏好；仅当按上述优先级得到的有效模式为 `default` 时，本次按 `direct`（推荐模式）执行。

每次提交前按优先级逐层解析，命中后立即停止，不读取更低优先级的来源：先使用当前对话偏好；否则读取当前仓库配置；仓库配置缺失时读取全局配置；两层配置均缺失时才读取个性化记忆。项目级或全局的 `default`/`auto` 是明确值，会阻止继续回退。无效配置不执行，报告问题与来源。

用户要求设置、查看或删除持久偏好时，只操作 Git 配置，不检查或提交工作树：

- 当前仓库：`git config --local`
- 全局：`git config --global`
- 写入使用 `--replace-all`，删除使用 `--unset-all` 或 `--remove-section`

修改前必须知道作用域，只改用户指定字段，完成后读回验证。读取偏好但未指定作用域时，显示有效值及来源。

## 个性化记忆

个性化记忆是用户选择启用的项目级推断状态，只学习提交模式 `direct`，不写入 Git 配置。使用 `scripts/` 下匹配当前操作系统和 CPU 架构的 `commit-memory-*` 二进制管理；Linux/macOS 首次运行前确保二进制可执行。状态写入 `${XDG_STATE_HOME:-$HOME/.local/state}/git-step-commit`；若设置 `GIT_STEP_COMMIT_STATE_DIR`，则使用该目录。不要手工拼接、改写或读取状态 JSON。

二进制对应关系：

- Windows amd64：`commit-memory-windows-amd64.exe`
- Linux amd64：`commit-memory-linux-amd64`
- Linux arm64：`commit-memory-linux-arm64`
- macOS amd64：`commit-memory-darwin-amd64`
- macOS arm64：`commit-memory-darwin-arm64`

用户要求开启、关闭、查看或忘记个性化记忆时，只执行相应脚本命令，不检查或提交工作树：

```text
<memory-bin> enable
<memory-bin> disable
<memory-bin> status --repo <repo>
<memory-bin> record-direct --repo <repo>
<memory-bin> forget --repo <repo>
```

记忆默认关闭。`disable` 保留已有项目状态但停止读取和学习；`forget` 只删除当前项目的状态。状态缺失、关闭或尚未达到阈值时不产生模式偏好。达到阈值后，模式为 `direct`，来源显示为“本项目个性化记忆”。

一次提交请求结束后，只有同时满足以下条件才运行 `record-direct`，并且一次请求最多记录一次：

- 用户在本次请求中明确说“按推荐提交”“直接提交”或“无需确认”
- 至少一个提交实际成功
- 用户没有说“仅这次”

不要记录对审查计划的确认、仅由先前对话偏好延续的 `direct`、由 Git 配置得到的 `direct`、由“提交并推送”特殊规则得到的 `direct`，或失败及未执行的提交。脚本累计三次合格成功后才学习 `direct`；达到阈值后的 `record-direct` 是无写入的幂等操作，并返回 `recorded: false`。同一次请求内复用已经读取的状态，不重复读取。写入失败不改变已经完成的 Git 结果，应分别准确报告。

## 分析与审查报告

先一次性检查仓库根目录、工作树/暂存区、提交历史、作者历史、当前分支与 upstream，以及两层配置。没有更改时直接说明。

按需阅读 diff 和未跟踪文件；不要覆盖或顺手提交无关修改。按单一意图划分批次，让每个提交可以独立审查和回滚。复用本轮已有验证，否则运行与改动风险相称的测试。

消息语言和格式遵循用户本轮明确要求。语言为 `auto` 时，优先沿用当前 Git 作者的历史；其次沿用仓库主要历史；仍无依据时使用简洁 Conventional Commit，摘要语言跟随当前对话。不要混用不同历史层级的语言和格式，也不要猜测身份或国籍。

凡是输出审查/计划，必须先显示当前有效模式及来源，例如：

```text
当前模式：推荐直提（来源：当前对话）
消息配置：中文 Conventional Commit（来源：作者历史）
验证：<结果或未运行原因>

建议提交：
1. <message>
   - 文件：...
   - 目的：...
```

若有效模式为 `review`，等待用户确认；若为 `direct`，报告可以简短，并继续执行。用户只询问建议或审查时，无论模式为何都不提交。

## 执行提交

每个文件整体属于一个批次时，使用精确 pathspec 暂存并提交，可把多批操作放进一条以 `&&` 连接的命令链。需要拆分同一文件、保留已有暂存内容或意图不清时，逐批检查并使用交互式暂存或临时 index。使用 `git add -p` 后，`git commit` 不得再带 pathspec 或 `--only`，否则会绕过 hunk 选择并提交文件的完整工作区状态。

提交前防止凭据、本地缓存、编辑器文件和意外构建产物进入提交。默认不添加 AI 署名或 `Co-authored-by`。

只有用户明确给出 Issue 编号时才在相关提交 body 中添加 `Closes #123`；不要从 diff 或分支名猜测。不要声称本地提交已经关闭 Issue。

遇到疑似凭据、无法判断归属、必要测试失败、冲突或异常 hook 时停止并说明。不要使用会丢失内容或改写历史的命令，也不要 amend、force push 或交互式 rebase，除非用户明确要求。

## 同步与推送

只有用户明确要求推送时才推送当前分支。目标优先使用用户指定值，其次使用 upstream；没有 upstream 时，仅在 `origin/<当前分支>` 可唯一确定时使用它，否则询问。

普通分支推送前检查进行中的 Git 操作、冲突和工作树。用户仅要求推送时，不得自动暂存、提交或 stash 未提交更改；它们阻碍安全同步时停止并说明。已有远端分支时先 `git pull --rebase` 再普通 `git push`；远端尚无同名分支时用 `git push -u` 建立 upstream。一次重试后仍被拒绝就停止。绝不默认强推。

rebase 冲突时保留现场，检查正在重放的提交和冲突语义。只有意图明确时才合并双方内容、验证并继续；否则让用户选择。不要用 abort、hard reset、checkout 或 clean 绕过冲突。

## 结果

仅根据命令结果报告成功。列出每个提交的短 hash、消息、验证、剩余未提交更改；推送后再说明远程、分支和同步结果。

如果能从实际使用的远程地址可靠得到仓库主页，额外输出一个可点击的 Markdown 链接，例如 `仓库主页：[owner/repo](https://github.com/owner/repo)`：

- 去掉末尾 `.git`
- 把常见 SSH 地址（如 `git@github.com:owner/repo.git`）转换为对应 HTTPS 主页
- 绝不输出 URL 中的凭据
- 本地路径、无法可靠转换或来源不确定时省略链接

提交或推送失败时不要打印成功链接，也不要假设操作已经完成。
