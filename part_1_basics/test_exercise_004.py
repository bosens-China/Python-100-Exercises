import unittest
from part_1_basics.exercise_004 import concatenate_strings

class TestExercise4(unittest.TestCase):
    def test_concatenate_strings(self):
        self.assertEqual(concatenate_strings("Hello", "Python"), "Hello Python")
        self.assertEqual(concatenate_strings("First", "Part"), "First Part")
        self.assertEqual(concatenate_strings("", ""), " ")

if __name__ == '__main__':
    unittest.main() 