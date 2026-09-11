"""
题目 098: Python的异步编程

要求:
1. 安装一个异步数据库驱动，例如 `aiosqlite`: `uv pip install aiosqlite`
2. 将你的数据库连接和会话设置为异步。
3. 将你的某个仓库方法（例如 `get_all`）重构为 `async def`。
4. 相应地更新你的API端点为 `async def`。

提示:
这是一个非常高级的话题。`create_async_engine` from `sqlalchemy.ext.asyncio`。
`result = await db.execute(select(models.Todo))`
`return result.scalars().all()`
"""
