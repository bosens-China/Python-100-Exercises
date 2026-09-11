"""
题目 087: 配置文件管理

要求:
1. 创建一个 `part_4_oop/config.py` 文件。
2. 使用 `pydantic_settings.BaseSettings` 创建一个 `Settings` 类。
3. 将 `DATABASE_URL`, `SECRET_KEY` 等配置项移入此类，并让它们可以从环境变量加载。
4. 在应用中，导入并使用这个 `Settings` 对象，而不是硬编码的值。

提示:
`uv pip install pydantic-settings`
`from pydantic_settings import BaseSettings`
`class Settings(BaseSettings): ...`
`settings = Settings()`
"""
