"""
### 59. 编写一个检查回文数的函数

- **描述:** 编写一个函数 `is_palindrome`，它接受一个字符串或数字，并判断它是否是回文（正读和反读都一样）。
- **提示:** 将输入转换为字符串，然后比较字符串和它的反转是否相等。字符串反转可以用 `s[::-1]`。
- **期待:**
  - `is_palindrome("madam")` 返回 `True`。
  - `is_palindrome(12321)` 返回 `True`。
  - `is_palindrome("hello")` 返回 `False`。
"""
from typing import Union

def is_palindrome(data: Union[str, int]) -> bool:
    """
    检查给定的字符串或数字是否是回文。
    :param data: 一个字符串或整数
    :return: 如果是回文则返回 True，否则返回 False
    """
    # 在这里写下你的代码
    # 统一将输入转换为字符串进行处理
    s = str(data)
    return s == s[::-1]

if __name__ == '__main__':
    print(f"'madam' 是回文吗? {is_palindrome('madam')}")
    print(f"12321 是回文吗? {is_palindrome(12321)}")
    print(f"'hello' 是回文吗? {is_palindrome('hello')}")
    print(f"12345 是回文吗? {is_palindrome(12345)}") 