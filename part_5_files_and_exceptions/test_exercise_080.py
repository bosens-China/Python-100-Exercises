from part_5_files_and_exceptions.exercise_080 import copy_file

def test_successful_copy(tmp_path):
    """测试成功的文件复制。"""
    source_file = tmp_path / "source.txt"
    dest_file = tmp_path / "dest.txt"
    content = "This is a test.\nIt has multiple lines.\nAnd special characters: !@#$%^&*()"
    source_file.write_text(content, encoding='utf-8')

    result = copy_file(source_file, dest_file)
    assert result is True
    
    # 验证目标文件是否存在并内容相同
    assert dest_file.exists()
    assert dest_file.read_text(encoding='utf-8') == content

def test_copy_to_existing_file(tmp_path):
    """测试复制到已存在的文件（应被覆盖）。"""
    source_file = tmp_path / "source.txt"
    dest_file = tmp_path / "dest.txt"
    content = "New content."
    source_file.write_text(content, encoding='utf-8')
    
    # 创建一个已存在的目标文件
    dest_file.write_text("This content should be overwritten.", encoding='utf-8')
        
    result = copy_file(source_file, dest_file)
    assert result is True
    
    # 验证内容是否已被覆盖
    assert dest_file.read_text(encoding='utf-8') == content

def test_source_file_not_found(tmp_path):
    """测试源文件不存在的情况。"""
    source_file = tmp_path / "non_existent_source.txt"
    dest_file = tmp_path / "dest.txt"
    
    result = copy_file(source_file, dest_file)
    assert result is False
    # 确保目标文件没有被创建
    assert not dest_file.exists() 