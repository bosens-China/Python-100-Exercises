import pytest

def test_password_hashing():
    try:
        from part_4_oop.hashing import get_password_hash, verify_password

        password = "secret"
        hashed = get_password_hash(password)

        assert isinstance(hashed, str)
        assert hashed != password
        assert verify_password(password, hashed) is True
        assert verify_password("wrongpassword", hashed) is False

    except ImportError:
        pytest.fail("Could not import hashing functions.")
    except Exception as e:
        pytest.fail(f"Password hashing test failed: {e}")
