# 027 · 筛选正数

## 学习目标

用 append 收集筛选结果。

## 前置知识

先完成第 026 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`result = []` 创建空列表，`result.append(value)` 向末尾加入一个值。

## 任务与约定

完成 `positive_numbers(numbers)`，输入整数列表，返回严格大于零的数，保留原顺序与重复项。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`positive_numbers([-1, 2, 0, 2])` → `[2, 2]`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

逐项判断是否大于零。

</details>

<details>
<summary>提示 2：实现方向</summary>

零不属于正数。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
