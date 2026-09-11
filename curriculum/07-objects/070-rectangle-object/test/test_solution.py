# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    shape = student.Rectangle(3, 4)
    assert shape.width == 3 and shape.height == 4
    assert shape.area() == 12
    assert shape.perimeter() == 14


def test_case_02():
    shape = student.Rectangle(0, 5)
    assert shape.area() == 0
    assert shape.perimeter() == 10


def test_case_03():
    with raises(ValueError):
        student.Rectangle(-1, 2)
    with raises(ValueError):
        student.Rectangle(2, -1)
