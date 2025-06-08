import unittest
from part_4_oop.exercise_064 import Car, ElectricCar

class TestMethodOverriding(unittest.TestCase):
    def test_car_fuel_type(self):
        """测试 Car 实例的 fuel_type 方法。"""
        my_car = Car("Honda", "Civic")
        self.assertEqual(my_car.fuel_type(), "Diesel/Petrol")

    def test_electric_car_fuel_type(self):
        """测试 ElectricCar 实例重写后的 fuel_type 方法。"""
        my_tesla = ElectricCar("Tesla", "Model Y", "82kWh")
        self.assertEqual(my_tesla.fuel_type(), "Electric")
        
    def test_another_car(self):
        """再测试一个普通汽车实例，确保其行为不受子类影响。"""
        another_car = Car("Ford", "Mustang")
        self.assertEqual(another_car.fuel_type(), "Diesel/Petrol")

if __name__ == '__main__':
    unittest.main() 