"""
### 29. 判断质数

- **描述:** 编写一个程序，判断一个给定的正整数是否为质数。
- **提示:** 质数是只能被 1 和它本身整除的大于 1 的正整数。遍历从 2 到该数平方根的整数，检查是否能被整除。
- **期待:** 如果输入是 `13`，输出 `13 是质数`。如果输入是 `12`，输出 `12 不是质数`。
"""
import math

def is_prime(number):
    """
    判断一个正整数是否为质数
    :param number: 一个正整数
    :return: 如果是质数返回 True，否则返回 False
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    num1 = 13
    if is_prime(num1):
        print(f"{num1} 是质数")
    else:
        print(f"{num1} 不是质数")

    num2 = 12
    if is_prime(num2):
        print(f"{num2} 是质数")
    else:
        print(f"{num2} 不是质数") 