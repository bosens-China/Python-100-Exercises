from part_5_files_and_exceptions.exercise_083 import divide_with_else_finally

def test_successful_case(capsys):
    """测试成功计算时，else 和 finally 块的行为。"""
    result = divide_with_else_finally(10, 2)
    
    # 检查返回值
    assert result == 5.0
    # 检查打印输出
    captured = capsys.readouterr()
    output = captured.out
    assert "计算成功" in output
    assert "计算结束" in output
    # 确保 "计算成功" 在 "计算结束" 之前
    assert output.find("计算成功") < output.find("计算结束")

def test_zero_division_case(capsys):
    """测试除以零时，except 和 finally 块的行为。"""
    result = divide_with_else_finally(10, 0)
    
    # 检查返回值
    assert result is None
    # 检查打印输出
    captured = capsys.readouterr()
    output = captured.out
    assert "错误：除数不能为零！" in output
    assert "计算结束" in output
    # 确保 else 块没有被执行
    assert "计算成功" not in output

def test_type_error_case(capsys):
    """测试类型错误时，except 和 finally 块的行为。"""
    result = divide_with_else_finally(10, "a")
    
    # 检查返回值
    assert result is None
    # 检查打印输出
    captured = capsys.readouterr()
    output = captured.out
    assert "错误：输入必须是数字！" in output
    assert "计算结束" in output
    # 确保 else 块没有被执行
    assert "计算成功" not in output 