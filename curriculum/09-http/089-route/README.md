# 089 · 分发模拟请求

## 学习目标

区分路径不存在与方法不支持。

## 前置知识

先完成第 088 题及其前置练习；本题复用此前学过的知识。

## 先学一点

404 表示路径不存在；405 表示已知路径不支持该方法。本题方法使用大写字符串，响应只用 status 与 body 两个键表示。

## 任务与约定

完成 `route(method, path)`。仅有 `/health` 路径：GET 返回 `{"status": 200, "body": {"ok": True}}`；该路径其他方法返回 405 与 `{"error": "method_not_allowed"}`；其他路径任何方法返回 404 与 `{"error": "not_found"}`。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`route("GET", "/health")` → `{"status": 200, "body": {"ok": True}}`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先判断路径是否存在。

</details>

<details>
<summary>提示 2：实现方向</summary>

本题不执行网络请求。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
