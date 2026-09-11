# 077 · 创建任务数据表

## 学习目标

理解表、列和建表语句。

## 前置知识

先完成第 076 题及其前置练习；本题复用此前学过的知识。

## 先学一点

数据库用表保存记录。`db.execute("SQL")` 执行语句。`CREATE TABLE IF NOT EXISTS` 可避免重复建表报错；`INTEGER PRIMARY KEY` 提供整数主键，`TEXT NOT NULL` 要求标题不为空值。测试提供内存数据库连接，不需要安装数据库服务。

## 任务与约定

完成 `create_tasks(db)`，建立 tasks 表：id 为 INTEGER PRIMARY KEY，title 为 TEXT NOT NULL，done 为 INTEGER NOT NULL DEFAULT 0。可重复调用且不清空已有记录，返回 None。不关闭传入连接。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

建表后插入 title 为 A 的记录，应得到整数 id 与默认 done=0。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先写列名与类型。

</details>

<details>
<summary>提示 2：实现方向</summary>

使用 IF NOT EXISTS，禁止先删表再创建。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
