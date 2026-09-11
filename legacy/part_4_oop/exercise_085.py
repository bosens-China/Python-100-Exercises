"""
题目 085: 授权：仅修改/删除自己的待办事项

要求:
修改 `PUT /todos/{todo_id}` 和 `DELETE /todos/{todo_id}` 端点。
在执行更新或删除之前，必须验证该待办事项是否属于当前认证用户。
如果不属于，`raise HTTPException(status_code=403, detail="Not authorized")`。

提示:
获取待办事项后，`if todo.owner_id != current_user.id:` ...
"""
