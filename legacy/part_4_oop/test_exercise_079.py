import pytest
from jose import jwt

def test_create_access_token():
    try:
        from part_4_oop.auth import create_access_token, SECRET_KEY, ALGORITHM
        token = create_access_token(data={"sub": "test@example.com"})
        assert isinstance(token, str)
        
        decoded = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        assert decoded["sub"] == "test@example.com"
        assert "exp" in decoded
    except ImportError:
        pytest.fail("Could not import create_access_token or JWT settings.")
