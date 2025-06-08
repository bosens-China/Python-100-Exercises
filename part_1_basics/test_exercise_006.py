from part_1_basics.exercise_006 import get_substring

def test_get_substring():
    """测试字符串切片功能"""
    assert get_substring("Programming") == "gram"
    assert get_substring("testing_gram_slice") == "gram" 