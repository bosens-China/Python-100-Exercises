import unittest
import os
from part_5_files_and_exceptions.exercise_076 import read_hello_file

class TestReadFile(unittest.TestCase):
    
    test_filename = "test_hello.txt"
    test_content = "Hello from the test!"

    def setUp(self):
        """在每个测试开始前，创建一个临时的测试文件。"""
        with open(self.test_filename, "w", encoding='utf-8') as f:
            f.write(self.test_content)

    def tearDown(self):
        """在每个测试结束后，删除这个临时文件。"""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_read_existing_file(self):
        """测试读取一个已存在的文件。"""
        content = read_hello_file(self.test_filename)
        self.assertEqual(content, self.test_content)

    def test_read_non_existing_file(self):
        """测试读取一个不存在的文件。"""
        # 先删除 setUp 创建的文件
        os.remove(self.test_filename)
        content = read_hello_file(self.test_filename)
        self.assertEqual(content, f"Error: The file '{self.test_filename}' was not found.")

if __name__ == '__main__':
    unittest.main() 