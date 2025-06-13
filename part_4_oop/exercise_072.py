"""
### 72. 创建一个 `Rectangle` 类

- **描述:** 创建一个 `Rectangle` 类，在 `__init__` 中接受 `width` 和 `height`。添加两个方法 `area()` 和 `perimeter()` 来计算面积和周长。
- **提示:** `area = width * height`, `perimeter = 2 * (width + height)`。
- **期待:** `rect = Rectangle(10, 5)`，`rect.area()` 返回 `50`，`rect.perimeter()` 返回 `30`。
"""

class Rectangle:
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    rect = Rectangle(10, 5)
    print(f"一个宽为 {rect.width}，高为 {rect.height} 的矩形：")
    print(f"  面积是: {rect.area()}")
    print(f"  周长是: {rect.perimeter()}")

    rect2 = Rectangle(3.5, 7.2)
    print(f"\n一个宽为 {rect2.width}，高为 {rect2.height} 的矩形：")
    print(f"  面积是: {rect2.area()}")
    print(f"  周长是: {rect2.perimeter()}") 