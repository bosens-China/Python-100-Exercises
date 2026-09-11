# student 是本次执行的 main.py 模块；raises 用于验证异常类型。


def test_case_01():
    assert student.enabled_names(
        '[ {"name": "提示", "enabled": true}, {"name": "声音", "enabled": false} ]'
    ) == ["提示"]


def test_case_02():
    assert student.enabled_names("[]") == []


def test_case_03():
    assert student.enabled_names(
        '[{"name":"A","enabled":true},{"name":"A","enabled":true}]'
    ) == ["A", "A"]
