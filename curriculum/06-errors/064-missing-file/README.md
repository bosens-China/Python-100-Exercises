# 064 · 给缺失文件提供默认内容

## 学习目标

避免把所有文件错误都视为不存在。

## 前置知识

先完成第 063 题及其前置练习；本题复用此前学过的知识。

## 先学一点

文件不存在时抛出 FileNotFoundError；路径指向目录则属于另一种错误。只捕获你能按约定处理的异常。

## 任务与约定

完成 `read_or_default(path, default="")`，读取 UTF-8 文件；仅当文件不存在时返回 default。其他读取错误继续抛出。文件为空时返回空字符串，不用 default。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`read_or_default("missing.txt", "新建")` → `"新建"`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

只捕获 FileNotFoundError。

</details>

<details>
<summary>提示 2：实现方向</summary>

不要因读到空字符串就返回默认值。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
