"""
题目 088: 使用 Fixture 优化测试

要求:
在你的测试文件中 (例如 `test_todos.py`)，创建一个 `pytest` fixture。
这个 fixture 负责创建一个测试用户、登录并获取token，
然后创建一个使用此token的认证 `TestClient` 实例并 `yield` 它。

提示:
`@pytest.fixture(scope="module")`
`def authenticated_client(): ...`
`def test_some_protected_endpoint(authenticated_client): ...`
"""
