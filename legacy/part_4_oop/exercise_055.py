"""
题目 055: 创建“获取单个待办事项”的端点

要求:
修改 `part_4_oop/main.py` 文件。
创建一个 `GET /todos/{todo_id}` 的端点，它能根据 `id` 检索单个待办事项。
- 如果找到，返回该 `Todo` 对象。
- 如果未找到，返回 404 Not Found 错误。

提示:
使用路径参数 `todo_id: int`。
遍历 `db` 列表查找匹配项。
如果未找到，`raise HTTPException(status_code=404, detail="Todo not found")`。
"""
