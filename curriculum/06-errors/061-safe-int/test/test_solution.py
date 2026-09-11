# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.parse_int(" -2 ") == -2


def test_case_02():
    assert student.parse_int("abc") is None


def test_case_03():
    assert student.parse_int("") is None
    assert student.parse_int("1.5") is None


def test_case_04():
    assert student.parse_int("0") == 0
