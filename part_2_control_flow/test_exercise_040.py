import unittest
from part_2_control_flow.exercise_040 import reverse_string

class TestExercise40(unittest.TestCase):
    def test_reverse_string(self):
        # 题目中的例子
        self.assertEqual(reverse_string("python"), "nohtyp")
        
        # 测试回文字符串
        self.assertEqual(reverse_string("madam"), "madam")
        
        # 测试包含空格的字符串
        self.assertEqual(reverse_string("hello world"), "dlrow olleh")
        
        # 测试空字符串
        self.assertEqual(reverse_string(""), "")
        
        # 测试单个字符的字符串
        self.assertEqual(reverse_string("a"), "a")

if __name__ == '__main__':
    unittest.main() 