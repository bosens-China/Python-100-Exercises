# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    from pathlib import Path

    assert student.write_text("out.txt", "完成") is None
    assert Path("out.txt").read_text(encoding="utf-8") == "完成"


def test_case_02():
    from pathlib import Path

    Path("out.txt").write_text("long old content", encoding="utf-8")
    student.write_text("out.txt", "新")
    assert Path("out.txt").read_text(encoding="utf-8") == "新"


def test_case_03():
    from pathlib import Path

    student.write_text("out.txt", "")
    assert Path("out.txt").read_text(encoding="utf-8") == ""
