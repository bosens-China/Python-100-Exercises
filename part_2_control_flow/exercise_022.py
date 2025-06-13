"""
### 22. 猜数字游戏

- **描述:** 程序随机生成一个 1 到 100 之间的整数，让用户来猜。如果猜的数字太大或太小，给出提示，直到猜中为止。
- **提示:** 使用 `random.randint(1, 100)` 生成随机数。使用 `while` 循环，直到用户猜对。
- **期待:** 游戏会持续提示 "太大了！" 或 "太小了！"，直到用户猜中，然后输出 "恭喜你，猜对了！"。
"""
import random

def check_guess(secret_number, guess):
    """
    检查用户的猜测并返回结果。
    这是一个"纯函数"，易于测试。
    
    :param secret_number: 秘密数字
    :param guess: 用户的猜测
    :return: "太大了！", "太小了！", or "恭喜你，猜对了！"
    """
    # 在这里写下你的代码
    pass

def guess_the_number_game():
    """
    猜数字游戏的主逻辑。
    """
    secret_number = random.randint(1, 100)
    print("我已经想好了一个 1 到 100 之间的数字，你来猜猜看吧！")

    while True:
        try:
            user_guess = int(input("请输入你的猜测: "))
            result = check_guess(secret_number, user_guess)
            print(result)
            if result == "恭喜你，猜对了！":
                break
        except ValueError:
            print("请输入一个有效的整数！")

if __name__ == '__main__':
    guess_the_number_game()
