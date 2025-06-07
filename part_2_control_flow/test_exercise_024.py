import unittest
from part_2_control_flow.exercise_024 import sum_1_to_100

class TestExercise24(unittest.TestCase):
    def test_sum_1_to_100(self):
        self.assertEqual(sum_1_to_100(), 5050)

if __name__ == '__main__':
    unittest.main() 