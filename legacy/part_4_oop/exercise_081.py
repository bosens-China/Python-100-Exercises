"""
题目 081: 创建“获取当前用户”的依赖项

要求:
1. 在 `auth.py` 中，创建一个 `OAuth2PasswordBearer` 实例。
2. 创建一个依赖项 `get_current_user`，它依赖于上一步的 bearer 实例。
3. 这个函数需要解码JWT，从token中提取用户ID或邮箱，然后从数据库中获取并返回用户对象。
4. 如果token无效或用户不存在，应抛出 `HTTPException(status_code=401)`。

提示:
这是一个复杂但可重用的标准认证模式。
`oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")`
`def get_current_user(token: str = Depends(oauth2_scheme), ...):`
"""
