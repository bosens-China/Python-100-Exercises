"""
题目 070: 分离Pydantic Schemas

要求:
1. 创建新文件 `part_4_oop/schemas.py`。
2. 将所有 Pydantic 模型（用于API请求和响应的类）从 `main.py` 移动到 `schemas.py`。
3. 更新 `main.py`，从 `schemas.py` 导入这些模型。

提示:
通常会有一个用于读取的 `Todo` schema，一个用于创建的 `TodoCreate` schema。
这有助于将API的数据形态与数据库的表结构解耦。
"""
