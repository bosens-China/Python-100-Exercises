"""
### 50. `map()` 函数

- **描述:** 给定一个列表 `numbers = [1, 2, 3, 4, 5]`，使用 `map()` 和一个 `lambda` 函数，生成一个新列表，其中每个元素都是原列表中对应元素的平方。
- **提示:** `map(function, iterable)`。记得将 `map` 对象转换为列表 `list(map(...))`。
- **期待:** 得到新列表 `[1, 4, 9, 16, 25]`。
"""

def square_list_with_map(numbers):
    """
    使用 map 和 lambda 函数计算列表中每个数字的平方。
    :param numbers: 一个数字列表
    :return: 一个包含原列表中每个数字平方的新列表
    """
    # 在这里写下你的代码
    squared_numbers = map(lambda x: x * x, numbers)
    return list(squared_numbers)

if __name__ == '__main__':
    original_numbers = [1, 2, 3, 4, 5]
    squared = square_list_with_map(original_numbers)
    print(f"原列表: {original_numbers}")
    print(f"平方后的列表: {squared}") 