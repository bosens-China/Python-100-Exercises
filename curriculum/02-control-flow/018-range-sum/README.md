# 018 · 累计 1 到 n

## 学习目标

使用 for 与累加变量。

## 前置知识

先完成第 017 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`for number in range(1, n + 1):` 依次取得 1 到 n。range 不包含右端点。用 `result = result + number` 更新累计值。

## 任务与约定

完成 `sum_to(n)`，n 是非负整数，返回 1 到 n 的整数和，n 为零返回 0。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`sum_to(4)` → `10`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先把累计值设为 0。

</details>

<details>
<summary>提示 2：实现方向</summary>

range 的终点应为 n + 1。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
