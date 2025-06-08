from unittest.mock import patch, Mock
import requests
from part_7_projects import exercise_097

# 使用 @patch 来临时修改 exercise_097 模块中的 API_KEY
@patch('part_7_projects.exercise_097.API_KEY', 'fake_api_key')
@patch('part_7_projects.exercise_097.requests.get')
def test_get_weather_success(mock_get):
    """测试成功获取天气数据。"""
    # 准备一个模拟的成功 JSON 响应
    mock_response_json = {
        "name": "London",
        "weather": [{"description": "light rain"}],
        "main": {"temp": 15.5}
    }
    
    # 配置 mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = mock_response_json
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    # 调用函数
    weather_data = exercise_097.get_weather("London")
    
    # 验证返回的数据
    assert weather_data == mock_response_json

    # 验证 requests.get 是否以正确的参数被调用
    expected_params = {
        'q': "London",
        'appid': 'fake_api_key',
        'units': 'metric',
        'lang': 'zh_cn'
    }
    mock_get.assert_called_once_with(
        exercise_097.BASE_URL,
        params=expected_params,
        timeout=10
    )

@patch('part_7_projects.exercise_097.API_KEY', 'fake_api_key')
@patch('part_7_projects.exercise_097.requests.get')
def test_get_weather_city_not_found(mock_get):
    """测试 API 返回 404 (城市未找到) 的情况。"""
    mock_response = Mock()
    mock_response.status_code = 404
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Not Found")
    mock_get.return_value = mock_response

    weather_data = exercise_097.get_weather("NonExistentCity")
    assert weather_data is None

@patch('part_7_projects.exercise_097.API_KEY', 'invalid_key')
@patch('part_7_projects.exercise_097.requests.get')
def test_get_weather_invalid_api_key(mock_get):
    """测试 API 返回 401 (无效 API Key) 的情况。"""
    mock_response = Mock()
    mock_response.status_code = 401
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("Unauthorized")
    mock_get.return_value = mock_response

    weather_data = exercise_097.get_weather("Beijing")
    assert weather_data is None 