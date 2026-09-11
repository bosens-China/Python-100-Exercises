# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.factorial(4) == 24


def test_case_02():
    assert student.factorial(0) == 1


def test_case_03():
    assert student.factorial(1) == 1


def test_case_04():
    assert student.factorial(6) == 720
