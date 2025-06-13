"""
### 53. 函数作为参数

- **描述:** 编写一个高阶函数 `operate_on_numbers`，它接受两个数字和一个函数作为参数，并返回将该函数应用于这两个数字的结果。
- **提示:** `def operate_on_numbers(a, b, operation): return operation(a, b)`。
- **期待:** 定义 `add = lambda x, y: x + y`，然后 `operate_on_numbers(10, 5, add)` 返回 `15`。
"""

def operate_on_numbers(a, b, operation):
    """
    接受两个数字和一个操作函数，并返回操作结果。
    :param a: 第一个数字
    :param b: 第二个数字
    :param operation: 一个接受两个参数并返回一个结果的函数
    :return: operation(a, b) 的结果
    """
    # 在这里写下你的代码
    pass

# --- 为了演示和测试，定义一些可以作为参数的函数 ---

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

# 使用 lambda 定义一个乘法函数
multiply = lambda x, y: x * y

if __name__ == '__main__':
    result_add = operate_on_numbers(10, 5, add)
    print(f"使用 add 函数的结果: {result_add}")