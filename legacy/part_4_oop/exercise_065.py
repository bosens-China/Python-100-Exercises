"""
题目 065: 重构“创建待办事项”以使用数据库

要求:
修改 `POST /todos` 端点。
1. 添加 `db: Session = Depends(get_db)` 到函数签名。
2. 移除对旧的内存 `db` 列表的操作。
3. 使用 SQLAlchemy session (`db`) 来创建新的 `Todo` 记录并存入数据库。

提示:
`db_todo = models.Todo(...)`
`db.add(db_todo)`
`db.commit()`
`db.refresh(db_todo)`
"""
