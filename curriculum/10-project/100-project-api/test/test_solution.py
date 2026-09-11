# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    store = student.Store()
    assert student.handle(store, "GET", "/tasks") == {"status": 200, "body": []}
    created = student.handle(store, "POST", "/tasks", {"title": " A "})
    assert created == {"status": 201, "body": {"id": 1, "title": "A", "done": False}}
    assert student.handle(store, "GET", "/tasks/01") == {
        "status": 200,
        "body": created["body"],
    }
    completed = student.handle(store, "PATCH", "/tasks/1", {"done": True})
    assert completed == {"status": 200, "body": {"id": 1, "title": "A", "done": True}}
    assert student.handle(store, "PATCH", "/tasks/1", {"done": True}) == completed
    student.save_store(store, "tasks.json")
    restored = student.Store()
    student.load_store(restored, "tasks.json")
    assert student.handle(restored, "GET", "/tasks/1") == completed
    assert student.handle(restored, "DELETE", "/tasks/1") == {
        "status": 204,
        "body": None,
    }
    assert student.handle(restored, "GET", "/tasks/1") == {
        "status": 404,
        "body": {"error": "not_found"},
    }


def test_case_02():
    store = student.Store()
    for body in [None, {}, {"title": " "}, {"title": 1}, {"title": "x" * 81}]:
        assert student.handle(store, "POST", "/tasks", body) == {
            "status": 400,
            "body": {"error": "invalid_title"},
        }
    assert store.add("A")["id"] == 1


def test_case_03():
    store = student.Store()
    store.add("A")
    for body in [None, {}, {"done": False}, {"done": 1}, {"done": "true"}]:
        assert student.handle(store, "PATCH", "/tasks/1", body) == {
            "status": 400,
            "body": {"error": "invalid_done"},
        }
    assert store.list()[0]["done"] is False


def test_case_04():
    store = student.Store()
    for path in [
        "/",
        "/tasks/",
        "/tasks/0",
        "/tasks/1/edit",
        "/tasks/１",
        "/tasks/1?x=2",
    ]:
        assert student.handle(store, "GET", path) == {
            "status": 404,
            "body": {"error": "not_found"},
        }, path
    assert student.handle(store, "PATCH", "/tasks/999", None) == {
        "status": 404,
        "body": {"error": "not_found"},
    }


def test_case_05():
    store = student.Store()
    assert student.handle(store, "PUT", "/tasks") == {
        "status": 405,
        "body": {"error": "method_not_allowed"},
    }
    assert student.handle(store, "POST", "/tasks/999") == {
        "status": 405,
        "body": {"error": "method_not_allowed"},
    }


def test_case_06():
    store = student.Store()
    created = student.handle(store, "POST", "/tasks", {"title": "A"})
    created["body"]["title"] = "changed"
    listing = student.handle(store, "GET", "/tasks")
    listing["body"][0]["done"] = True
    assert store.list() == [{"id": 1, "title": "A", "done": False}]


def test_case_07():
    store = student.Store()
    store.add("A")
    store.add("B")
    student.handle(store, "DELETE", "/tasks/2")
    assert student.handle(store, "POST", "/tasks", {"title": "C"})["body"]["id"] == 3
