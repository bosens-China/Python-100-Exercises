from part_2_control_flow.exercise_029 import is_prime

def test_is_prime_true():
    """测试质数的情况"""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(13) is True
    assert is_prime(97) is True

def test_is_prime_false():
    """测试合数的情况"""
    assert is_prime(4) is False
    assert is_prime(12) is False
    assert is_prime(99) is False
    assert is_prime(100) is False

def test_is_prime_edge_cases():
    """测试边界情况"""
    assert is_prime(0) is False
    assert is_prime(1) is False
    assert is_prime(-5) is False 