from part_5_files_and_exceptions.exercise_076 import read_hello_file

def test_read_existing_file(tmp_path):
    """测试读取一个已存在的文件。"""
    test_dir = tmp_path / "sub"
    test_dir.mkdir()
    test_file = test_dir / "hello.txt"
    test_content = "Hello from the test!"
    test_file.write_text(test_content, encoding='utf-8')
    
    content = read_hello_file(test_file)
    assert content == test_content

def test_read_non_existing_file(tmp_path):
    """测试读取一个不存在的文件。"""
    non_existent_file = tmp_path / "non_existent.txt"
    content = read_hello_file(non_existent_file)
    assert content == f"Error: The file '{non_existent_file}' was not found." 