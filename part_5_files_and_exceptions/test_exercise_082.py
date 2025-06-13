from part_5_files_and_exceptions.exercise_082 import divide

def test_divide_success():
    """
    测试正常除法。
    """
    assert divide(10, 2) == 5.0

def test_divide_by_zero():
    """
    测试除以零的情况。
    """
    assert divide(10, 0) == "错误：除数不能为零！"

def test_divide_with_type_error():
    """
    测试输入类型错误的情况。
    """
    assert divide(10, "a") == "错误：输入必须是数字！"
    assert divide("b", 2) == "错误：输入必须是数字！" 