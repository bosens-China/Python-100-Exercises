import os
from part_5_files_and_exceptions.exercise_077 import write_to_file

def test_write_to_new_file(tmp_path):
    """测试写入一个新文件。"""
    test_file = tmp_path / "output.txt"
    test_content = "This is a test content."
    
    result = write_to_file(test_file, test_content)
    assert result is True
    assert os.path.exists(test_file)
    
    # 读取文件内容进行验证
    content = test_file.read_text(encoding='utf-8')
    assert content == test_content

def test_overwrite_existing_file(tmp_path):
    """测试写入操作是否会覆盖一个已存在的文件。"""
    test_file = tmp_path / "output.txt"
    
    # 先创建一个有初始内容的文件
    initial_content = "Initial content."
    test_file.write_text(initial_content, encoding='utf-8')
        
    new_content = "This should overwrite the initial content."
    result = write_to_file(test_file, new_content)
    assert result is True
    
    # 读取文件内容进行验证
    content = test_file.read_text(encoding='utf-8')
    assert content == new_content 