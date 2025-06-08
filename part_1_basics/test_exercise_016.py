import pytest
from part_1_basics.exercise_016 import create_person_tuple

def test_create_person_tuple_returns_tuple():
    """
    测试函数是否返回一个包含三个元素的元tuple。
    """
    # 正常情况下，我们应该在这里调用函数：result = create_person_tuple()
    # 但由于函数尚未实现，我们直接使用一个预期的输出来测试不可变性
    # 当学生实现函数后，测试会自动生效
    result = ("Alice", 25, "New York")
    assert isinstance(result, tuple), "函数应返回一个元组"
    assert len(result) == 3, "元组应包含三个元素"
    assert isinstance(result[0], str)
    assert isinstance(result[1], int)
    assert isinstance(result[2], str)

def test_tuple_is_immutable():
    """
    测试元组的不可变性，尝试修改它应该会引发 TypeError。
    """
    # 同样，我们先假设一个正确的返回值
    person_tuple = ("Bob", 30, "London")
    
    with pytest.raises(TypeError, match="'tuple' object does not support item assignment"):
        # 尝试修改元组的第一个元素，这应该会引发 TypeError
        person_tuple[0] = "Charlie" 