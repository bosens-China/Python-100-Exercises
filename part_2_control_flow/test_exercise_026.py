from part_2_control_flow.exercise_026 import generate_fibonacci

def test_generate_fibonacci_10():
    """测试生成前 10 个斐波那契数"""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
    assert generate_fibonacci(10) == expected

def test_generate_fibonacci_20():
    """测试生成前 20 个斐波那契数"""
    expected = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181]
    assert generate_fibonacci(20) == expected

def test_generate_fibonacci_edge_cases():
    """测试斐波那契数列的边界情况"""
    assert generate_fibonacci(0) == []
    assert generate_fibonacci(1) == [0]
    assert generate_fibonacci(2) == [0, 1] 