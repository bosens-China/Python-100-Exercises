# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.route("GET", "/health") == {"status": 200, "body": {"ok": True}}


def test_case_02():
    assert student.route("POST", "/health") == {
        "status": 405,
        "body": {"error": "method_not_allowed"},
    }


def test_case_03():
    assert student.route("GET", "/missing") == {
        "status": 404,
        "body": {"error": "not_found"},
    }
    assert student.route("POST", "/missing") == {
        "status": 404,
        "body": {"error": "not_found"},
    }
