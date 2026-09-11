# 074 · 扩展会员折扣

## 学习目标

理解基本继承与方法覆盖。

## 前置知识

先完成第 073 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`class MemberCustomer(Customer):` 继承已有构造函数，可以只重写价格计算方法。继承用于稳定的共同契约，不必为每个差异都创建类。

## 任务与约定

保留提供的 `Customer(name)`，其 `payable(amount)` 返回原金额。实现子类 `MemberCustomer`，沿用 name 属性，重写 payable：返回非负整数分金额的九折，向下取整。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`MemberCustomer("Ada").payable(105)` → `94`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

子类可以沿用父类的 __init__。

</details>

<details>
<summary>提示 2：实现方向</summary>

使用整数计算 amount * 9 // 10。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
