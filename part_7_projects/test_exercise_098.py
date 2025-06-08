import pytest
from unittest.mock import patch, Mock
import requests
from bs4 import BeautifulSoup
from part_7_projects.exercise_098 import fetch_and_parse, extract_title_and_paragraphs

# 准备一个固定的 HTML 字符串用于测试
FAKE_HTML = """
<html>
<head><title>测试标题</title></head>
<body>
    <h1>一个标题</h1>
    <p>这是第一个段落。</p>
    <p>这是第二个段落，包含一个<b>加粗</b>标签。</p>
    <div><p>嵌套的段落。</p></div>
</body>
</html>
"""

@patch('requests.get')
def test_fetch_and_parse_success(mock_get):
    """测试 fetch_and_parse 在成功请求时能否正确返回 soup 对象。"""
    # 配置 mock response
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.text = FAKE_HTML
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response
    
    soup = fetch_and_parse("http://fakeurl.com")
    
    assert soup is not None
    assert soup.title.string == "测试标题"
    assert len(soup.find_all('p')) == 3

@patch('requests.get')
def test_fetch_and_parse_failure(mock_get):
    """测试 fetch_and_parse 在请求失败时返回 None。"""
    mock_get.side_effect = requests.exceptions.RequestException("Test Error")
    
    soup = fetch_and_parse("http://fakeurl.com")
    
    assert soup is None

def test_extract_title_and_paragraphs():
    """测试 extract_title_and_paragraphs 能否从 soup 对象中正确提取数据。"""
    soup = BeautifulSoup(FAKE_HTML, 'html.parser')
    
    title, paragraphs = extract_title_and_paragraphs(soup)
    
    assert title == "测试标题"
    assert len(paragraphs) == 3
    assert paragraphs[0] == "这是第一个段落。"
    assert paragraphs[1] == "这是第二个段落，包含一个加粗标签。"
    assert paragraphs[2] == "嵌套的段落。"

def test_extract_with_no_title():
    """测试当 HTML 没有 title 时的提取情况。"""
    html_no_title = "<html><body><p>段落。</p></body></html>"
    soup = BeautifulSoup(html_no_title, 'html.parser')
    
    title, _ = extract_title_and_paragraphs(soup)
    assert title == "无标题"

def test_extract_with_no_paragraphs():
    """测试当 HTML 没有 p 标签时的提取情况。"""
    html_no_p = "<html><head><title>标题</title></head><body></body></html>"
    soup = BeautifulSoup(html_no_p, 'html.parser')
    
    _, paragraphs = extract_title_and_paragraphs(soup)
    assert paragraphs == []
