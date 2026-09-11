"""
题目 079: 创建JWT令牌函数

要求:
1. 创建新文件 `part_4_oop/auth.py`。
2. 在 `auth.py` 中定义 `SECRET_KEY`, `ALGORITHM`, 和 `ACCESS_TOKEN_EXPIRE_MINUTES`。
3. 创建一个函数 `create_access_token(data: dict)`，它接收一个字典，
   添加一个 `exp` (过期时间) claim，然后使用 `jose.jwt.encode` 生成JWT字符串。

提示:
`from datetime import timedelta`
`expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)`
`to_encode.update({"exp": expire})`
"""
