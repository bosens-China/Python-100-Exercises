"""
题目 061: 安装SQLAlchemy并设置数据库

要求:
1. 安装 SQLAlchemy: `uv pip install sqlalchemy`
2. 创建新文件 `part_4_oop/database.py`。
3. 在 `database.py` 中，配置 SQLAlchemy engine 连接到名为 `todos.db` 的SQLite数据库。
4. 同时，在 `database.py` 中创建 `SessionLocal` (一个 session 工厂) 和 `Base` (一个声明式基类)。

提示:
`from sqlalchemy import create_engine`
`from sqlalchemy.ext.declarative import declarative_base`
`from sqlalchemy.orm import sessionmaker`
`SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"`
`engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})`
"""
