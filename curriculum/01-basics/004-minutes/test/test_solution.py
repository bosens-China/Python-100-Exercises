# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.whole_minutes(125) == 2


def test_case_02():
    assert student.whole_minutes(59) == 0


def test_case_03():
    assert student.whole_minutes(60) == 1


def test_case_04():
    assert type(student.whole_minutes(0)) is int
