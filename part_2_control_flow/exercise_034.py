"""
### 34. 模拟用户登录

- **描述:** 创建一个简单的用户登录程序。预设一个用户名和密码。程序提示用户输入，如果都正确，则登录成功，否则提示错误。
- **提示:** 使用 `input()` 获取输入，使用 `if-else` 判断。
- **期待:** 输入正确的用户名和密码后，输出 "登录成功！"。否则输出 "用户名或密码错误！"。
"""

def simple_login(correct_user, correct_pass, provided_user, provided_pass):
    """
    模拟简单的用户登录验证
    :param correct_user: 正确的用户名
    :param correct_pass: 正确的密码
    :param provided_user: 用户输入的用户名
    :param provided_pass: 用户输入的密码
    :return: "登录成功！" 或 "用户名或密码错误！"
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 交互式部分
    # 预设的用户名和密码
    CORRECT_USERNAME = "admin"
    CORRECT_PASSWORD = "password123"
    
    print("请输入用户名和密码登录。")
    username_input = input("用户名: ")
    password_input = input("密码: ")

    # 调用验证逻辑
    # 注意：这里的实现与测试函数是独立的
    if username_input == CORRECT_USERNAME and password_input == CORRECT_PASSWORD:
        print("登录成功！")
    else:
        print("用户名或密码错误！")

# 注意:
# 为了方便测试，我们将核心判断逻辑放在 simple_login 函数中。
# __main__ 部分则用于实际的交互演示。 