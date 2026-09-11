# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.group_names(["Amy", "Ann", "Bob"]) == {
        "A": ["Amy", "Ann"],
        "B": ["Bob"],
    }


def test_case_02():
    assert student.group_names([]) == {}


def test_case_03():
    assert student.group_names(["a", "A", "a"]) == {"a": ["a", "a"], "A": ["A"]}
