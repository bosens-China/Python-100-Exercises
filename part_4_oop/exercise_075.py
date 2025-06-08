"""
### 75. 运算符重载

- **描述:** 创建一个 `Vector` 类，表示二维向量（有 `x` 和 `y` 属性）。重载 `+` 运算符（使用 `__add__` 方法），使其能够将两个向量相加。
- **提示:** `def __add__(self, other): return Vector(self.x + other.x, self.y + other.y)`
- **期待:** `v1 = Vector(2, 3)`, `v2 = Vector(3, 4)`, `v3 = v1 + v2`，则 `v3.x` 为 `5`，`v3.y` 为 `7`。
"""

class Vector:
    """一个代表二维向量的类，支持向量加法。"""
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __add__(self, other):
        """重载 + 运算符以实现向量加法。"""
        # 在这里写下你的代码
        if not isinstance(other, Vector):
            # 为了简单起见，我们只支持 Vector + Vector
            # 更完善的实现可能会处理与其他类型的相加
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self) -> str:
        """提供一个明确的字符串表示。"""
        return f"Vector({self.x}, {self.y})"
        
    def __eq__(self, other) -> bool:
        """重载 == 运算符以比较两个向量是否相等，这对于测试很有用。"""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

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