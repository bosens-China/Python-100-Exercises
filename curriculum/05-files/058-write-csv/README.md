# 058 · 导出 CSV 人员表

## 学习目标

写入表头与记录。

## 前置知识

先完成第 057 题及其前置练习；本题复用此前学过的知识。

## 先学一点

`csv.DictWriter(file, fieldnames=["name", "age"])` 创建写入器，`writeheader()` 写表头，`writerows(rows)` 写多条记录。

## 任务与约定

完成 `write_people(path, people)`，记录含 name 字符串和 age 非负整数。覆盖写入 UTF-8 CSV，列顺序 name、age，始终保留表头，返回 None。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

输入 `[{"name": "Ada", "age": 20}]`，导出后可按相同表头读回。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

空列表也应输出表头。

</details>

<details>
<summary>提示 2：实现方向</summary>

用 CSV 写入器处理逗号与引号。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
