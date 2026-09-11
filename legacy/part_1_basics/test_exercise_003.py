import pytest
from part_1_basics.exercise_003 import join_strings

def test_join_strings():
    assert join_strings("hello", "world") == "helloworld"
    assert join_strings("py", "thon") == "python"
    assert join_strings("", "test") == "test"
