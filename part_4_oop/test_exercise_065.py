import unittest
from part_4_oop.exercise_065 import Car, ElectricCar

class TestSuperFunction(unittest.TestCase):
    def test_electric_car_creation_with_super(self):
        """测试使用 super() 的 ElectricCar 实例创建和所有属性。"""
        my_porsche = ElectricCar("Porsche", "Taycan", "93.4kWh")
        
        # 测试实例类型
        self.assertIsInstance(my_porsche, ElectricCar)
        self.assertIsInstance(my_porsche, Car)
        
        # 测试继承的属性
        self.assertEqual(my_porsche.brand, "Porsche")
        self.assertEqual(my_porsche.model, "Taycan")
        
        # 测试自己的属性
        self.assertEqual(my_porsche.battery_size, "93.4kWh")

if __name__ == '__main__':
    unittest.main() 