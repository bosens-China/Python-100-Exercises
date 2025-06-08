from part_3_functions.exercise_045 import sum_all

def test_multiple_arguments():
    """测试多个参数"""
    assert sum_all(1, 2, 3, 4, 5) == 15

def test_two_arguments():
    """测试两个参数"""
    assert sum_all(10, 20) == 30
    
def test_negative_numbers():
    """测试负数参数"""
    assert sum_all(-1, -2, -3) == -6

def test_mixed_numbers():
    """测试混合正负数参数"""
    assert sum_all(1, -2, 3, -4) == -2

def test_no_arguments():
    """测试没有参数"""
    assert sum_all() == 0
    
def test_one_argument():
    """测试单个参数"""
    assert sum_all(100) == 100 