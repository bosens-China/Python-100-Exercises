# 085 · 构造模拟响应

## 学习目标

理解状态码与响应体。

## 前置知识

先完成第 084 题及其前置练习；本题复用此前学过的知识。

## 先学一点

HTTP 响应包含状态码、头和响应体。这里用字典表示它们，供在线练习调用，不启动 Web 服务。200 表示成功，400 表示请求有误。

## 任务与约定

完成 `response(status, body)`，status 是整数，body 是字符串键到 JSON 标量的字典。返回 status、headers、body 三个键；headers 固定为 `{"Content-Type": "application/json"}`，body 为输入副本。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`response(200, {"ok": True})` → `{"status": 200, "headers": {"Content-Type": "application/json"}, "body": {"ok": True}}`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

按约定构造三部分。

</details>

<details>
<summary>提示 2：实现方向</summary>

复制 body，避免调用者修改输入。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
