from part_1_basics.exercise_009 import calculate_rectangle_properties

def test_calculate_rectangle_properties_1():
    """测试 length=10, width=5 的情况"""
    perimeter, area = calculate_rectangle_properties(10, 5)
    assert perimeter == 30
    assert area == 50

def test_calculate_rectangle_properties_2():
    """测试 length=3, width=4 的情况"""
    perimeter, area = calculate_rectangle_properties(3, 4)
    assert perimeter == 14
    assert area == 12 