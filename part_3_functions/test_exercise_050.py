import unittest
from part_3_functions.exercise_050 import square_list_with_map

class TestSquareListWithMap(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(square_list_with_map([1, 2, 3, 4, 5]), [1, 4, 9, 16, 25])

    def test_empty_list(self):
        self.assertEqual(square_list_with_map([]), [])

    def test_mixed_numbers(self):
        self.assertEqual(square_list_with_map([-1, -2, 0, 3]), [1, 4, 0, 9])
        
    def test_floats(self):
        self.assertEqual(square_list_with_map([1.5, 2.0]), [2.25, 4.0])

if __name__ == '__main__':
    unittest.main() 