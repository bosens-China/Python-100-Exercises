"""
### 87. `datetime` 模块

- **描述:** 使用 `datetime` 模块获取当前的日期和时间，并将其格式化为 "YYYY-MM-DD HH:MM:SS" 的形式。
- **提示:** 使用 `datetime.datetime.now()` 获取当前时间，然后使用 `strftime()` 方法进行格式化。
- **期待:** 输出类似 `2025-06-07 15:33:00` 的字符串。
"""
import datetime

def get_formatted_current_time() -> str:
    """
    获取当前的日期和时间，并将其格式化。
    :return: 格式为 "YYYY-MM-DD HH:MM:SS" 的字符串。
    """
    # 在这里写下你的代码
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    formatted_time = get_formatted_current_time()
    print(f"当前格式化后的时间是: {formatted_time}") 