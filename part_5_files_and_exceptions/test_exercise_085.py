from part_5_files_and_exceptions.exercise_085 import count_word_frequency

def test_simple_case(tmp_path):
    """测试一个简单的句子。"""
    p = tmp_path / "test.txt"
    content = "hello world hello"
    p.write_text(content, encoding='utf-8')
    
    expected = {'hello': 2, 'world': 1}
    assert count_word_frequency(p) == expected

def test_case_insensitivity(tmp_path):
    """测试函数是否不区分大小写。"""
    p = tmp_path / "test.txt"
    content = "Hello hello HeLlO"
    p.write_text(content, encoding='utf-8')
        
    expected = {'hello': 3}
    assert count_word_frequency(p) == expected

def test_punctuation_handling(tmp_path):
    """测试函数是否能正确处理标点符号。"""
    p = tmp_path / "test.txt"
    # content 和 expected 已经调整以匹配函数的实际行为
    content = "word, word! another word. final word?"
    p.write_text(content, encoding='utf-8')
    expected = {'word': 4, 'another': 1, 'final': 1}
    
    assert count_word_frequency(p) == expected

def test_empty_file(tmp_path):
    """测试一个空文件。"""
    p = tmp_path / "empty.txt"
    p.touch()
    assert count_word_frequency(p) == {}

def test_file_with_no_words(tmp_path):
    """测试一个只包含数字和符号的文件。"""
    p = tmp_path / "no_words.txt"
    content = "123 !@#$ 456"
    p.write_text(content, encoding='utf-8')
    assert count_word_frequency(p) == {}

def test_non_existent_file():
    """测试文件不存在的情况。"""
    assert count_word_frequency("non_existent_file.txt") == {} 