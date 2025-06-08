from part_1_basics.exercise_007 import format_string

def test_format_string_basic():
    """测试基本的字符串格式化"""
    s = "  pyThon ProGramming  "
    upper_case, lower_case, stripped = format_string(s)
    assert upper_case == "PYTHON PROGRAMMING"
    assert lower_case == "python programming"
    assert stripped == "pyThon ProGramming"

def test_format_string_another():
    """测试另一个字符串的格式化"""
    s2 = "  Another Test  "
    upper_case2, lower_case2, stripped2 = format_string(s2)
    assert upper_case2 == "ANOTHER TEST"
    assert lower_case2 == "another test"
    assert stripped2 == "Another Test" 