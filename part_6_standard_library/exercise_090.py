"""
### 90. `sys` 模块

- **描述:** 编写一个脚本，可以从命令行接收参数。打印出脚本名和所有传入的参数。
- **提示:** 使用 `sys.argv`。`sys.argv` 是一个列表，第一个元素是脚本名。
- **期待:** 在命令行运行 `python your_script.py arg1 arg2`，会输出脚本名和 `['arg1', 'arg2']`。
"""
import sys

def process_command_line_args():
    """
    处理并返回命令行参数。
    """
    # sys.argv 是一个包含命令行参数的列表
    # sys.argv[0] 是脚本的名称
    script_name = sys.argv[0]
    
    # sys.argv[1:] 包含了脚本名之后的所有参数
    args = sys.argv[1:]
    
    return script_name, args

# 注意：这个练习的目的是让你学会如何在命令行中运行 Python 脚本并传递参数。
# `sys.argv` 的内容是由你运行脚本的方式决定的，因此不适合编写传统的单元测试。
#
# 要测试这个脚本，请在你的终端（命令行）中执行以下命令：
#
# 1. python part_6_standard_library/exercise_090.py
#    (no arguments)
#
# 2. python part_6_standard_library/exercise_090.py hello world
#    (two arguments)
#
# 3. python part_6_standard_library/exercise_090.py "an argument with spaces" 123
#    (arguments with spaces)
#

if __name__ == '__main__':
    script, arguments = process_command_line_args()
    
    print(f"脚本名称: {script}")
    print(f"传入的参数: {arguments}")
    
    if arguments:
        print(f"第一个参数是: {arguments[0]}")
    else:
        print("没有传入任何参数。") 