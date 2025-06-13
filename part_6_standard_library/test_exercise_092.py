import csv
import os
from part_6_standard_library.exercise_092 import write_data_to_csv

def test_write_data_to_csv(tmp_path):
    """
    测试能否成功将数据写入 CSV 文件。
    使用 pytest 的 tmp_path fixture 来创建一个临时目录和文件，
    这样就不会在项目目录中留下测试文件。
    """
    # 1. 准备测试数据和临时文件路径
    test_data = [
        ['name', 'score', 'grade'],
        ['Alice', 95, 'A'],
        ['Bob', 88, 'B'],
        ['Charlie', 72, 'C']
    ]
    # tmp_path 是一个 Pathlib 对象
    temp_csv_file = tmp_path / "test_scores.csv"

    # 2. 调用被测函数
    write_data_to_csv(str(temp_csv_file), test_data)

    # 3. 验证文件是否被创建
    assert os.path.exists(temp_csv_file)

    # 4. 验证文件内容是否正确
    with open(temp_csv_file, 'r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        # 将读取器转换为列表
        content_read = list(reader)

    # csv 模块写入时，所有字段都会被视为字符串
    expected_data_as_str = [
        ['name', 'score', 'grade'],
        ['Alice', '95', 'A'],
        ['Bob', '88', 'B'],
        ['Charlie', '72', 'C']
    ]
    
    assert content_read == expected_data_as_str 