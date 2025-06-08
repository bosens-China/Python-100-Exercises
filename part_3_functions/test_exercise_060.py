import unittest
from part_3_functions.exercise_060 import bubble_sort

class TestBubbleSort(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8]), [1, 2, 4, 5, 8])

    def test_already_sorted(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_with_duplicates(self):
        self.assertEqual(bubble_sort([5, 1, 4, 2, 8, 4, 1]), [1, 1, 2, 4, 4, 5, 8])

    def test_with_negatives(self):
        self.assertEqual(bubble_sort([-5, 1, -4, 2, 0]), [-5, -4, 0, 1, 2])

    def test_empty_list(self):
        self.assertEqual(bubble_sort([]), [])

    def test_single_element(self):
        self.assertEqual(bubble_sort([100]), [100])
        
    def test_original_list_is_unchanged(self):
        original_list = [5, 1, 4, 2, 8]
        # 创建一个副本以进行比较
        original_list_copy = original_list[:]
        bubble_sort(original_list)
        self.assertEqual(original_list, original_list_copy)

if __name__ == '__main__':
    unittest.main() 