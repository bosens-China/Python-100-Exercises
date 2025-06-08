"""
### 81. 处理 `try-except`

- **描述:** 编写一个程序，尝试将一个字符串 "abc" 转换为整数。使用 `try-except` 块来捕获 `ValueError` 异常，并打印一条友好的错误消息。
- **提示:** 将可能引发错误的代码放在 `try` 块中，在 `except ValueError:` 块中处理错误。
- **期待:** 程序不会崩溃，而是输出 "转换失败，请输入一个有效的数字！"。
"""

def convert_to_int(s: str) -> int | str:
    """
    尝试将一个字符串转换为整数。
    如果转换成功，返回该整数。
    如果发生 ValueError，返回一条错误消息字符串。
    
    :param s: 要转换的字符串。
    :return: 转换后的整数或错误消息。
    """
    # 在这里写下你的代码
    raise NotImplementedError 