import unittest
from part_2_control_flow.exercise_032 import search_in_list

class TestExercise32(unittest.TestCase):
    def setUp(self):
        self.my_list = [1, 2, 3, 4]

    def test_item_found(self):
        self.assertEqual(search_in_list(self.my_list, 3), "找到了")
        self.assertEqual(search_in_list(self.my_list, 1), "找到了")

    def test_item_not_found(self):
        self.assertEqual(search_in_list(self.my_list, 5), "没找到")
        self.assertEqual(search_in_list(self.my_list, 0), "没找到")

    def test_empty_list(self):
        self.assertEqual(search_in_list([], 5), "没找到")

if __name__ == '__main__':
    unittest.main() 