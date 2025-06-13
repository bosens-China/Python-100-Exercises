"""
### 42. 带返回值的函数

- **描述:** 编写一个名为 `add` 的函数，它接受两个数字作为参数，并返回它们的和。
- **提示:** 使用 `return` 语句来返回结果。
- **期待:** `result = add(5, 3)` 后，`print(result)` 输出 `8`。
"""

def add(a, b):
    """
    返回两个数字的和。
    :param a: 第一个数字
    :param b: 第二个数字
    :return: a 和 b 的和
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    num1, num2 = 5, 3
    sum_result = add(num1, num2)
    print(f"{num1} + {num2} = {sum_result}") 