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

# --- 游戏设置 ---
WIDTH = 20
HEIGHT = 10
SNAKE_CHAR = '■'
FOOD_CHAR = '★'
EMPTY_CHAR = ' '
INITIAL_SPEED = 0.5 # 初始速度（秒/帧）

# --- 游戏状态 ---
snake = deque([(WIDTH // 2, HEIGHT // 2)]) # 蛇的身体，用双端队列表示
food = (random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)) # 食物位置
direction = (0, 1) # 初始方向 (dx, dy)，向右
score = 0
speed = INITIAL_SPEED
game_over = False

def clear_screen():
    """清空控制台屏幕。"""
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_board():
    """在控制台绘制游戏面板。"""
    clear_screen()
    print("贪吃蛇游戏 | 得分: {}".format(score))
    print('+' + '-' * WIDTH + '+')
    for y in range(HEIGHT):
        print('|', end='')
        for x in range(WIDTH):
            if (x, y) == food:
                print(FOOD_CHAR, end='')
            elif (x, y) in snake:
                print(SNAKE_CHAR, end='')
            else:
                print(EMPTY_CHAR, end='')
        print('|')
    print('+' + '-' * WIDTH + '+')
    print("控制: w(上) a(左) s(下) d(右) | q(退出)")

def get_input():
    """获取用户输入来改变方向 (简化版，在循环中调用)。"""
    global direction
    # 这是一个简化的输入，实际游戏需要非阻塞输入
    # 这里我们只在每次循环时等待输入
    # 注意：这个输入方式会让游戏暂停直到用户按 Enter
    move = input("输入方向 (w/a/s/d) 然后按 Enter: ").lower()
    if move == 'w' and direction != (0, 1):
        direction = (0, -1)
    elif move == 's' and direction != (0, -1):
        direction = (0, 1)
    elif move == 'a' and direction != (1, 0):
        direction = (-1, 0)
    elif move == 'd' and direction != (-1, 0):
        direction = (1, 0)
    elif move == 'q':
        global game_over
        game_over = True


def update_game_state():
    """更新游戏状态（移动蛇，检查碰撞等）。"""
    global snake, food, score, speed, game_over

    # 计算新蛇头的位置
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])

    # 检查碰撞
    # 1. 撞墙
    if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
        game_over = True
        return
    # 2. 撞自己
    if new_head in snake:
        game_over = True
        return

    # 将新蛇头添加到蛇的身体
    snake.appendleft(new_head)

    # 检查是否吃到食物
    if new_head == food:
        score += 1
        # 速度加快一点点
        speed = max(0.1, speed * 0.9)
        # 生成新食物
        while food in snake:
            food = (random.randint(1, WIDTH - 2), random.randint(1, HEIGHT - 2))
    else:
        # 如果没吃到食物，移除蛇尾
        snake.pop()

def main_loop():
    """游戏主循环。"""
    while not game_over:
        draw_board()
        get_input()
        if not game_over:
            update_game_state()
        # time.sleep(speed) # 简化版输入，不再需要 sleep

    print("\n游戏结束！")
    print("最终得分: {}".format(score))

if __name__ == '__main__':
    # 这是一个简化版的贪吃蛇，每次移动都需要你手动输入方向并按回车
    # 这种方式是为了避免在不同操作系统上处理复杂、有依赖的实时键盘监听
    main_loop() 