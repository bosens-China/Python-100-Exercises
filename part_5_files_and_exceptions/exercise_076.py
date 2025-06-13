"""
### 76. 读取一个文本文件

- **描述:** 创建一个名为 `hello.txt` 的文件，内容为 "Hello, Python!"。编写 Python 脚本读取该文件的全部内容并打印出来。
- **提示:** 使用 `open()` 函数以读取模式 (`'r'`) 打开文件，然后调用 `read()` 方法。
- **期待:** 程序输出 `Hello, Python!`。
"""
import os

def read_hello_file(filename):
    """
    读取指定文件的全部内容。
    :param filename: 要读取的文件的路径
    :return: 文件的内容字符串，如果文件不存在则返回错误信息。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # --- 运行前准备 ---
    # 请手动在 part_5_files_and_exceptions 文件夹下创建一个名为 "hello.txt" 的文件，
    # 并写入内容 "Hello, Python!"。
    
    # 调用函数读取文件并打印内容
    file_content = read_hello_file("hello.txt")
    print("文件内容是:")
    print(file_content) 