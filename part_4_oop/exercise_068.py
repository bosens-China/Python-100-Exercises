"""
### 68. `@property` 装饰器

- **描述:** 创建一个 `Circle` 类，它有一个私有半径 `_radius`。使用 `@property` 提供一个公有的 `radius` 属性来获取半径，并提供一个 `setter` 来设置半径（确保半径是正数）。
- **提示:** 使用 `@property` 定义 getter，使用 `@radius.setter` 定义 setter。
- **期待:**
  - `c.radius` 能获取值。
  - `c.radius = 10` 能设置值。
  - `c.radius = -5` 会触发你设置的错误提示。
"""
import math

class Circle:
    """一个 Circle 类，使用 @property 来控制对半径的访问。"""
    def __init__(self, radius: float):
        # 初始化时也通过 setter 来进行验证
        self.radius = radius

    @property
    def radius(self) -> float:
        """
        这是 'radius' 属性的 getter 方法。
        它允许我们像访问属性一样获取 _radius 的值 (e.g., c.radius)。
        """
        print("Getting radius...")
        return self._radius

    @radius.setter
    def radius(self, value: float):
        """
        这是 'radius' 属性的 setter 方法。
        它允许我们像给属性赋值一样设置 _radius 的值 (e.g., c.radius = 10)，
        同时可以在赋值前进行验证。
        """
        print(f"Setting radius to {value}...")
        if value < 0:
            raise ValueError("Radius cannot be negative.")
        # 私有变量的命名通常用一个下划线开头
        self._radius = value

    @property
    def area(self) -> float:
        """
        一个只读的 property，用于计算面积。
        它依赖于 radius 属性。
        """
        print("Calculating area...")
        return math.pi * (self._radius ** 2)

if __name__ == '__main__':
    print("--- 创建一个 Circle 实例 ---")
    c = Circle(5)
    
    print("\n--- 获取半径 ---")
    print(f"The radius is: {c.radius}")
    
    print("\n--- 设置新的半径 ---")
    c.radius = 10
    print(f"The new radius is: {c.radius}")
    
    print("\n--- 计算面积 ---")
    # 注意，area 没有括号，因为它是一个 property
    print(f"The area is: {c.area:.2f}")

    print("\n--- 尝试设置一个无效的半径 ---")
    try:
        c.radius = -2
    except ValueError as e:
        print(f"捕获到错误: {e}")
        
    print(f"Radius remains: {c.radius}") 