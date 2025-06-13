"""
### 88. `math` 模块

- **描述:** 使用 `math` 模块计算数字 81 的平方根，并获取圆周率 π 的值。
- **提示:** 使用 `math.sqrt()` 和 `math.pi`。
- **期待:** 输出 `9.0` 和 `3.141592653589793`。
"""
import math

def get_sqrt_and_pi(number):
    """
    计算一个数的平方根和圆周率 pi 的值。
    如果输入是负数，则应抛出 ValueError。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    num_to_sqrt = 81
    sqrt_val, pi = get_sqrt_and_pi(num_to_sqrt)
    
    print(f"{num_to_sqrt} 的平方根是: {sqrt_val}")
    print(f"PI 的值是: {pi}") 