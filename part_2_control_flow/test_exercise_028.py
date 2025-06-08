from part_2_control_flow.exercise_028 import generate_triangle

def test_generate_triangle_height_5():
    """测试高度为 5 的情况"""
    expected = "*\n**\n***\n****\n*****\n"
    assert generate_triangle(5) == expected

def test_generate_triangle_height_3():
    """测试高度为 3 的情况"""
    expected = "*\n**\n***\n"
    assert generate_triangle(3) == expected

def test_generate_triangle_height_1():
    """测试高度为 1 的情况"""
    expected = "*\n"
    assert generate_triangle(1) == expected
    
def test_generate_triangle_height_0():
    """测试高度为 0 的情况"""
    expected = ""
    assert generate_triangle(0) == expected 