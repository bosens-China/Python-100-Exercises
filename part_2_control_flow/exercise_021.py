"""
### 21. 判断闰年

- **描述:** 编写一个程序，判断一个给定的年份是否是闰年。
- **提示:** 闰年的条件是：能被 4 整除但不能被 100 整除，或者能被 400 整除。使用 `if-elif-else` 结构。
- **期待:** 如果年份是 `2024`，输出 `2024 是闰年`。如果年份是 `1900`，输出 `1900 不是闰年`。
"""

def is_leap_year(year):
    """
    判断一个年份是否是闰年
    :param year: 年份 (整数)
    :return: 如果是闰年返回 True，否则返回 False
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    year1 = 2024
    if is_leap_year(year1):
        print(f"{year1} 是闰年")
    else:
        print(f"{year1} 不是闰年")

    year2 = 1900
    if is_leap_year(year2):
        print(f"{year2} 是闰年")
    else:
        print(f"{year2} 不是闰年") 