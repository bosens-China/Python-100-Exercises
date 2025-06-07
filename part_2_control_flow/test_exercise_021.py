import unittest
from part_2_control_flow.exercise_021 import is_leap_year

class TestExercise21(unittest.TestCase):
    def test_is_leap_year(self):
        # 能被 4 整除但不能被 100 整除
        self.assertTrue(is_leap_year(2024))
        self.assertTrue(is_leap_year(1996))

        # 能被 400 整除
        self.assertTrue(is_leap_year(2000))

        # 不能被 4 整除
        self.assertFalse(is_leap_year(2023))
        self.assertFalse(is_leap_year(1997))

        # 能被 100 整除但不能被 400 整除
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2100))

if __name__ == '__main__':
    unittest.main() 