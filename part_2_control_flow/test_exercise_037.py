import unittest
from part_2_control_flow.exercise_037 import get_even_numbers

class TestExercise37(unittest.TestCase):
    def test_get_even_numbers(self):
        self.assertEqual(get_even_numbers([1, 2, 3, 4, 5, 6]), [2, 4, 6])
        self.assertEqual(get_even_numbers([1, 3, 5, 7]), [])
        self.assertEqual(get_even_numbers([2, 4, 6, 8]), [2, 4, 6, 8])
        self.assertEqual(get_even_numbers([-2, -1, 0, 1, 2]), [-2, 0, 2])
        self.assertEqual(get_even_numbers([]), [])

if __name__ == '__main__':
    unittest.main() 