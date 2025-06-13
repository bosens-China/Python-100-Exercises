"""
### 91. `json` 模块

- **描述:** 将一个 Python 字典 `{'name': 'Alice', 'age': 20}` 转换为 JSON 格式的字符串，然后再将该 JSON 字符串解析回 Python 字典。
- **提示:** 使用 `json.dumps()` 进行编码，使用 `json.loads()` 进行解码。
- **期待:**
  - `dumps` 返回 `'{"name": "Alice", "age": 20}'`。
  - `loads` 将该字符串转换回原始字典。
"""

def dict_to_json_string(data ):
    """
    将 Python 字典转换为 JSON 格式的字符串。
    
    :param data: 一个 Python 字典。
    :return: JSON 格式的字符串。
    """
    # 在这里写下你的代码
    pass

def json_string_to_dict(json_str):
    """
    将 JSON 格式的字符串解析回 Python 字典。
    
    :param json_str: JSON 格式的字符串。
    :return: 一个 Python 字典。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 示例数据
    my_dict = {'name': 'Alice', 'age': 20}
    
    # 转换为 JSON 字符串
    json_string = dict_to_json_string(my_dict)
    print(f"原始字典: {my_dict}")
    print(f"转换后的 JSON 字符串: {json_string}")
    
    # 解析回字典
    parsed_dict = json_string_to_dict(json_string)
    print(f"解析回来的字典: {parsed_dict}")
    
    # 验证
    assert my_dict == parsed_dict
    print("转换和解析成功！") 