# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    from pathlib import Path

    Path("note.txt").write_text("你好\nPython\n", encoding="utf-8")
    assert student.read_text("note.txt") == "你好\nPython\n"


def test_case_02():
    from pathlib import Path

    Path("empty.txt").write_text("", encoding="utf-8")
    assert student.read_text("empty.txt") == ""


def test_case_03():
    from pathlib import Path

    Path("space.txt").write_text(" a ", encoding="utf-8")
    assert student.read_text("space.txt") == " a "
