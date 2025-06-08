import unittest
from part_4_oop.exercise_063 import Car, ElectricCar

class TestInheritance(unittest.TestCase):
    def test_car_creation(self):
        """测试 Car 类的实例创建和属性。"""
        car = Car("Ford", "Focus")
        self.assertEqual(car.brand, "Ford")
        self.assertEqual(car.model, "Focus")
        self.assertEqual(car.get_full_name(), "Ford Focus")

    def test_electric_car_creation(self):
        """测试 ElectricCar 类的实例创建和所有属性。"""
        my_tesla = ElectricCar("Tesla", "Model S", "100kWh")
        self.assertIsInstance(my_tesla, ElectricCar)
        # 测试继承的属性
        self.assertEqual(my_tesla.brand, "Tesla")
        self.assertEqual(my_tesla.model, "Model S")
        # 测试自己的属性
        self.assertEqual(my_tesla.battery_size, "100kWh")

    def test_electric_car_methods(self):
        """测试 ElectricCar 是否能调用父类和自己的方法。"""
        my_tesla = ElectricCar("Rivian", "R1T", "135kWh")
        # 测试继承的方法
        self.assertEqual(my_tesla.get_full_name(), "Rivian R1T")
        # 测试自己的方法
        self.assertEqual(my_tesla.get_battery_info(), "Battery size: 135kWh")
        
    def test_is_instance_of_car(self):
        """测试 ElectricCar 的实例同时也是 Car 的实例。"""
        my_tesla = ElectricCar("Lucid", "Air", "118kWh")
        self.assertIsInstance(my_tesla, Car)

if __name__ == '__main__':
    unittest.main() 