from part_2_control_flow.exercise_023 import generate_multiplication_table

def test_generate_multiplication_table():
    """测试九九乘法表的生成"""
    table = generate_multiplication_table()
    
    # 检查是否生成了内容
    assert len(table) > 0
    
    # 检查第一行的内容
    assert table.strip().startswith("1*1=1")
    
    # 检查最后一行的最后一个表达式
    assert "9*9=81" in table
    
    # 检查是否包含中间的某个表达式
    assert "5*7=35" in table
    
    # 检查换行符数量，应该有 9 行
    assert table.strip().count('\\n') == 8 