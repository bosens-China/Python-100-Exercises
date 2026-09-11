# 075 · 表示一条任务

## 学习目标

为对象提供状态切换与序列化。

## 前置知识

先完成第 074 题及其前置练习；本题复用此前学过的知识。

## 先学一点

对象用于保存状态，字典用于传递数据。转换时创建新的字典，避免调用者影响对象本身。

## 任务与约定

实现 `Task(title)`，title 是字符串，done 初始为 False；`complete()` 设为 True，返回 None，多次调用保持完成；`to_dict()` 返回 title、done 两个键的新字典。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`Task("学习").to_dict()` → `{"title": "学习", "done": False}`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

complete 应设置状态，不是反转状态。

</details>

<details>
<summary>提示 2：实现方向</summary>

to_dict 每次创建新字典。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
