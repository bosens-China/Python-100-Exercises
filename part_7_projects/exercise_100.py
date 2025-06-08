"""
### 100. 个人联系人管理器

- **描述:** 创建一个程序来管理你的联系人。程序应能让你添加、查询、修改和删除联系人。每个联系人信息至少包括姓名和电话。信息应保存在 CSV 或 JSON 文件中。
- **提示:** 这是一个面向对象编程(OOP)和文件操作的绝佳实践。可以创建一个 `Contact` 类，再创建一个 `ContactManager` 类来处理所有逻辑和文件读写。
- **期待:** 一个实用的个人联系人管理工具，每次重启程序后，之前的联系人信息都还在。
"""

import json
import sys
import os
from typing import List, Dict, Optional

# --- 定义数据文件路径 ---
CONTACTS_FILE = 'contacts.json'

class Contact:
    """表示单个联系人的类。"""
    def __init__(self, name: str, phone: str, email: Optional[str] = None):
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self) -> Dict[str, str]:
        """将联系人对象转换为字典。"""
        data = {'name': self.name, 'phone': self.phone}
        if self.email:
            data['email'] = self.email
        return data

    def __str__(self) -> str:
        """返回联系人的字符串表示。"""
        email_str = f", Email: {self.email}" if self.email else ""
        return f"姓名: {self.name}, 电话: {self.phone}{email_str}"

class ContactManager:
    """管理所有联系人逻辑的类。"""
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.contacts = self._load_contacts()

    def _load_contacts(self) -> List[Contact]:
        """从 JSON 文件加载联系人。"""
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return [Contact(**c) for c in data]
        except (json.JSONDecodeError, IOError):
            return []

    def _save_contacts(self):
        """将当前联系人列表保存到 JSON 文件。"""
        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=4, ensure_ascii=False)

    def add_contact(self, name: str, phone: str, email: Optional[str] = None):
        """添加一个新联系人。"""
        if any(c.name == name for c in self.contacts):
            print(f"错误: 姓名为 '{name}' 的联系人已存在。")
            return
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        self._save_contacts()
        print(f"成功添加联系人: {name}")

    def list_contacts(self):
        """列出所有联系人。"""
        if not self.contacts:
            print("联系人列表为空。")
            return
        print("--- 所有联系人 ---")
        for i, contact in enumerate(self.contacts, 1):
            print(f"{i}. {contact}")
        print("--------------------")

    def find_contact(self, name: str) -> Optional[Contact]:
        """按姓名查找联系人。"""
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def delete_contact(self, name: str):
        """按姓名删除联系人。"""
        contact_to_delete = self.find_contact(name)
        if contact_to_delete:
            self.contacts.remove(contact_to_delete)
            self._save_contacts()
            print(f"成功删除联系人: {name}")
        else:
            print(f"错误: 未找到姓名为 '{name}' 的联系人。")
    
    def update_contact(self, name: str, new_phone: Optional[str] = None, new_email: Optional[str] = None):
        """更新联系人信息。"""
        contact_to_update = self.find_contact(name)
        if not contact_to_update:
            print(f"错误: 未找到姓名为 '{name}' 的联系人。")
            return
        
        updated = False
        if new_phone:
            contact_to_update.phone = new_phone
            updated = True
        if new_email:
            contact_to_update.email = new_email
            updated = True
            
        if updated:
            self._save_contacts()
            print(f"成功更新联系人: {name}")
        else:
            print("未提供任何要更新的信息。")


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