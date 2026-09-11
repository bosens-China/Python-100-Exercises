# 044 · 把处理函数当作参数

## 学习目标

调用传入的函数。

## 前置知识

先完成第 043 题及其前置练习；本题复用此前学过的知识。

## 先学一点

函数本身也可以作为值传递。`transform(value)` 调用传入的函数；`lambda x: x * 2` 是一个简短的函数表达式。

## 任务与约定

完成 `transform_all(items, transform)`，对整数列表的每个元素调用 transform，返回结果列表，顺序不变；空列表不调用 transform。transform 保证可接受一个整数。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`transform_all([1, 2], lambda x: x * 2)` → `[2, 4]`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

不要把处理逻辑写死为某一种变换。

</details>

<details>
<summary>提示 2：实现方向</summary>

循环中 append(transform(item))。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
