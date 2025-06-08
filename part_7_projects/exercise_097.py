"""
### 97. 天气查询应用

- **描述:** 使用 `requests` 库调用一个免费的天气 API（如 OpenWeatherMap），获取并显示用户指定城市的天气信息。
- **提示:** 你需要去天气 API 网站注册并获取一个 API Key。程序会接收用户输入的城市名，构造 API 请求 URL，解析返回的 JSON 数据。
- **期待:** 输入城市名后，程序能打印出类似 "北京: 晴, 25°C" 的信息。
"""
import requests
import sys
from typing import Dict, Optional

# --- 配置 ---
# TODO: 在这里替换成你自己的 OpenWeatherMap API Key
# 你可以从 https://openweathermap.org/api 免费注册获取
API_KEY = "YOUR_API_KEY_HERE" 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name: str) -> dict | None:
    """
    获取指定城市的天气信息。
    :param city_name: 城市名称 (例如, "London", "Tokyo")
    :return: 包含天气数据的字典，或者在出错时返回 None
    """
    # 在这里写下你的代码
    raise NotImplementedError

def display_weather(weather_data: Dict):
    """
    格式化并打印天气信息。
    """
    if not weather_data:
        return
        
    city = weather_data.get('name')
    # get('weather') 返回一个列表，我们取第一个元素
    weather_desc = weather_data['weather'][0].get('description')
    # get('main') 返回一个字典
    temp = weather_data['main'].get('temp')
    
    print(f"\n--- {city} 的天气 ---")
    print(f"天气: {weather_desc}")
    print(f"温度: {temp}°C")
    print("-" * (len(city) + 12))

def main():
    """主函数入口"""
    if len(sys.argv) > 1:
        city_name = " ".join(sys.argv[1:])
        print(f"正在查询 '{city_name}' 的天气...")
        weather = get_weather(city_name)
        display_weather(weather)
    else:
        print("用法: python exercise_097.py <城市名称>")
        print("例如: python exercise_097.py 北京")

if __name__ == "__main__":
    main() 