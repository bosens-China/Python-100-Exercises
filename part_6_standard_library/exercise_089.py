"""
### 89. `os` 模块

- **描述:** 使用 `os` 模块列出当前目录下的所有文件和文件夹。并使用 `os.path.join()` 安全地拼接一个文件路径。
- **提示:** 使用 `os.listdir('.')` 和 `os.path.join('folder', 'file.txt')`。
- **期待:**
  - 输出当前目录内容的列表。
  - 路径拼接能正确处理不同操作系统的分隔符。
"""
import os
from typing import List

def list_current_directory() -> List[str]:
    """
    列出当前工作目录下的所有文件和文件夹。
    """
    # 在这里写下你的代码
    return os.listdir('.')

def join_path_components(part1: str, part2: str) -> str:
    """
    安全地拼接两个路径部分。
    """
    # 在这里写下你的代码
    return os.path.join(part1, part2)

if __name__ == '__main__':
    print("--- 列出当前目录内容 ---")
    try:
        contents = list_current_directory()
        print("当前目录包含:")
        for item in contents:
            print(f"  - {item}")
    except Exception as e:
        print(f"无法列出目录内容: {e}")

    print("\n--- 拼接路径 ---")
    path1 = "folder"
    path2 = "file.txt"
    joined_path = join_path_components(path1, path2)
    print(f"拼接 '{path1}' 和 '{path2}' 得到: {joined_path}")
    # 注意，在 Windows 上输出会是 'folder\\file.txt'
    
    path3 = "/root/path"
    path4 = "subfolder/file.log"
    joined_path2 = join_path_components(path3, path4)
    print(f"拼接 '{path3}' 和 '{path4}' 得到: {joined_path2}") 