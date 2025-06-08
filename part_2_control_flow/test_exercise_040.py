from part_2_control_flow.exercise_040 import reverse_string

def test_reverse_string_basic():
    """测试基本字符串反转"""
    assert reverse_string("python") == "nohtyp"

def test_reverse_string_palindrome():
    """测试回文字符串"""
    assert reverse_string("madam") == "madam"

def test_reverse_string_with_space():
    """测试带空格的字符串"""
    assert reverse_string("hello world") == "dlrow olleh"

def test_reverse_string_empty():
    """测试空字符串"""
    assert reverse_string("") == ""

def test_reverse_string_single_char():
    """测试单字符字符串"""
    assert reverse_string("a") == "a" 