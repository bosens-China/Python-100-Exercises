from unittest.mock import patch
from part_3_functions.exercise_056 import repeat

def test_return_values():
    """测试装饰一个返回值的函数"""
    @repeat(num_times=4)
    def get_number(n):
        return n

    assert get_number(10) == [10, 10, 10, 10]

def test_no_return_value():
    """测试装饰一个没有返回值的函数"""
    @repeat(num_times=2)
    def do_nothing():
        pass
    
    assert do_nothing() == [None, None]

@patch('builtins.print')
def test_print_calls(mock_print):
    """测试装饰一个打印的函数，并验证 print 被调用的次数和内容"""
    @repeat(num_times=3)
    def greet(name):
        print(f"Hi {name}")

    greet("Test")
    
    # 验证 print 被调用了3次
    assert mock_print.call_count == 3
    
    # 验证每次调用 print 时的参数
    mock_print.assert_called_with("Hi Test")

def test_with_arguments():
    """测试装饰一个带多个参数的函数"""
    @repeat(num_times=2)
    def multiply(a, b, c=1):
        return a * b * c
        
    assert multiply(2, 3) == [6, 6]
    assert multiply(2, 3, c=4) == [24, 24]
    
def test_repeat_zero_times():
    """测试重复0次的情况"""
    @repeat(num_times=0)
    def should_not_run():
        return "should not be in result"
        
    assert should_not_run() == [] 