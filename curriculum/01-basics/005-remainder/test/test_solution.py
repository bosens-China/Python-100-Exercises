# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.remaining_seconds(125) == 5


def test_case_02():
    assert student.remaining_seconds(60) == 0


def test_case_03():
    assert student.remaining_seconds(0) == 0


def test_case_04():
    assert student.remaining_seconds(59) == 59
