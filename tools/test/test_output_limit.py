from tools.grader import grade


def test_print_loop_stops_at_output_limit():
    result = grade(
        {"main.py": "def noisy():\n    while True:\n        print('x' * 1000)"},
        "def test_output():\n    student.noisy()",
    )
    assert result["passed"] is False
    assert len(result["cases"][0]["stdout"]) <= 32_000
    assert "OutputLimitExceeded" in result["cases"][0]["message"]
