"""
### 63. 类的继承

- **描述:** 创建一个 `Car` 类，有 `brand` 和 `model` 属性。然后创建一个 `ElectricCar` 类，它继承自 `Car` 类，并有一个额外的 `battery_size` 属性。
- **提示:** `class ElectricCar(Car):`。在 `ElectricCar` 的 `__init__` 中调用父类的 `__init__`。
- **期待:** `my_tesla = ElectricCar("Tesla", "Model S", "100kWh")` 能成功创建对象。
"""

class Car:
    """一个代表汽车的基类。"""
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def get_full_name(self) -> str:
        """返回汽车的完整名称。"""
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    """一个代表电动汽车的子类。"""
    def __init__(self, brand: str, model: str, battery_size: str):
        """
        初始化电动汽车。
        :param brand: 品牌
        :param model: 型号
        :param battery_size: 电池容量
        """
        # 在这里写下你的代码
        # 调用父类的 __init__ 方法
        Car.__init__(self, brand, model)
        self.battery_size = battery_size

    def get_battery_info(self) -> str:
        """返回电池信息。"""
        return f"Battery size: {self.battery_size}"

if __name__ == '__main__':
    my_car = Car("Toyota", "Corolla")
    print(f"My car is a {my_car.get_full_name()}.")
    
    my_tesla = ElectricCar("Tesla", "Model S", "100kWh")
    print(f"My electric car is a {my_tesla.get_full_name()}.")
    print(my_tesla.get_battery_info()) 