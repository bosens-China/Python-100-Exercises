# 041 · 拆分价格计算

## 学习目标

让一个函数调用另一个函数。

## 前置知识

先完成第 040 题及其前置练习；本题复用此前学过的知识。

## 先学一点

函数可以调用本模块中已经定义的函数。先把单件规则写清楚，再在订单函数中复用。

## 任务与约定

实现 `line_total(price, quantity)` 和 `cart_total(items)`。前者返回两个非负整数的乘积；后者汇总含 price、quantity 字段的记录列表，空列表为 0。两者均需可独立调用。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`line_total(100, 3)` → `300`；`cart_total([])` → `0`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先解决一行的小问题。

</details>

<details>
<summary>提示 2：实现方向</summary>

cart_total 遍历各项并调用 line_total。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
