import pytest
import requests
from part_3_functions.exercise_044 import search_posts_by_user

def test_search_posts_by_user(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = [{"userId": 1, "title": "Test Post"}]
    mocker.patch("requests.get", return_value=mock_response)

    posts = search_posts_by_user(1)

    requests.get.assert_called_once_with(
        "https://api.example.com/posts", 
        params={"userId": 1}
    )
    assert posts == [{"userId": 1, "title": "Test Post"}]
