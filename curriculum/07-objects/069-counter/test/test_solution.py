# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    counter = student.Counter(2)
    assert counter.value == 2
    assert counter.increment() == 3
    assert counter.increment() == 4


def test_case_02():
    first = student.Counter()
    second = student.Counter()
    first.increment()
    assert second.value == 0


def test_case_03():
    assert student.Counter(-1).increment() == 0
