import unittest
from part_2_control_flow.exercise_035 import count_vowels

class TestExercise35(unittest.TestCase):
    def test_count_vowels(self):
        self.assertEqual(count_vowels("Hello Python"), 3) # e, o, o
        self.assertEqual(count_vowels("AEIOU aeiou"), 10)
        self.assertEqual(count_vowels("Rhythm"), 0)
        self.assertEqual(count_vowels(""), 0)
        self.assertEqual(count_vowels("This is a test sentence."), 7)

if __name__ == '__main__':
    unittest.main() 