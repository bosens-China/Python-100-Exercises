"""
### 66. 类变量与实例变量

- **描述:** 创建一个 `Cat` 类。为它定义一个类变量 `species = "Felis catus"` 和一个实例变量 `name`。
- **提示:** 类变量直接在 `class` 下定义，实例变量在 `__init__` 中用 `self` 定义。
- **期待:**
  - `cat1 = Cat("Whiskers")`, `cat2 = Cat("Tom")`。
  - `cat1.name` 是 "Whiskers"，`cat2.name` 是 "Tom"。
  - `cat1.species` 和 `cat2.species` 以及 `Cat.species` 都是 "Felis catus"。
"""

class Cat:
    """
    一个 Cat 类，用于演示类变量和实例变量的区别。
    
    类变量 `species` 对于所有 Cat 实例都是共享的。
    实例变量 `name` 是每个实例独有的。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 创建两个 Cat 实例
    cat1 = Cat("Whiskers")
    cat2 = Cat("Tom")

    # 验证实例变量
    print(f"第一只猫的名字是: {cat1.name}")
    print(f"第二只猫的名字是: {cat2.name}")
    assert cat1.name == "Whiskers"
    assert cat2.name == "Tom"

    # 验证类变量
    # 类变量可以通过类直接访问，也可以通过实例访问
    print(f"通过类访问物种: {Cat.species}")
    print(f"通过 cat1 访问物种: {cat1.species}")
    print(f"通过 cat2 访问物种: {cat2.species}")
    assert Cat.species == "Felis catus"
    assert cat1.species == "Felis catus"
    
    # 改变类变量会影响所有实例
    Cat.species = "A new species"
    print(f"\n修改类变量后，通过 cat1 访问物种: {cat1.species}")
    assert cat1.species == "A new species"
    
    print("\n练习完成！")