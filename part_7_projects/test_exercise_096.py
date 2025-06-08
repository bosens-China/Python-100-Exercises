import pytest
from part_7_projects.exercise_096 import add_note, list_notes, delete_note, load_notes

@pytest.fixture
def temp_notepad(tmp_path):
    """一个 pytest fixture，用于提供一个临时文件路径用于测试。"""
    return tmp_path / "test_notes.txt"

def test_add_note(temp_notepad, capsys):
    """测试添加笔记功能。"""
    add_note("第一条笔记", temp_notepad)
    notes = load_notes(temp_notepad)
    assert "第一条笔记" in notes
    
    add_note("第二条笔记", temp_notepad)
    notes = load_notes(temp_notepad)
    assert "第一条笔记" in notes
    assert "第二条笔记" in notes
    
    captured = capsys.readouterr()
    assert '成功添加笔记: "第一条笔记"' in captured.out
    assert '成功添加笔记: "第二条笔记"' in captured.out

def test_list_notes_empty(temp_notepad, capsys):
    """测试当文件不存在时，列出笔记应显示空记事本信息。"""
    list_notes(temp_notepad)
    captured = capsys.readouterr()
    assert "记事本是空的" in captured.out

def test_list_notes_with_content(temp_notepad, capsys):
    """测试列出有内容的记事本。"""
    add_note("笔记A", temp_notepad)
    add_note("笔记B", temp_notepad)
    
    # 清除之前 add_note 的输出
    capsys.readouterr() 
    
    list_notes(temp_notepad)
    captured = capsys.readouterr()
    assert "1. 笔记A" in captured.out
    assert "2. 笔记B" in captured.out

def test_delete_note(temp_notepad, capsys):
    """测试删除笔记功能。"""
    add_note("待删除的笔记", temp_notepad)
    add_note("保留的笔记", temp_notepad)
    
    delete_note("1", temp_notepad)
    
    notes = load_notes(temp_notepad)
    assert len(notes) == 1
    assert "保留的笔记" in notes
    assert "待删除的笔记" not in notes
    
    captured = capsys.readouterr()
    assert '成功删除笔记 1: "待删除的笔记"' in captured.out

def test_delete_invalid_note_number(temp_notepad, capsys):
    """测试删除无效行号的情况。"""
    add_note("唯一的一条笔记", temp_notepad)
    
    delete_note("99", temp_notepad)
    captured = capsys.readouterr()
    assert "错误：无效的行号 '99'" in captured.out
    
    delete_note("abc", temp_notepad)
    captured = capsys.readouterr()
    assert "错误：行号 'abc' 必须是一个数字" in captured.out
