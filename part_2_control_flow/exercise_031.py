"""
### 31. 字典推导式

- **描述:** 给定一个列表 `["name", "age", "city"]`，使用字典推导式创建一个字典，其中键是列表中的字符串，值是字符串的长度。
- **提示:** 语法为 `{key_expression: value_expression for item in iterable}`。
- **期待:** `print(result_dict)` 输出 `{'name': 4, 'age': 3, 'city': 4}`。
"""

def create_dict_from_list(keys):
    """
    使用字典推导式从列表创建字典
    :param keys: 字符串列表
    :return: 一个字典，键是列表中的字符串，值是其长度
    """
    # 在这里写下你的代码
    result_dict = {}
    return result_dict

if __name__ == '__main__':
    key_list = ["name", "age", "city"]
    my_dict = create_dict_from_list(key_list)
    print(f"从列表 {key_list} 创建的字典是:")
    print(my_dict) 