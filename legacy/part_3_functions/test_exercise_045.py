import pytest
import requests
from part_3_functions.exercise_045 import create_post

def test_create_post(mocker):
    mock_response = mocker.Mock()
    mock_response.json.return_value = {"id": 101, "title": "New Post", "body": "This is a post."}
    mocker.patch("requests.post", return_value=mock_response)

    post_data = {"title": "New Post", "body": "This is a post."}
    response_data = create_post(post_data["title"], post_data["body"])

    requests.post.assert_called_once_with(
        "https://api.example.com/posts", 
        json=post_data
    )
    assert response_data["id"] == 101
