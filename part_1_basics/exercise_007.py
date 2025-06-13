"""
### 7. 字符串方法

- **描述:** 给定一个混合大小写的字符串，如 `s = "  pyThon ProGramming  "`，请将其转换为全大写、全小写，并移除两端的空白字符。
- **提示:** 使用字符串的内置方法：`upper()`，`lower()` 和 `strip()`。
- **期待:**
  - 全大写输出: `PYTHON PROGRAMMING`
  - 全小写输出: `python programming`
  - 移除空白后输出: `pyThon ProGramming`
"""

def format_string(s):
    """
    将字符串s进行格式化
    :param s: 输入字符串
    :return: 一个元组，包含转换后的全大写、全小写和移除两端空白后的字符串
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    original_string = "  pyThon ProGramming  "
    up, low, stripped = format_string(original_string)
    print(f"原字符串: '{original_string}'")
    print(f"全大写: '{up}'")
    print(f"全小写: '{low}'")
    print(f"移除空白后: '{stripped}'") 