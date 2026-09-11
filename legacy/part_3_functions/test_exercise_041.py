import pytest
from part_3_functions.exercise_041 import get_json_from_url

def test_get_json_from_url(mocker):
    # Mock the requests.get call
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"key": "value"}
    mocker.patch("requests.get", return_value=mock_response)

    url = "https://api.example.com/data"
    data = get_json_from_url(url)

    # Assert that requests.get was called with the correct URL
    requests.get.assert_called_once_with(url)
    # Assert that the returned data is correct
    assert data == {"key": "value"}
