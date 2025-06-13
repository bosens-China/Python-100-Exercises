"""
### 69. `@classmethod` 和 `@staticmethod`

- **描述:** 在一个 `Calculator` 类中，添加一个实例方法 `add` (需要实例)，一个 `@classmethod` 方法 `info` (打印类信息，需要类)，和一个 `@staticmethod` 方法 `multiply` (只是一个相关的函数，不需要类或实例)。
- **提示:** 静态方法就像一个放在类里面的普通函数，类方法第一个参数是类本身(通常是`cls`)。
- **期待:**
  - `calc = Calculator(); calc.add(2, 3)`
  - `Calculator.info()`
  - `Calculator.multiply(3, 4)`
"""

class Calculator:
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 调用实例方法
    print("--- 实例方法调用 ---")
    calc = Calculator("Alice")
    sum_result = calc.add(2, 3)
    print(f"2 + 3 = {sum_result}")
    
    # 调用类方法
    print("\n--- 类方法调用 ---")
    # 可以通过类或实例调用，但通常通过类调用
    Calculator.info()
    calc.info() # 也可以工作
    
    # 调用静态方法
    print("\n--- 静态方法调用 ---")
    # 可以通过类或实例调用，但通常通过类调用
    product_result = Calculator.multiply(3, 4)
    print(f"3 * 4 = {product_result}")
    product_result_2 = calc.multiply(5, 6) # 也可以工作
    print(f"5 * 6 = {product_result_2}") 