# 023 · 跳过空白字符

## 学习目标

使用 continue 跳过当前一轮。

## 前置知识

先完成第 022 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`continue` 跳到下一轮循环。`char.isspace()` 判断字符是否为空白，包括空格、换行与制表符。

## 任务与约定

完成 `compact(text)`，移除所有空白字符，保留其余字符及顺序。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`compact(" a\tb\nc ")` → `"abc"`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

空白字符不应追加到结果。

</details>

<details>
<summary>提示 2：实现方向</summary>

匹配空白时 continue，其余字符拼接到结果。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
