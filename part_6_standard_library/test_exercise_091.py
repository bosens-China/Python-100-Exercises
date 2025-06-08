from part_6_standard_library.exercise_091 import dict_to_json_string, json_string_to_dict

def test_dict_to_json():
    """
    测试字典到 JSON 字符串的转换。
    """
    py_dict = {'name': 'Alice', 'age': 20}
    # json.dumps 可能会也可能不会在分隔符后加空格
    # 所以我们先解析回来再比较，确保语义正确
    json_str = dict_to_json_string(py_dict)
    
    import json
    # 验证生成的字符串可以被成功解析，并且内容与原字典相同
    assert json.loads(json_str) == py_dict

def test_json_to_dict():
    """
    测试 JSON 字符串到字典的转换。
    """
    json_str = '{"name": "Alice", "age": 20}'
    expected_dict = {'name': 'Alice', 'age': 20}
    
    assert json_string_to_dict(json_str) == expected_dict

def test_json_cycle():
    """
    测试一个完整的编码 -> 解码周期。
    """
    py_dict = {'city': 'London', 'is_capital': True, 'population': 8900000}
    
    json_str = dict_to_json_string(py_dict)
    new_py_dict = json_string_to_dict(json_str)
    
    assert new_py_dict == py_dict 