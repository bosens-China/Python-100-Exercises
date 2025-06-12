"""
### 41. 编写一个简单的问候函数

- **描述:** 编写一个名为 `greet` 的函数，它接受一个参数 `name`，并打印出 "Hello, [name]!"。
- **提示:** 使用 `def` 关键字定义函数 `def greet(name):`。
- **期待:** 调用 `greet("Alice")` 会输出 `Hello, Alice!`。
"""

def greet():
    """
    生成一个问候字符串。
    为了方便测试，函数将返回字符串而不是直接打印。
    :param name: 要问候的人的名字
    :return: 问候语字符串
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    user_name = "Alice"
    greeting = greet(user_name)
    print(greeting) 