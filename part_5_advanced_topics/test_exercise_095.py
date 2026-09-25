from typer.testing import CliRunner
from part_4_oop.cli import app


def test_create_user_command_is_available():
    result = CliRunner().invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "create-user" in result.output or ("email" in result.output.lower() and "password" in result.output.lower())
