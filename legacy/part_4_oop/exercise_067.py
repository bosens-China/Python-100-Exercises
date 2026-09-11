"""
题目 067: 重构“获取单个待办事项”以使用数据库

要求:
修改 `GET /todos/{todo_id}` 端点。
使用数据库会话查询具有指定 `id` 的待办事项。

提示:
`db.query(models.Todo).filter(models.Todo.id == todo_id).first()`
"""
