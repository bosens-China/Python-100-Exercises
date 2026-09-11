"""
题目 074: 创建用户与待办事项的关联

要求:
1. 修改 `models.py` 中的 `Todo` 模型。
2. 添加一个 `owner_id` 列，它是指向 `users.id` 的外键。
3. 使用 `sqlalchemy.orm.relationship` 创建一个 `owner` 属性，将 `Todo` 链接到其 `User`。
4. 在 `User` 模型中，也添加一个 `todos` 关系，反向链接到该用户的所有 `Todo` 项。

提示:
`owner_id = Column(Integer, ForeignKey("users.id"))`
`owner = relationship("User", back_populates="todos")`
In User model: `todos = relationship("Todo", back_populates="owner")`
"""
