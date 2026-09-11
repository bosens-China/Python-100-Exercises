# 069 · 创建独立计数器

## 学习目标

认识类、实例和 self。

## 前置知识

先完成第 068 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`class Counter:` 定义一类对象。`__init__` 在创建时初始化，`self.value` 保存当前实例的数据；方法第一个参数 self 表示这个实例。

## 任务与约定

实现 `Counter(start=0)`，start 为整数。value 初值为 start；`increment()` 加一并返回新值；不同实例独立。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`Counter(2).increment()` → `3`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

把 value 放在 self 上。

</details>

<details>
<summary>提示 2：实现方向</summary>

increment 更新并返回 self.value。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
