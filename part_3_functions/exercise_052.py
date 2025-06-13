"""
### 52. `reduce()` 函数

- **描述:** 从 `functools` 模块导入 `reduce`。使用 `reduce` 来计算一个列表中所有元素的乘积。
- **提示:** `reduce(function, iterable)`。`function` 应接受两个参数。
- **期待:** 对于列表 `[1, 2, 3, 4]`，`reduce` 返回 `24`。
"""
from functools import reduce

def product_of_list(numbers):
    """
    使用 reduce 计算列表中所有元素的乘积。
    :param numbers: 一个数字列表
    :return: 列表中所有元素的乘积。如果列表为空，此实现会引发TypeError。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    my_list = [1, 2, 3, 4]
    # 调用 product_of_list 并打印结果
    result = product_of_list(my_list)
    print(f"列表 {my_list} 中所有元素的乘积是: {result}")

    empty_list = []
    result_empty = product_of_list(empty_list)
    print(f"列表 {empty_list} 中所有元素的乘积是: {result_empty}")
    
    single_item_list = [10]
    result_single = product_of_list(single_item_list)
    print(f"列表 {single_item_list} 中所有元素的乘积是: {result_single}") 