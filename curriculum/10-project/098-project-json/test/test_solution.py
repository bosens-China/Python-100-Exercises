# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    import json

    store = student.Store()
    store.add("旧")
    assert store.import_json('[{"id":7,"title":" A ","done":true}]') == 1
    assert store.list() == [{"id": 7, "title": "A", "done": True}]
    assert json.loads(store.export_json()) == store.list()
    assert store.add("B")["id"] == 8


def test_case_02():
    import json

    store = student.Store()
    store.add("原始")
    invalid = [
        "broken",
        "{}",
        '[{"id":1,"title":"A","done":false},{"id":2,"title":" ","done":false}]',
        '[{"id":1,"title":"A","done":false},{"id":1,"title":"B","done":true}]',
    ]
    for text in invalid:
        with raises(ValueError):
            store.import_json(text)
        assert store.list() == [{"id": 1, "title": "原始", "done": False}]
    assert store.add("下一条")["id"] == 2


def test_case_03():
    import json

    store = student.Store()
    for row in [
        {"id": True, "title": "A", "done": False},
        {"id": 0, "title": "A", "done": False},
        {"id": 1, "title": "A", "done": 1},
        {"id": 1, "title": "A"},
        {"id": 1, "title": "A", "done": False, "extra": 1},
    ]:
        with raises(ValueError):
            store.import_json(json.dumps([row]))


def test_case_04():
    store = student.Store()
    store.add("A")
    assert store.import_json("[]") == 0
    assert store.list() == []
    assert store.add("B")["id"] == 1


def test_case_05():
    import json

    store = student.Store()
    store.import_json(
        '[{"id":9,"title":"九","done":false},{"id":2,"title":"二","done":true}]'
    )
    assert [row["id"] for row in json.loads(store.export_json())] == [2, 9]
