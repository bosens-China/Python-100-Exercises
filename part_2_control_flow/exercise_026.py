"""
### 26. 斐波那契数列

- **描述:** 生成斐波那契数列的前 20 个数。斐波那契数列的前两项是 0 和 1，之后每一项都是前两项之和。
- **提示:** 使用循环，维护两个变量来保存前两项的值，然后计算下一项。
- **期待:** 输出 `[0, 1, 1, 2, 3, 5, 8, ...]`，直到第 20 个数。
"""

def generate_fibonacci(n):
    """
    生成斐波那契数列的前 n 个数
    :param n: 要生成的数的个数
    :return: 一个包含斐波那契数列的列表
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    count = 20
    fibonacci_sequence = generate_fibonacci(count)
    print(f"斐波那契数列的前 {count} 个数是:")
    print(fibonacci_sequence) 