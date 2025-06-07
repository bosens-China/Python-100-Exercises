import unittest
from part_1_basics.exercise_020 import get_types_of_variables

class TestExercise20(unittest.TestCase):
    def test_get_types_of_variables(self):
        # 假设函数按顺序返回 int, float, str, list, dict, tuple, set 的类型
        types = get_types_of_variables()
        expected_types = [int, float, str, list, dict, tuple, set]
        
        # 确保返回了正确数量的类型
        self.assertEqual(len(types), len(expected_types))
        
        # 逐一检查类型是否匹配
        for i in range(len(types)):
            self.assertEqual(types[i], expected_types[i])


if __name__ == '__main__':
    unittest.main() 