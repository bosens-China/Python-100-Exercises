# 056 · 保存 JSON 数据

## 学习目标

序列化数据并验证往返。

## 前置知识

先完成第 055 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`json.dump(data, file, ensure_ascii=False)` 将数据写入文件，保留中文可读性。测试按解析后的内容判断，不要求某一种空格排版。

## 任务与约定

完成 `save_json(path, data)`，data 由 JSON 支持的字典、列表、字符串、整数、布尔值和 None 组成。写入 UTF-8 JSON 文件，覆盖原内容，返回 None。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

保存 `{"name": "小林"}` 后重新解析文件，应恢复同一字典。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

使用 json.dump，不用 str(data)。

</details>

<details>
<summary>提示 2：实现方向</summary>

True、None 的 JSON 写法由标准库处理。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
