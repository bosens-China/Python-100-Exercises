from part_1_basics.exercise_011 import check_odd_even

def test_check_odd_even():
    """测试奇偶数判断功能"""
    assert check_odd_even(7) == "奇数"
    assert check_odd_even(4) == "偶数"
    assert check_odd_even(0) == "偶数"
    assert check_odd_even(-1) == "奇数"
    assert check_odd_even(-2) == "偶数" 