"""
### 47. 作用域 (局部变量和全局变量)

- **描述:** 定义一个全局变量 `x = 10`。编写一个函数，尝试在函数内部修改 `x` 的值。先不使用 `global` 关键字，再使用 `global` 关键字，观察区别。
- **提示:** 直接在函数内赋值会创建一个新的局部变量。使用 `global x` 来声明你要修改的是全局变量 `x`。
- **期待:**
  - 不使用 `global`，函数执行后全局 `x` 仍然是 `10`。
  - 使用 `global`，函数执行后全局 `x` 的值被改变。
"""

# 定义全局变量
x = 10

def attempt_to_modify_x_without_global():
    """
    这个函数尝试修改全局变量 x，但没有使用 global 关键字。
    实际上，它创建了一个新的同名局部变量。
    """
    x = 20
    print(f"在函数内部 (无 global)，x 的值是: {x}")

def modify_x_with_global():
    """
    这个函数使用 global 关键字来修改全局变量 x。
    """
    global x
    x = 30
    print(f"在函数内部 (有 global)，x 的值是: {x}")

# 注意：这个练习的目的是通过直接运行和观察输出来理解作用域。
# 编写自动化单元测试来验证全局变量的状态虽然可能，但会使测试变得复杂且不直观，
# 与本练习的教学目的相悖。因此，我们不为此练习提供 test 文件。

if __name__ == '__main__':
    print("--- 场景1: 不使用 global 关键字 ---")
    print(f"调用函数前，全局 x 的值是: {x}")
    attempt_to_modify_x_without_global()
    print(f"调用函数后，全局 x 的值是: {x}")

    print("\n" + "="*40 + "\n")

    # 为了演示场景2，我们重置x的值
    x = 10 

    print("--- 场景2: 使用 global 关键字 ---")
    print(f"调用函数前，全局 x 的值是: {x}")
    modify_x_with_global()
    print(f"调用函数后，全局 x 的值是: {x}") 