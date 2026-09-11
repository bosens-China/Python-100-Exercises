# 090 · 按完成状态筛选接口结果

## 学习目标

解析布尔查询值。

## 前置知识

先完成第 089 题及其前置练习；本题复用此前学过的知识。

## 先学一点

字符串 `"false"` 本身是非空字符串，bool("false") 仍为 True；查询参数必须按明确字符串规则转换。

## 任务与约定

完成 `filter_tasks(tasks, completed=None)`。tasks 各项有 id 整数、title 字符串和 done 布尔值。completed 为 None 时返回全部，`"true"` 返回完成任务，`"false"` 返回未完成任务；其他值抛 ValueError。返回新列表及记录副本，保留顺序。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

一条 done=False 的任务，在 completed="false" 时保留。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

不能直接 bool(completed)。

</details>

<details>
<summary>提示 2：实现方向</summary>

先解析选项，再筛选并复制字典。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
