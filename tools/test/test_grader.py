import sys
import types
from pathlib import Path

import pytest

from tools.grader import grade


def test_reports_actual_expected_and_keeps_other_cases_running():
    result = grade(
        {"main.py": "def add(a, b): return a - b"},
        "def test_wrong():\n    assert student.add(2, 3) == 5\n"
        "def test_zero():\n    assert student.add(1, 0) == 1\n",
    )
    assert result["passed"] is False
    assert result["passed_count"] == 1
    assert "预期：5；实际：-1" in result["cases"][0]["message"]


def test_comparison_does_not_call_student_twice():
    result = grade(
        {
            "main.py": "count = 0\ndef next_value():\n    global count\n    count += 1\n    return count"
        },
        "def test_calls():\n    assert student.next_value() == 1\n    assert student.count == 1",
    )
    assert result["passed"]


def test_boolean_identity_is_not_replaced_by_equality():
    result = grade(
        {"main.py": "value = 1"}, "def test_bool():\n    assert student.value is True"
    )
    assert result["passed"] is False


def test_module_and_filesystem_state_reset_for_each_case(tmp_path):
    original_cwd = Path.cwd()
    original_path = sys.path.copy()
    sentinel = types.ModuleType("helper")
    previous = sys.modules.get("helper")
    sys.modules["helper"] = sentinel
    try:
        result = grade(
            {
                "main.py": "from helper import values\nfrom pathlib import Path\ndef update():\n    values.append(1)\n    Path('created.txt').write_text('x')",
                "helper.py": "values = []",
            },
            "from pathlib import Path\n"
            "def test_first():\n    assert student.values == []\n    assert not Path('created.txt').exists()\n    student.update()\n"
            "def test_second():\n    assert student.values == []\n    assert not Path('created.txt').exists()",
        )
        assert result["passed"], result
        assert sys.modules["helper"] is sentinel
        assert Path.cwd() == original_cwd
        assert sys.path == original_path
    finally:
        if previous is None:
            sys.modules.pop("helper", None)
        else:
            sys.modules["helper"] = previous


@pytest.mark.parametrize(
    "source, error",
    [
        ("def broken(:", "SyntaxError"),
        ("import nonexistent_python100_package", "ModuleNotFoundError"),
        ("raise SystemExit(2)", "SystemExit"),
    ],
)
def test_student_load_errors_do_not_escape(source, error):
    result = grade(
        {"main.py": source}, "def test_value():\n    assert student.value == 1"
    )
    assert result["passed"] is False
    assert error in result["cases"][0]["message"]


def test_output_and_expected_exceptions_are_reported():
    result = grade(
        {
            "main.py": "def reject():\n    print('正在检查')\n    raise ValueError('无效')"
        },
        "def test_rejection():\n    with raises(ValueError):\n        student.reject()",
    )
    assert result["passed"]
    assert result["cases"][0]["stdout"] == "正在检查\n"


@pytest.mark.parametrize(
    "tests", ["", "def broken(:", "def test_a(): pass\ndef test_a(): pass"]
)
def test_empty_invalid_or_duplicate_tests_cannot_pass(tests):
    result = grade({"main.py": "value = 1"}, tests)
    assert result["passed"] is False
    assert result["content_error"]


def test_test_setup_error_is_distinct_from_student_failure():
    result = grade(
        {"main.py": "value = 1"},
        "raise RuntimeError('bad fixture')\ndef test_value():\n    assert student.value == 1",
    )
    assert result["cases"][0]["status"] == "content_error"


def test_workspace_filenames_cannot_escape():
    with pytest.raises(ValueError):
        grade({"main.py": "", "../outside.py": ""}, "def test_a(): pass")


def test_edited_source_is_loaded_on_next_submission():
    tests = "def test_value():\n    assert student.value() == 2"
    assert not grade(
        {"main.py": "from helper import value", "helper.py": "def value(): return 1"},
        tests,
    )["passed"]
    assert grade(
        {"main.py": "from helper import value", "helper.py": "def value(): return 2"},
        tests,
    )["passed"]
