from part_4_oop.exercise_064 import Car, ElectricCar

def test_car_fuel_type():
    """测试 Car 实例的 fuel_type 方法。"""
    my_car = Car("Honda", "Civic")
    assert my_car.fuel_type() == "Diesel/Petrol"

def test_electric_car_fuel_type():
    """测试 ElectricCar 实例重写后的 fuel_type 方法。"""
    my_tesla = ElectricCar("Tesla", "Model Y", "82kWh")
    assert my_tesla.fuel_type() == "Electric"
    
def test_another_car():
    """再测试一个普通汽车实例，确保其行为不受子类影响。"""
    another_car = Car("Ford", "Mustang")
    assert another_car.fuel_type() == "Diesel/Petrol" 