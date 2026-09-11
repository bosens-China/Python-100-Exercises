# Python-100-Exercises

![image](../image.png)

![GitHub issues](https://img.shields.io/github/issues/bosens-China/Python-100-Exercises) ![GitHub forks](https://img.shields.io/github/forks/bosens-China/Python-100-Exercises) ![GitHub stars](https://img.shields.io/github/stars/bosens-China/Python-100-Exercises)

这个项目的诞生是因为自己想要转行 AI 方向，此外女朋友对 Python 也有很浓厚的兴趣，但是都说实战是最好的老师，所以就有了这个仓库可以在学习一阶段后通过题目来去对照 APi 和知识点进行复习和练习。

这个仓库包含了 100 道题目，全部都有相关的测试用例，此外还包含了一些最佳工程实践。

## 课程大纲

- 第一部分 (1-40 题): Python 核心与面向对象
  - 掌握变量、控制流、函数、类、继承及错误处理等基础内功。
- 第二部分 (41-50 题): Python 进阶特性
  - 学习文件操作、网络请求、装饰器、高阶函数等实用高级技巧。
- 第三部分 (51-100 题): 后端 API 项目实战
  - 使用 FastAPI，从零到一构建一个带数据库、用户认证和授权的完整 API。

> 关于 `part_4_oop/main.py` 文件
>
> 请注意，从第三部分（练习 51）开始，你将进入一个完整的项目实战阶段。`part_4_oop/main.py` 是这个 FastAPI 应用的主入口文件。后续的很多练习，都需要你在这个文件的基础上，不断地进行修改、添加和重构，就像在真实的工作中一样。它将从一个简单的文件，最终演变成一个功能完备的 Web 应用。

## 快速开始

仅需几步，即可开始你的 Python 学习之旅。

### 第一步：安装 Python

请确保你的系统中已安装 Python (>= 3.8 版本)。可从 [Python 官网](https://www.python.org/downloads/) 下载。

### 第二步：安装 uv

`uv` 是一个现代、极速的 Python 包管理工具。

- macOS / Linux: `curl -LsSf https://astral.sh/uv/install.sh | sh`
- Windows: `powershell -c "irm https://astral.sh/uv/install.ps1 | iex"`

### 第三步：拉取项目

```bash
# 克隆本项目
git clone https://github.com/bosens-China/Python-100-Exercises.git

# 进入项目目录
cd Python-100-Exercises

# 使用uv创建虚拟环境
uv venv

# 激活虚拟环境
# macOS / Linux: source .venv/bin/activate
# Windows: .venv\Scripts\activate

# 安装所有依赖
uv pip install -r requirements.txt
```

环境配置完成。

### 运行测试用例

为了获得实时反馈，当你完成一道题目后（例如第 5 题 `exercise_005.py`），我们推荐使用 `uv run` 来运行测试。这种方式可以确保你始终使用虚拟环境中正确的工具版本：

```bash
uv run pytest part_1_basics/test_exercise_005.py
```

这个命令会精准地只测试你当前关心的题目。后续你会在终端看到测试是通过还是失败。

## 参与贡献

相关的题目全部通过 AI 生成，所以在这个过程中肯定会有不完善甚至错误的地方，欢迎通过下面的方式来进行反馈，当然如果你完成一道题目或者遇到问题也可以在 issues 来搜索查看其他人的解题思路。

- 提交答案: 完成题目后，欢迎通过 [答案提交 Issue](https://github.com/bosens-China/Python-100-Exercises/issues/new?assignees=&labels=答案,待审核&template=answer_submission.yml&title=[答案提交]+题目+) 分享你的解法。
- 反馈与建议: 如有任何问题或建议，请通过 [意见反馈 Issue](https://github.com/bosens-China/Python-100-Exercises/issues/new?assignees=&labels=反馈,建议&template=feedback.yml&title=[反馈/建议]+) 进行反馈。
