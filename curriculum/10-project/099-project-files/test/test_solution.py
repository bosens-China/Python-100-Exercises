# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    store = student.Store()
    store.add("学习")
    store.complete(1)
    assert student.save_store(store, "tasks.json") is None
    restored = student.Store()
    assert student.load_store(restored, "tasks.json") == 1
    assert restored.list() == store.list()
    assert restored.add("继续")["id"] == 2


def test_case_02():
    from pathlib import Path

    store = student.Store()
    store.add("原始")
    with raises(FileNotFoundError):
        student.load_store(store, "missing.json")
    Path("bad.json").write_text("broken", encoding="utf-8")
    with raises(ValueError):
        student.load_store(store, "bad.json")
    assert store.list() == [{"id": 1, "title": "原始", "done": False}]


def test_case_03():
    import json
    from pathlib import Path

    Path("tasks.json").write_text("long old content", encoding="utf-8")
    store = student.Store()
    student.save_store(store, "tasks.json")
    assert json.loads(Path("tasks.json").read_text(encoding="utf-8")) == []
