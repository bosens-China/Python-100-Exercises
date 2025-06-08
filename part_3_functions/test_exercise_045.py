import unittest
from part_3_functions.exercise_045 import sum_all

class TestSumAll(unittest.TestCase):
    def test_multiple_arguments(self):
        self.assertEqual(sum_all(1, 2, 3, 4, 5), 15)

    def test_two_arguments(self):
        self.assertEqual(sum_all(10, 20), 30)
        
    def test_negative_numbers(self):
        self.assertEqual(sum_all(-1, -2, -3), -6)

    def test_mixed_numbers(self):
        self.assertEqual(sum_all(1, -2, 3, -4), -2)

    def test_no_arguments(self):
        self.assertEqual(sum_all(), 0)
        
    def test_one_argument(self):
        self.assertEqual(sum_all(100), 100)

if __name__ == '__main__':
    unittest.main() 