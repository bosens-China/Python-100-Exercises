"""
### 67. 公有和私有成员

- **描述:** 创建一个 `Person` 类，有公有属性 `name` 和一个 "私有" 属性 `_age` (单下划线) 和 `__bank_account` (双下划线)。尝试从外部访问这些属性，观察区别。
- **提示:** 单下划线是约定俗成的 "内部使用"，但仍可访问。双下划线会触发 Python 的名称改写机制。
- **期待:**
  - `person.name` 和 `person._age` 可以直接访问。
  - 直接访问 `person.__bank_account` 会失败，需要通过 `person._Person__bank_account` 才能访问。
"""

class Person:
    def __init__(self, name: str, age: int, bank_account: str):
        # 公有属性，可以从任何地方访问
        self.name = name
        # "受保护"的属性（单下划线），约定为内部使用，但仍然可以直接访问
        self._age = age
        # "私有"属性（双下划线），会触发名称改写
        self.__bank_account = bank_account

    def display_info(self):
        # 在类的内部，所有属性都可以正常访问
        print(f"Name: {self.name}")
        print(f"Age: {self._age}")
        print(f"Bank Account (accessed from inside): {self.__bank_account}")


# 注意：本练习旨在演示 Python 的访问控制约定。
# 直接测试这些约定（例如，确认访问 __bank_account 会引发 AttributeError）
# 与练习的目的（理解为什么会发生以及如何访问）相悖。
# 因此，我们不提供 test 文件，建议直接运行此脚本并观察输出和错误。

if __name__ == '__main__':
    p = Person("Alice", 30, "123-456-789")

    print("--- 访问公有属性 ---")
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
    print(f"p._Person__bank_account: {p._Person__bank_account}") 