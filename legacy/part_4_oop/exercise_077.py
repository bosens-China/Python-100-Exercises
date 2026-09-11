"""
题目 077: 处理重复用户

要求:
修改 `POST /users` 端点。
在创建用户之前，检查该邮箱是否已在数据库中存在。
如果存在，则 `raise HTTPException(status_code=400, detail="Email already registered")`。

提示:
在你的 user repository 中创建一个 `get_user_by_email` 方法来简化这个检查。
"""
