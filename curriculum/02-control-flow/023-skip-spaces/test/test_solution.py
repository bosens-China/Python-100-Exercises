# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.compact(" a	b\nc ") == "abc"


def test_case_02():
    assert student.compact("你好！") == "你好！"


def test_case_03():
    assert student.compact(" \n") == ""
