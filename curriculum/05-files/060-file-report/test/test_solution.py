# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    import json
    from pathlib import Path

    Path("in.txt").write_text("Py py\nWeb", encoding="utf-8")
    assert student.word_report("in.txt", "out.json") == {"py": 2, "web": 1}
    assert json.loads(Path("out.json").read_text(encoding="utf-8")) == {
        "py": 2,
        "web": 1,
    }
    assert Path("in.txt").read_text(encoding="utf-8") == "Py py\nWeb"


def test_case_02():
    import json
    from pathlib import Path

    Path("in.txt").write_text("", encoding="utf-8")
    Path("out.json").write_text("old", encoding="utf-8")
    assert student.word_report("in.txt", "out.json") == {}
    assert json.loads(Path("out.json").read_text(encoding="utf-8")) == {}


def test_case_03():
    from pathlib import Path

    Path("in.txt").write_text("Hi! hi! 你好", encoding="utf-8")
    assert student.word_report("in.txt", "out.json") == {"hi!": 2, "你好": 1}
