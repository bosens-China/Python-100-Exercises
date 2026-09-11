# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.average([2, 3]) == 2.5


def test_case_02():
    assert student.average([]) is None


def test_case_03():
    assert student.average([-4, 4]) == 0


def test_case_04():
    assert student.average([7]) == 7
