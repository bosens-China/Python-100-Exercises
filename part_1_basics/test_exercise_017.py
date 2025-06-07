import unittest
from part_1_basics.exercise_017 import get_student_age

class TestExercise17(unittest.TestCase):
    def test_get_student_age(self):
        student1 = {'name': 'Alice', 'age': 20, 'score': 90}
        self.assertEqual(get_student_age(student1), 20)

        student2 = {'name': 'Bob', 'city': 'Beijing', 'age': 25}
        self.assertEqual(get_student_age(student2), 25)

if __name__ == '__main__':
    unittest.main() 