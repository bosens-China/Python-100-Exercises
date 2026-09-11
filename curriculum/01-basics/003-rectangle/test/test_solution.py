# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.area(3, 7) == 21


def test_case_02():
    assert student.area(0, 9) == 0


def test_case_03():
    assert student.area(8, 1) == 8
