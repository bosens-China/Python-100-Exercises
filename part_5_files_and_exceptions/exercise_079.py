"""
### 79. 逐行读取文件

- **描述:** 创建一个有多行内容的文本文件 `lines.txt`。编写程序逐行读取文件内容，并在每行内容前加上行号打印出来。
- **提示:** 在 `with open(...) as f:` 块中，可以直接对文件对象 `f` 进行 `for` 循环。
- **期待:** 如果文件内容是 "First line\nSecond line"，输出应为：
  ```
  1: First line
  2: Second line
  ```
"""
import os
from typing import List

def read_lines_with_numbers(filename: str) -> List[str]:
    """
    逐行读取文件，并返回一个带有行号的字符串列表。
    :param filename: 要读取的文件的路径
    :return: 一个字符串列表，每项格式为 "行号: 内容"。如果文件未找到，返回空列表。
    """
    formatted_lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            # 在这里写下你的代码
            for i, line in enumerate(f, 1):
                # line.strip() 用于移除每行末尾的换行符 \n
                formatted_lines.append(f"{i}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    
    return formatted_lines

if __name__ == '__main__':
    test_file = "lines.txt"
    # 注意： `\n` 是换行符
    test_content = "First line\nSecond line\nThird line"

    # 准备文件
    with open(test_file, 'w', encoding='utf-8') as f:
        f.write(test_content)

    # 调用函数并打印结果
    result = read_lines_with_numbers(test_file)
    for line in result:
        print(line)
        
    # 清理
    if os.path.exists(test_file):
        os.remove(test_file) 