import unittest
from part_1_basics.exercise_012 import is_in_range

class TestExercise12(unittest.TestCase):
    def test_is_in_range(self):
        # 在范围内
        self.assertTrue(is_in_range(22))
        # 边界值
        self.assertTrue(is_in_range(18))
        self.assertTrue(is_in_range(30))
        # 在范围外
        self.assertFalse(is_in_range(17))
        self.assertFalse(is_in_range(31))
        self.assertFalse(is_in_range(10))

if __name__ == '__main__':
    unittest.main() 