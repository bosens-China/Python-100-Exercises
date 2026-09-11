# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.parse_counts(["2", "bad", "-1"]) == {
        "values": [2, -1],
        "errors": [2],
    }


def test_case_02():
    assert student.parse_counts([]) == {"values": [], "errors": []}


def test_case_03():
    assert student.parse_counts(["", "0", "1.5", " 3 "]) == {
        "values": [0, 3],
        "errors": [1, 3],
    }
