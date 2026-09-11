"""
题目 069: 重构“删除待办事项”以使用数据库

要求:
修改 `DELETE /todos/{todo_id}` 端点。
使用数据库会话找到记录，删除它，并提交事务。

提示:
`db.delete(db_todo)`
`db.commit()`
"""
