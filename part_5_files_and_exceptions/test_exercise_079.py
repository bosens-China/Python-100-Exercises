from part_5_files_and_exceptions.exercise_079 import read_lines_with_numbers

def test_read_lines_with_numbers_standard_file(tmp_path):
    """测试读取一个标准的多行文件。"""
    test_file = tmp_path / "lines.txt"
    test_content = "First line\nSecond line\nThird line"
    test_file.write_text(test_content, encoding='utf-8')
    
    expected = [
        "1: First line",
        "2: Second line",
        "3: Third line"
    ]
    assert read_lines_with_numbers(test_file) == expected

def test_read_lines_with_numbers_empty_file(tmp_path):
    """测试读取一个空文件。"""
    test_file = tmp_path / "empty.txt"
    test_file.write_text("", encoding='utf-8')
    
    assert read_lines_with_numbers(test_file) == []

def test_read_lines_with_numbers_non_existent_file():
    """测试读取一个不存在的文件时应返回空列表。"""
    assert read_lines_with_numbers("non_existent_file.txt") == []

def test_read_lines_with_blank_lines(tmp_path):
    """测试读取包含空行的文件。"""
    test_file = tmp_path / "blank_lines.txt"
    test_content = "Line 1\n\nLine 3"
    test_file.write_text(test_content, encoding='utf-8')
    
    expected = [
        "1: Line 1",
        "2: ",
        "3: Line 3"
    ]
    assert read_lines_with_numbers(test_file) == expected 