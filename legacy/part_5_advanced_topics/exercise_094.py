"""
题目 094: WebSocket 入门

要求:
在 `main.py` 中，添加一个WebSocket端点 `/@app.websocket("/ws")`。
它应该能接受连接，并可以接收和发送文本消息。

提示:
`async def websocket_endpoint(websocket: WebSocket):`
`    await websocket.accept()`
`    while True:`
`        data = await websocket.receive_text()`
`        await websocket.send_text(f"Message text was: {data}")`
"""
