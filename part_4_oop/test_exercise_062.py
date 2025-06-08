import unittest
from part_4_oop.exercise_062 import Dog
from io import StringIO
import sys

class TestDogMethod(unittest.TestCase):
    def setUp(self):
        """在每个测试用例运行前设置好 Dog 实例。"""
        self.my_dog = Dog("Fido", 5)

    def test_bark_return_value(self):
        """测试 bark 方法的返回值。"""
        self.assertEqual(self.my_dog.bark(), "Woof! Woof!")
        
    def test_bark_print_output(self):
        """测试 bark 方法是否在控制台打印了正确的内容。"""
        # 保存原始的标准输出
        original_stdout = sys.stdout
        # 重定向标准输出到一个 StringIO 对象
        sys.stdout = captured_output = StringIO()

        self.my_dog.bark()

        # 恢复原始的标准输出
        sys.stdout = original_stdout
        
        # 获取捕获到的输出
        output = captured_output.getvalue().strip()
        self.assertEqual(output, "Woof! Woof!")

if __name__ == '__main__':
    unittest.main() 