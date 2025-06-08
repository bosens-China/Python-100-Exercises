import unittest
import os
import shutil
from part_6_standard_library.exercise_089 import list_current_directory, join_path_components

class TestOsModule(unittest.TestCase):
    
    test_dir = "temp_test_dir_for_os"

    def setUp(self):
        """创建一个临时目录和一些文件/子目录用于测试。"""
        os.makedirs(self.test_dir, exist_ok=True)
        # 在临时目录中创建文件和目录
        with open(os.path.join(self.test_dir, "file1.txt"), "w") as f:
            f.write("test")
        with open(os.path.join(self.test_dir, "file2.log"), "w") as f:
            f.write("log")
        os.makedirs(os.path.join(self.test_dir, "subdir"), exist_ok=True)
        
    def tearDown(self):
        """删除临时目录及其所有内容。"""
        if os.path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def test_list_directory(self):
        """测试 os.listdir 在一个受控的环境中。"""
        # 保存当前工作目录
        original_cwd = os.getcwd()
        try:
            # 切换到我们的测试目录
            os.chdir(self.test_dir)
            # 调用函数，它会列出当前目录（即 self.test_dir）的内容
            contents = list_current_directory()
            # 比较 set，因为 listdir 不保证返回顺序
            self.assertEqual(set(contents), {"file1.txt", "file2.log", "subdir"})
        finally:
            # 无论如何都要切回原始目录
            os.chdir(original_cwd)
            
    def test_join_path(self):
        """测试 os.path.join 的行为。"""
        # os.sep 是当前操作系统的路径分隔符 ('\\' for Windows, '/' for others)
        expected = "folder" + os.sep + "file.txt"
        self.assertEqual(join_path_components("folder", "file.txt"), expected)

        expected2 = os.path.join("C:", "Users", "Test")
        self.assertEqual(join_path_components("C:", "Users/Test"), expected2)

if __name__ == '__main__':
    unittest.main() 