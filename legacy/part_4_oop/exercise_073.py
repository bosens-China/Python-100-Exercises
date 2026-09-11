"""
题目 073: 添加“用户”模型

要求:
1. 在 `models.py` 中，创建一个 `User` 模型，继承自 `Base`。
2. 字段应包括 `id` (Integer, PK), `email` (String, unique, index), `hashed_password` (String)。
3. 在 `schemas.py` 中，创建对应的 `User` 和 `UserCreate` Pydantic schemas。

提示:
`email = Column(String, unique=True, index=True)`
`UserCreate` schema should contain `email` and `password` (not hashed yet).
"""
