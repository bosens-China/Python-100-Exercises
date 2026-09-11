"""
题目 092: CORS 跨域资源共享

要求:
在 `main.py` 中，添加 `CORSMiddleware`。
配置它以允许来自特定源（例如 `http://localhost:3000`）的请求，
允许所有方法和所有头部信息。

提示:
`from fastapi.middleware.cors import CORSMiddleware`
`app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:3000"], ...)`
"""
