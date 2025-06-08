from part_3_functions.exercise_059 import is_palindrome

def test_string_palindrome():
    """测试回文字符串"""
    assert is_palindrome("madam") is True

def test_string_not_palindrome():
    """测试非回文字符串"""
    assert is_palindrome("hello") is False

def test_number_palindrome():
    """测试回文数字"""
    assert is_palindrome(12321) is True

def test_number_not_palindrome():
    """测试非回文数字"""
    assert is_palindrome(12345) is False

def test_case_sensitivity():
    """回文检查通常是大小写敏感的"""
    assert is_palindrome("Madam") is False

def test_string_with_spaces():
    """
    "taco cat" 不是一个严格的回文
    如果需要处理空格，函数逻辑需要修改
    """
    assert is_palindrome("taco cat") is False
    assert is_palindrome("taco cat".replace(" ", "")) is True
    
def test_single_character():
    """测试单个字符或数字"""
    assert is_palindrome("a") is True
    assert is_palindrome(7) is True
    
def test_empty_string():
    """测试空字符串"""
    assert is_palindrome("") is True 