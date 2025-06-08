import unittest
from io import StringIO
from contextlib import redirect_stdout
from part_5_files_and_exceptions.exercise_083 import divide_with_else_finally

class TestElseAndFinally(unittest.TestCase):
    def test_successful_case(self):
        """测试成功计算时，else 和 finally 块的行为。"""
        f = StringIO()
        with redirect_stdout(f):
            result = divide_with_else_finally(10, 2)
        
        # 检查返回值
        self.assertEqual(result, 5.0)
        # 检查打印输出
        output = f.getvalue()
        self.assertIn("计算成功", output)
        self.assertIn("计算结束", output)
        # 确保 "计算成功" 在 "计算结束" 之前
        self.assertLess(output.find("计算成功"), output.find("计算结束"))

    def test_zero_division_case(self):
        """测试除以零时，except 和 finally 块的行为。"""
        f = StringIO()
        with redirect_stdout(f):
            result = divide_with_else_finally(10, 0)
        
        # 检查返回值
        self.assertIsNone(result)
        # 检查打印输出
        output = f.getvalue()
        self.assertIn("错误：除数不能为零！", output)
        self.assertIn("计算结束", output)
        # 确保 else 块没有被执行
        self.assertNotIn("计算成功", output)

    def test_type_error_case(self):
        """测试类型错误时，except 和 finally 块的行为。"""
        f = StringIO()
        with redirect_stdout(f):
            result = divide_with_else_finally(10, "a")
        
        # 检查返回值
        self.assertIsNone(result)
        # 检查打印输出
        output = f.getvalue()
        self.assertIn("错误：输入必须是数字！", output)
        self.assertIn("计算结束", output)
        # 确保 else 块没有被执行
        self.assertNotIn("计算成功", output)

if __name__ == '__main__':
    unittest.main() 