"""
### 39. 查找列表中的最大值

- **描述:** 不使用内置的 `max()` 函数，找到一个数字列表中的最大值。
- **提示:** 初始化一个变量 `max_val` 为列表的第一个元素，然后遍历列表，如果发现更大的数，就更新 `max_val`。
- **期待:** 对于列表 `[1, 5, 2, 8, 3]`，输出 `最大值: 8`。
"""

def find_max(numbers):
    """
    不使用 max() 函数，查找列表中的最大值。
    :param numbers: 数字列表
    :return: 列表中的最大值。如果列表为空，可以返回 None。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    my_numbers = [1, 5, 2, 8, 3, -2, 7]
    max_value = find_max(my_numbers)
    print(f"列表 {my_numbers} 中的最大值是: {max_value}")

    empty_list = []
    max_value_empty = find_max(empty_list)
    print(f"列表 {empty_list} 中的最大值是: {max_value_empty}") 