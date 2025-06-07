import unittest
from part_1_basics.exercise_008 import create_intro_string

class TestExercise8(unittest.TestCase):
    def test_create_intro_string(self):
        self.assertEqual(create_intro_string("Bob", 25), "Bob is 25 years old.")
        self.assertEqual(create_intro_string("Alice", 30), "Alice is 30 years old.")

if __name__ == '__main__':
    unittest.main() 