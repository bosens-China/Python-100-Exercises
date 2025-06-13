"""
### 48. 递归函数：计算阶乘

- **描述:** 使用递归编写一个函数来计算一个非负整数的阶乘。
- **提示:** 阶乘的定义是 n! = n * (n-1)!，并且 0! = 1。函数需要一个基本情况（终止条件）和一个递归调用。
- **期待:** `factorial(5)` 返回 `120`。
"""

def factorial(n):
    """
    使用递归计算一个非负整数的阶乘。
    :param n: 一个非负整数
    :return: n 的阶乘
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':

    print(f"5! = {factorial(5)}")
    print(f"0! = {factorial(0)}")
    print(f"1! = {factorial(1)}")
    try:
        factorial(-1)
    except ValueError as e:
        print(e) 