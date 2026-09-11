import pytest
from part_1_basics.exercise_016 import contains_substring

def test_contains_substring():
    assert contains_substring("hello world", "world") == True
    assert contains_substring("python", "java") == False
    assert contains_substring("test", "test") == True
    assert contains_substring("abc", "d") == False
