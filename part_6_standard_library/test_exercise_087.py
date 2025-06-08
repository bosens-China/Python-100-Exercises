import datetime
import pytest
from part_6_standard_library.exercise_087 import get_formatted_current_time

def test_format_of_current_time():
    """
    测试返回的时间字符串是否符合 "YYYY-MM-DD HH:MM:SS" 格式。
    我们通过尝试用指定的格式解析字符串来验证它。
    如果解析成功，说明格式正确；如果失败，则会抛出 ValueError。
    """
    formatted_time_str = get_formatted_current_time()
    
    try:
        # 尝试使用相同的格式代码来解析函数返回的字符串
        datetime.datetime.strptime(formatted_time_str, "%Y-%m-%d %H:%M:%S")
    except ValueError:
        # 如果解析失败，说明格式不正确，测试失败
        pytest.fail(f"返回的字符串 '{formatted_time_str}' 不符合 '%Y-%m-%d %H:%M:%S' 格式")

if __name__ == '__main__':
    pytest.main() 