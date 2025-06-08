import unittest
from part_3_functions.exercise_051 import filter_even_numbers

class TestFilterEvenNumbers(unittest.TestCase):
    def test_mixed_list(self):
        self.assertEqual(filter_even_numbers([1, 2, 3, 4, 5]), [2, 4])

    def test_all_evens(self):
        self.assertEqual(filter_even_numbers([2, 4, 6, 8]), [2, 4, 6, 8])

    def test_all_odds(self):
        self.assertEqual(filter_even_numbers([1, 3, 5, 7]), [])

    def test_empty_list(self):
        self.assertEqual(filter_even_numbers([]), [])

    def test_with_zero_and_negatives(self):
        self.assertEqual(filter_even_numbers([-2, -1, 0, 1, 2, 3, 4]), [-2, 0, 2, 4])

if __name__ == '__main__':
    unittest.main() 