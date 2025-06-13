from part_2_control_flow.exercise_023 import generate_multiplication_table

def test_generate_multiplication_table():
    """测试九九乘法表的生成"""
    table = generate_multiplication_table()

    # 如果学生还未实现，函数可能返回 None 或空字符串
    assert table is not None, "函数不应返回 None"
    assert len(table) > 0, "函数应返回一个非空字符串"
    
    # 检查是否以 "1*1=1" 开头 (忽略前导/尾随空白)
    assert table.strip().startswith("1*1=1")
    
    # 检查是否以 "9*9=81" 结尾 (忽略前导/尾随空白)
    assert table.strip().endswith("9*9=81")
    
    # 检查是否包含中间的某个表达式 (注意 j <= i 的规则)
    assert "7*5=35" not in table # 不应该有 7*5
    assert "5*7=35" in table     # 应该有 5*7
    
    # 检查行数是否正确。splitlines() 会按换行符分割字符串。
    # 过滤掉可能的空行。
    lines = [line for line in table.strip().splitlines() if line]
    assert len(lines) == 9, f"乘法表应有 9 行，但检测到 {len(lines)} 行。"