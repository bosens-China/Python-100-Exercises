import pytest
import os

def test_requirements_file_exists():
    assert os.path.exists("requirements.txt"), "requirements.txt was not created."
