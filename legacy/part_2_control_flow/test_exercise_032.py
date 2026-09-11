import pytest
from part_2_control_flow.exercise_032 import Person

def test_person_init():
    p = Person(name="Alice", age=30)
    assert p.name == "Alice"
    assert p.age == 30
