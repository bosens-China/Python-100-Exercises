import pytest
import requests
from part_3_functions.exercise_042 import safe_get_request

def test_safe_get_request_success(mocker):
    mock_response = mocker.Mock()
    mocker.patch("requests.get", return_value=mock_response)
    
    response = safe_get_request("https://good.url/data")
    assert response is not None

def test_safe_get_request_failure(mocker):
    mocker.patch("requests.get", side_effect=requests.exceptions.RequestException)
    
    response = safe_get_request("https://bad.url/data")
    assert response is None
