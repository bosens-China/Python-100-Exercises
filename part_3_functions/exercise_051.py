"""
### 51. `filter()` 函数

- **描述:** 给定一个列表 `numbers = [1, 2, 3, 4, 5]`，使用 `filter()` 和一个 `lambda` 函数，筛选出所有的偶数。
- **提示:** `filter(function, iterable)`。`function` 应返回 `True` 或 `False`。
- **期待:** 得到新列表 `[2, 4]`。
"""

def filter_even_numbers(numbers):
    """
    使用 filter 和 lambda 函数筛选出列表中的所有偶数。
    :param numbers: 一个数字列表
    :return: 一个只包含原列表中偶数的新列表
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    original_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # 调用 filter_even_numbers 并打印结果
    evens = filter_even_numbers(original_numbers)
    print(f"原列表: {original_numbers}")
    print(f"筛选出的偶数: {evens}") 