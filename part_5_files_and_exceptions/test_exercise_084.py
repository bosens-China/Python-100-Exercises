import unittest
from part_5_files_and_exceptions.exercise_084 import set_age

class TestRaiseException(unittest.TestCase):
    def test_valid_age(self):
        """测试设置一个有效的年龄时，不应抛出任何异常。"""
        try:
            set_age(25)
            set_age(0)
            set_age(100)
        except ValueError:
            self.fail("set_age() 抛出了一个不应出现的 ValueError")

    def test_negative_age_raises_value_error(self):
        """测试设置一个负数年龄时，是否会抛出 ValueError。"""
        # assertRaises 是一个上下文管理器，如果块内的代码没有抛出指定的异常，测试就会失败
        with self.assertRaises(ValueError):
            set_age(-1)
            
        with self.assertRaises(ValueError):
            set_age(-99)

    def test_exception_message(self):
        """测试抛出的 ValueError 是否包含了正确的错误信息。"""
        with self.assertRaisesRegex(ValueError, "年龄不能为负数"):
            set_age(-5)

if __name__ == '__main__':
    unittest.main() 