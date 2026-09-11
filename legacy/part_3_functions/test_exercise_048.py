import pytest
from datetime import date
from part_3_functions.exercise_048 import days_between

def test_days_between():
    d1 = date(2023, 1, 1)
    d2 = date(2023, 1, 11)
    assert days_between(d1, d2) == 10
    assert days_between(d2, d1) == 10  # Order shouldn't matter
    assert days_between(d1, d1) == 0
