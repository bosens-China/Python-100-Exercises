"""
### 16. 元组基础

- **描述:** 创建一个包含三个元素的元组，例如你的姓名、年龄和城市。然后尝试修改元组的第一个元素，并观察会发生什么。
- **提示:** 元组用圆括号 `()` 创建。元组是不可变的，修改它会引发 `TypeError`。
- **期待:** 程序会因为尝试修改元组而报错，这有助于你理解元组的不可变性。
"""

def create_person_tuple():
    """
    创建一个包含姓名（字符串）、年龄（整数）和城市（字符串）的元组。
    
    :return: 一个包含三个元素的元组。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 1. 创建元组
    person = create_person_tuple()
    print(f"创建的元组: {person}")

    # 2. 访问元组元素
    print(f"姓名: {person[0]}")
    
    # 3. 尝试修改元组（这将导致 TypeError）
    print("\n现在尝试修改元组的第一个元素...")
    try:
        person[0] = "Bob"
    except TypeError as e:
        print("操作失败，正如预期！")
        print(f"错误信息: {e}") 