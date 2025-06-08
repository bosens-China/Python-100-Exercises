from part_1_basics.exercise_008 import create_intro_string

def test_create_intro_string():
    """测试f-string格式化功能"""
    assert create_intro_string("Bob", 25) == "Bob is 25 years old."
    assert create_intro_string("Alice", 30) == "Alice is 30 years old." 