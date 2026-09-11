"""
题目 082: 保护端点

要求:
修改 `POST /todos` 端点，为其添加 `Depends(get_current_user)` 依赖。
这将确保只有提供了有效JWT的认证用户才能访问该端点。

提示:
`from .. import auth`
`def create_todo(..., current_user: schemas.User = Depends(auth.get_current_user)):`
"""
