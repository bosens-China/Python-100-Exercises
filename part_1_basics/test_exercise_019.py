import unittest
from part_1_basics.exercise_019 import remove_duplicates

class TestExercise19(unittest.TestCase):
    def test_remove_duplicates(self):
        numbers = [1, 2, 3, 2, 4, 5, 4, 1]
        self.assertEqual(remove_duplicates(numbers), {1, 2, 3, 4, 5})

        words = ["hello", "world", "hello"]
        self.assertEqual(remove_duplicates(words), {"hello", "world"})

        empty_list = []
        self.assertEqual(remove_duplicates(empty_list), set())

if __name__ == '__main__':
    unittest.main() 