import unittest
from part_3_functions.exercise_043 import greet_with_default

class TestExercise43(unittest.TestCase):
    def test_greet_with_default(self):
        # 测试提供了参数的情况
        self.assertEqual(greet_with_default("Bob"), "Hello, Bob!")
        
        # 测试没有提供参数，使用默认值的情况
        self.assertEqual(greet_with_default(), "Hello, World!")

if __name__ == '__main__':
    unittest.main() 