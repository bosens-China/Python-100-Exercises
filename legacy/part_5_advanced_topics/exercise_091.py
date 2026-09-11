"""
题目 091: API速率限制

要求:
1. 安装 `slowapi`: `uv pip install slowapi`
2. 在你的 `main.py` 中，集成 `slowapi`。
3. 为 `/login/token` 端点设置一个限制，例如“每分钟5次”。

提示:
需要一个 `Limiter` 实例，并将其作为应用的中间件或依赖项。
`limiter = Limiter(key_func=get_remote_address)`
`app.state.limiter = limiter`
`@app.post("/login/token")`
`@limiter.limit("5/minute")`
"""
