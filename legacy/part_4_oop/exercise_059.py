"""
题目 059: 添加基本输入验证

要求:
修改 `part_4_oop/main.py` 中的Pydantic模型。
在用于创建待办事项的模型中，确保 `title` 字段不能为空字符串。

提示:
从 `pydantic` 导入 `Field`。
在模型中定义 `title: str = Field(..., min_length=1)`。
FastAPI会自动利用这个验证规则。
"""
