"""
### 72. 创建一个 `Rectangle` 类

- **描述:** 创建一个 `Rectangle` 类，在 `__init__` 中接受 `width` 和 `height`。添加两个方法 `area()` 和 `perimeter()` 来计算面积和周长。
- **提示:** `area = width * height`, `perimeter = 2 * (width + height)`。
- **期待:** `rect = Rectangle(10, 5)`，`rect.area()` 返回 `50`，`rect.perimeter()` 返回 `30`。
"""

class Rectangle:
    """一个代表矩形的类。"""
    def __init__(self, width: float, height: float):
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative")
        self.width = width
        self.height = height

    def area(self) -> float:
        """计算矩形的面积。"""
        # 在这里写下你的代码
        return self.width * self.height

    def perimeter(self) -> float:
        """计算矩形的周长。"""
        # 在这里写下你的代码
        return 2 * (self.width + self.height)

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(f"一个宽为 {rect.width}，高为 {rect.height} 的矩形：")
    print(f"  面积是: {rect.area()}")
    print(f"  周长是: {rect.perimeter()}")

    rect2 = Rectangle(3.5, 7.2)
    print(f"\n一个宽为 {rect2.width}，高为 {rect2.height} 的矩形：")
    print(f"  面积是: {rect2.area()}")
    print(f"  周长是: {rect2.perimeter()}") 