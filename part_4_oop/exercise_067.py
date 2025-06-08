"""
### 67. 公有和私有成员

- **描述:** 创建一个 `Person` 类，有公有属性 `name` 和一个 "私有" 属性 `_age` (单下划线) 和 `__bank_account` (双下划线)。尝试从外部访问这些属性，观察区别。
- **提示:** 单下划线是约定俗成的 "内部使用"，但仍可访问。双下划线会触发 Python 的名称改写机制。
- **期待:**
  - `person.name` 和 `person._age` 可以直接访问。
  - 直接访问 `person.__bank_account` 会失败，需要通过 `person._Person__bank_account` 才能访问。
"""

class Person:
    """
    一个 Person 类，用于演示公有、受保护和私有属性的访问约定。
    """
    def __init__(self, name: str, age: int, bank_account: str):
        """
        :param name: 姓名 (公有)
        :param age: 年龄 (受保护)
        :param bank_account: 银行账户 (私有)
        """
        # 在这里写下你的代码
        # 提示：分别使用 self.name, self._age, 和 self.__bank_account 来赋值
        raise NotImplementedError

    def display_info(self) -> str:
        """
        在类的内部，所有属性都可以正常访问。
        返回一个包含所有信息的字符串，以便于测试。
        """
        # 在这里写下你的代码
        # 提示: 返回一个类似 "Name: ..., Age: ..., Bank Account: ..." 的字符串
        raise NotImplementedError

# 主程序入口，用于直接运行时进行演示
if __name__ == '__main__':
    # 假设 Person 类已经正确实现
    class PersonDemo:
        def __init__(self, name: str, age: int, bank_account: str):
            self.name = name
            self._age = age
            self.__bank_account = bank_account
        def display_info(self):
            print(f"Name: {self.name}, Age: {self._age}, Bank Account: {self.__bank_account}")

    p = PersonDemo("Alice", 30, "123-456-789")
    print(f"公有属性: p.name -> {p.name}")
    print(f"受保护属性: p._age -> {p._age}")
    print("尝试直接访问私有属性 p.__bank_account 会导致 AttributeError。")
    print(f"通过名称改写访问: p._PersonDemo__bank_account -> {p._PersonDemo__bank_account}")

    print("\n--- 访问公有属性 ---")
    print(f"p.name: {p.name}")

    print("\n--- 访问"受保护"属性 ---")
    print("单下划线 _age 是一个约定，表示 '不应在外部直接访问'，但技术上是可行的。")
    print(f"p._age: {p._age}")
    
    print("\n--- 在类内部方法中访问所有属性 ---")
    p.display_info()

    print("\n--- 尝试访问"私有"属性 ---")
    print("直接访问 p.__bank_account 会失败，因为 Python 将其名称改写了。")
    try:
        print(p.__bank_account)
    except AttributeError as e:
        print(f"捕获到错误: {e}")

    print("\n--- 访问被名称改写后的"私有"属性 ---")
    print("可以通过 _ClassName__attributeName 的方式访问它。")
    # 注意：下面的访问方式不推荐在实际项目中使用，这里仅为演示。
    print(f"p._PersonDemo__bank_account: {p._PersonDemo__bank_account}") 