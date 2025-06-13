"""
### 80. 复制文件

- **描述:** 编写一个程序，将一个文件（例如 `hello.txt`）的内容复制到另一个新文件（`hello_copy.txt`）中。
- **提示:** 先以读取模式打开源文件，再以写入模式打开目标文件，然后读取源文件内容并写入目标文件。
- **期待:** 程序执行后，`hello_copy.txt` 的内容与 `hello.txt` 完全相同。
"""
import os

def copy_file(source_filename, destination_filename):
    """
    将源文件的内容复制到目标文件。
    :param source_filename: 源文件的路径
    :param destination_filename: 目标文件的路径
    :return: 如果成功返回 True，否则返回 False
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    source_file = "source.txt"
    dest_file = "destination.txt"
    content = "This is the content of the source file."

    # 创建源文件
    with open(source_file, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"Attempting to copy '{source_file}' to '{dest_file}'...")
    
    if copy_file(source_file, dest_file):
        print("File copied successfully.")
        # 验证内容
        with open(dest_file, 'r', encoding='utf-8') as f:
            copied_content = f.read()
        print(f"Content of destination file: '{copied_content}'")
        print(f"Are contents identical? {content == copied_content}")
    else:
        print("File copy failed.")

    # 清理
    if os.path.exists(source_file):
        os.remove(source_file)
    if os.path.exists(dest_file):
        os.remove(dest_file) 