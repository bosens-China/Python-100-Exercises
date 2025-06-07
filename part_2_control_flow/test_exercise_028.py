import unittest
from part_2_control_flow.exercise_028 import generate_triangle

class TestExercise28(unittest.TestCase):
    def test_generate_triangle(self):
        # 测试高度为 5
        expected_5 = "*\n**\n***\n****\n*****\n"
        self.assertEqual(generate_triangle(5), expected_5)

        # 测试高度为 3
        expected_3 = "*\n**\n***\n"
        self.assertEqual(generate_triangle(3), expected_3)

        # 测试高度为 1
        expected_1 = "*\n"
        self.assertEqual(generate_triangle(1), expected_1)
        
        # 测试高度为 0
        expected_0 = ""
        self.assertEqual(generate_triangle(0), expected_0)

if __name__ == '__main__':
    unittest.main() 