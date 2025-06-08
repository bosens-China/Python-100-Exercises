import unittest
from part_2_control_flow.exercise_038 import deduplicate_list

class TestExercise38(unittest.TestCase):
    def test_deduplicate_list(self):
        # 题目中的例子
        self.assertEqual(deduplicate_list([1, 2, 2, 3, 4, 3]), [1, 2, 3, 4])
        
        # 测试字符串列表
        self.assertEqual(deduplicate_list(["apple", "banana", "apple", "cherry"]), ["apple", "banana", "cherry"])
        
        # 测试没有重复元素的列表
        self.assertEqual(deduplicate_list([10, 20, 30]), [10, 20, 30])
        
        # 测试空列表
        self.assertEqual(deduplicate_list([]), [])
        
        # 测试包含混合类型的列表
        self.assertEqual(deduplicate_list([1, "a", 1, "b", "a"]), [1, "a", "b"])

if __name__ == '__main__':
    unittest.main() 