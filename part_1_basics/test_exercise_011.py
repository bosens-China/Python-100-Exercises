import unittest
from part_1_basics.exercise_011 import check_odd_even

class TestExercise11(unittest.TestCase):
    def test_check_odd_even(self):
        self.assertEqual(check_odd_even(7), "奇数")
        self.assertEqual(check_odd_even(4), "偶数")
        self.assertEqual(check_odd_even(0), "偶数")
        self.assertEqual(check_odd_even(-1), "奇数")
        self.assertEqual(check_odd_even(-2), "偶数")

if __name__ == '__main__':
    unittest.main() 