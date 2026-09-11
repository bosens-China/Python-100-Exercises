# 091 · 判断当前用户能否修改记录

## 学习目标

区分登录身份与访问权限。

## 前置知识

先完成第 090 题及其前置练习；本题复用此前学过的知识。

## 先学一点

身份回答“是谁”，授权回答“是否允许”。这里直接提供模拟用户字典，不实现登录、令牌或真实身份认证。

## 任务与约定

完成 `can_edit(user, owner_id)`。user 为 None 或包含 id 整数和 role 字符串的字典；owner_id 为整数。未登录返回 False；role 为 admin 或 user.id 等于 owner_id 时返回 True；其他返回 False。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`can_edit({"id": 2, "role": "member"}, 2)` → `True`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先处理 None，再访问字段。

</details>

<details>
<summary>提示 2：实现方向</summary>

管理员身份与所有者匹配任一个满足即可。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
