import unittest
from part_2_control_flow.exercise_030 import generate_squares

class TestExercise30(unittest.TestCase):
    def test_generate_squares(self):
        expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(generate_squares(), expected)

if __name__ == '__main__':
    unittest.main() 