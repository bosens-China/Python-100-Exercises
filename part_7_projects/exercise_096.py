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

# 定义存储笔记的文件名
FILENAME = "notepad.txt"

def show_usage():
    """打印使用说明。"""
    print("\n欢迎使用命令行记事本！")
    print("用法:")
    print(f"  python {sys.argv[0]} list             - 列出所有笔记")
    print(f"  python {sys.argv[0]} add \"笔记内容\"   - 添加一条新笔记")
    print(f"  python {sys.argv[0]} delete <行号>    - 删除指定行号的笔记")
    print("-" * 30)

def load_notes():
    """从文件中加载所有笔记。"""
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f.readlines()]

def save_notes(notes):
    """将笔记列表保存回文件。"""
    with open(FILENAME, 'w', encoding='utf-8') as f:
        for note in notes:
            f.write(note + '\n')

def list_notes():
    """列出所有笔记。"""
    notes = load_notes()
    if not notes:
        print("记事本是空的。")
        return
    
    print("\n--- 你的笔记 ---")
    for i, note in enumerate(notes, 1):
        print(f"{i}. {note}")
    print("-" * 18)

def add_note(note_content):
    """添加一条新笔记。"""
    if not note_content:
        print("错误：笔记内容不能为空。")
        return
    notes = load_notes()
    notes.append(note_content)
    save_notes(notes)
    print(f"成功添加笔记: \"{note_content}\"")
    list_notes()

def delete_note(note_number):
    """删除指定编号的笔记。"""
    try:
        note_index = int(note_number) - 1
        notes = load_notes()
        
        if 0 <= note_index < len(notes):
            removed_note = notes.pop(note_index)
            save_notes(notes)
            print(f"成功删除笔记 {note_number}: \"{removed_note}\"")
            list_notes()
        else:
            print(f"错误：无效的行号 '{note_number}'。请输入一个 1 到 {len(notes)} 之间的数字。")
    except ValueError:
        print(f"错误：行号 '{note_number}' 必须是一个数字。")

def main():
    """程序主入口。"""
    # sys.argv 列表包含了所有命令行参数
    # sys.argv[0] 是脚本名
    # sys.argv[1] 是第一个参数 (命令)
    # sys.argv[2] 是第二个参数 (内容/行号)
    
    args = sys.argv[1:]
    
    if not args:
        show_usage()
        return
        
    command = args[0].lower()
    
    if command == "list":
        list_notes()
    elif command == "add":
        if len(args) > 1:
            # 将 'add' 命令之后的所有部分都作为笔记内容
            note_content = " ".join(args[1:])
            add_note(note_content)
        else:
            print("错误：'add' 命令需要提供笔记内容。")
            show_usage()
    elif command == "delete":
        if len(args) > 1:
            note_number = args[1]
            delete_note(note_number)
        else:
            print("错误：'delete' 命令需要提供行号。")
            show_usage()
    else:
        print(f"错误：未知命令 '{command}'")
        show_usage()

if __name__ == '__main__':
    main() 