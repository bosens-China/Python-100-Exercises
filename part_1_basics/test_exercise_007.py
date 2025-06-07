import unittest
from part_1_basics.exercise_007 import format_string

class TestExercise7(unittest.TestCase):
    def test_format_string(self):
        s = "  pyThon ProGramming  "
        upper_case, lower_case, stripped = format_string(s)
        self.assertEqual(upper_case, "PYTHON PROGRAMMING")
        self.assertEqual(lower_case, "python programming")
        self.assertEqual(stripped, "pyThon ProGramming")

        s2 = "  Another Test  "
        upper_case2, lower_case2, stripped2 = format_string(s2)
        self.assertEqual(upper_case2, "ANOTHER TEST")
        self.assertEqual(lower_case2, "another test")
        self.assertEqual(stripped2, "Another Test")

if __name__ == '__main__':
    unittest.main() 