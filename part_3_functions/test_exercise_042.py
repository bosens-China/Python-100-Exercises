import unittest
from part_3_functions.exercise_042 import add

class TestExercise42(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-5, 3), -2)
        self.assertEqual(add(0, 0), 0)
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)

if __name__ == '__main__':
    unittest.main() 