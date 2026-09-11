"""
题目 031: 类的定义与继承

要求:
1. 创建一个名为 `Shape` 的基类，它有一个 `area()` 方法，该方法直接 `return 0`。
2. 创建一个名为 `Rectangle` 的子类，继承自 `Shape`。
3. `Rectangle` 的 `__init__` 方法应接受 `width` 和 `height`。
4. 重写 `area()` 方法，使其能正确计算并返回矩形的面积。

提示:
子类通过在类定义时括号内放入父类名来实现继承，例如 `class Child(Parent):`。
"""

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    # 在这里写下你的代码
    pass
