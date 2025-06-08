import unittest
import os
from part_5_files_and_exceptions.exercise_078 import read_with_with, write_with_with

class TestWithStatement(unittest.TestCase):
    
    test_filename = "test_with_statement.txt"

    def setUp(self):
        # 确保测试开始前，测试文件是不存在的
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def tearDown(self):
        # 确保测试结束后，测试文件被删除
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_write_and_read(self):
        """测试使用 'with' 语句的写入和读取功能。"""
        test_content = "Hello with statement!"
        
        # 1. 测试写入
        write_result = write_with_with(self.test_filename, test_content)
        self.assertTrue(write_result)
        
        # 2. 验证文件确实被创建并且内容正确
        self.assertTrue(os.path.exists(self.test_filename))
        
        # 3. 测试读取
        read_content = read_with_with(self.test_filename)
        self.assertEqual(read_content, test_content)

    def test_read_non_existent_file(self):
        """测试使用 'with' 语句读取一个不存在的文件。"""
        content = read_with_with("non_existent_file.txt")
        self.assertEqual(content, "Error: File 'non_existent_file.txt' not found.")

if __name__ == '__main__':
    unittest.main() 