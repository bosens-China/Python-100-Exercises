import unittest
import io
import sys
from part_1_basics.exercise_001 import hello_world

class TestExercise1(unittest.TestCase):
    def test_hello_world(self):
        # 准备捕获标准输出
        captured_output = io.StringIO()
        sys.stdout = captured_output

        hello_world()

        # 恢复标准输出
        sys.stdout = sys.__stdout__

        # 检查输出是否符合预期
        self.assertEqual(captured_output.getvalue(), "Hello, World!\n")

if __name__ == '__main__':
    unittest.main() 