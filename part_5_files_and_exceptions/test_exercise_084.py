import pytest
from part_5_files_and_exceptions.exercise_084 import set_age

def test_valid_age():
    """测试设置一个有效的年龄时，不应抛出任何异常。"""
    try:
        set_age(25)
        set_age(0)
        set_age(100)
    except ValueError:
        pytest.fail("set_age() 抛出了一个不应出现的 ValueError")

def test_negative_age_raises_value_error():
    """测试设置一个负数年龄时，是否会抛出 ValueError。"""
    with pytest.raises(ValueError):
        set_age(-1)
        
    with pytest.raises(ValueError):
        set_age(-99)

def test_exception_message():
    """测试抛出的 ValueError 是否包含了正确的错误信息。"""
    with pytest.raises(ValueError, match="年龄不能为负数"):
        set_age(-5)

if __name__ == '__main__':
    pytest.main() 