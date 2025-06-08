# Python-100-Exercises

本项目将经典的 "Python 100 例" 从一个简单的清单，转变成一个结构化、可执行、可测试的完整 Python 项目。它为每一道练习题都创建了独立的 Python 文件，并为绝大多数题目配备了使用 `pytest` 框架的单元测试。

这非常适合 Python 初学者进行系统性的练习，也适合有经验的开发者快速回顾和检验自己的基础知识。

## 项目背景

最初，这 100 道题只是一个 `.md` 文件中的列表。为了让学习过程更加规范和高效，我们启动了这个项目，旨在：

1.  **结构化**：将题目按知识点分门别类，存放在不同的目录中。
2.  **可执行**：为每道题创建可独立运行的 `.py` 文件。
3.  **可测试**：为绝大部分题目编写了基于 `pytest` 的单元测试，确保代码的正确性。
4.  **现代化**：代码遵循现代 Python 风格，包含类型提示、文档字符串等良好实践。

完整的 100 道题目描述、提示和期待结果，请参见文件 **[题目清单.md](题目清单.md)**。

## 项目结构

项目严格按照知识领域划分为七个主要部分：

```
.
├── part_1_basics/            # 基础语法和数据类型 (1-20)
├── part_2_control_flow/      # 控制流 (21-40)
├── part_3_functions/         # 函数 (41-60)
├── part_4_oop/               # 面向对象编程 (61-75)
├── part_5_files_exceptions/  # 文件和异常处理 (76-85)
├── part_6_standard_library/  # 标准库和常用模块 (86-95)
└── part_7_projects/          # 实战项目 (96-100)
```

在每个目录中，您会看到对应的练习文件和测试文件：

- `exercise_NNN.py`: 第 NNN 题的源代码。
- `test_exercise_NNN.py`: 第 NNN 题的单元测试文件。

### 关于部分练习缺少测试文件的说明

有少数练习由于其性质，我们特意没有为其提供自动化单元测试，目的是为了让学习者专注于该练习的核心目标。这些练习包括：

- **交互式学习与观察类:**
  - `exercise_057.py` (文档字符串): 重点在于使用 `help()` 交互式查看文档，而不是测试阶乘函数的实现。
  - `exercise_090.py` (`sys` 模块): 重点在于从真实命令行运行 `python your_script.py arg1 arg2` 并观察 `sys.argv` 的结果。
- **文件生成与验证类:**
  - `exercise_092.py` (`csv` 模块): 核心任务是成功生成一个 CSV 文件，并用 Excel 或文本编辑器打开查看，直观感受其结构。
- **复杂项目与游戏类:**
  - `exercise_099.py` (贪吃蛇游戏): 这是一个复杂的实时交互应用，为其编写单元测试需要对架构进行大量修改，超出了本练习的范畴。我们鼓励您直接运行和体验游戏。
  - `exercise_100.py` (个人联系人管理器): 作为最终的综合项目，它融合了前面学到的多种技能，重点在于设计和实现一个完整流畅的应用。

## 安装与设置 (推荐的标准流程)

为了保证项目依赖的纯净和可复现性，我们强烈推荐使用 Python 虚拟环境。

### 1. 克隆项目

```bash
git clone git@github.com:bosens-China/Python-100-Exercises.git
cd Python-100-Exercises
```

### 2. 创建并激活虚拟环境

在项目根目录执行以下命令来创建一个名为 `.venv` 的虚拟环境：

```bash
python -m venv .venv
```

接着，您需要**激活**这个环境。

- **在 Windows 上 (PowerShell):**

  ```powershell
  .venv\Scripts\Activate.ps1
  ```

  _如果您遇到执行策略问题，请先以管理员身份运行 PowerShell，执行 `Set-ExecutionPolicy Unrestricted -Scope Process`，然后再尝试激活。_

- **在 macOS 和 Linux 上:**
  ```bash
  source .venv/bin/activate
  ```

成功激活后，您会看到终端提示符前面出现了 `(.venv)` 字样。

### 3. 安装依赖

激活虚拟环境后，使用 `requirements.txt` 文件来安装所有必需的依赖包：

```bash
pip install -r requirements.txt
```

这个文件包含了项目正常运行和测试所需的所有第三方库。

## 如何运行与测试

请确保您已经激活了虚拟环境。

### 运行单个练习

您可以直接运行任何一个练习文件来查看其效果：

```bash
# 运行第3题：计算圆的面积
python part_1_basics\exercise_003.py

# 运行第97题：天气查询应用 (需要提供城市作为参数)
python part_7_projects\exercise_097.py "Beijing"
```

### 使用 Pytest 进行测试

本项目采用强大的 `pytest` 框架进行测试。

#### 自动化实时测试 (推荐的工作流)

这是最高效的开发方式。在终端中启动 `pytest-watch`，它会监控您的代码变动，一旦您保存文件，相关的测试就会自动重新运行。

**启动监控:**

```bash
ptw . -- -v
```

- `ptw .` 命令告诉 `pytest-watch` 监控当前目录下的所有文件。
- `-- -v` 是传递给 `pytest` 的参数，`-v` 表示使用详细模式（verbose）输出，结果更清晰。

#### 手动运行测试

- **运行所有测试:**

  ```bash
  pytest -v
  ```

- **运行单个测试文件:**
  ```bash
  # 只测试第1题
  pytest -v part_1_basics\test_exercise_001.py
  ```

## 贡献

欢迎任何形式的贡献！无论是发现了一个 bug，对某个练习有更好的解法，还是想改进测试用例，都请随时提出 Issue 或提交 Pull Request。

## 许可

本项目采用 [MIT 许可](LICENSE)。
