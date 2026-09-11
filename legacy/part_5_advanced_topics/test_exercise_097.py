import pytest
import os

def test_gil_explanation_file_exists():
    assert os.path.exists("GIL_EXPLANATION.md"), "The markdown file was not created."
