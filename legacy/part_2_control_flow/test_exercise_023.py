import pytest
from part_2_control_flow.exercise_023 import is_palindrome

def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("level") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("a") == True
    assert is_palindrome("") == True
