"""
题目 060: 按完成状态筛选待办事项

要求:
修改 `GET /todos` 端点。
使其接受一个可选的布尔查询参数 `completed`。
- 如果 `completed=true`，只返回已完成的待办事项。
- 如果 `completed=false`，只返回未完成的待办事项。
- 如果不提供该参数，返回所有待办事项。

提示:
端点函数签名可以这样写: `def get_all_todos(completed: bool | None = None):`
"""
