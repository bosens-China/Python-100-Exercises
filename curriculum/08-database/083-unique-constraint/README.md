# 083 · 处理重复用户名

## 学习目标

依靠唯一约束维护一致性。

## 前置知识

先完成第 082 题及其前置练习；本题复用此前学过的知识。

## 先学一点

UNIQUE 约束阻止重复数据，违反约束抛出 sqlite3.IntegrityError。`with db:` 在成功时提交、异常时回滚；捕获异常应在 with 外层。

## 任务与约定

完成 `register(db, name)`。测试已创建 `users(id INTEGER PRIMARY KEY, name TEXT NOT NULL UNIQUE)`；name 是非空字符串，大小写敏感。新增成功提交返回 True，已有同名则回滚并返回 False。连接保持可继续使用。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

连续注册 `Ada`：第一次 True，第二次 False；注册 `ada` 仍为 True。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

不要先删掉旧用户。

</details>

<details>
<summary>提示 2：实现方向</summary>

在参数化插入外捕获 IntegrityError。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
