# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.response(200, {"ok": True}) == {
        "status": 200,
        "headers": {"Content-Type": "application/json"},
        "body": {"ok": True},
    }


def test_case_02():
    body = {"error": "bad_request"}
    result = student.response(400, body)
    result["body"]["error"] = "changed"
    assert body == {"error": "bad_request"}


def test_case_03():
    assert student.response(201, {})["body"] == {}
