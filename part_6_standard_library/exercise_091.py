"""
### 91. `json` 模块

- **描述:** 将一个 Python 字典 `{'name': 'Alice', 'age': 20}` 转换为 JSON 格式的字符串，然后再将该 JSON 字符串解析回 Python 字典。
- **提示:** 使用 `json.dumps()` 进行编码，使用 `json.loads()` 进行解码。
- **期待:**
  - `dumps` 返回 `'{"name": "Alice", "age": 20}'`。
  - `loads` 将该字符串转换回原始字典。
"""
from typing import Dict, Any

def dict_to_json_string(data: Dict[str, Any]) -> str:
    """
    将 Python 字典转换为 JSON 格式的字符串。
    
    :param data: 一个 Python 字典。
    :return: JSON 格式的字符串。
    """
    # 在这里写下你的代码
    raise NotImplementedError

def json_string_to_dict(json_str: str) -> Dict[str, Any]:
    """
    将 JSON 格式的字符串解析回 Python 字典。
    
    :param json_str: JSON 格式的字符串。
    :return: 一个 Python 字典。
    """
    # 在这里写下你的代码
    raise NotImplementedError 