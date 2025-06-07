"""
### 27. 循环中断与继续

- **描述:** 遍历一个数字列表 `[1, 2, 3, 4, 5, 6, 7, 8, 9]`，打印出所有小于 5 的数字，当遇到大于等于 5 的数字时，停止循环。再写一个循环，打印所有奇数。
- **提示:** 第一个任务使用 `break`。第二个任务使用 `continue` 和 `%` 运算符。
- **期待:**
  - 第一个循环输出: `1`, `2`, `3`, `4`
  - 第二个循环输出: `1`, `3`, `5`, `7`, `9`
"""

def loop_control_break(numbers):
    """
    使用 break: 遍历列表，返回所有小于 5 的数字。
    :param numbers: 数字列表
    :return: 一个包含小于5的数字的列表
    """
    result = []
    # 在这里写下你的代码
    return result

def loop_control_continue(numbers):
    """
    使用 continue: 遍历列表，返回所有奇数。
    :param numbers: 数字列表
    :return: 一个包含所有奇数的列表
    """
    result = []
    # 在这里写下你的代码
    return result


if __name__ == '__main__':
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    print(f"使用 break (小于5的数):")
    less_than_5 = loop_control_break(num_list)
    print(less_than_5)

    print(f"\n使用 continue (所有奇数):")
    only_odds = loop_control_continue(num_list)
    print(only_odds) 