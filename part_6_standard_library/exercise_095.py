"""
### 95. `urllib` 模块 (或 `requests` 库)

- **描述:** 使用 `requests` 库（如果未安装，请先 `pip install requests`）向 "https://api.github.com" 发送一个 GET 请求，并打印响应的状态码。
- **提示:** `import requests; response = requests.get(url); print(response.status_code)`。
- **期待:** 输出 `200`（表示请求成功）。
"""
import requests
from typing import Optional

def get_github_api_status_code() -> Optional[int]:
    """
    向 GitHub API 发送一个 GET 请求并返回其状态码。
    :return: HTTP 状态码（整数），如果请求失败则返回 None。
    """
    url = "https://api.github.com"
    try:
        # 在这里写下你的代码
        response = requests.get(url, timeout=10) # 设置10秒超时
        # raise_for_status() 会在发生 4xx 或 5xx 错误时抛出异常
        response.raise_for_status() 
        return response.status_code
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
        return None

if __name__ == '__main__':
    print("正在向 https://api.github.com 发送请求...")
    status_code = get_github_api_status_code()
    
    if status_code is not None:
        print(f"请求成功，状态码: {status_code}")
    else:
        print("请求未能成功完成。") 