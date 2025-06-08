import unittest
from part_2_control_flow.exercise_039 import find_max

class TestExercise39(unittest.TestCase):
    def test_find_max(self):
        # 题目中的例子
        self.assertEqual(find_max([1, 5, 2, 8, 3]), 8)
        
        # 包含负数的列表
        self.assertEqual(find_max([-1, -5, -2, -8, -3]), -1)
        
        # 包含正负数和零的列表
        self.assertEqual(find_max([-2, 0, 5, -8, 3]), 5)
        
        # 只有一个元素的列表
        self.assertEqual(find_max([42]), 42)
        
        # 列表中的最大值在开头
        self.assertEqual(find_max([10, 1, 2, 3]), 10)

        # 测试空列表
        self.assertIsNone(find_max([]))

if __name__ == '__main__':
    unittest.main() 