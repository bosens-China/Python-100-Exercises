import unittest
from part_4_oop.exercise_074 import Flyable, Swimmable, Duck

class TestMultipleInheritance(unittest.TestCase):
    def setUp(self):
        self.duck = Duck()

    def test_duck_can_fly(self):
        """测试 Duck 实例是否从 Flyable 继承了 fly 方法。"""
        self.assertEqual(self.duck.fly(), "I am flying!")

    def test_duck_can_swim(self):
        """测试 Duck 实例是否从 Swimmable 继承了 swim 方法。"""
        self.assertEqual(self.duck.swim(), "I am swimming!")
        
    def test_duck_can_quack(self):
        """测试 Duck 实例是否有自己的 quack 方法。"""
        self.assertEqual(self.duck.quack(), "Quack! Quack!")
        
    def test_duck_is_instance_of_all(self):
        """测试 Duck 实例是否是所有父类的实例。"""
        self.assertIsInstance(self.duck, Duck)
        self.assertIsInstance(self.duck, Flyable)
        self.assertIsInstance(self.duck, Swimmable)

if __name__ == '__main__':
    unittest.main() 