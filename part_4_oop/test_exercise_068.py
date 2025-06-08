import unittest
import math
from part_4_oop.exercise_068 import Circle

class TestCircleProperty(unittest.TestCase):
    def test_initialization(self):
        """测试 Circle 是否能用有效半径正确初始化。"""
        c = Circle(5)
        self.assertEqual(c._radius, 5) # 直接测试内部变量以避免 getter 的 print
        self.assertEqual(c.radius, 5)   # 测试 getter

    def test_initialization_with_negative_radius(self):
        """测试用负半径初始化时是否会引发 ValueError。"""
        with self.assertRaises(ValueError):
            Circle(-5)

    def test_setter(self):
        """测试 radius 的 setter 是否能正确更新值。"""
        c = Circle(5)
        c.radius = 10
        self.assertEqual(c._radius, 10)
        self.assertEqual(c.radius, 10)

    def test_setter_with_negative_value(self):
        """测试给 radius 设置负值时是否会引发 ValueError。"""
        c = Circle(5)
        with self.assertRaises(ValueError):
            c.radius = -10
        # 验证半径值没有被改变
        self.assertEqual(c.radius, 5)

    def test_area_property(self):
        """测试 area 属性是否能正确计算面积。"""
        c = Circle(10)
        expected_area = math.pi * 100
        self.assertAlmostEqual(c.area, expected_area)

    def test_area_is_readonly(self):
        """测试 area 属性是否是只读的。"""
        c = Circle(10)
        with self.assertRaises(AttributeError):
            c.area = 500

if __name__ == '__main__':
    unittest.main() 