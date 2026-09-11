# 076 · 封装任务集合

## 学习目标

组合对象、查询与状态管理。

## 前置知识

先完成第 075 题及其前置练习；本题复用此前学过的知识。

## 先学一点

本题提供 Task 类，集合管理器负责按位置找到任务。位置从 0 开始，不允许 Python 的负数索引行为。

## 任务与约定

保留 Task。实现 `TaskList()`：`add(title)` 创建未完成 Task 并返回从 0 开始的位置；`complete(index)` 将该任务完成，返回 None，非法整数位置抛 IndexError；`pending()` 返回未完成任务的 title 列表，保留添加顺序。空集合返回空列表。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

添加 A、B 后完成位置 0，`pending()` → `["B"]`。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先校验位置，再调用任务的方法。

</details>

<details>
<summary>提示 2：实现方向</summary>

pending 根据 task.done 筛选。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
