"""
### 48. 递归函数实现阶乘计算

- **描述:** 实现一个递归函数来计算非负整数的阶乘，并正确处理边界条件。
- **要点:**
  - 递归终止条件：0! = 1
  - 递归关系：n! = n × (n-1)!
  - 输入验证：拒绝负数输入
- **示例:**
  - 输入: 5 → 输出: 120
  - 输入: 0 → 输出: 1
  - 输入: -1 → 抛出 ValueError
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