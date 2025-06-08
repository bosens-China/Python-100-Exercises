import unittest
import os
from part_5_files_and_exceptions.exercise_077 import write_to_file

class TestWriteFile(unittest.TestCase):
    
    test_filename = "test_output.txt"
    test_content = "This is a test content."

    def tearDown(self):
        """确保在每个测试后都删除测试文件，以保持环境清洁。"""
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)

    def test_write_to_new_file(self):
        """测试写入一个新文件。"""
        # 确保文件开始时不存在
        if os.path.exists(self.test_filename):
            os.remove(self.test_filename)
            
        result = write_to_file(self.test_filename, self.test_content)
        self.assertTrue(result)
        self.assertTrue(os.path.exists(self.test_filename))
        
        # 读取文件内容进行验证
        with open(self.test_filename, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, self.test_content)

    def test_overwrite_existing_file(self):
        """测试写入操作是否会覆盖一个已存在的文件。"""
        # 先创建一个有初始内容的文件
        initial_content = "Initial content."
        with open(self.test_filename, 'w', encoding='utf-8') as f:
            f.write(initial_content)
            
        new_content = "This should overwrite the initial content."
        result = write_to_file(self.test_filename, new_content)
        self.assertTrue(result)
        
        # 读取文件内容进行验证
        with open(self.test_filename, 'r', encoding='utf-8') as f:
            content = f.read()
        self.assertEqual(content, new_content)

if __name__ == '__main__':
    unittest.main() 