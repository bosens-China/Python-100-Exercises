# 055 · 解析 JSON 配置

## 学习目标

把 JSON 文本转换为 Python 数据。

## 前置知识

先完成第 054 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`import json` 后，`json.loads(text)` 把 JSON 文本解析成字典或列表。JSON 的 true 对应 Python 的 True。

## 任务与约定

完成 `enabled_names(text)`。合法 JSON 文本表示记录列表，每项有 name 字符串与 enabled 布尔值，返回启用记录的 name 列表，保留顺序。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`enabled_names('[ {"name": "提示", "enabled": true} ]')` → `["提示"]`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

先解析再筛选。

</details>

<details>
<summary>提示 2：实现方向</summary>

无需自己切分 JSON 字符串。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
