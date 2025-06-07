import unittest
from part_1_basics.exercise_002 import swap_variables

class TestExercise2(unittest.TestCase):
    def test_swap_variables(self):
        # 测试整数
        a, b = 5, 10
        swapped_a, swapped_b = swap_variables(a, b)
        self.assertEqual(swapped_a, 10)
        self.assertEqual(swapped_b, 5)

        # 测试字符串
        x, y = "hello", "world"
        swapped_x, swapped_y = swap_variables(x, y)
        self.assertEqual(swapped_x, "world")
        self.assertEqual(swapped_y, "hello")

if __name__ == '__main__':
    unittest.main() 