"""
题目 080: 用户登录端点

要求:
1. 在 `users.py` (或一个新的 `auth.py` router) 中创建一个 `POST /login/token` 端点。
2. 端点应接收 `OAuth2PasswordRequestForm` 形式的表单数据。
3. 验证用户名（邮箱）和密码是否正确。
4. 如果凭证有效，使用 `create_access_token` 生成一个JWT并返回。

提示:
`from fastapi.security import OAuth2PasswordRequestForm`
`def login(form_data: OAuth2PasswordRequestForm = Depends()):`
`user = user_repo.get_user_by_email(form_data.username)`
`verify_password(form_data.password, user.hashed_password)`
"""
