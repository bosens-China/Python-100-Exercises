"""
### 28. 打印三角形图案

- **描述:** 使用 `*` 字符打印一个高度为 5 的直角三角形。
- **提示:** 使用嵌套 `for` 循环。外层循环控制行数，内层循环控制每行打印的 `*` 数量。
- **期待:**
  ```
  *
  **
  ***
  ****
  *****
  ```
"""

def generate_triangle(height):
    """
    生成一个指定高度的由 '*' 组成的直角三角形字符串。
    :param height: 三角形的高度
    :return: 代表三角形的字符串
    """
    triangle_str = ""
    # 在这里写下你的代码
    return triangle_str

if __name__ == '__main__':
    h = 5
    triangle = generate_triangle(h)
    print(f"高度为 {h} 的三角形:")
    print(triangle) 