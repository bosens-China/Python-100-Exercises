"""
### 36. 简单的计算器

- **描述:** 编写一个程序，接收用户输入的两个数字和一个运算符（+,-,*,/），然后执行相应的计算。
- **提示:** 使用 `if-elif-else` 来判断用户选择了哪个运算符。注意处理除数为零的情况。
- **期待:** 用户输入 `10`, `*`, `5`，程序输出 `结果: 50`。
"""

def simple_calculator(num1, operator, num2):
    """
    一个简单的计算器函数
    :param num1: 第一个数字
    :param operator: 运算符 (+, -, *, /)
    :param num2: 第二个数字
    :return: 计算结果。如果除以零，返回一个错误信息字符串。
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    # 交互式部分
    try:
        n1 = float(input("请输入第一个数字: "))
        op = input("请输入运算符 (+, -, *, /): ")
        n2 = float(input("请输入第二个数字: "))
        
        # 这里是独立的交互逻辑
        if op == '+':
            result = n1 + n2
        elif op == '-':
            result = n1 - n2
        elif op == '*':
            result = n1 * n2
        elif op == '/':
            if n2 == 0:
                result = "错误：除数不能为零！"
            else:
                result = n1 / n2
        else:
            result = "无效的运算符"
            
        print(f"结果: {result}")

    except ValueError:
        print("输入无效，请输入数字。")

# 注意:
# 为了方便测试，我们将核心判断逻辑放在 simple_calculator 函数中。
# __main__ 部分则用于实际的交互演示。 