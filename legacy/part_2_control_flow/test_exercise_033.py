import pytest
from part_2_control_flow.exercise_033 import Person

def test_person_introduce():
    p1 = Person(name="Bob", age=25)
    assert p1.introduce() == "Hi, my name is Bob and I am 25 years old."
    p2 = Person(name="Charlie", age=40)
    assert p2.introduce() == "Hi, my name is Charlie and I am 40 years old."
