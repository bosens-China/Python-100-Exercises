# 040 · 用参数控制格式

## 学习目标

理解关键字参数与默认行为。

## 前置知识

先完成第 039 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`format_name("Ada", uppercase=True)` 按参数名指定选项。False 是默认开关值，可在函数内分支处理。

## 任务与约定

完成 `format_name(name, uppercase=False)`，先去掉首尾空白；uppercase 为 True 时将结果转大写，否则保留原大小写。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`format_name(" Ada ", uppercase=True)` → `"ADA"`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

清理空白是两种情况共有的步骤。

</details>

<details>
<summary>提示 2：实现方向</summary>

不要在默认分支强行转成小写。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
