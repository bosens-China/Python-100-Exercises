"""
### 63. 类的继承

- **描述:** 
  1. 创建一个 `Car` 基类，包含品牌(brand)和型号(model)属性
  2. 实现 `get_full_name()` 方法返回完整车型名称
  3. 创建 `ElectricCar` 子类继承 `Car` 类，增加电池容量(battery_size)属性

- **提示:**
  1. 使用 `class ElectricCar(Car):` 语法实现继承
  2. 在子类 `__init__` 中使用 `super()` 调用父类初始化方法
  3. 子类需添加 `get_battery_info()` 方法返回电池信息

- **期待:**
  1. `my_car = Car("Toyota", "Corolla")` 能正确创建实例
  2. `my_tesla = ElectricCar("Tesla", "Model S", "100kWh")` 能正确创建实例
  3. 能通过 `isinstance(my_tesla, Car)` 测试
  4. 能正确调用继承和新增的方法
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