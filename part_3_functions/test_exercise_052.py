import unittest
from part_3_functions.exercise_052 import product_of_list
from functools import reduce

class TestProductOfList(unittest.TestCase):
    def test_basic_case(self):
        self.assertEqual(product_of_list([1, 2, 3, 4]), 24)

    def test_empty_list(self):
        # 根据我们函数的定义，空列表的乘积为1
        self.assertEqual(product_of_list([]), 1)

    def test_single_item(self):
        self.assertEqual(product_of_list([10]), 10)

    def test_with_zero(self):
        self.assertEqual(product_of_list([1, 2, 0, 4, 5]), 0)

    def test_with_negatives(self):
        self.assertEqual(product_of_list([-1, 2, -3, 4]), 24)
        self.assertEqual(product_of_list([-1, -2, -3]), -6)
        
    def test_against_alternative_implementation(self):
        # 与提供了初始值的 reduce 函数进行比较
        self.assertEqual(product_of_list([5, 5, 5]), reduce(lambda x,y: x*y, [5, 5, 5], 1))

if __name__ == '__main__':
    unittest.main() 