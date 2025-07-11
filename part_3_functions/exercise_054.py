"""
### 54. 闭包

- **描述:** 编写一个函数 `make_multiplier_of`，它接受一个数字 `n`，并返回一个新的函数。这个新函数接受一个数字 `x` 并返回 `n * x`。
- **提示:** 在一个外部函数中定义并返回一个内部函数，内部函数使用了外部函数的变量。
- **期待:** `times3 = make_multiplier_of(3)`，然后 `times3(5)` 返回 `15`。
"""

def make_multiplier_of(n):
    """
    创建一个"乘法器"函数。
    
    这个函数展示了闭包的概念：返回的内部函数 `multiplier` 
    "记住"了它被创建时外部作用域中的变量 `n`。
    
    :param n: 将要被用于乘法的数字。
    :return: 一个新的函数，该函数接受一个参数 `x` 并返回 `n * x`。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 使用 make_multiplier_of 创建一个乘以 3 的函数
    times3 = make_multiplier_of(3)
    
    # 使用新创建的函数
    result = times3(5)
    print(f"调用 times3(5) 的结果是: {result}") # 应该输出 15