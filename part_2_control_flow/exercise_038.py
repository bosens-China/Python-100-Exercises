"""
### 38. 列表元素去重

- **描述:** 不使用 `set`，编写代码移除一个列表中的重复元素。
- **提示:** 创建一个新列表，遍历原始列表，如果元素不在新列表中，就把它添加进去。
- **期待:** 对于列表 `[1, 2, 2, 3, 4, 3]`，得到新列表 `[1, 2, 3, 4]`。
"""

def deduplicate_list(items):
    """
    不使用 set, 移除列表中的重复元素，并保持原始顺序。
    :param items: 可能包含重复元素的列表
    :return: 一个移除了重复元素的新列表
    """
    # 在这里写下你的代码
    unique_items = []
    return unique_items

if __name__ == '__main__':
    my_list = [1, 2, 2, 3, 4, 3, 5, 1]
    print(f"原始列表: {my_list}")
    new_list = deduplicate_list(my_list)
    print(f"去重后的列表: {new_list}") 