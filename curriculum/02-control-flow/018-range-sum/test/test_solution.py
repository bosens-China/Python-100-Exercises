# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.sum_to(4) == 10


def test_case_02():
    assert student.sum_to(0) == 0


def test_case_03():
    assert student.sum_to(1) == 1


def test_case_04():
    assert student.sum_to(100) == 5050
