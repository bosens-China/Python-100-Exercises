"""
### 18. 字典修改

- **描述:** 在第 17 题创建的学生字典中，将学生的成绩修改为 95，并添加一个新的键值对表示他的城市 "city": "Beijing"。
- **提示:** 通过键直接赋值可以修改现有值 `student['score'] = 95` 或添加新值 `student['city'] = 'Beijing'`。
- **期待:** 修改后的字典为 `{'name': 'Alice', 'age': 20, 'score': 95, 'city': 'Beijing'}`。
"""

def modify_student_info(student):
    """
    修改学生字典：更新成绩，添加城市
    :param student: 学生信息字典
    :return: 修改后的字典
    """
    # 在这里写下你的代码
    # 注意: 字典是可变对象，此函数可以直接修改传入的字典
    return student

if __name__ == '__main__':
    student_info = {'name': 'Alice', 'age': 20, 'score': 90}
    print(f"原始字典: {student_info}")
    modified_info = modify_student_info(student_info)
    print(f"修改后字典: {modified_info}") 