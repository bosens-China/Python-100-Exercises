import pytest
from part_1_basics.exercise_017 import reverse_string

def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("python") == "nohtyp"
    assert reverse_string("a") == "a"
    assert reverse_string("") == ""
