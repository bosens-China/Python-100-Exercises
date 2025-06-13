"""
### 84. 抛出异常

- **描述:** 编写一个函数，接受一个年龄作为参数。如果年龄小于 0，使用 `raise` 关键字主动抛出一个 `ValueError` 异常。
- **提示:** `if age < 0: raise ValueError("年龄不能为负数")`。
- **期待:** 调用 `set_age(-5)` 会使程序因 `ValueError` 而停止，并显示你提供的错误信息。
"""

def set_age(age):
    """
    设置年龄，如果年龄为负则抛出异常。
    :param age: 要设置的年龄
    :raises ValueError: 如果年龄小于 0
    """
    # 在这里写下你的代码
    pass


if __name__ == '__main__':
    print("--- 尝试设置一个有效的年龄 ---")
    try:
        set_age(30)
    except ValueError as e:
        print(f"不应捕获到错误，但捕获到了: {e}")

    print("\n--- 尝试设置一个无效的年龄 ---")
    try:
        set_age(-5)
    except ValueError as e:
        print(f"成功捕获到预期的错误: {e}") 