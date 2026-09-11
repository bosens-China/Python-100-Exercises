"""
题目 066: 重构“获取所有待办事项”以使用数据库

要求:
修改 `GET /todos` 端点。
使用 `db: Session = Depends(get_db)` 来获取数据库会话，
并查询数据库以返回所有的待办事项。

提示:
`return db.query(models.Todo).all()`
"""
