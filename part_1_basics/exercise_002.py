"""
### 2. 变量交换

- **描述:** 定义两个变量，例如 `a = 5` 和 `b = 10`，然后编写代码交换它们的值，使得 `a` 的值为 `10`，`b` 的值为 `5`。
- **提示:** 你可以引入一个临时变量 `c` 来辅助交换，或者尝试使用 Python 特有的元组解包赋值 `a, b = b, a`。
- **期待:** 交换后，`print(a)` 输出 `10`，`print(b)` 输出 `5`。
"""

def swap_variables(a, b):
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    a, b = 5, 10
    a, b = swap_variables(a, b)
    print(f"a 的值为: {a}")
    print(f"b 的值为: {b}") 