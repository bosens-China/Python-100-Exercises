"""
### 95. `urllib` 模块 (或 `requests` 库)

- **描述:** 使用 `requests` 库（如果未安装，请先 `pip install requests`）向 "https://api.github.com" 发送一个 GET 请求，并打印响应的状态码。
- **提示:** `import requests; response = requests.get(url); print(response.status_code)`。
- **期待:** 输出 `200`（表示请求成功）。
"""
import requests
from typing import Optional

def get_github_api_status_code() -> int | None:
    """
    使用 requests 库向 GitHub API (https://api.github.com) 发起 GET 请求。
    如果请求成功（没有抛出异常），则返回响应的状态码。
    如果发生任何 requests.exceptions.RequestException（例如超时、连接错误等），
    则捕获异常并返回 None。
    """
    # 在这里写下你的代码
    raise NotImplementedError

if __name__ == '__main__':
    print("正在向 https://api.github.com 发送请求...")
    status_code = get_github_api_status_code()
    
    if status_code is not None:
        print(f"请求成功，状态码: {status_code}")
    else:
        print("请求未能成功完成。") 