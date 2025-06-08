"""
### 85. 统计文件中单词出现的次数

- **描述:** 读取一个文本文件，统计其中每个单词出现的频率，并以字典形式返回结果。
- **提示:** 读取文件内容，使用 `split()` 分割成单词列表。遍历列表，使用字典来存储每个单词的计数。注意处理标点符号和大小写。
- **期待:** 对于文件内容 "hello world hello"，返回 `{'hello': 2, 'world': 1}`。
"""
import os
import re
from collections import Counter
from typing import Dict

def count_word_frequency(filename: str) -> Dict[str, int]:
    """
    读取文件，统计其中每个单词的出现频率。
    处理方式：
    1. 将所有单词转为小写。
    2. 使用正则表达式移除非字母数字字符。
    :param filename: 要处理的文件的路径
    :return: 一个包含单词及其频率的字典。
    """
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        
        # 将所有内容转为小写
        text = text.lower()
        
        # 使用正则表达式匹配所有单词（只包含字母）
        words = re.findall(r'\b[a-z]+\b', text)
        
        # 使用 collections.Counter 快速统计频率
        word_counts = Counter(words)
        
        return dict(word_counts)
        
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return {}


if __name__ == '__main__':
    test_file = "word_count_test.txt"
    content = """
    Hello world, this is a test.
    Hello again, world! This test is simple.
    """
    
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(content)

    frequency = count_word_frequency(test_file)
    
    print(f"Word frequencies in '{test_file}':")
    # 打印排序后的结果，方便查看
    for word, count in sorted(frequency.items()):
        print(f"  '{word}': {count}")

    # 清理
    if os.path.exists(test_file):
        os.remove(test_file) 