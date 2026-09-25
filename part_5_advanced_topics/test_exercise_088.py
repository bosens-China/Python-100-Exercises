import ast
from pathlib import Path


def test_authenticated_client_fixture_is_used():
    path = Path("part_4_oop/test_todos.py")
    assert path.is_file(), "请创建 part_4_oop/test_todos.py"
    tree = ast.parse(path.read_text(encoding="utf-8"))
    functions = [node for node in tree.body if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))]
    fixture = next((node for node in functions if node.name == "authenticated_client"), None)
    assert fixture is not None, "请定义 authenticated_client fixture"
    assert any(isinstance(node, ast.Attribute) and node.attr == "fixture" for decorator in fixture.decorator_list for node in ast.walk(decorator))
    assert any(isinstance(node, (ast.Yield, ast.YieldFrom)) for node in ast.walk(fixture))
    assert any(node.name.startswith("test_") and "authenticated_client" in [arg.arg for arg in node.args.args] for node in functions)
