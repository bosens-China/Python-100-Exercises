import pytest

def test_python_jose_installed():
    try:
        import jose
    except ImportError:
        pytest.fail("The 'python-jose' library is not installed.")
