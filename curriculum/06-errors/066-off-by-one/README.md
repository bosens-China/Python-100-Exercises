# 066 · 修复分页边界

## 学习目标

用边界用例定位索引错误。

## 前置知识

先完成第 065 题及其前置练习；本题复用此前学过的知识。

## 先学一点

第 1 页的起点是 0，第 2 页的起点是 page_size。切片的右端点不包含在结果中。

## 任务与约定

修复 `paginate(items, page, page_size)`，items 为整数列表，page 和 page_size 均保证为正整数。页码从 1 开始，返回当前页的新列表；超出范围返回空列表。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`paginate([1, 2, 3, 4, 5], 2, 2)` → `[3, 4]`

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

用第一页检查起点是否算对。

</details>

<details>
<summary>提示 2：实现方向</summary>

start = (page - 1) * page_size。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
