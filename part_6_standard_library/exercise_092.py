"""
### 92. `csv` 模块

- **描述:** 创建一个包含学生姓名和分数的列表的列表，如 `[['name', 'score'], ['Alice', 95], ['Bob', 88]]`。使用 `csv` 模块将其写入一个名为 `scores.csv` 的文件。
- **提示:** 使用 `csv.writer` 对象和 `writerow()` 或 `writerows()` 方法。
- **期待:** 生成一个标准的 CSV 文件，可以用 Excel 或文本编辑器打开。
"""
import csv
import os
from typing import List

def write_data_to_csv(filename: str, data: List[List[Any]]):
    """
    将列表的列表数据写入到 CSV 文件中。
    :param filename: 要写入的 CSV 文件名
    :param data: 包含多行数据的列表，每行本身也是一个列表
    """
    # 在这里写下你的代码
    try:
        # newline='' 是写入 CSV 文件时的推荐做法，可以防止出现空行
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            # 创建一个 writer 对象
            csv_writer = csv.writer(csvfile)
            # 使用 writerows 一次性写入所有数据
            csv_writer.writerows(data)
        return True
    except IOError:
        return False

if __name__ == '__main__':
    student_data = [
        ['name', 'score'], # 这是表头
        ['Alice', 95],
        ['Bob', 88],
        ['Charlie', 72]
    ]
    
    csv_filename = "scores.csv"
    
    success = write_data_to_csv(csv_filename, student_data)
    
    if success:
        print(f"成功将数据写入到 '{csv_filename}'。")
        print("\n文件内容:")
        # 读取并打印文件内容以供验证
        with open(csv_filename, 'r', encoding='utf-8') as f:
            print(f.read())
        # 清理
        os.remove(csv_filename)
    else:
        print(f"写入文件 '{csv_filename}' 失败。") 