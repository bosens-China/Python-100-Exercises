"""
### 45. 可变参数 `*args`

- **描述:** 编写一个函数 `sum_all`，它可以接受任意数量的位置参数，并返回它们的总和。
- **提示:** 使用 `*args` 来接收一个包含所有位置参数的元组。
- **期待:** `sum_all(1, 2, 3, 4, 5)` 返回 `15`。
"""

def sum_all(*args):
    """
    计算所有位置参数的总和。
    :param args: 一个包含所有位置参数的元组
    :return: 所有参数的总和
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    print(sum_all(1, 2, 3, 4, 5))
    print(sum_all(10, 20))
    print(sum_all()) 