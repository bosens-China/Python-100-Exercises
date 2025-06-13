"""
### 35. 统计字符串中的元音字母

- **描述:** 统计一个给定字符串中元音字母（a, e, i, o, u）的总数。
- **提示:** 遍历字符串中的每个字符，判断它是否在元音字母集合 `"aeiou"` 中。不区分大小写。
- **期待:** 对于字符串 `"Hello Python"`，输出 `元音字母数量: 3`。
"""

def count_vowels(s):
    """
    统计字符串中的元音字母数量（不区分大小写）
    :param s: 输入字符串
    :return: 元音字母的总数
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    text = "Hello Python"
    vowel_count = count_vowels(text)
    print(f"字符串 '{text}' 中的元音字母数量: {vowel_count}") 