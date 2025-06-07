import unittest
from part_1_basics.exercise_009 import calculate_rectangle_properties

class TestExercise9(unittest.TestCase):
    def test_calculate_rectangle_properties(self):
        # 测试 length=10, width=5
        perimeter, area = calculate_rectangle_properties(10, 5)
        self.assertEqual(perimeter, 30)
        self.assertEqual(area, 50)

        # 测试其他值
        perimeter, area = calculate_rectangle_properties(3, 4)
        self.assertEqual(perimeter, 14)
        self.assertEqual(area, 12)

if __name__ == '__main__':
    unittest.main() 