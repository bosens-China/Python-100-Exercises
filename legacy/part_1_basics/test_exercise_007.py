import pytest
from part_1_basics.exercise_007 import minutes_to_seconds

def test_minutes_to_seconds():
    assert minutes_to_seconds(1) == 60
    assert minutes_to_seconds(5) == 300
    assert minutes_to_seconds(0) == 0
