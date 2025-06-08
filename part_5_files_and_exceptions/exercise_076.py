"""
### 76. 读取一个文本文件

- **描述:** 创建一个名为 `hello.txt` 的文件，内容为 "Hello, Python!"。编写 Python 脚本读取该文件的全部内容并打印出来。
- **提示:** 使用 `open()` 函数以读取模式 (`'r'`) 打开文件，然后调用 `read()` 方法。
- **期待:** 程序输出 `Hello, Python!`。
"""
import os

def read_hello_file(filename="hello.txt"):
    """
    读取指定文件的全部内容。
    :param filename: 要读取的文件的路径
    :return: 文件的内容字符串，如果文件不存在则返回错误信息。
    """
    try:
        f = open(filename, 'r', encoding='utf-8')
        content = f.read()
        f.close()
        return content
    except FileNotFoundError:
        return f"Error: The file '{filename}' was not found."

if __name__ == '__main__':
    # 为了让脚本可以独立运行，我们在运行前先创建这个文件
    try:
        with open("hello.txt", "w", encoding='utf-8') as f:
            f.write("Hello, Python!")
        
        # 调用函数读取文件并打印内容
        file_content = read_hello_file()
        print(file_content)

    finally:
        # 清理创建的文件
        if os.path.exists("hello.txt"):
            os.remove("hello.txt") 