import pytest
import os
from part_7_projects.exercise_096 import add_note, list_notes, delete_note, load_notes, save_notes

@pytest.fixture
def temp_notepad(tmp_path):
    """一个 pytest fixture，用于提供一个临时文件路径用于测试，并在测试后清理。"""
    return tmp_path / "test_notes.txt"

def test_load_notes_non_existent_file(temp_notepad):
    """测试当文件不存在时，load_notes 应返回一个空列表。"""
    assert load_notes(temp_notepad) == []

def test_save_and_load_notes(temp_notepad):
    """测试保存和加载笔记的功能。"""
    notes_to_save = ["第一行笔记\n", "第二行笔记\n"]
    save_notes(notes_to_save, temp_notepad)
    
    assert os.path.exists(temp_notepad)
    
    loaded_notes = load_notes(temp_notepad)
    assert loaded_notes == notes_to_save

def test_add_note(temp_notepad, capsys):
    """测试添加笔记功能。"""
    add_note("第一条笔记", temp_notepad)
    notes = load_notes(temp_notepad)
    assert "第一条笔记\n" in notes
    
    add_note("第二条笔记", temp_notepad)
    notes = load_notes(temp_notepad)
    assert "第一条笔记\n" in notes
    assert "第二条笔记\n" in notes
    
    captured = capsys.readouterr()
    assert "笔记已添加。" in captured.out

def test_list_notes_empty(temp_notepad, capsys):
    """测试当文件不存在时，列出笔记应显示特定信息。"""
    list_notes(temp_notepad)
    captured = capsys.readouterr()
    assert "没有笔记。" in captured.out

def test_list_notes_with_content(temp_notepad, capsys):
    """测试列出有内容的记事本。"""
    save_notes(["笔记A\n", "笔记B\n"], temp_notepad)
    
    list_notes(temp_notepad)
    captured = capsys.readouterr()
    # 确保 strip() 被正确使用
    assert "1: 笔记A" in captured.out
    assert "2: 笔记B" in captured.out

def test_delete_note(temp_notepad, capsys):
    """测试删除笔记功能。"""
    save_notes(["笔记1\n", "笔记2\n"], temp_notepad)
    
    delete_note("1", temp_notepad)
    
    notes = load_notes(temp_notepad)
    assert len(notes) == 1
    assert "笔记2\n" in notes
    assert "笔记1\n" not in notes
    
    captured = capsys.readouterr()
    assert "笔记 1 已删除。" in captured.out

def test_delete_invalid_note_number(temp_notepad, capsys):
    """测试删除无效行号的情况。"""
    save_notes(["唯一的一条笔记\n"], temp_notepad)
    
    # 无效索引
    delete_note("99", temp_notepad)
    captured = capsys.readouterr()
    assert "错误：无效的行号。" in captured.out
    
    # 非数字输入
    delete_note("abc", temp_notepad)
    captured = capsys.readouterr()
    assert "错误：行号必须是一个数字。" in captured.out
