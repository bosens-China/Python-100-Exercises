# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.next_count(" 9 ") == 10


def test_case_02():
    assert student.next_count("-2") == -1


def test_case_03():
    assert student.next_count("0") == 1
