from collections import Counter
from part_6_standard_library.exercise_093 import count_character_frequency

def test_basic_string():
    """测试一个基本的字符串。"""
    s = "abracadabra"
    expected = Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})
    assert count_character_frequency(s) == expected

def test_string_with_spaces_and_cases():
    """测试包含空格和不同大小写的字符串。"""
    s = "Hello World"
    # Counter 是区分大小写的
    expected = Counter({'l': 3, 'o': 2, 'H': 1, 'e': 1, ' ': 1, 'W': 1, 'r': 1, 'd': 1})
    assert count_character_frequency(s) == expected

def test_empty_string():
    """测试空字符串。"""
    s = ""
    expected = Counter()
    assert count_character_frequency(s) == expected
    
def test_string_with_all_same_characters():
    """测试所有字符都相同的字符串。"""
    s = "aaaaa"
    expected = Counter({'a': 5})
    assert count_character_frequency(s) == expected 