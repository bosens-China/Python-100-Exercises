"""
题目 075: 基本的密码哈希

要求:
1. 安装 passlib: `uv pip install "passlib[bcrypt]"`
2. 创建新文件 `part_4_oop/hashing.py`。
3. 在 `hashing.py` 中，创建一个 `CryptContext` 实例，并创建两个函数:
   - `get_password_hash(password: str) -> str`
   - `verify_password(plain_password: str, hashed_password: str) -> bool`

提示:
`from passlib.context import CryptContext`
`pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")`
"""
