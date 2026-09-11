# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.text_length("你好 Python") == 9


def test_case_02():
    assert student.text_length("") == 0


def test_case_03():
    assert student.text_length(" a ") == 3
