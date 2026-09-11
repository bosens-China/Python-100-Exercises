# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.normalize("  Py Thon  ") == "py thon"


def test_case_02():
    assert student.normalize("	ABC\n") == "abc"


def test_case_03():
    assert student.normalize("   ") == ""
