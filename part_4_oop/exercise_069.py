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
    """一个用于演示不同类型方法的计算器类。"""
    
    def __init__(self, owner: str):
        # 实例方法需要一个实例来调用
        self.owner = owner

    def add(self, a: int, b: int) -> int:
        """实例方法：需要一个类的实例才能调用。它可以访问实例属性。"""
        print(f"{self.owner}'s calculator is adding.")
        return a + b
    
    @classmethod
    def info(cls):
        """类方法：通过类本身调用，第一个参数是类（约定为 cls）。"""
        # 为了方便测试，返回字符串
        message = f"This is a {cls.__name__} class."
        print(message)
        return message

    @staticmethod
    def multiply(a: int, b: int) -> int:
        """静态方法：不需要类或实例作为第一个参数。它本质上是放在类命名空间下的一个普通函数。"""
        print("Multiplying...")
        return a * b

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