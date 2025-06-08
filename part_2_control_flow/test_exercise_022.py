import pytest
from part_2_control_flow.exercise_022 import check_guess

@pytest.mark.parametrize("secret, guess, expected_result", [
    (50, 70, "太大了！"),
    (50, 30, "太小了！"),
    (50, 50, "恭喜你，猜对了！"),
    (1, 100, "太大了！"),
    (100, 1, "太小了！"),
    (1, 1, "恭喜你，猜对了！")
])
def test_check_guess(secret, guess, expected_result):
    """
    测试 check_guess 函数的各种情况。
    """
    # 这个测试会因为 check_guess 中的 NotImplementedError 而失败，
    # 直到学生实现了该函数。
    assert check_guess(secret, guess) == expected_result 