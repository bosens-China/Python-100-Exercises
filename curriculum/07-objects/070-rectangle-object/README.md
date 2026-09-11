# 070 · 封装矩形尺寸

## 学习目标

从实例状态计算结果。

## 前置知识

先完成第 069 题及其前置练习；本题复用此前学过的知识。

## 先学一点

方法通过 self 读取构造时保存的值。构造阶段可以复用前面学过的 ValueError 校验。

## 任务与约定

实现 `Rectangle(width, height)`，参数保证为整数；任一边为负数抛出 ValueError。保存 width、height 属性；`area()` 返回面积，`perimeter()` 返回两边和的两倍。零边长合法。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`Rectangle(3, 4).perimeter()` → `14`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先校验，再保存属性。

</details>

<details>
<summary>提示 2：实现方向</summary>

两个方法复用同一份尺寸。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
