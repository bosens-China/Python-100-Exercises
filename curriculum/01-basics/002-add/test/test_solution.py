# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.total(120, 30) == 150


def test_case_02():
    assert student.total(-80, 20) == -60


def test_case_03():
    assert student.total(0, 0) == 0
