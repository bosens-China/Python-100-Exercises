# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.add_item("a") == ["a"]
    assert student.add_item("b") == ["b"]


def test_case_02():
    items = ["x"]
    assert student.add_item("y", items) == ["x", "y"]
    assert items == ["x"]


def test_case_03():
    assert student.add_item("a", None) == ["a"]
