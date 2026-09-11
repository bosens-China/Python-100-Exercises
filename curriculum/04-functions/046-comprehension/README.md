# 046 · 提取启用用户

## 学习目标

认识列表推导式。

## 前置知识

先完成第 045 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`[row["name"] for row in rows if row["active"]]` 把遍历、条件和结果表达式写在一起；普通循环也是有效解法。

## 任务与约定

完成 `active_names(users)`，每条字典有 name 字符串与 active 布尔值，返回 active 为 True 的姓名，保留顺序与重名。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`active_names([{"name": "Ada", "active": True}])` → `["Ada"]`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先按 active 筛选，再取 name。

</details>

<details>
<summary>提示 2：实现方向</summary>

可以用推导式，也可以复用普通循环。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
