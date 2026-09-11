# 057 · 读取 CSV 人员表

## 学习目标

正确处理带引号的逗号。

## 前置知识

先完成第 056 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`csv.DictReader(file)` 按表头生成字典。打开 CSV 时使用 `newline=""`；字段中有逗号时标准库会处理引号。

## 任务与约定

完成 `read_people(path)`，UTF-8 CSV 表头为 name,age，age 均为合法非负整数字符串。返回 name 字符串和 age 整数的字典列表。只有表头时返回空列表。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

内容 `name,age\nAda,20\n` → `[{"name": "Ada", "age": 20}]`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

不能简单按逗号 split。

</details>

<details>
<summary>提示 2：实现方向</summary>

DictReader 的 age 仍是字符串，需要 int。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
