# 034 · 排序成绩副本

## 学习目标

使用 sorted 排序。

## 前置知识

先完成第 033 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`sorted(values)` 返回升序新列表；加 `reverse=True` 得到降序。重复值会保留。

## 任务与约定

完成 `rank_scores(scores)`，输入整数列表，返回降序新列表，不修改输入。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`rank_scores([70, 90, 70])` → `[90, 70, 70]`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

最高分应该排在最前面。

</details>

<details>
<summary>提示 2：实现方向</summary>

sorted 的 reverse 参数可以控制方向。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
