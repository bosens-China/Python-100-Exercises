"""
### 12. 布尔表达式

- **描述:** 给定一个年龄 `age = 22`，判断它是否在 18 到 30 岁之间（包含边界）。
- **提示:** 使用 `and` 逻辑运算符来组合两个条件：`age >= 18` 和 `age <= 30`。
- **期待:** `print(is_in_range)` 输出 `True`。
"""

def is_in_range(age):
    """
    判断年龄是否在 18 到 30 岁之间
    :param age: 年龄
    :return: 布尔值，如果在范围内则为 True，否则为 False
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    age1 = 22
    print(f"{age1} 岁在 18-30 范围内吗? {is_in_range(age1)}")
    age2 = 35
    print(f"{age2} 岁在 18-30 范围内吗? {is_in_range(age2)}") 