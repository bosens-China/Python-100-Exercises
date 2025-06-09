"""
### 20. 类型检查

- **描述:** 创建不同类型的变量（整数、浮点数、字符串、列表、字典），并使用 `type()` 函数检查并打印它们的类型。
- **提示:** `print(type(variable))`。
- **期待:**
  - `print(type(5))` -> `<class 'int'>`
  - `print(type(3.14))` -> `<class 'float'>`
  - `print(type("hello"))` -> `<class 'str'>`
"""

def get_types_of_variables():
    """
    请根据下面的注释，创建相应类型的变量，
    并将它们的类型 (type) 依次添加到 `types` 列表中。
    :return: 一个包含各种变量类型的列表，顺序应为：int, float, str, list, dict
    """
    # TODO: 在下方创建 'integer_var', 'float_var', 'string_var', 'list_var', 'dict_var' 五个变量，并赋予相应类型的值。
    
    # TODO: 将以上变量的类型 (type) 按顺序添加到下面的列表中
    types = []

    # 为了方便测试，我们将类型返回
    return types


if __name__ == '__main__':
    # 这个练习主要是为了直接观察 type() 函数的输出
    print(f"Type of 5 is {type(5)}")
    print(f"Type of 3.14 is {type(3.14)}")
    print(f"Type of 'hello' is {type('hello')}")
    print(f"Type of [1, 2, 3] is {type([1, 2, 3])}")
    print(f"Type of {{'a': 1}} is {type({'a': 1})}")
    print(f"Type of (1, 2) is {type((1, 2))}")
    print(f"Type of {{1, 2}} is {type({1, 2})}")

    # 当你在 get_types_of_variables 中完成代码后，
    # 调用函数并打印返回的类型列表
    variable_types = get_types_of_variables()
    print(f"\n函数返回的类型列表: {variable_types}") 