from part_3_functions.exercise_055 import my_decorator

def test_my_decorator(capsys):
    """
    测试装饰器是否在函数执行前后打印了预期的消息。
    """
    @my_decorator
    def say_hello():
        print("Hello!")

    say_hello()

    captured = capsys.readouterr()
    expected_output = (
        "Something is happening before the function is called.\n"
        "Hello!\n"
        "Something is happening after the function is called.\n"
    )
    assert captured.out == expected_output

def test_my_decorator_with_return_value(capsys):
    """
    测试装饰器是否能正确处理带返回值的函数。
    """
    @my_decorator
    def add(a, b):
        return a + b

    result = add(2, 3)
    
    assert result == 5
    
    captured = capsys.readouterr()
    expected_output = (
        "Something is happening before the function is called.\n"
        "Something is happening after the function is called.\n"
    )
    assert captured.out == expected_output