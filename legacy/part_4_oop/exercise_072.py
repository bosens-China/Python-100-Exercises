"""
题目 072: 高级依赖项：获取仓库

要求:
1. 修改 `TodoRepository` 类，使其在 `__init__` 时接收一个数据库会话 `db: Session`。
2. 创建一个新的依赖项 `get_repository(db: Session = Depends(get_db))`，它返回一个 `TodoRepository` 的实例。
3. 修改所有端点，使其依赖于 `get_repository` 而不是直接依赖 `get_db`。

提示:
This pattern is called Dependency Injection and is a cornerstone of good application design.
`def get_repository(db: Session = Depends(get_db)):`
`    return TodoRepository(db=db)`
`@router.get("/", response_model=list[schemas.Todo])`
`def read_todos(repo: TodoRepository = Depends(get_repository)):`
`    return repo.get_all()`
"""
