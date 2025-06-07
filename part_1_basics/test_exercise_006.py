import unittest
from part_1_basics.exercise_006 import get_substring

class TestExercise6(unittest.TestCase):
    def test_get_substring(self):
        self.assertEqual(get_substring("Programming"), "gram")
        self.assertEqual(get_substring("testing_gram_slice"), "gram")

if __name__ == '__main__':
    unittest.main() 