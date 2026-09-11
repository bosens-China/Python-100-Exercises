"""
题目 071: 使用APIRouter组织端点

要求:
1. 创建新文件 `part_4_oop/routers/todos.py`。
2. 将所有与todo相关的API端点从 `main.py` 移动到 `todos.py` 中。
3. 在 `todos.py` 中，使用 `fastapi.APIRouter` 来创建路由。
4. 在 `main.py` 中，导入并包含这个新的router。

提示:
`from fastapi import APIRouter`
`router = APIRouter()`
`@router.get(...)`
In main.py: `app.include_router(todos.router, prefix="/todos", tags=["todos"])`
"""
