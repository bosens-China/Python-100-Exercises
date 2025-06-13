from part_5_files_and_exceptions.exercise_081 import convert_to_int

def test_convert_to_int_with_valid_string():
    """
    测试当输入是有效数字字符串时，函数能否正确转换。
    """
    assert convert_to_int("123") == 123

def test_convert_to_int_with_invalid_string():
    """
    测试当输入是无效字符串时，函数能否返回预期的错误消息。
    """
    expected_error_message = "转换失败，请输入一个有效的数字！"
    assert convert_to_int("abc") == expected_error_message

def test_convert_to_int_with_float_string():
    """
    测试当输入是浮点数字符串时，int() 会引发 ValueError。
    """
    expected_error_message = "转换失败，请输入一个有效的数字！"
    assert convert_to_int("12.3") == expected_error_message 