# 081 · 删除指定数据库任务

## 学习目标

根据受影响记录反馈删除结果。

## 前置知识

先完成第 080 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`DELETE FROM tasks WHERE id = ?` 删除目标记录，cursor.rowcount 表示受影响行数。

## 任务与约定

完成 `delete_task(db, task_id)`，ID 为整数。删除并提交，存在返回 True，不存在返回 False；保留其他任务，不关闭连接。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

删除 1 后再次删除 1 → `False`。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

WHERE 条件不能遗漏。

</details>

<details>
<summary>提示 2：实现方向</summary>

依据受影响行数返回布尔值。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
