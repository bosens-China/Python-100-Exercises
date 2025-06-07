import unittest
from part_1_basics.exercise_010 import celsius_to_fahrenheit

class TestExercise10(unittest.TestCase):
    def test_celsius_to_fahrenheit(self):
        # 冰点
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)
        # 沸点
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)
        # 题目中的例子
        self.assertAlmostEqual(celsius_to_fahrenheit(20), 68.0)
        # 负数温度
        self.assertAlmostEqual(celsius_to_fahrenheit(-10), 14.0)

if __name__ == '__main__':
    unittest.main() 