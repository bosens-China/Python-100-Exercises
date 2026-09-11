import pytest
import os

def test_alembic_init():
    # This test checks if the alembic directory and ini file are created.
    # A full test would involve running migrations.
    assert os.path.isdir("alembic")
    assert os.path.isfile("alembic.ini")
