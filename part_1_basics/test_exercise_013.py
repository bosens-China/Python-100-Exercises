import pytest
from part_1_basics.exercise_013 import get_third_element

def test_get_third_element():
    """测试获取列表第三个元素"""
    assert get_third_element([1, 2, 3, 4, 5]) == 3
    assert get_third_element(['a', 'b', 'c']) == 'c'
    assert get_third_element([True, False, True]) is True

def test_get_third_element_empty_list():
    """测试空列表的情况"""
    with pytest.raises(IndexError):
        get_third_element([])

def test_get_third_element_short_list():
    """测试列表长度不足的情况"""
    with pytest.raises(IndexError):
        get_third_element([1, 2])
 