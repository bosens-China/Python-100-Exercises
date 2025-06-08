from part_1_basics.exercise_002 import swap_variables

def test_swap_integers():
    """测试整数交换"""
    a, b = 5, 10
    swapped_a, swapped_b = swap_variables(a, b)
    assert swapped_a == 10
    assert swapped_b == 5

def test_swap_strings():
    """测试字符串交换"""
    x, y = "hello", "world"
    swapped_x, swapped_y = swap_variables(x, y)
    assert swapped_x == "world"
    assert swapped_y == "hello" 