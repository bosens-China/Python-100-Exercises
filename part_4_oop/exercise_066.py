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
    species = "Felis catus"

    def __init__(self, name):
        self.name = name

    raise NotImplementedError