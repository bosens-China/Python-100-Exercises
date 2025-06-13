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
    # 在这里写下你的代码
    pass

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