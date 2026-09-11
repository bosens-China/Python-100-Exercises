# 048 · 从另一个文件导入函数

## 学习目标

在两份文件之间组织代码。

## 前置知识

先完成第 047 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`from pricing import subtotal` 导入同目录 pricing.py 的函数。编辑器需要保留两份文件，main.py 是测试入口。

## 任务与约定

在 `pricing.py` 实现 `subtotal(price, quantity)` 返回非负整数乘积；在 `main.py` 实现 `checkout(price, quantity, fee)`，使用该函数并加非负整数运费 fee。两个函数都可调用。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`checkout(100, 2, 80)` → `280`

## 开始编写

编辑 `pricing.py`, `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先完成 pricing.py，再导入它。

</details>

<details>
<summary>提示 2：实现方向</summary>

不要在 main.py 中复制另一份 subtotal。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
