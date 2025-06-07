import unittest
import math
from part_1_basics.exercise_003 import calculate_circle_area

class TestExercise3(unittest.TestCase):
    def test_calculate_circle_area(self):
        # 测试半径为 5 的情况
        self.assertAlmostEqual(calculate_circle_area(5), math.pi * 5 * 5)
        # 测试半径为 1 的情况
        self.assertAlmostEqual(calculate_circle_area(1), math.pi)
        # 测试半径为 0 的情况
        self.assertAlmostEqual(calculate_circle_area(0), 0)

if __name__ == '__main__':
    unittest.main() 