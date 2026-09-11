"""
题目 090: FastAPI 后台任务

要求:
创建一个端点，例如 `POST /send-welcome-email`。
此端点应接受一个 `BackgroundTasks` 依赖项，并添加一个任务来模拟发送邮件。
这个任务可以只是一个打印消息或 `time.sleep` 的函数。
端点应立即返回响应，而任务在后台运行。

提示:
`from fastapi import BackgroundTasks`
`def my_task(message: str): ...`
`def endpoint(background_tasks: BackgroundTasks):`
`    background_tasks.add_task(my_task, "Hello")`
"""
