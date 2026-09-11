# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.format_name(" Ada ") == "Ada"


def test_case_02():
    assert student.format_name(" Ada ", uppercase=True) == "ADA"


def test_case_03():
    assert student.format_name(" ", False) == ""
