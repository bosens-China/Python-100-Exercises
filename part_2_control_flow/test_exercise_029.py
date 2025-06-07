import unittest
from part_2_control_flow.exercise_029 import is_prime

class TestExercise29(unittest.TestCase):
    def test_is_prime(self):
        # 质数
        self.assertTrue(is_prime(2))
        self.assertTrue(is_prime(3))
        self.assertTrue(is_prime(13))
        self.assertTrue(is_prime(97))

        # 合数
        self.assertFalse(is_prime(4))
        self.assertFalse(is_prime(12))
        self.assertFalse(is_prime(99))
        self.assertFalse(is_prime(100))

        # 边界情况
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))
        self.assertFalse(is_prime(-5))

if __name__ == '__main__':
    unittest.main() 