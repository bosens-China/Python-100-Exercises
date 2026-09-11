# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.unique(["b", "a", "b"]) == ["b", "a"]


def test_case_02():
    assert student.unique([]) == []


def test_case_03():
    assert student.unique(["A", "a", "A"]) == ["A", "a"]
