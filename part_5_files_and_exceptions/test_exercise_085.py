from part_5_files_and_exceptions.exercise_085 import count_word_frequency
import pytest

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
    """
    测试函数是否能正确处理标点符号。
    注意：基础的实现可能只是简单地移除标点，这对于 "word's" 这样的词可能不理想，
    但对于本练习来说，我们将测试简单的标点移除。
    """
    p = tmp_path / "test.txt"
    content = "word, word! another-word. final word?"
    p.write_text(content, encoding='utf-8')
    # 根据提示中的replace方法，预期结果是移除非字母字符后进行计数
    # 'another-word' 在移除非字母后会变成 'anotherword'
    expected = {'word': 4, 'anotherword': 1, 'final': 1}
    
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