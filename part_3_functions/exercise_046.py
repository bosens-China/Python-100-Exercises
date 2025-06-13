"""
### 46. 可变参数 `**kwargs`

- **描述:** 编写一个函数 `display_info`，它可以接受任意数量的关键字参数，并将它们作为键值对打印出来。
- **提示:** 使用 `**kwargs` 来接收一个包含所有关键字参数的字典。
- **期待:** 调用 `display_info(name="Alice", age=25)` 会输出:
  ```
  name: Alice
  age: 25
  ```
"""

def display_info(**kwargs):
    """
    接受任意数量的关键字参数，并返回一个格式化的、包含所有键值对的字符串。
    每个键值对占一行，格式为 "key: value"。
    
    :param kwargs: 任意数量的关键字参数
    :return: 一个多行字符串，描述所有传入的参数
    """
    # 在这里写下你的代码
    pass


if __name__ == '__main__':
    info = display_info(name="Alice", age=25, city="New York")
    print(info)