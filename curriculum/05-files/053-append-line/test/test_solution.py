# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    from pathlib import Path

    student.append_line("log.txt", "第一条")
    student.append_line("log.txt", "第二条")
    assert Path("log.txt").read_text(encoding="utf-8") == "第一条\n第二条\n"


def test_case_02():
    from pathlib import Path

    Path("log.txt").write_text("旧\n", encoding="utf-8")
    assert student.append_line("log.txt", "新") is None
    assert Path("log.txt").read_text(encoding="utf-8") == "旧\n新\n"


def test_case_03():
    from pathlib import Path

    student.append_line("log.txt", "")
    assert Path("log.txt").read_text(encoding="utf-8") == "\n"
