import pytest
from part_2_control_flow.exercise_027 import loop_control_break, loop_control_continue

@pytest.fixture
def sample_numbers():
    """提供一个标准的数字列表作为测试数据"""
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_loop_control_break(sample_numbers):
    """测试 break 语句的效果"""
    assert loop_control_break(sample_numbers) == [1, 2, 3, 4]
    # 测试一个没有数字大于等于5的列表
    assert loop_control_break([1, 2, 3]) == [1, 2, 3]
    # 测试一个第一个数字就大于等于5的列表
    assert loop_control_break([5, 6, 7]) == []

def test_loop_control_continue(sample_numbers):
    """测试 continue 语句的效果"""
    assert loop_control_continue(sample_numbers) == [1, 3, 5, 7, 9]
    # 测试一个只包含偶数的列表
    assert loop_control_continue([2, 4, 6, 8]) == []
    # 测试一个只包含奇数的列表
    assert loop_control_continue([1, 3, 5]) == [1, 3, 5] 