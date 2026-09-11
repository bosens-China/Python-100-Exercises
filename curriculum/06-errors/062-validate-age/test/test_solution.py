# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.validate_age(0) == 0
    assert student.validate_age(120) == 120


def test_case_02():
    with raises(ValueError):
        student.validate_age(-1)
    with raises(ValueError):
        student.validate_age(121)


def test_case_03():
    for value in [True, "18", 18.0, None]:
        with raises(ValueError):
            student.validate_age(value)
