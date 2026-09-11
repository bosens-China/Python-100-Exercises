import pytest

def test_config_settings_structure():
    try:
        from part_4_oop.config import settings
        assert hasattr(settings, 'DATABASE_URL')
        assert hasattr(settings, 'SECRET_KEY')
    except ImportError:
        pytest.fail("Could not import settings from config.py")
