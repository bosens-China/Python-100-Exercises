import unittest
from part_3_functions.exercise_053 import operate_on_numbers

# 定义一些用于测试的函数
def add(a, b):
    return a + b

def power(a, b):
    return a ** b

class TestOperateOnNumbers(unittest.TestCase):
    def test_with_add_function(self):
        self.assertEqual(operate_on_numbers(10, 5, add), 15)

    def test_with_lambda_subtract(self):
        subtract = lambda x, y: x - y
        self.assertEqual(operate_on_numbers(10, 5, subtract), 5)

    def test_with_inline_lambda_multiply(self):
        self.assertEqual(operate_on_numbers(10, 5, lambda x, y: x * y), 50)

    def test_with_power_function(self):
        self.assertEqual(operate_on_numbers(2, 3, power), 8)
        
    def test_with_floats(self):
        self.assertAlmostEqual(operate_on_numbers(2.5, 1.5, add), 4.0)
        
    def test_string_concatenation(self):
        concat = lambda s1, s2: s1 + s2
        self.assertEqual(operate_on_numbers("hello", " world", concat), "hello world")

if __name__ == '__main__':
    unittest.main() 