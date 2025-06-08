import unittest
import math
from part_6_standard_library.exercise_088 import get_sqrt_and_pi

class TestMathModule(unittest.TestCase):
    def test_sqrt_and_pi(self):
        """测试函数能否正确返回平方根和 pi 的值。"""
        sqrt_val, pi_val = get_sqrt_and_pi(81)
        
        # 测试平方根
        self.assertEqual(sqrt_val, 9.0)
        
        # 测试 pi 的值
        self.assertEqual(pi_val, math.pi)
        
    def test_with_another_number(self):
        """用另一个数字测试。"""
        sqrt_val, pi_val = get_sqrt_and_pi(16)
        self.assertEqual(sqrt_val, 4.0)
        self.assertEqual(pi_val, math.pi)

    def test_with_float_number(self):
        """用浮点数测试。"""
        sqrt_val, pi_val = get_sqrt_and_pi(2.25)
        self.assertEqual(sqrt_val, 1.5)
        self.assertEqual(pi_val, math.pi)
        
    def test_with_zero(self):
        """用 0 测试。"""
        sqrt_val, pi_val = get_sqrt_and_pi(0)
        self.assertEqual(sqrt_val, 0.0)
        self.assertEqual(pi_val, math.pi)
        
    def test_with_negative_number(self):
        """测试负数输入会引发 ValueError。"""
        with self.assertRaises(ValueError):
            get_sqrt_and_pi(-1)

if __name__ == '__main__':
    unittest.main() 