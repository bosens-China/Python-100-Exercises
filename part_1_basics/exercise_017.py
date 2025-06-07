"""
### 17. 字典创建与访问

- **描述:** 创建一个字典来存储一个学生的信息：姓名、年龄和成绩。然后访问并打印学生的年龄。
- **提示:** 字典用花括号 `{}` 创建，包含键值对，如 `{'name': 'Alice', 'age': 20}`。通过键来访问值 `student['age']`。
- **期待:** `print(student_age)` 输出 `20`。
"""

def get_student_age(student):
    """
    从学生字典中获取年龄
    :param student: 学生信息字典
    :return: 学生的年龄
    """
    # 在这里写下你的代码
    pass

if __name__ == '__main__':
    student_info = {'name': 'Alice', 'age': 20, 'score': 90}
    age = get_student_age(student_info)
    print(f"学生 {student_info['name']} 的年龄是: {age}") 