# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.word_counts(["py", "js", "py"]) == {"py": 2, "js": 1}


def test_case_02():
    assert student.word_counts([]) == {}


def test_case_03():
    assert student.word_counts(["A", "a", ""]) == {"A": 1, "a": 1, "": 1}
