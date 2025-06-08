"""
### 49. Lambda 表达式

- **描述:** 使用 `lambda` 表达式创建一个简单的匿名函数，它接受一个数字并返回它的平方。
- **提示:** `lambda` 表达式的语法是 `lambda arguments: expression`。
- **期待:** `square = lambda x: x * x`，然后 `square(5)` 返回 `25`。
"""

# 使用 lambda 表达式定义一个计算平方的匿名函数
square = lambda x: x * x

# 注意：本练习的重点是理解 lambda 表达式的语法，它通常用于需要一个简单、一次性函数的场景
# （例如作为高阶函数的参数）。为其编写单元测试虽然可行，但有些过度。
# 我们直接在主程序块中验证其功能即可。

if __name__ == '__main__':
    result = square(5)
    print(f"5 的平方是: {result}")
    
    result_2 = square(10)
    print(f"10 的平方是: {result_2}")

    # 验证 lambda 函数的行为
    assert square(5) == 25
    assert square(0) == 0
    assert square(-3) == 9
    print("\nLambda 函数验证通过。") 