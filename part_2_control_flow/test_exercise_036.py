import unittest
from part_2_control_flow.exercise_036 import simple_calculator

class TestExercise36(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(simple_calculator(10, '+', 5), 15)

    def test_subtraction(self):
        self.assertEqual(simple_calculator(10, '-', 5), 5)

    def test_multiplication(self):
        self.assertEqual(simple_calculator(10, '*', 5), 50)

    def test_division(self):
        self.assertEqual(simple_calculator(10, '/', 5), 2.0)

    def test_division_by_zero(self):
        self.assertEqual(simple_calculator(10, '/', 0), "错误：除数不能为零！")

    def test_invalid_operator(self):
        self.assertIsNone(simple_calculator(10, '%', 5)) # 或者返回特定的错误信息

if __name__ == '__main__':
    unittest.main() 