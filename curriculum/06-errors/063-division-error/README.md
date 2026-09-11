# 063 · 区分错误和正常结果

## 学习目标

处理特定运行异常。

## 前置知识

先完成第 062 题及其前置练习；本题复用此前学过的知识。

## 先学一点

除数为零会抛出 ZeroDivisionError。异常处理分支可以返回约定结构，让调用者知道失败原因。

## 任务与约定

完成 `divide_result(a, b)`，输入两个整数，成功返回 `{"ok": True, "value": a / b}`；除数为零返回 `{"ok": False, "error": "division_by_zero"}`，不返回额外键。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`divide_result(5, 2)` → `{"ok": True, "value": 2.5}`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

只处理除零错误。

</details>

<details>
<summary>提示 2：实现方向</summary>

成功结果为普通除法，不要截断小数。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
