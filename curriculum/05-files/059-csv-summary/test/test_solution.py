# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    from pathlib import Path

    Path("sales.csv").write_text("price,quantity\n100,2\n50,3\n", encoding="utf-8")
    assert student.sales_total("sales.csv") == 350


def test_case_02():
    from pathlib import Path

    Path("sales.csv").write_text("price,quantity\n", encoding="utf-8")
    assert student.sales_total("sales.csv") == 0


def test_case_03():
    from pathlib import Path

    Path("sales.csv").write_text("price,quantity\n0,20\n99,0\n", encoding="utf-8")
    assert student.sales_total("sales.csv") == 0
