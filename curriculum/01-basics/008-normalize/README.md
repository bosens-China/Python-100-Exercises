# 008 · 整理用户输入

## 学习目标

调用字符串方法。

## 前置知识

先完成第 007 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`text.strip()` 去掉首尾空白，`text.lower()` 转成小写。方法可连续调用，例如 `text.strip().lower()`。

## 任务与约定

完成 `normalize(text)`，输入字符串，移除首尾空白并将英文字母转小写，保留内部空格。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`normalize("  Py Thon  ")` → `"py thon"`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先清理两端，再统一大小写。

</details>

<details>
<summary>提示 2：实现方向</summary>

strip 不会删除中间空格。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
