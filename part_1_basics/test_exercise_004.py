from part_1_basics.exercise_004 import concatenate_strings

def test_concatenate_strings():
    """测试字符串拼接功能"""
    assert concatenate_strings("Hello", "Python") == "Hello Python"
    assert concatenate_strings("First", "Part") == "First Part"
    assert concatenate_strings("", "") == " " 