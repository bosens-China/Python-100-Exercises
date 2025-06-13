import pytest
from part_1_basics.exercise_016 import create_person_tuple

def test_create_person_tuple_properties():
    """
    测试 create_person_tuple 函数返回的元组的属性。
    """
    # 1. 调用学生实现的函数
    result = create_person_tuple()
    
    # 2. 验证返回的是否是元组
    assert isinstance(result, tuple), "函数应返回一个元组"
    
    # 3. 验证元组的长度
    assert len(result) == 3, "元组应包含三个元素"
    
    # 4. 验证元组中元素的类型
    assert isinstance(result[0], str), "第一个元素（姓名）应为字符串"
    assert isinstance(result[1], int), "第二个元素（年龄）应为整数"
    assert isinstance(result[2], str), "第三个元素（城市）应为字符串"

def test_tuple_is_immutable():
    """
    测试元组的不可变性。
    直接对函数返回的元组进行修改，应该会引发 TypeError。
    """
    # 1. 获取函数返回的元组
    person_tuple = create_person_tuple()
    
    # 2. 使用 pytest.raises 来断言 TypeError
    with pytest.raises(TypeError, match="'tuple' object does not support item assignment"):
        # 尝试修改元组的第一个元素，这应该会引发 TypeError
        person_tuple[0] = "Charlie" 