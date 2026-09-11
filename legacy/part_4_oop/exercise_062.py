"""
题目 062: 定义数据库表模型

要求:
1. 创建新文件 `part_4_oop/models.py`。
2. 在 `models.py` 中，定义一个名为 `Todo` 的类，它继承自 `database.Base`。
3. 这个类将映射到数据库中的 `todos` 表。
4. 为该类添加列: `id` (Integer, primary_key), `title` (String), `completed` (Boolean)。

提示:
`from sqlalchemy import Column, Integer, String, Boolean`
`from .database import Base`
`class Todo(Base):`
`    __tablename__ = "todos"`
"""
