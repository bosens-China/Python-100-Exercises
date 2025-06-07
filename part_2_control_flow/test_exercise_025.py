import unittest
from part_2_control_flow.exercise_025 import find_narcissistic_numbers

class TestExercise25(unittest.TestCase):
    def test_find_narcissistic_numbers(self):
        # 将两个列表转换为集合进行比较，可以忽略元素的顺序
        self.assertSetEqual(set(find_narcissistic_numbers()), {153, 370, 371, 407})

if __name__ == '__main__':
    unittest.main() 