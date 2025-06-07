import unittest
from part_2_control_flow.exercise_031 import create_dict_from_list

class TestExercise31(unittest.TestCase):
    def test_create_dict_from_list(self):
        keys = ["name", "age", "city"]
        expected = {'name': 4, 'age': 3, 'city': 4}
        self.assertDictEqual(create_dict_from_list(keys), expected)

        keys2 = ["python", "is", "fun"]
        expected2 = {'python': 6, 'is': 2, 'fun': 3}
        self.assertDictEqual(create_dict_from_list(keys2), expected2)

        keys3 = []
        expected3 = {}
        self.assertDictEqual(create_dict_from_list(keys3), expected3)

if __name__ == '__main__':
    unittest.main() 