# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.common_tags(["py", "web", "py"], ["py", "db"]) == ["py"]


def test_case_02():
    assert student.common_tags([], ["a"]) == []


def test_case_03():
    assert student.common_tags(["b", "a", "A"], ["a", "b"]) == ["a", "b"]
