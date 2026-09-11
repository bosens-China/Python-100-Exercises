import pytest
import os

def test_readme_is_substantial():
    assert os.path.exists("README.md")
    with open("README.md", "r", encoding="utf-8") as f:
        content = f.read()
        # A simple check for a reasonably detailed README
        assert len(content) > 500, "README.md is too short. Please add more details."
