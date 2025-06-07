import unittest
from part_2_control_flow.exercise_026 import generate_fibonacci

class TestExercise26(unittest.TestCase):
    def test_generate_fibonacci(self):
        # 测试前 10 个数
        expected_10 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        self.assertEqual(generate_fibonacci(10), expected_10)

        # 测试题目要求的前 20 个数
        expected_20 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
        self.assertEqual(generate_fibonacci(20), expected_20)

        # 测试边界情况
        self.assertEqual(generate_fibonacci(0), [])
        self.assertEqual(generate_fibonacci(1), [0])
        self.assertEqual(generate_fibonacci(2), [0, 1])

if __name__ == '__main__':
    unittest.main() 