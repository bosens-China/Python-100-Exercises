from part_1_basics.exercise_018 import modify_student_info

def test_modify_student_info_no_city():
    """测试为没有城市的学生添加信息"""
    student = {'name': 'Alice', 'age': 20, 'score': 90}
    # 因为函数会修改原始字典，我们传递一个副本进行测试
    modified = modify_student_info(student.copy())
    expected = {'name': 'Alice', 'age': 20, 'score': 95, 'city': 'Beijing'}
    assert modified == expected

def test_modify_student_info_with_city():
    """测试为已有城市的学生修改信息"""
    student2 = {'name': 'Bob', 'age': 22, 'score': 80, 'city': 'Shanghai'}
    modified2 = modify_student_info(student2.copy())
    expected2 = {'name': 'Bob', 'age': 22, 'score': 95, 'city': 'Beijing'}
    assert modified2 == expected2 