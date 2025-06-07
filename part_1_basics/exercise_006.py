"""
### 6. 字符串切片

- **描述:** 给定一个字符串，如 `s = "Programming"`，提取并输出子字符串 "gram"。
- **提示:** 使用字符串的索引和切片功能 `s[start:end]`。记住索引从 0 开始。
- **期待:** `print(substring)` 输出 `gram`。
"""

def get_substring(s):
    """
    从字符串 s 中提取 "gram"
    :param s: 输入字符串, e.g., "Programming"
    :return: 子字符串 "gram"
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    source_string = "Programming"
    substring = get_substring(source_string)
    print(f"从 '{source_string}' 中提取的子字符串是: '{substring}'") 