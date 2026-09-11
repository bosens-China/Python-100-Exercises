import pytest
from part_1_basics.exercise_001 import hello_world

def test_hello_world():
    assert hello_world() == "Hello, World!"
