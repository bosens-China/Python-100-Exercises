from part_2_control_flow.exercise_035 import count_vowels

def test_count_vowels():
    """测试元音字母计数"""
    assert count_vowels("Hello Python") == 3 # e, o, o
    assert count_vowels("AEIOU aeiou") == 10
    assert count_vowels("Rhythm") == 0
    assert count_vowels("") == 0
    assert count_vowels("This is a test sentence.") == 7 