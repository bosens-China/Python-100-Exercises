"""
### 67. 公有和私有成员

- **描述:** 创建一个 `Person` 类，有公有属性 `name` 和一个 "私有" 属性 `_age` (单下划线) 和 `__bank_account` (双下划线)。尝试从外部访问这些属性，观察区别。
- **提示:** 单下划线是约定俗成的 "内部使用"，但仍可访问。双下划线会触发 Python 的名称改写机制。
- **期待:**
  - `person.name` 和 `person._age` 可以直接访问。
  - 直接访问 `person.__bank_account` 会失败，需要通过 `person._Person__bank_account` 才能访问。
"""

class Person:
    # 在这里写下你的代码
    pass

# 主程序入口，用于直接运行时进行演示
if __name__ == '__main__':
    # 实例化你将要实现的 Person 类
    p = Person("Alice", 30, "123-456-789")

    print("\n--- 访问公有属性 ---")
    print(f"p.name: {p.name}")

    print("\n--- 访问\"受保护\"属性 ---")
    print("单下划线 _age 是一个约定，表示 '不应在外部直接访问'，但技术上是可行的。")
    print(f"p._age: {p._age}")
    
    print("\n--- 在类内部方法中访问所有属性 ---")
    info = p.display_info()
    print(info)

    print("\n--- 尝试访问\"私有\"属性 ---")
    print("直接访问 p.__bank_account 会失败，因为 Python 将其名称改写了。")
    try:
        print(p.__bank_account)
    except AttributeError as e:
        print(f"成功捕获到错误: {e}")

    print("\n--- 访问被名称改写后的\"私有\"属性 ---")
    print("可以通过 _ClassName__attributeName 的方式访问它。")
    # 注意：下面的访问方式不推荐在实际项目中使用，这里仅为演示。
    # 警告：为了让程序能顺利运行而不预先报错，访问私有属性的这行代码被注释掉了。
    # 完成练习后，你可以取消注释来观察其效果。
    # print(f"p._Person__bank_account: {getattr(p, '_Person__bank_account')}")
