# 061 · 处理无效整数输入

## 学习目标

捕获指定类型的异常。

## 前置知识

先完成第 060 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`try` 中执行可能失败的代码；`except ValueError:` 只处理数值格式错误。不要用笼统的 except 吞掉所有错误。

## 任务与约定

完成 `parse_int(text)`。text 为字符串；能被 int 转换时返回整数，否则捕获 ValueError 并返回 None。保留 int 对首尾空格和正负号的行为。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`parse_int("abc")` → `None`；`parse_int(" -2 ")` → `-2`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

把 int 调用放进 try。

</details>

<details>
<summary>提示 2：实现方向</summary>

只捕获 ValueError，错误时返回 None。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
