"""
题目 056: 创建“更新待办事项”的端点

要求:
修改 `part_4_oop/main.py` 文件。
创建一个 `PUT /todos/{todo_id}` 的端点，用于更新一个已存在的待办事项。
- 它应该接受一个包含待更新字段的JSON对象。
- 如果找到 `todo_id` 对应的待办事项，则更新其内容并返回更新后的对象。
- 如果未找到，返回 404 错误。

提示:
你需要一个用于请求体的Pydantic模型，其中字段是可选的。
例如: `class TodoUpdate(BaseModel): title: str | None = None`
"""
