"""
### 100. 个人联系人管理器

- **描述:** 创建一个程序来管理你的联系人。程序应能让你添加、查询、修改和删除联系人。每个联系人信息至少包括姓名和电话。信息应保存在 CSV 或 JSON 文件中。
- **提示:** 这是一个面向对象编程(OOP)和文件操作的绝佳实践。可以创建一个 `Contact` 类，再创建一个 `ContactManager` 类来处理所有逻辑和文件读写。
- **期待:** 一个实用的个人联系人管理工具，每次重启程序后，之前的联系人信息都还在。
"""

import json
import sys
import os

# --- 定义数据文件路径 ---
CONTACTS_FILE = 'contacts.json'

class Contact:
    """表示单个联系人的类。"""
    pass

class ContactManager:
    """管理所有联系人逻辑的类。"""
    pass


def print_usage():
    """打印使用说明。"""
    print("\n--- 个人联系人管理器 ---")
    print("用法: python exercise_100.py <命令> [参数...]")
    print("命令:")
    print("  list                      - 列出所有联系人")
    print("  add <name> <phone> [email] - 添加新联系人")
    print("  find <name>               - 查找联系人")
    print("  delete <name>             - 删除联系人")
    print("  update <name> --phone <new_phone> --email <new_email> - 更新联系人")
    print("--------------------------\n")

def main():
    """主函数入口。"""
    manager = ContactManager(CONTACTS_FILE)
    args = sys.argv[1:]

    if not args:
        print_usage()
        return

    command = args[0]

    if command == 'list':
        manager.list_contacts()
    elif command == 'add':
        if len(args) < 3:
            print("错误: 'add' 命令需要姓名和电话。")
            print_usage()
        else:
            name = args[1]
            phone = args[2]
            email = args[3] if len(args) > 3 else None
            manager.add_contact(name, phone, email)
    elif command == 'find':
        if len(args) < 2:
            print("错误: 'find' 命令需要姓名。")
        else:
            contact = manager.find_contact(args[1])
            if contact:
                print(f"找到联系人: {contact}")
            else:
                print(f"未找到姓名为 '{args[1]}' 的联系人。")
    elif command == 'delete':
        if len(args) < 2:
            print("错误: 'delete' 命令需要姓名。")
        else:
            manager.delete_contact(args[1])
    elif command == 'update':
        if len(args) < 2:
            print("错误: 'update' 命令需要姓名和至少一个要更新的字段。")
            print_usage()
        else:
            name = args[1]
            # 简单的参数解析
            phone_to_update = None
            email_to_update = None
            try:
                if '--phone' in args:
                    phone_to_update = args[args.index('--phone') + 1]
                if '--email' in args:
                    email_to_update = args[args.index('--email') + 1]
            except IndexError:
                print("错误：--phone 或 --email 参数后需要提供值。")
                return
            manager.update_contact(name, phone_to_update, email_to_update)

    else:
        print(f"未知命令: {command}")
        print_usage()

if __name__ == "__main__":
    main() 