# 073 · 组合购物车和商品

## 学习目标

通过组合使用已有对象。

## 前置知识

先完成第 072 题及其前置练习；本题复用此前学过的知识。

## 先学一点

组合意味着一个对象持有或使用另一个对象。已提供 Product，你只需要编写 Cart，通过 product.price 读取单价。

## 任务与约定

保留提供的 `Product(name, price)`。实现 `Cart()`：`add(product, quantity=1)` 记录商品和正整数数量、返回 None；`total()` 返回所有条目金额之和，空车为 0。价格非负整数，商品在加入后不会被修改。不同购物车独立。

除题目明确要求外，不修改传入的可变数据，不额外打印内容。只验收约定范围内的输入，不要求猜测未说明的规则。

## 示例

`cart.add(Product("笔", 100), 2)` 后 `cart.total()` → `200`。

## 开始编写

编辑 `main.py`。起始代码位于 [starter](./starter/)，测试位于 [test/test_solution.py](./test/test_solution.py)。起始代码尚未完成，出现未通过是正常反馈。

## 分层提示

<details>
<summary>提示 1：思路</summary>

购物车保存商品对象与数量。

</details>

<details>
<summary>提示 2：实现方向</summary>

每项小计使用 product.price * quantity。

</details>

## 如何验收

提交后检查题目约定中的正常行为及适用边界。测试针对结果，不要求与参考实现写法相同。失败时先对照测试输入和约定，再修改代码。
