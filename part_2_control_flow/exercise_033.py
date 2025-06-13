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
    pass

if __name__ == '__main__':
    # 注意：这个 main 部分只是为了演示，真正的逻辑和测试在函数中
    # 场景1: 成功
    print("场景1: 第二次尝试成功")
    inputs1 = ["wrong", "python123", "another_wrong"]
    result1 = password_checker("python123", inputs1)
    print(result1) # 应该输出 "登录成功"

    print("\n场景2: 失败")
    # 场景2: 失败
    inputs2 = ["wrong1", "wrong2", "wrong3"]
    result2 = password_checker("python123", inputs2)
    print(result2) # 应该输出 "尝试次数过多，账户已锁定"