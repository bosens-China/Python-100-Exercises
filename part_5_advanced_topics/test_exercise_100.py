from pathlib import Path


def test_project_readme_covers_delivery():
    readme = Path("PROJECT_README.md")
    assert readme.is_file(), "请为 API 项目创建 PROJECT_README.md"
    content = readme.read_text(encoding="utf-8").lower()
    for item in ("# ", "uvicorn", "pytest", "curl", "/todos"):
        assert item in content, f"交付文档缺少：{item}"
