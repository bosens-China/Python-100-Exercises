from part_2_control_flow.exercise_030 import generate_squares

def test_generate_squares():
    """测试生成 1 到 10 的平方数列表"""
    expected = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    assert generate_squares() == expected 