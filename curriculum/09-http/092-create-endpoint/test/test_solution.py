# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    calls = []

    def save(title):
        calls.append(title)
        return 7

    assert student.create_task({"title": " A "}, save) == {
        "status": 201,
        "body": {"id": 7, "title": "A", "done": False},
    }
    assert calls == ["A"]


def test_case_02():
    calls = []
    for body in [{}, {"title": " "}, {"title": "x" * 81}, None, {"title": 1}]:
        assert student.create_task(body, lambda title: calls.append(title)) == {
            "status": 400,
            "body": {"error": "invalid_title"},
        }
    assert calls == []


def test_case_03():
    def broken(title):
        raise ValueError("storage failure")

    with raises(ValueError):
        student.create_task({"title": "A"}, broken)


def test_case_04():
    assert student.create_task({"title": "x" * 80}, lambda title: 1)["status"] == 201
