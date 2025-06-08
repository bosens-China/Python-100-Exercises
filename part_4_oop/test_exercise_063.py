from part_4_oop.exercise_063 import Car, ElectricCar

def test_car_creation():
    """测试 Car 类的实例创建和属性。"""
    car = Car("Ford", "Focus")
    assert car.brand == "Ford"
    assert car.model == "Focus"
    assert car.get_full_name() == "Ford Focus"

def test_electric_car_creation():
    """测试 ElectricCar 类的实例创建和所有属性。"""
    my_tesla = ElectricCar("Tesla", "Model S", "100kWh")
    assert isinstance(my_tesla, ElectricCar)
    # 测试继承的属性
    assert my_tesla.brand == "Tesla"
    assert my_tesla.model == "Model S"
    # 测试自己的属性
    assert my_tesla.battery_size == "100kWh"

def test_electric_car_methods():
    """测试 ElectricCar 是否能调用父类和自己的方法。"""
    my_tesla = ElectricCar("Rivian", "R1T", "135kWh")
    # 测试继承的方法
    assert my_tesla.get_full_name() == "Rivian R1T"
    # 测试自己的方法
    assert my_tesla.get_battery_info() == "Battery size: 135kWh"
    
def test_is_instance_of_car():
    """测试 ElectricCar 的实例同时也是 Car 的实例。"""
    my_tesla = ElectricCar("Lucid", "Air", "118kWh")
    assert isinstance(my_tesla, Car) 