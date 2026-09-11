import pytest
from part_2_control_flow.exercise_022 import count_vowels

def test_count_vowels():
    assert count_vowels("hello world") == 3
    assert count_vowels("Python Programming") == 4
    assert count_vowels("AEIOU") == 5
    assert count_vowels("rhythm") == 0
    assert count_vowels("") == 0
