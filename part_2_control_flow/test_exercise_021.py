from part_2_control_flow.exercise_021 import is_leap_year

def test_leap_year_divisible_by_4_not_100():
    """测试能被 4 整除但不能被 100 整除的年份"""
    assert is_leap_year(2024) is True
    assert is_leap_year(1996) is True

def test_leap_year_divisible_by_400():
    """测试能被 400 整除的年份"""
    assert is_leap_year(2000) is True

def test_not_leap_year_not_divisible_by_4():
    """测试不能被 4 整除的年份"""
    assert is_leap_year(2023) is False
    assert is_leap_year(1997) is False

def test_not_leap_year_divisible_by_100_not_400():
    """测试能被 100 整除但不能被 400 整除的年份"""
    assert is_leap_year(1900) is False
    assert is_leap_year(2100) is False 