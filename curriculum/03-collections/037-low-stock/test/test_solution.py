# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.low_stock({"b": 2, "a": 0}, 2) == ["a"]


def test_case_02():
    assert student.low_stock({}, 2) == []


def test_case_03():
    assert student.low_stock({"z": 0, "a": 1}, 2) == ["a", "z"]


def test_case_04():
    assert student.low_stock({"a": 0}, 0) == []
