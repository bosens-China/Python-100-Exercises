"""
题目 076: 用户注册端点

要求:
1. 创建新文件 `part_4_oop/routers/users.py` 并设置一个 `APIRouter`。
2. 在新 router 中创建一个 `POST /users` 端点。
3. 端点应接收 `schemas.UserCreate` 数据，使用 `hashing.get_password_hash` 哈希密码，
   并通过 repository 将新用户存入数据库。
4. 在 `main.py` 中包含这个新的 users router。
"""
