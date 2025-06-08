import os
from part_6_standard_library.exercise_089 import list_current_directory, join_path_components

def test_list_directory(tmp_path, monkeypatch):
    """测试 os.listdir 在一个受控的环境中。"""
    test_dir = tmp_path / "test_dir"
    test_dir.mkdir()
    (test_dir / "file1.txt").touch()
    (test_dir / "file2.log").touch()
    (test_dir / "subdir").mkdir()
    
    # 使用 monkeypatch 来修改当前工作目录
    monkeypatch.chdir(test_dir)
    
    # 调用函数，它会列出当前目录（即 test_dir）的内容
    contents = list_current_directory()
    
    # 比较 set，因为 listdir 不保证返回顺序
    assert set(contents) == {"file1.txt", "file2.log", "subdir"}

def test_join_path():
    """测试 os.path.join 的行为。"""
    # os.sep 是当前操作系统的路径分隔符 ('\\' for Windows, '/' for others)
    expected = os.path.join("folder", "file.txt")
    assert join_path_components("folder", "file.txt") == expected

    # 在 Windows 上，os.path.join("C:", "Users/Test") 会返回 'C:Users/Test'
    # 在类 Unix 系统上，它会是 'C:/Users/Test'
    # 我们测试一个更通用的例子
    expected2 = os.path.join("C:/Users", "Test")
    assert join_path_components("C:/Users", "Test") == expected2