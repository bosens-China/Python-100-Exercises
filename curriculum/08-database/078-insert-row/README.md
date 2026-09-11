# 078 · 插入任务记录

## 学习目标

使用参数化 SQL。

## 前置知识

先完成第 077 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`db.execute("INSERT ... VALUES (?)", (title,))` 将数据与 SQL 分开；单元素元组要有逗号。游标的 lastrowid 是新增记录 ID，`db.commit()` 提交修改。

## 任务与约定

完成 `add_task(db, title)`，连接已有上一题的 tasks 表，title 为字符串。插入未完成任务、提交并返回整数 ID。标题中的引号或 SQL 文本都应按普通数据存储，不关闭连接。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`add_task(db, "阅读")` → 新记录 ID。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

不要用 f 字符串拼接 SQL 数据。

</details>

<details>
<summary>提示 2：实现方向</summary>

执行参数化插入后提交，并返回 lastrowid。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
