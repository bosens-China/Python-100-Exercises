"""
### 8. 格式化字符串

- **描述:** 定义两个变量，`name = "Bob"` 和 `age = 25`。使用 f-string 创建一个字符串，介绍 Bob。
- **提示:** f-string 的语法是 `f"这是一个包含 {variable} 的字符串"`。
- **期待:** `print(intro_string)` 输出 `Bob is 25 years old.`。
"""

def create_intro_string(name, age):
    """
    使用 f-string 创建介绍性字符串
    :param name: 姓名
    :param age: 年龄
    :return: 格式化后的字符串
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    user_name = "Bob"
    user_age = 25
    intro = create_intro_string(user_name, user_age)
    print(intro) 