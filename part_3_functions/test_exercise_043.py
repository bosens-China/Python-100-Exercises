from part_3_functions.exercise_043 import greet_with_default

def test_greet_with_name():
    """测试提供了参数的情况"""
    assert greet_with_default("Bob") == "Hello, Bob!"

def test_greet_with_default():
    """测试没有提供参数，使用默认值的情况"""
    assert greet_with_default() == "Hello, World!" 