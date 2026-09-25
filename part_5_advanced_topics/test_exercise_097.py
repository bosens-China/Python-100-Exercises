import pytest
from part_5_advanced_topics.exercise_097 import retry_call


def test_retry_call_stops_after_success():
    calls = []

    def flaky():
        calls.append(1)
        if len(calls) < 3:
            raise RuntimeError("try again")
        return "ok"

    assert retry_call(flaky, attempts=4) == "ok"
    assert len(calls) == 3


def test_retry_call_preserves_last_error():
    with pytest.raises(RuntimeError, match="last"):
        retry_call(lambda: (_ for _ in ()).throw(RuntimeError("last")), attempts=2)
    with pytest.raises(ValueError):
        retry_call(lambda: None, attempts=0)
