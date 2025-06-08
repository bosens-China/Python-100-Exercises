"""
### 65. `super()` 函数

- **描述:** 修改第 63 题中 `ElectricCar` 的 `__init__` 方法，使用 `super()` 来调用父类 `Car` 的 `__init__` 方法。
- **提示:** `super().__init__(brand, model)`。
- **期待:** 功能与第 63 题相同，但代码更规范、更易于维护。
"""

class Car:
    """一个代表汽车的基类。"""
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model

class ElectricCar(Car):
    """一个代表电动汽车的子类。"""
    def __init__(self, brand: str, model: str, battery_size: str):
        """
        初始化电动汽车，使用 super() 调用父类构造器。
        """
        # 在这里写下你的代码
        super().__init__(brand, model)
        self.battery_size = battery_size

if __name__ == '__main__':
    my_nio = ElectricCar("NIO", "ET7", "150kWh")
    
    # 验证属性是否被正确设置
    print(f"Brand: {my_nio.brand}")
    print(f"Model: {my_nio.model}")
    print(f"Battery Size: {my_nio.battery_size}") 