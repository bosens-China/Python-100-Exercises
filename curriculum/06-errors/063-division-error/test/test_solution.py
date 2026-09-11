# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.divide_result(5, 2) == {"ok": True, "value": 2.5}


def test_case_02():
    assert student.divide_result(3, 0) == {"ok": False, "error": "division_by_zero"}


def test_case_03():
    assert student.divide_result(0, 4) == {"ok": True, "value": 0}
    assert student.divide_result(-6, 2) == {"ok": True, "value": -3}
