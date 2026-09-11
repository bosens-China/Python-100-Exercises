"""
题目 053: 创建“获取所有待办事项”的端点

要求:
修改 `part_4_oop/main.py` 文件。
创建一个 `GET /todos` 的API端点，它应该返回 `db` 列表中的所有待办事项。

提示:
使用 `@app.get("/todos")` 装饰器。函数体只需 `return db`。
FastAPI会自动处理 `Todo` 对象的JSON序列化。
"""
