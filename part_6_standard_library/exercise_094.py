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
    在给定的文本中查找并返回第一个有效的电子邮件地址。
    如果没有找到，则返回 None。
    """
    # 在这里写下你的代码
    raise NotImplementedError

if __name__ == '__main__':
    text1 = "My email is test@example.com, please contact me."
    text2 = "Contact us at support@my-company.co.uk for help."
    text3 = "No email here."
    
    print(f"在 '{text1}' 中找到的邮箱: {find_email_in_text(text1)}")
    print(f"在 '{text2}' 中找到的邮箱: {find_email_in_text(text2)}")
    print(f"在 '{text3}' 中找到的邮箱: {find_email_in_text(text3)}") 