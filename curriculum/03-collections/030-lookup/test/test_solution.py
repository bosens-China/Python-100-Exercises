# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.get_setting({"theme": "dark"}, "theme", "light") == "dark"


def test_case_02():
    assert student.get_setting({}, "theme", "light") == "light"


def test_case_03():
    assert student.get_setting({"name": ""}, "name", "guest") == ""
