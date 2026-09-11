import pytest
from datetime import date
from part_3_functions.exercise_047 import parse_date

def test_parse_date():
    assert parse_date("2023-01-15") == date(2023, 1, 15)
    assert parse_date("1999-12-31") == date(1999, 12, 31)
