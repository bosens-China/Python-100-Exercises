import pytest
import requests
from part_3_functions.exercise_043 import get_user_name_from_api

def test_get_user_name_from_api(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"id": 1, "name": "Alice"}
    mocker.patch("requests.get", return_value=mock_response)

    user_name = get_user_name_from_api(1)

    requests.get.assert_called_once_with("https://api.example.com/users/1")
    assert user_name == "Alice"
