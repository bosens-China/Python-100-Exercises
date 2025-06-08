import unittest
from io import StringIO
from contextlib import redirect_stdout
from part_5_files_and_exceptions.exercise_081 import convert_to_int

class TestTryExcept(unittest.TestCase):
    def test_valid_conversion(self):
        """测试有效的字符串转换。"""
        self.assertEqual(convert_to_int("123"), 123)
        self.assertEqual(convert_to_int("-50"), -50)
        self.assertEqual(convert_to_int("0"), 0)

    def test_invalid_conversion_returns_none(self):
        """测试无效的字符串转换时，函数是否返回 None。"""
        self.assertIsNone(convert_to_int("abc"))
        self.assertIsNone(convert_to_int("12.34")) # int() 不能转换包含小数点的字符串
        self.assertIsNone(convert_to_int(""))

    def test_invalid_conversion_prints_message(self):
        """测试无效的字符串转换时，是否打印了正确的错误消息。"""
        # 创建一个 StringIO 对象来捕获 stdout
        f = StringIO()
        # 使用 redirect_stdout 将打印输出重定向到 f
        with redirect_stdout(f):
            convert_to_int("abc")
        # 获取捕获到的输出
        output = f.getvalue().strip()
        
        self.assertEqual(output, "转换失败，请输入一个有效的数字！")

if __name__ == '__main__':
    unittest.main() 