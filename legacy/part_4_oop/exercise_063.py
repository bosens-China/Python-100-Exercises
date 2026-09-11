"""
题目 063: 在应用启动时创建数据表

要求:
修改 `main.py`。
导入 `models`, `engine`。
调用 `models.Base.metadata.create_all(bind=engine)` 来在程序启动时创建数据库表。

提示:
这行代码应该在 `main.py` 的全局作用域内，但在定义路由之前执行。
"""
