"""
题目 064: 创建数据库会话依赖项

要求:
修改 `main.py`。
创建一个名为 `get_db` 的依赖项函数。
这个函数应该:
1. 从 `database.SessionLocal` 创建一个数据库会话。
2. 使用 `yield` 将会话提供给路径操作函数。
3. 在 `finally` 块中确保会话被关闭。

提示:
`def get_db():`
`    db = SessionLocal()`
`    try:`
`        yield db`
`    finally:`
`        db.close()`
"""
