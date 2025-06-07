"""
### 37. 打印列表中的所有偶数

- **描述:** 给定一个数字列表，只打印出其中的所有偶数。
- **提示:** 遍历列表，使用 `% 2 == 0` 来判断是否为偶数。
- **期待:** 对于列表 `[1, 2, 3, 4, 5, 6]`，程序输出 `2`, `4`, `6`。
"""

def get_even_numbers(numbers):
    """
    从列表中筛选出所有的偶数
    :param numbers: 数字列表
    :return: 一个只包含偶数的列表
    """
    # 在这里写下你的代码
    even_numbers = []
    return even_numbers

if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    evens = get_even_numbers(num_list)
    print(f"从列表 {num_list} 中筛选出的偶数是:")
    # 为了清晰，我们逐个打印
    for num in evens:
        print(num) 