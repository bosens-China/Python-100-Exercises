"""
题目 045: 发送POST请求

要求:
编写一个名为 `create_post` 的函数，它接受 `title` 和 `body` 两个字符串参数。
函数需要向 `https://api.example.com/posts` 发送一个POST请求，
请求体为一个包含 `title` 和 `body` 的JSON对象。
函数应返回服务器响应的JSON内容。

提示:
使用 `requests.post()` 方法。你可以通过 `json` 参数传递一个字典作为请求体，
例如 `requests.post(url, json={'title': title, 'body': body})`。
"""
import requests

def create_post(title, body):
    # 在这里写下你的代码
    pass
