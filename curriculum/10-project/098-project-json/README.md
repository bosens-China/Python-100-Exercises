# 098 · 任务清单：安全导入与导出

## 学习目标

验证完整数据后再替换状态。

## 前置知识

先完成第 097 题及其前置练习；本题复用此前学过的知识。

## 先学一点

导入时先构造临时字典，全部验证成功后再替换内部数据；这样中途发现坏数据不会丢掉已有任务。

## 任务与约定

实现 `Store.export_json()`，返回按 ID 升序排列的任务列表 JSON 字符串。实现 `import_json(text)`：text 为字符串，必须是 JSON 列表，每条恰好含 id、title、done；ID/标题规则同 domain，done 类型恰好为 bool，ID 不重复。成功整体替换、规范化标题，下一 ID 设为最大导入 ID 加 1（空列表为 1），返回导入条数。任何非法数据抛 ValueError 且原数据及下一 ID 保持不变。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

导入 `[{"id": 7, "title": " A ", "done": true}]` 后添加 B，B 的 ID 为 8。

## 开始编写

编辑 `domain.py`, `store.py`, `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

使用临时 tasks，最后一次性赋值。

</details>

<details>
<summary>提示 2：实现方向</summary>

不能边解析边清空或更新现有字典。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
