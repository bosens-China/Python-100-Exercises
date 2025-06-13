"""
### 64. 方法重写

- **描述:** 在 `Car` 类中有一个 `fuel_type` 方法返回 "Diesel/Petrol"。在 `ElectricCar` 类中重写这个方法，让它返回 "Electric"。
- **提示:** 在子类中定义一个和父类同名的方法即可。
- **期待:**
  - `my_car.fuel_type()` 返回 "Diesel/Petrol"。
  - `my_tesla.fuel_type()` 返回 "Electric"。
"""

class Car:
    # 在这里写下你的代码
    pass

class ElectricCar(Car):
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    my_car = Car("Toyota", "Camry")
    print(f"My {my_car.brand} car uses {my_car.fuel_type()} fuel.")
    
    my_tesla = ElectricCar("Tesla", "Model 3", "75kWh")
    print(f"My {my_tesla.brand} car uses {my_tesla.fuel_type()} fuel.") 