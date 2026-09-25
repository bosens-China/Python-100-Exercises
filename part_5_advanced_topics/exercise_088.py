"""
题目 088: 使用 Fixture 优化测试

要求:
在 `part_4_oop/test_todos.py` 中创建一个名为 `authenticated_client` 的 `pytest` fixture。
这个 fixture 负责创建一个测试用户、登录并获取token，
然后创建一个使用此 token 的认证 `TestClient` 实例并 `yield` 它。
至少编写一个使用该 fixture 的 `test_...` 测试函数，验证受保护的端点。

提示:
`@pytest.fixture(scope="module")`
`def authenticated_client(): ...`
`def test_some_protected_endpoint(authenticated_client): ...`
"""
