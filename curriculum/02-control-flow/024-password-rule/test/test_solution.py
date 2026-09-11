# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.valid_password("python12") is True


def test_case_02():
    assert student.valid_password("abcdefg1") is True


def test_case_03():
    assert student.valid_password("abc1234") is False


def test_case_04():
    assert student.valid_password("abcdefgh") is False
    assert student.valid_password("12345678") is False


def test_case_05():
    assert student.valid_password("中文中文中文１２") is False
