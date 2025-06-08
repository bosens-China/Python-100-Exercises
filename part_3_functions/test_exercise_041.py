from part_3_functions.exercise_041 import greet

def test_greet():
    """测试 greet 函数"""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"
    assert greet("World") == "Hello, World!" 