# 080 · 完成指定数据库任务

## 学习目标

精确更新目标记录。

## 前置知识

先完成第 079 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`UPDATE tasks SET done = 1 WHERE id = ?` 只修改指定记录。更新前查询是否存在，可明确返回 True 或 False。

## 任务与约定

完成 `complete_task(db, task_id)`，ID 为整数。存在则将 done 设为 1，提交并返回 True（已经完成也返回 True）；不存在返回 False。不得影响其他任务，不关闭连接。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`complete_task(db, 1)` → `True`，再次调用仍为 True。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

完成是设置为 1，不是切换。

</details>

<details>
<summary>提示 2：实现方向</summary>

检查不存在与已经完成的区别。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
