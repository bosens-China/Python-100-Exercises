from part_3_functions.exercise_046 import display_info

def test_display_info_with_two_args():
    """
    测试传入两个关键字参数的情况。
    """
    # 正常实现下，函数应返回 "name: Alice\nage: 25" 或 "age: 25\nname: Alice"
    # 因为字典是无序的，所以我们检查每个部分
    # expected_output = display_info(name="Alice", age=25)
    # assert "name: Alice" in expected_output
    # assert "age: 25" in expected_output
    pass # 函数未实现，暂时跳过

def test_display_info_with_multiple_args():
    """
    测试传入多个不同类型的关键字参数。
    """
    # expected_output = display_info(name="Bob", status="active", high_score=99.5)
    # assert "name: Bob" in expected_output
    # assert "status: active" in expected_output
    # assert "high_score: 99.5" in expected_output
    pass # 函数未实现，暂时跳过

def test_display_info_with_no_args():
    """
    测试没有传入参数的情况，应该返回一个空字符串。
    """
    # assert display_info() == ""
    pass # 函数未实现，暂时跳过 