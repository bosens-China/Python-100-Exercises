from part_2_control_flow.exercise_031 import create_dict_from_list

def test_create_dict_from_list_basic():
    """测试基本列表的转换"""
    keys = ["name", "age", "city"]
    expected = {'name': 4, 'age': 3, 'city': 4}
    assert create_dict_from_list(keys) == expected

def test_create_dict_from_list_another():
    """测试另一个列表的转换"""
    keys2 = ["python", "is", "fun"]
    expected2 = {'python': 6, 'is': 2, 'fun': 3}
    assert create_dict_from_list(keys2) == expected2

def test_create_dict_from_list_empty():
    """测试空列表的转换"""
    keys3 = []
    expected3 = {}
    assert create_dict_from_list(keys3) == expected3 