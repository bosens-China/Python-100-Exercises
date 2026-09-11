# 050 · 组织一份统计报告

## 学习目标

综合函数拆分与模块复用。

## 前置知识

先完成第 049 题及其前置练习；本题复用此前学过的知识。

## 先学一点

一个模块负责计算，入口模块负责组织结果。模块职责清楚后，各部分可以独立测试。

## 任务与约定

在 `stats.py` 实现 `total(numbers)`（总和）与 `mean(numbers)`（均值，空列表为 None）；在 `main.py` 实现 `summarize(numbers)`，返回 count、total、mean 三个键。输入是整数列表。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`summarize([2, 4])` → `{"count": 2, "total": 6, "mean": 3.0}`

## 开始编写

编辑 `stats.py`, `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先验证计算模块，再组织字典。

</details>

<details>
<summary>提示 2：实现方向</summary>

主入口调用导入的 total 和 mean。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
