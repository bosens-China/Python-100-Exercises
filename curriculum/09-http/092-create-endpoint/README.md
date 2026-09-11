# 092 · 组合创建任务接口

## 学习目标

把校验、依赖调用与响应连起来。

## 前置知识

先完成第 091 题及其前置练习；本题复用此前学过的知识。

## 先学一点

传入的 `save(title)` 代表存储依赖。通过传函数，可以在测试中检查调用次数，而不连接外部服务。校验错误和存储故障应区别处理。

## 任务与约定

完成 `create_task(body, save)`。body 和标题规则同第 087 题。不合法返回 `{"status": 400, "body": {"error": "invalid_title"}}`，不得调用 save；合法仅调用一次 save(清理后标题)，save 返回整数 ID；返回 201 与 body 中的 id、title、done=False。save 抛出的异常向上传播，不改成 400。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

输入 `{"title": " A "}` 且 save 返回 7 → `{"status": 201, "body": {"id": 7, "title": "A", "done": False}}`。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先完成校验，再调用依赖。

</details>

<details>
<summary>提示 2：实现方向</summary>

不要用包住整个函数的 except ValueError。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
