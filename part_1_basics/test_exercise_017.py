from part_1_basics.exercise_017 import get_student_age

def test_get_student_age():
    """测试从字典中获取学生年龄"""
    student1 = {'name': 'Alice', 'age': 20, 'score': 90}
    assert get_student_age(student1) == 20

    student2 = {'name': 'Bob', 'city': 'Beijing', 'age': 25}
    assert get_student_age(student2) == 25 