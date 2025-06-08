from part_1_basics.exercise_001 import hello_world

def test_hello_world(capsys):
    """
    测试 hello_world 函数是否正确打印 "Hello, World!"。

    使用 pytest 的 capsys fixture 来捕获标准输出。
    """
    hello_world()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n" 