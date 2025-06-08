import pytest
from part_2_control_flow.exercise_032 import search_in_list

@pytest.fixture
def sample_list():
    """提供一个标准的列表作为测试数据"""
    return [1, 2, 3, 4]

def test_item_found(sample_list):
    """测试能找到元素的情况"""
    assert search_in_list(sample_list, 3) == "找到了"
    assert search_in_list(sample_list, 1) == "找到了"

def test_item_not_found(sample_list):
    """测试找不到元素的情况"""
    assert search_in_list(sample_list, 5) == "没找到"
    assert search_in_list(sample_list, 0) == "没找到"

def test_empty_list():
    """测试空列表的情况"""
    assert search_in_list([], 5) == "没找到"

if __name__ == '__main__':
    pytest.main() 