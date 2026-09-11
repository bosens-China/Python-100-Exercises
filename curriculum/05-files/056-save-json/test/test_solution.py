# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    import json
    from pathlib import Path

    data = {"name": "小林", "done": True, "note": None}
    assert student.save_json("data.json", data) is None
    assert json.loads(Path("data.json").read_text(encoding="utf-8")) == data


def test_case_02():
    import json
    from pathlib import Path

    Path("data.json").write_text("old content", encoding="utf-8")
    student.save_json("data.json", [])
    assert json.loads(Path("data.json").read_text(encoding="utf-8")) == []


def test_case_03():
    import json
    from pathlib import Path

    student.save_json("data.json", {"x": [1, 2]})
    assert json.loads(Path("data.json").read_text(encoding="utf-8")) == {"x": [1, 2]}
