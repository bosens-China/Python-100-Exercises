"""
### 33. `while-else` 循环

- **描述:** 使用 `while-else` 模拟一个密码输入场景，用户有 3 次机会。如果密码正确，循环中断；如果 3 次都错误，`else` 部分执行。
- **提示:** `while-else` 的 `else` 子句在循环条件变为 `False` 时执行。
- **期待:** 用户输入正确密码后提示 "登录成功"。3 次错误后提示 "尝试次数过多，账户已锁定"。
"""

def password_checker(correct_password, user_inputs):
    """
    模拟密码检查器。
    为了便于测试，我们不使用真实的 input()，而是从一个列表中读取用户输入。
    :param correct_password: 正确的密码
    :param user_inputs: 一个模拟用户输入的列表
    :return: 字符串 "登录成功" 或 "尝试次数过多，账户已锁定"
    """
    # 在这里写下你的代码
    # 使用 while-else 结构
    return ""

if __name__ == '__main__':
    # 这是一个交互式演示，与测试函数逻辑分离
    # 实际测试请看 test_exercise_033.py
    
    correct_pass = "python123"
    attempts = 3
    print("请输入密码，你有 3 次机会。")

    while attempts > 0:
        guess = input("密码: ")
        if guess == correct_pass:
            print("登录成功")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"密码错误，你还有 {attempts} 次机会。")
    else:
        print("尝试次数过多，账户已锁定") 