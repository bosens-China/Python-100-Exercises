"""
### 43. 默认参数

- **描述:** 修改第 41 题的 `greet` 函数，让它在没有提供名字时，默认问候 "World"。
- **提示:** 在函数定义中给参数赋一个默认值 `def greet(name="World"):`。
- **期待:**
  - `greet("Bob")` 输出 `Hello, Bob!`
  - `greet()` 输出 `Hello, World!`
"""

# 我们将重新定义这个函数，而不是修改之前的文件
def greet_with_default():
    """
    生成一个问候字符串，name 参数有默认值。
    :param name: 要问候的人的名字，默认为 "World"
    :return: 问候语字符串
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    print(greet_with_default("Bob"))
    print(greet_with_default()) 