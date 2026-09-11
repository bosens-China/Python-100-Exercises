# 100 · 任务清单：完成在线业务闭环

## 学习目标

把多文件项目接入模拟接口并回归已有能力。

## 前置知识

先完成第 099 题及其前置练习；本题复用此前学过的知识。

## 先学一点

最后一步把 domain、store、persistence 和 api 组合起来。模拟请求只是函数调用，测试可重复完成创建、查询、完成、保存恢复和删除，无网络依赖。

## 任务与约定

在 api.py 实现 `handle(store, method, path, body=None)`，method 与 path 保证为字符串，方法用大写。返回仅含 status、body 的字典：

- `GET /tasks`：200，body 为全部任务列表。
- `POST /tasks`：body 必须为字典，title 遵循 domain 规则；成功 201，body 为新记录。无效返回 400，body 为 `{"error": "invalid_title"}`，不创建记录。额外字段忽略。
- `/tasks/<id>`：id 是表示正整数的 ASCII 数字串，允许前导零；无尾部斜杠或查询串。GET 返回 200 与记录；PATCH 仅接受字典且 done 值为 True，返回 200 与已完成记录，其他 body 返回 400 和 `{"error": "invalid_done"}`；DELETE 返回 204 与 None。
- 合法路径不支持的方法：405 和 `{"error": "method_not_allowed"}`，先于查找记录处理。
- 不匹配路径，或支持的方法对应任务不存在：404 和 `{"error": "not_found"}`，先于 PATCH 的 body 校验处理。
- 保留前面全部行为，失败请求不改变记录，返回记录不可用于修改内部状态。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

POST 创建 A → GET 查询 → PATCH 完成 → 保存并恢复 → DELETE 删除 → GET 返回 404。

## 开始编写

编辑 `domain.py`, `store.py`, `persistence.py`, `api.py`, `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先分集合路径与单任务路径，再分方法。

</details>

<details>
<summary>提示 2：实现方向</summary>

复用 Store 的方法，先校验再变更。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
