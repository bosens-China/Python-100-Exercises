"""
### 3. 计算圆的面积

- **描述:** 编写一个程序，计算给定半径的圆的面积。假设半径为 `r = 5`。
- **提示:** 圆的面积公式是 π * r²。你可以使用 `3.14159` 作为 π 的近似值，或者导入 `math` 模块使用 `math.pi`。`**` 是 Python 中的幂运算符。
- **期待:** 如果半径是 `5`，程序应该输出 `78.53975` (使用 `3.14159`) 或 `78.53981633974483` (使用 `math.pi`)。
"""
import math

def calculate_circle_area(radius):
    """
    计算圆的面积
    :param radius: 圆的半径
    :return: 圆的面积
    """
    # 在这里写下你的代码
    # 建议使用 math.pi 以获得更精确的结果
    pass

if __name__ == '__main__':
    r = 5
    area = calculate_circle_area(r)
    print(f"半径为 {r} 的圆的面积是: {area}") 