"""
### 94. `re` 模块 (正则表达式)

- **描述:** 在字符串 "My email is test@example.com, please contact me." 中，使用正则表达式找到并提取出电子邮件地址。
- **提示:** 使用 `re.search()` 和一个匹配电子邮件模式的正则表达式，例如 `r'\S+@\S+'`。
- **期待:** 提取出 `test@example.com`。
"""
import re
from typing import Optional

def find_email_in_text(text: str) -> Optional[str]:
    """
    在文本中使用正则表达式查找第一个出现的电子邮件地址。
    :param text: 要搜索的文本
    :return: 找到的电子邮件地址字符串，如果没找到则返回 None。
    """
    # 在这里写下你的代码
    # 一个更精确一点的、但仍然很基础的电子邮件正则表达式
    # \b 表示单词边界，确保我们匹配的是完整的"单词"
    # [a-zA-Z0-9._%+-]+ 匹配用户名部分
    # @ 匹配 @ 符号
    # [a-zA-Z0-9.-]+ 匹配域名部分
    # \. 匹配点
    # [a-zA-Z]{2,} 匹配顶级域名（至少两个字母）
    email_pattern = r'\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'
    
    # re.search() 会在字符串中寻找第一个匹配项
    match = re.search(email_pattern, text)
    
    if match:
        # 如果找到匹配项，.group(0) 会返回整个匹配的字符串
        return match.group(0)
    else:
        return None

if __name__ == '__main__':
    text1 = "My email is test@example.com, please contact me."
    text2 = "Contact us at support@my-company.co.uk for help."
    text3 = "No email here."
    
    print(f"在 '{text1}' 中找到的邮箱: {find_email_in_text(text1)}")
    print(f"在 '{text2}' 中找到的邮箱: {find_email_in_text(text2)}")
    print(f"在 '{text3}' 中找到的邮箱: {find_email_in_text(text3)}") 