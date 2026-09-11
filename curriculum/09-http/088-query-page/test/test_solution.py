# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.parse_page({}) == 1
    assert student.parse_page({"page": "02"}) == 2
    assert student.parse_page({"page": "1000"}) == 1000


def test_case_02():
    for value in ["", "0", "1001", "-1", " 2 ", "２", 2, None]:
        with raises(ValueError):
            student.parse_page({"page": value})


def test_case_03():
    assert student.parse_page({"other": "x"}) == 1
