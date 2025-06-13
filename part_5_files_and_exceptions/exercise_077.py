"""
### 77. 写入一个文本文件

- **描述:** 编写一个 Python 脚本，创建一个新文件 `output.txt`，并向其中写入 "This is a new file."。
- **提示:** 使用 `open()` 函数以写入模式 (`'w'`) 打开文件，然后调用 `write()` 方法。
- **期待:** 程序执行后，会生成一个 `output.txt` 文件，其内容为指定字符串。
"""
import os

def write_to_file(filename, content):
    """
    将指定的 content 写入到 filename 文件中。
    如果文件已存在，会覆盖其内容。
    :param filename: 要写入的文件的路径
    :param content: 要写入的字符串内容
    :return: 如果成功则返回 True，否则返回 False
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 调用函数写入文件
    filename = "output.txt"
    content = "This is a new file."
    success = write_to_file(filename, content)
    
    if success:
        print(f"成功将内容写入到 '{filename}'。")
        print("请手动检查该文件以验证内容。")
    else:
        print(f"写入文件 '{filename}' 失败。")
    
    # 提示：你可以尝试运行多次，看看文件内容是否被覆盖。
    # 你也可以在程序运行后手动删除 output.txt 文件。 