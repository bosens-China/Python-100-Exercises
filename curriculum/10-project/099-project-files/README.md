# 099 · 任务清单：保存与恢复工作区

## 学习目标

组合存储对象和文件模块。

## 前置知识

先完成第 098 题及其前置练习；本题复用此前学过的知识。

## 先学一点

persistence.py 负责文件读写，Store 负责数据规则。文件仅是练习工作区的虚拟文件；跨浏览器或刷新后的保存由网站另外负责。

## 任务与约定

实现 `save_store(store, path)`：覆盖写入 UTF-8 JSON 文件、返回 None。实现 `load_store(store, path)`：读取文件并通过 import_json 替换数据、返回条数。缺失文件抛 FileNotFoundError，非法内容抛 ValueError，失败不能改变 store。父目录存在。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

保存已完成任务，再加载到新的 Store，应恢复标题、ID 和完成状态。

## 开始编写

编辑 `domain.py`, `store.py`, `persistence.py`, `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

复用 export_json 和 import_json。

</details>

<details>
<summary>提示 2：实现方向</summary>

不要在读取文件前清空 store。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
