"""
### 99. 命令行版的贪吃蛇游戏

- **描述:** 在命令行界面中实现一个简单的贪吃蛇游戏。蛇可以移动，吃食物后变长，撞到墙或自己则游戏结束。
- **提示:** 这是一个综合性挑战。你需要用列表表示蛇的身体，用循环控制游戏进程，用 `os.system('cls')` 或 `os.system('clear')` 来清屏实现动画效果。
- **期待:** 一个可以在命令行窗口中玩的，虽然简陋但功能完整的贪吃蛇游戏。
"""

import os
import random
import time
from collections import deque
import sys

class SnakeGame:
    """封装贪吃蛇游戏的所有逻辑和状态。"""
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 这是一个简化版的贪吃蛇，每次移动都需要你手动输入方向并按回车
    # 这种方式是为了避免在不同操作系统上处理复杂、有依赖的实时键盘监听
    game = SnakeGame()
    game.run() 