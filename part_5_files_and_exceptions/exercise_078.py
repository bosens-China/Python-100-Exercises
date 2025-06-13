"""
### 78. 使用 `with` 语句

- **描述:** 重写第 76 和 77 题，但这次使用 `with open(...) as f:` 结构来自动管理文件的打开和关闭。
- **提示:** `with` 语句确保即使发生错误，文件也会被正确关闭，是处理文件的推荐方式。
- **期待:** 功能与原题相同，但代码更健壮、更简洁。
"""
import os

def read_with_with(filename):
    # 在这里写下你的代码
    pass

def write_with_with(filename, content):
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    test_file = "temp_file_for_with.txt"
    test_content = "This was written using a 'with' statement."

    print("--- 演示写入 ---")
    if write_with_with(test_file, test_content):
        print(f"Successfully wrote to '{test_file}'.")
    else:
        print(f"Failed to write to '{test_file}'.")

    print("\n--- 演示读取 ---")
    read_content = read_with_with(test_file)
    print(f"Content read from '{test_file}':")
    print(read_content)
    
    # 清理
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\nCleaned up '{test_file}'.") 