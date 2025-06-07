"""
### 11. 检查数字奇偶性

- **描述:** 编写一个程序，判断一个给定的整数是奇数还是偶数。
- **提示:** 使用取模运算符 `%`。如果一个数能被 2 整除（余数为 0），它就是偶数。使用 `if-else` 结构。
- **期待:** 如果数字是 `7`，输出 `7 是奇数`。如果数字是 `4`，输出 `4 是偶数`。
"""

def check_odd_even(number):
    """
    检查数字是奇数还是偶数
    :param number: 一个整数
    :return: 字符串 "奇数" 或 "偶数"
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    num1 = 7
    result1 = check_odd_even(num1)
    print(f"{num1} 是{result1}")

    num2 = 4
    result2 = check_odd_even(num2)
    print(f"{num2} 是{result2}") 