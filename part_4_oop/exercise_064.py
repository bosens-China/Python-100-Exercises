"""
### 64. 方法重写

- **描述:** 在 `Car` 类中有一个 `fuel_type` 方法返回 "Diesel/Petrol"。在 `ElectricCar` 类中重写这个方法，让它返回 "Electric"。
- **提示:** 在子类中定义一个和父类同名的方法即可。
- **期待:**
  - `my_car.fuel_type()` 返回 "Diesel/Petrol"。
  - `my_tesla.fuel_type()` 返回 "Electric"。
"""

class Car:
    """一个代表汽车的基类。"""
    def __init__(self, brand: str, model: str):
        self.brand = brand
        self.model = model
    
    def fuel_type(self) -> str:
        """返回汽车的燃料类型。"""
        # 在这里写下你的代码
        return "Diesel/Petrol"

class ElectricCar(Car):
    """一个代表电动汽车的子类。"""
    def __init__(self, brand: str, model: str, battery_size: str):
        Car.__init__(self, brand, model)
        self.battery_size = battery_size

    def fuel_type(self) -> str:
        """重写父类的方法，返回电动汽车的燃料类型。"""
        # 在这里写下你的代码
        return "Electric"

if __name__ == '__main__':
    my_car = Car("Toyota", "Camry")
    print(f"My {my_car.brand} car uses {my_car.fuel_type()} fuel.")
    
    my_tesla = ElectricCar("Tesla", "Model 3", "75kWh")
    print(f"My {my_tesla.brand} car uses {my_tesla.fuel_type()} fuel.") 