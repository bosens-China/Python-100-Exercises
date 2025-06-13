"""
### 75. 运算符重载

- **描述:** 创建一个 `Vector` 类，表示二维向量（有 `x` 和 `y` 属性）。重载 `+` 运算符（使用 `__add__` 方法），使其能够将两个向量相加。
- **提示:** `def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)`
- **期待:** `v1 = Vector(2, 3)`, `v2 = Vector(3, 4)`, `v3 = v1 + v2`，则 `v3.x` 为 `5`，`v3.y` 为 `7`。
"""

class Vector:
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    v1 = Vector(2, 3)
    v2 = Vector(3, 4)
    
    # 使用重载后的 + 运算符
    v3 = v1 + v2
    
    print(f"{v1} + {v2} = {v3}")
    
    # 验证结果
    print(f"v3.x is {v3.x}")
    print(f"v3.y is {v3.y}")
    
    # 验证相等性
    print(f"Is v3 equal to Vector(5, 7)? {v3 == Vector(5, 7)}") 