"""
题目 095: 编写命令行脚本

要求:
1. 安装 `typer`: `uv pip install typer`
2. 创建一个 `cli.py` 文件。
3. 使用 `typer` 创建一个可以从命令行添加新用户的函数。

提示:
`import typer`
`app = typer.Typer()`
`@app.command()`
`def create_user(email: str, password: str): ...`
`if __name__ == "__main__": app()`
"""
