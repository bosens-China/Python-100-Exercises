import ast
import json
import shutil

import pytest

from tools import course
from tools.grader import grade


def test_course_category_counts_and_dependencies():
    manifest, exercises = course.validate()
    assert manifest["id"] == "python-100-v2"
    assert [len(category["exercises"]) for category in manifest["categories"]] == [
        12,
        12,
        14,
        12,
        10,
        8,
        8,
        8,
        8,
        8,
    ]
    assert len(exercises) == 100
    assert exercises[0]["prerequisites"] == []


def test_export_uses_authoritative_sources_without_current_answers():
    bundle = json.loads(json.dumps(course.export_bundle(), ensure_ascii=False))
    assert len(bundle["exercises"]) == 100
    for exercise in bundle["exercises"]:
        assert "solution" not in exercise
        assert exercise["files"] == course.sources(exercise, "starter")
        assert exercise["tests"] == course.test_source(exercise)
    first = bundle["exercises"][0]
    assert "pass" in first["files"]["main.py"]
    assert not grade(first["files"], first["tests"])["passed"]


def test_forward_dependency_is_rejected(tmp_path):
    root = tmp_path / "curriculum"
    shutil.copytree(course.CURRICULUM, root)
    path = root / "01-basics/001-hello/exercise.json"
    metadata = json.loads(path.read_text(encoding="utf-8"))
    metadata["prerequisites"] = ["002"]
    path.write_text(json.dumps(metadata), encoding="utf-8")
    with pytest.raises(ValueError, match="前置题"):
        course.validate(root)


# 这些实现能通过一部分示例，却违背关键边界，必须被对应题目拒绝。
@pytest.mark.parametrize(
    "identifier, source",
    [
        ("004", "def whole_minutes(seconds): return round(seconds / 60)"),
        ("011", "def is_even(number): return int(number % 2 == 0)"),
        (
            "016",
            "def shipping_fee(amount, is_member): return 0 if is_member or amount > 9900 else 800",
        ),
        ("017", "def is_leap(year): return year % 4 == 0"),
        ("029", "def unique(items): return sorted(set(items))"),
        (
            "030",
            "def get_setting(settings, key, default): return settings.get(key) or default",
        ),
        (
            "062",
            "def validate_age(age):\n    if not isinstance(age, int) or not 0 <= age <= 120: raise ValueError()\n    return age",
        ),
        (
            "064",
            "def read_or_default(path, default=''):\n    try:\n        with open(path, encoding='utf-8') as f: return f.read()\n    except OSError: return default",
        ),
        ("067", "def check_shipping(shipping): assert shipping(10000) == 0"),
        (
            "086",
            "def task_id(path):\n    try: return int(path.split('/')[2])\n    except (ValueError, IndexError): return None",
        ),
        ("091", "def can_edit(user, owner_id): return user is not None"),
    ],
)
def test_exercise_rejects_plausible_wrong_solution(identifier, source):
    _, exercises = course.load_course()
    exercise = next(item for item in exercises if item["id"] == identifier)
    result = grade({"main.py": source}, course.test_source(exercise))
    assert not result["passed"], identifier
    assert all(case["status"] != "content_error" for case in result["cases"])


def test_project_import_rejects_partial_commit():
    _, exercises = course.load_course()
    exercise = next(item for item in exercises if item["id"] == "098")
    files = course.sources(exercise, "solution")
    files["store.py"] = files["store.py"].replace(
        "        tasks = {}\n",
        "        self._tasks = {}\n        tasks = self._tasks\n",
    )
    assert not grade(files, course.test_source(exercise))["passed"]


def test_transfer_rejects_committing_half_of_transaction():
    _, exercises = course.load_course()
    exercise = next(item for item in exercises if item["id"] == "084")
    files = course.sources(exercise, "solution")
    tree = ast.parse(files["main.py"])
    transaction = next(node for node in ast.walk(tree) if isinstance(node, ast.With))
    transaction.body.insert(1, ast.parse("db.commit()").body[0])
    files["main.py"] = ast.unparse(tree)
    assert not grade(files, course.test_source(exercise))["passed"]
