"""
题目 044: 使用查询参数

要求:
编写一个名为 `search_posts_by_user` 的函数，它接受一个 `user_id`。
函数需要向 `https://api.example.com/posts` 发送GET请求，
并附带一个查询参数 `userId`，其值为传入的 `user_id`。
函数应返回响应的JSON内容（一个帖子列表）。

提示:
`requests.get()` 函数有一个 `params` 参数，你可以传递一个字典给它，
例如 `params={'userId': user_id}`。
"""
import requests

def search_posts_by_user(user_id):
    # 在这里写下你的代码
    pass
