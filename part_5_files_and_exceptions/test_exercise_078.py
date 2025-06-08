from part_5_files_and_exceptions.exercise_078 import read_with_with, write_with_with

def test_write_and_read(tmp_path):
    """测试使用 'with' 语句的写入和读取功能。"""
    test_file = tmp_path / "test_with.txt"
    test_content = "Hello with statement!"
    
    # 1. 测试写入
    write_result = write_with_with(test_file, test_content)
    assert write_result is True
    
    # 2. 验证文件确实被创建并且内容正确
    assert test_file.exists()
    
    # 3. 测试读取
    read_content = read_with_with(test_file)
    assert read_content == test_content

def test_read_non_existent_file():
    """测试使用 'with' 语句读取一个不存在的文件。"""
    # 这里我们不需要 tmp_path，因为我们就是想测试一个不存在的路径
    content = read_with_with("non_existent_file.txt")
    assert content == "Error: File 'non_existent_file.txt' not found." 