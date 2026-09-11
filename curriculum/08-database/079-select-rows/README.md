# 079 · 查询未完成任务

## 学习目标

使用 WHERE 与 ORDER BY。

## 前置知识

先完成第 078 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`SELECT id, title FROM tasks WHERE done = 0 ORDER BY id` 筛选并排序；游标的 fetchall() 返回由元组组成的列表。

## 任务与约定

完成 `pending_tasks(db)`，连接已有 tasks 表，返回未完成任务的 `(id, title)` 元组列表，按 id 升序。没有匹配则空列表，不修改数据。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

A 未完成、B 已完成时，只返回 A 的 ID 和标题。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

查询列顺序决定元组顺序。

</details>

<details>
<summary>提示 2：实现方向</summary>

显式 ORDER BY，不依赖数据库默认顺序。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
