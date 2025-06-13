"""
### 96. 简单的命令行记事本

- **描述:** 实现一个命令行程序，可以添加、查看、删除笔记。笔记需要被持久化存储在文件中（例如 a.txt）。
  - `python notepad.py add "第一条笔记"`
  - `python notepad.py list`
  - `python notepad.py delete 1`
- **提示:** 综合运用文件操作、`sys.argv`、函数和列表/字典。
- **期待:** 一个功能完整的命令行记事本工具。
"""
import sys
import os

# 定义默认的存储笔记的文件名
DEFAULT_FILENAME = "notepad.txt"

def show_usage():
    """打印使用说明。"""
    print("\n欢迎使用命令行记事本！")
    print("用法:")
    print(f"  python {sys.argv[0]} list             - 列出所有笔记")
    print(f"  python {sys.argv[0]} add \"笔记内容\"   - 添加一条新笔记")
    print(f"  python {sys.argv[0]} delete <行号>    - 删除指定行号的笔记")
    print("-" * 30)

def load_notes(filename):
    """从指定文件中加载所有笔记。"""
    # 在这里写下你的代码
    pass

def save_notes(notes, filename):
    """将笔记列表保存到指定文件。"""
    # 在这里写下你的代码
    pass

def list_notes(filename):
    """列出指定文件中的所有笔记。"""
    # 在这里写下你的代码
    pass

def add_note(note_content, filename):
    """向指定文件添加一条新笔记。"""
    # 在这里写下你的代码
    pass

def delete_note(note_number_str, filename):
    """从指定文件中删除指定编号的笔记。"""
    # 在这里写下你的代码
    pass

def main():
    """程序主入口，处理命令行参数。"""
    args = sys.argv[1:]
    
    if not args:
        show_usage()
        return
        
    command = args[0].lower()
    
    # 所有文件操作都使用默认文件名
    filename = DEFAULT_FILENAME
    
    if command == "list":
        list_notes(filename)
    elif command == "add":
        if len(args) > 1:
            note_content = " ".join(args[1:])
            add_note(note_content, filename)
        else:
            print("错误：'add' 命令需要提供笔记内容。")
    elif command == "delete":
        if len(args) > 1:
            note_number_str = args[1]
            delete_note(note_number_str, filename)
        else:
            print("错误：'delete' 命令需要提供行号。")
    else:
        print(f"错误：未知命令 '{command}'")
        show_usage()

if __name__ == '__main__':
    # 调用主函数来处理命令行参数
    main() 