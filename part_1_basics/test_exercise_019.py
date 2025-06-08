from part_1_basics.exercise_019 import remove_duplicates

def test_remove_duplicates_numbers():
    """测试从数字列表中移除重复项"""
    numbers = [1, 2, 3, 2, 4, 5, 4, 1]
    assert remove_duplicates(numbers) == {1, 2, 3, 4, 5}

def test_remove_duplicates_words():
    """测试从字符串列表中移除重复项"""
    words = ["hello", "world", "hello"]
    assert remove_duplicates(words) == {"hello", "world"}

def test_remove_duplicates_empty():
    """测试空列表的情况"""
    empty_list = []
    assert remove_duplicates(empty_list) == set() 