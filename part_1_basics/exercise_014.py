"""
### 14. 列表修改

- **描述:** 创建一个列表 `fruits = ["apple", "banana", "cherry"]`。在列表末尾添加 "orange"，然后在 "apple" 后面插入 "grape"。
- **提示:** 使用 `append()` 方法在末尾添加，使用 `insert()` 方法在指定位置插入。
- **期待:** 修改后的列表 `fruits` 为 `['apple', 'grape', 'banana', 'cherry', 'orange']`。
"""

def modify_list(fruits):
    """
    修改列表：末尾添加 "orange"，在 "apple" 后插入 "grape"
    :param fruits: 初始列表
    :return: 修改后的列表
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    my_fruits = ["apple", "banana", "cherry"]
    print(f"原始列表: {my_fruits}")
    modified_fruits = modify_list(my_fruits)
    print(f"修改后列表: {modified_fruits}") 