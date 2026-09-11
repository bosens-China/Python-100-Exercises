# 093 · 任务清单：定义数据规则

## 学习目标

为综合项目建立可复用的数据契约。

## 前置知识

先完成第 092 题及其前置练习；本题复用此前学过的知识。

## 先学一点

从此题开始构建任务清单。每题带有独立快照；可以复用自己的实现，也可以从提供的前置代码继续。domain.py 负责规则，main.py 暴露验收入口。

## 任务与约定

在 domain.py 实现 `normalize_title(title)`：必须为字符串，strip 后长度 1–80，否则 ValueError。实现 `new_task(identifier, title)`：ID 类型恰好为 int 且大于零，否则 ValueError；返回仅含 id、规范化 title、done=False 的新字典。保留 main.py 的导入。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`new_task(1, " 学习 ")` → `{"id": 1, "title": "学习", "done": False}`

## 开始编写

编辑 `domain.py`, `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

把标题校验集中在 normalize_title。

</details>

<details>
<summary>提示 2：实现方向</summary>

new_task 调用该函数，避免维护两套规则。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
