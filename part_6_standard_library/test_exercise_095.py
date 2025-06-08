from unittest.mock import patch, Mock
import requests
from part_6_standard_library.exercise_095 import get_github_api_status_code

# @patch 会用一个 Mock 对象替换掉 'part_6_standard_library.exercise_095.requests.get'
# 这个 Mock 对象会作为参数 'mock_get' 传入测试方法
@patch('part_6_standard_library.exercise_095.requests.get')
def test_successful_request(mock_get):
    """测试一个成功的请求（状态码 200）。"""
    
    # 配置我们的 mock 对象
    # 1. 创建一个模拟的 Response 对象
    mock_response = Mock()
    # 2. 设置这个模拟 Response 的 status_code 属性
    mock_response.status_code = 200
    # 3. 让 raise_for_status() 方法什么也不做（因为是成功请求）
    mock_response.raise_for_status.return_value = None
    # 4. 当 mock_get 被调用时，让它返回我们创建的模拟 Response
    mock_get.return_value = mock_response
    
    # 调用我们的函数
    status_code = get_github_api_status_code()
    
    # 验证结果
    assert status_code == 200
    # 验证 mock_get 是否被用正确的 URL 调用了一次
    mock_get.assert_called_once_with("https://api.github.com", timeout=10)

@patch('part_6_standard_library.exercise_095.requests.get')
def test_failed_request_404(mock_get):
    """测试一个失败的请求（状态码 404）。"""
    
    # 配置 mock
    mock_response = Mock()
    mock_response.status_code = 404
    # 模拟当 status_code 是 404 时，raise_for_status() 会抛出 HTTPError
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError("404 Not Found")
    mock_get.return_value = mock_response
    
    # 调用函数并验证返回值为 None
    assert get_github_api_status_code() is None
    
@patch('part_6_standard_library.exercise_095.requests.get')
def test_request_timeout(mock_get):
    """测试发生请求超时的情况。"""
    # 配置 mock，让它在被调用时直接抛出 Timeout 异常
    mock_get.side_effect = requests.exceptions.Timeout("Connection timed out")
    
    # 调用函数并验证返回值为 None
    assert get_github_api_status_code() is None 