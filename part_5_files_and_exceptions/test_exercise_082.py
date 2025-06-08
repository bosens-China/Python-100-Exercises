import unittest
from io import StringIO
from contextlib import redirect_stdout
from part_5_files_and_exceptions.exercise_082 import divide

class TestSpecificExceptions(unittest.TestCase):
    def test_successful_division(self):
        """测试成功的除法运算。"""
        self.assertEqual(divide(10, 2), 5.0)
        self.assertEqual(divide(10, 4), 2.5)
        self.assertEqual(divide(-10, 2), -5.0)
        self.assertEqual(divide(0, 10), 0.0)

    def test_zero_division(self):
        """测试除以零的情况。"""
        f = StringIO()
        with redirect_stdout(f):
            result = divide(10, 0)
        
        self.assertIsNone(result)
        output = f.getvalue().strip()
        self.assertEqual(output, "错误：除数不能为零！")

    def test_type_error_denominator(self):
        """测试除数类型错误的情况。"""
        f = StringIO()
        with redirect_stdout(f):
            result = divide(10, "a")
            
        self.assertIsNone(result)
        output = f.getvalue().strip()
        self.assertEqual(output, "错误：输入必须是数字！")

    def test_type_error_numerator(self):
        """测试被除数类型错误的情况。"""
        f = StringIO()
        with redirect_stdout(f):
            result = divide("a", 10)
            
        self.assertIsNone(result)
        output = f.getvalue().strip()
        self.assertEqual(output, "错误：输入必须是数字！")

if __name__ == '__main__':
    unittest.main() 