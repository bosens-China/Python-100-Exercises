# 067 · 为免运费规则补测试

## 学习目标

主动编写断言识别错误实现。

## 前置知识

先完成第 066 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`assert actual == expected` 在条件不成立时抛出 AssertionError。好的测试同时覆盖边界两侧；不能把参考公式重新写进被测函数。

## 任务与约定

实现 `check_shipping(shipping)`，shipping 是待检查的单参数函数。规则：订单金额为非负整数分，至少 9900 分返回运费 0，否则返回 800。你的函数调用 shipping 并用 assert 检查；正确实现应正常结束并返回 None。必须识别把边界写成 >、始终免运费、始终收 800 的错误实现。不要捕获自己的断言错误。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

对正确 shipping 调用 `check_shipping(shipping)` → `None`；对始终返回 0 的 shipping 抛出 `AssertionError`。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

选择 0、9899、9900、超过边界的金额。

</details>

<details>
<summary>提示 2：实现方向</summary>

分别断言边界两侧的具体费用。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
