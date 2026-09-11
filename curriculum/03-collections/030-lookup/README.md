# 030 · 查询字典配置

## 学习目标

认识键值映射与缺省值。

## 前置知识

先完成第 029 题及其前置练习；本题复用此前学过的知识。

## 先学一点

字典如 `{"theme": "dark"}` 把键映射到值。`mapping.get(key, default)` 在键缺失时返回缺省值；已有的空字符串不是缺失。

## 任务与约定

完成 `get_setting(settings, key, default)`，settings 为字符串键和值的字典，返回已有值，否则返回 default 字符串。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`get_setting({"theme": "dark"}, "theme", "light")` → `"dark"`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

判断的是键是否存在。

</details>

<details>
<summary>提示 2：实现方向</summary>

不要把空字符串当成缺失。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
