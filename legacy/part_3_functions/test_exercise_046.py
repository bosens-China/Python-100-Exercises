import pytest
from part_3_functions.exercise_046 import log_call
import time

# We need to capture print output for this test
from io import StringIO
import sys

@pytest.fixture
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err

def test_log_call_decorator(captured_output):
    @log_call
    def say_hello(name):
        return f"Hello, {name}"

    result = say_hello("World")
    
    # Check return value
    assert result == "Hello, World"

    # Check printed output
    output = captured_output[0].getvalue().strip()
    assert "Calling function 'say_hello'..." in output
    assert "Function 'say_hello' finished." in output
