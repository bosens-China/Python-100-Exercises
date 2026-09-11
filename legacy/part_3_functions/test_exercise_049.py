import pytest
import os
from part_3_functions.exercise_049 import join_path

def test_join_path():
    # os.path.join behaves differently on Windows vs. Unix-like systems
    # On Windows, it will use backslashes. On others, forward slashes.
    # The test should account for this.
    expected = os.path.join("my_folder", "my_file.txt")
    assert join_path("my_folder", "my_file.txt") == expected
    expected_nested = os.path.join("a", "b", "c")
    assert join_path("a/b", "c") == expected_nested or join_path("a\\b", "c") == expected_nested
