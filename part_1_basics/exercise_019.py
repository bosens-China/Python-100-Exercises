"""
### 19. 集合基础

- **描述:** 给定一个包含重复元素的列表 `numbers = [1, 2, 3, 2, 4, 5, 4, 1]`，使用集合来移除重复的元素。
- **提示:** 使用 `set()` 函数可以将列表转换为集合，集合会自动去重。
- **期待:** `print(unique_numbers)` 输出 `{1, 2, 3, 4, 5}`。
"""

def remove_duplicates(numbers):
    """
    使用集合移除列表中的重复元素
    :param numbers: 包含重复元素的列表
    :return: 一个移除了重复元素的集合
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    num_list = [1, 2, 3, 2, 4, 5, 4, 1]
    unique_set = remove_duplicates(num_list)
    print(f"原始列表: {num_list}")
    print(f"去重后的集合: {unique_set}") 