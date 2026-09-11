# 095 · 任务清单：查询与隔离

## 学习目标

返回有序、可安全使用的数据。

## 前置知识

先完成第 094 题及其前置练习；本题复用此前学过的知识。

## 先学一点

查询应返回副本，保证 UI 修改展示数据不会改变存储。done=None 表示不筛选；False 则是明确筛选未完成。

## 任务与约定

在提供的 Store 基础上实现 `list(done=None)`，只接受 None 或类型恰好为 bool 的筛选值，其他抛 ValueError。返回按 ID 升序的记录副本列表。创建逻辑保持不变。当前新任务都未完成，因此 done=True 得到空列表。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

添加 A、B 后 `list(False)` 返回两条记录，`list(True)` → `[]`。

## 开始编写

编辑 `domain.py`, `store.py`, `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

不要用 if done 判断是否启用筛选。

</details>

<details>
<summary>提示 2：实现方向</summary>

逐条 copy，不只复制外层列表。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
