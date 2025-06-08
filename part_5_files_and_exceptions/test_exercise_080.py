import unittest
import os
from part_5_files_and_exceptions.exercise_080 import copy_file

class TestCopyFile(unittest.TestCase):
    
    source_filename = "test_source.txt"
    dest_filename = "test_dest.txt"
    content = "This is a test.\nIt has multiple lines.\nAnd special characters: !@#$%^&*()"

    def setUp(self):
        # 创建源文件
        with open(self.source_filename, "w", encoding='utf-8') as f:
            f.write(self.content)
            
    def tearDown(self):
        # 清理源文件和目标文件
        if os.path.exists(self.source_filename):
            os.remove(self.source_filename)
        if os.path.exists(self.dest_filename):
            os.remove(self.dest_filename)

    def test_successful_copy(self):
        """测试成功的文件复制。"""
        result = copy_file(self.source_filename, self.dest_filename)
        self.assertTrue(result)
        
        # 验证目标文件是否存在
        self.assertTrue(os.path.exists(self.dest_filename))
        
        # 验证目标文件内容是否与源文件相同
        with open(self.dest_filename, "r", encoding='utf-8') as f:
            copied_content = f.read()
        self.assertEqual(copied_content, self.content)

    def test_copy_to_existing_file(self):
        """测试复制到已存在的文件（应被覆盖）。"""
        # 创建一个已存在的目标文件
        with open(self.dest_filename, "w", encoding='utf-8') as f:
            f.write("This content should be overwritten.")
            
        result = copy_file(self.source_filename, self.dest_filename)
        self.assertTrue(result)
        
        # 验证内容是否已被覆盖
        with open(self.dest_filename, "r", encoding='utf-8') as f:
            copied_content = f.read()
        self.assertEqual(copied_content, self.content)

    def test_source_file_not_found(self):
        """测试源文件不存在的情况。"""
        # 删除由 setUp 创建的源文件
        os.remove(self.source_filename)
        result = copy_file(self.source_filename, self.dest_filename)
        self.assertFalse(result)
        # 确保目标文件没有被创建
        self.assertFalse(os.path.exists(self.dest_filename))

if __name__ == '__main__':
    unittest.main() 