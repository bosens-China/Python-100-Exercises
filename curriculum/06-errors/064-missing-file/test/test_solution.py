# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.read_or_default("missing.txt", "新建") == "新建"
    assert student.read_or_default("missing.txt") == ""


def test_case_02():
    from pathlib import Path

    Path("empty.txt").write_text("", encoding="utf-8")
    assert student.read_or_default("empty.txt", "新建") == ""


def test_case_03():
    from pathlib import Path

    Path("content.txt").write_text("内容\n", encoding="utf-8")
    assert student.read_or_default("content.txt") == "内容\n"


def test_case_04():
    from pathlib import Path

    Path("folder").mkdir()
    with raises(OSError):
        student.read_or_default("folder", "不应隐藏错误")
