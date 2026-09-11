"""
题目 052: 内存数据库与Pydantic模型

要求:
修改 `part_4_oop/main.py` 文件。
1. 导入 `pydantic` 的 `BaseModel`。
2. 定义一个名为 `Todo` 的Pydantic模型，包含以下字段:
   - `id`: int
   - `title`: str
   - `completed`: bool
3. 创建一个名为 `db` 的列表，作为内存数据库，并预先添加一两个 `Todo` 实例。

提示:
这个练习没有API端点，我们只是在为后续步骤准备数据结构。
"""
