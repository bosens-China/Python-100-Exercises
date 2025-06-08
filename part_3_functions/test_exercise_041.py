import unittest
from part_3_functions.exercise_041 import greet

class TestExercise41(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertEqual(greet("World"), "Hello, World!")

if __name__ == '__main__':
    unittest.main() 