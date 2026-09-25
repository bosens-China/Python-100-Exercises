# Python 100：初级工程师练习

100 道循序渐进的 Python 练习，最低支持 Python 3.12。前半段练基础与标准库；后半段持续完成一个待办事项 API 项目。每题有独立的题目文件和测试文件，题目源码保留待实现部分。

## 学习路线

| 题号 | 模块 | 形式 |
| --- | --- | --- |
| 001–010 | 语法与函数入门 | 独立练习 |
| 011–020 | 字符串与容器 | 独立练习 |
| 021–030 | 控制流与数据处理 | 独立练习 |
| 031–035 | 面向对象 | 独立练习 |
| 036–040 | 文件与综合练习 | 独立练习 |
| 041–050 | 网络、日期与常用工具 | 独立练习 |
| 051–060 | Web API 起步 | 连续项目 |
| 061–072 | 数据库与项目结构 | 连续项目 |
| 073–085 | 认证与授权 | 连续项目 |
| 086–100 | 交付与工程实践 | 项目题与独立练习 |

51–95 题以及 99–100 题围绕 `part_4_oop/main.py` 逐步扩展项目。它们共享代码状态，应按顺序完成。96–98 题重新回到可独立运行的工程练习。

## 在浏览器做题

`web/` 是 React + Vite + React Compiler + Ant Design + UnoCSS 的静态应用，可部署到 GitHub Pages。题目直接从仓库中的 `exercise_*.py` 与 `test_exercise_*.py` 构建，避免维护第二份题库。

- 001–050、096–098：在浏览器写代码并运行对应测试。
- 连续项目题：在网页阅读要求、保存草稿与进度，在本地仓库修改项目并运行测试。
- 草稿与完成状态保存在当前浏览器的 LocalStorage 中，不会自动跨设备同步。

本地启动网页：

```bash
cd web
npm ci
npm run dev
```

生产构建：`npm run build`。GitHub Pages 构建流程位于 `.github/workflows/pages.yml`；仓库管理员需要在 **Settings → Pages → Build and deployment** 里选择 **GitHub Actions**。构建产物位于 `web/dist`，站点路径为 `/Python-100-Exercises/`。

## 在本地做题

安装 Python 3.12 或更新版本、[uv](https://docs.astral.sh/uv/) 后，在仓库根目录运行：

```bash
uv venv --python 3.12
uv pip install -r requirements.txt
uv run pytest part_1_basics/test_exercise_005.py -q
```

Windows 使用 `.venv\Scripts\activate`、macOS/Linux 使用 `source .venv/bin/activate` 可激活环境。完成其他题目时，把测试文件路径替换为对应的 `test_exercise_NNN.py`。题目源码尚未完成，所以运行整套测试会出现预期的失败；连续项目题还依赖前面的实现和新增文件。

## 反馈

- [提交解法](https://github.com/bosens-China/Python-100-Exercises/issues/new?template=answer_submission.yml)
- [报告题目或测试问题](https://github.com/bosens-China/Python-100-Exercises/issues/new?template=feedback.yml)
