import unittest
from part_3_functions.exercise_048 import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial_of_5(self):
        self.assertEqual(factorial(5), 120)

    def test_factorial_of_0(self):
        # 测试基本情况
        self.assertEqual(factorial(0), 1)

    def test_factorial_of_1(self):
        self.assertEqual(factorial(1), 1)
        
    def test_factorial_of_10(self):
        self.assertEqual(factorial(10), 3628800)

    def test_negative_input(self):
        # 测试无效输入（负数）
        with self.assertRaises(ValueError):
            factorial(-1)
            
    def test_non_integer_input(self):
        # 测试无效输入（非整数）
        with self.assertRaises(ValueError):
            factorial(1.5)

if __name__ == '__main__':
    unittest.main() 