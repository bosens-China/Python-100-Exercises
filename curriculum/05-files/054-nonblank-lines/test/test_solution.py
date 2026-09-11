# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    from pathlib import Path

    Path("in.txt").write_text(" a\n\n b \n", encoding="utf-8")
    assert student.read_nonblank("in.txt") == ["a", "b"]


def test_case_02():
    from pathlib import Path

    Path("in.txt").write_text(" \n	", encoding="utf-8")
    assert student.read_nonblank("in.txt") == []


def test_case_03():
    from pathlib import Path

    Path("in.txt").write_text("a\na", encoding="utf-8")
    assert student.read_nonblank("in.txt") == ["a", "a"]
