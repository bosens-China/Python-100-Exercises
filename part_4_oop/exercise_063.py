"""
### 63. 类的继承

- **描述:** 创建一个 `Car` 类，有 `brand` 和 `model` 属性。然后创建一个 `ElectricCar` 类，它继承自 `Car` 类，并有一个额外的 `battery_size` 属性。
- **提示:** `class ElectricCar(Car):`。在 `ElectricCar` 的 `__init__` 中调用父类的 `__init__`。
- **期待:** `my_tesla = ElectricCar("Tesla", "Model S", "100kWh")` 能成功创建对象。
"""

class Car:
    """一个代表汽车的基类。"""
    # 在这里写下你的代码
    pass

class ElectricCar(Car):
    """一个代表电动汽车的子类。"""
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    my_car = Car("Toyota", "Corolla")
    print(f"My car is a {my_car.get_full_name()}.")
    
    my_tesla = ElectricCar("Tesla", "Model S", "100kWh")
    print(f"My electric car is a {my_tesla.get_full_name()}.")
    print(my_tesla.get_battery_info()) 