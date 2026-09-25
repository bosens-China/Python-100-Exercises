from part_5_advanced_topics.exercise_096 import profile_call


def test_profile_call_returns_result_and_report():
    calls = []

    def double(value):
        calls.append(value)
        return value * 2

    result, report = profile_call(double, 4)
    assert result == 8
    assert calls == [4]
    assert "double" in report
    assert "function calls" in report
