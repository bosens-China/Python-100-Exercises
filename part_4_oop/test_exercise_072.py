import unittest
from part_4_oop.exercise_072 import Rectangle

class TestRectangle(unittest.TestCase):
    def test_integer_dimensions(self):
        """测试整数尺寸的矩形。"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)
        self.assertEqual(rect.perimeter(), 30)

    def test_float_dimensions(self):
        """测试浮点数尺寸的矩形。"""
        rect = Rectangle(3.5, 7.2)
        # 使用 assertAlmostEqual 来处理浮点数计算可能带来的微小误差
        self.assertAlmostEqual(rect.area(), 25.2)
        self.assertAlmostEqual(rect.perimeter(), 21.4)

    def test_square(self):
        """测试正方形（宽和高相等）的情况。"""
        square = Rectangle(6, 6)
        self.assertEqual(square.area(), 36)
        self.assertEqual(square.perimeter(), 24)

    def test_zero_dimension(self):
        """测试当某个尺寸为0时的情况。"""
        rect = Rectangle(10, 0)
        self.assertEqual(rect.area(), 0)
        self.assertEqual(rect.perimeter(), 20)
        
        rect2 = Rectangle(0, 0)
        self.assertEqual(rect2.area(), 0)
        self.assertEqual(rect2.perimeter(), 0)
        
    def test_negative_dimension(self):
        """测试当某个尺寸为负数时，是否会引发 ValueError。"""
        with self.assertRaises(ValueError):
            Rectangle(-10, 5)
            
        with self.assertRaises(ValueError):
            Rectangle(10, -5)
            
        with self.assertRaises(ValueError):
            Rectangle(-10, -5)

if __name__ == '__main__':
    unittest.main() 