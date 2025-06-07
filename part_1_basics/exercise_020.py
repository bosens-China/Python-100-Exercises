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
    创建不同类型的变量并返回它们的类型
    :return: 一个包含各种变量类型的列表
    """
    integer_var = 5
    float_var = 3.14
    string_var = "hello"
    list_var = [1, 2, 3]
    dict_var = {'a': 1}
    tuple_var = (1, 2)
    set_var = {1, 2}

    # 在这里写下你的代码，获取以上变量的类型
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

    # 调用函数并打印返回的类型列表
    variable_types = get_types_of_variables()
    print(f"\n函数返回的类型列表: {variable_types}") 