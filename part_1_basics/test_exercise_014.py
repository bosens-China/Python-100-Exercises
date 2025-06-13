from part_1_basics.exercise_014 import modify_list

def test_modify_list():
    """
    测试 modify_list 函数是否能按要求修改列表。
    - 在末尾添加 "orange"
    - 在索引 1 处插入 "grape"
    """
    # 初始列表
    initial_fruits = ["apple", "banana", "cherry"]
    
    # 调用函数。注意：我们传递一个列表的副本 fruits[:]，
    # 以防止测试之间互相影响（虽然在这个文件中只有一个测试）。
    modified_fruits = modify_list(initial_fruits[:])
    
    # 预期的结果列表
    expected_fruits = ['apple', 'grape', 'banana', 'cherry', 'orange']
    
    # 断言结果是否符合预期
    assert modified_fruits == expected_fruits

def test_modify_list_on_empty_list():
    """
    测试在空列表上执行操作。
    根据提示，应该在末尾添加 'orange'，在索引 1 插入 'grape'。
    insert(1, ...) 在空列表上会插入到索引 0 的后面，即索引 1。
    """
    initial_list = []
    modified_list = modify_list(initial_list[:])
    
    # append("orange") -> ["orange"]
    # insert(1, "grape") -> ["orange", "grape"]
    assert modified_list == ["orange", "grape"]