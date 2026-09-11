"""
题目 089: 仓库逻辑的单元测试

要求:
为你的 `TodoRepository` 中的一个方法（例如 `get_by_id`）编写一个单元测试。
使用 `unittest.mock.MagicMock` 来模拟 `db.session` 对象，
确保测试在不接触真实数据库的情况下验证方法的逻辑。

提示:
`from unittest.mock import MagicMock`
`mock_db = MagicMock()`
`mock_db.query(...).filter(...).first.return_value = ...`
"""
