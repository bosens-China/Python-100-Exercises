import importlib
from part_3_functions import exercise_047

def test_attempt_to_modify_x_without_global():
    """
    测试不使用 global 关键字时，函数调用不会改变全局变量。
    """
    # 每次测试前，我们都重新加载模块来重置全局变量 x 的状态
    importlib.reload(exercise_047)
    assert exercise_047.x == 10
    
    # 调用函数
    exercise_047.attempt_to_modify_x_without_global()
    
    # 验证全局变量 x 的值没有改变
    assert exercise_047.x == 10

def test_modify_x_with_global():
    """
    测试使用 global 关键字时，函数调用会改变全局变量。
    """
    # 再次重新加载模块以确保 x 的初始值为 10
    importlib.reload(exercise_047)
    assert exercise_047.x == 10
    
    # 调用函数
    exercise_047.modify_x_with_global()
    
    # 验证全局变量 x 的值已经被修改
    assert exercise_047.x == 30 