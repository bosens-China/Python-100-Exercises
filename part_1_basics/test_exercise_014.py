import pytest
from part_1_basics.exercise_014 import modify_list


def test_standard_case():
    """
    测试题目描述中的标准用例。
    """
    fruits = ["apple", "banana", "cherry"]
    modified_fruits = modify_list(fruits[:])
    assert modified_fruits == ['apple', 'grape', 'banana', 'cherry', 'orange']


def test_apple_at_different_position():
    """
    测试 'apple' 在列表其他位置的情况。
    """
    items = ["foo", "bar", "apple", "baz"]
    modified_items = modify_list(items[:])
    assert modified_items == ['foo', 'bar', 'apple', 'grape', 'baz', 'orange']


def test_edge_case_apple_only():
    """
    测试列表中只有 'apple' 的边界情况。
    """
    items = ["apple"]
    modified_items = modify_list(items[:])
    assert modified_items == ['apple', 'grape', 'orange']


def test_no_apple_raises_error():
    """
    测试当列表中没有 'apple' 时，函数是否按预期抛出 ValueError。
    """
    items_without_apple = ["foo", "bar", "baz"]
    with pytest.raises(ValueError):
        modify_list(items_without_apple)