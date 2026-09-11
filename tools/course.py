"""维护者入口：python -m tools.course validate / check / export。"""

import argparse
import ast
import json
from pathlib import Path
import subprocess
import sys

from tools.grader import grade, validate_files

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"


def load_course(root=CURRICULUM):
    manifest = json.loads((root / "course.json").read_text(encoding="utf-8"))
    exercises = []
    for category in manifest["categories"]:
        for identifier in category["exercises"]:
            candidates = list(
                (root / category["id"]).glob(f"{identifier}-*/exercise.json")
            )
            if len(candidates) != 1:
                raise ValueError(f"{identifier} 必须恰好对应一个题目目录")
            metadata = json.loads(candidates[0].read_text(encoding="utf-8"))
            if metadata["id"] != identifier or metadata["category"] != category["id"]:
                raise ValueError(f"{identifier} 分类或编号与清单不符")
            if (root / metadata["path"]).resolve() != candidates[0].parent.resolve():
                raise ValueError(f"{identifier} 路径与清单不符")
            exercises.append(metadata)
    return manifest, exercises


def sources(exercise, kind, root=CURRICULUM):
    directory = root / exercise["path"] / kind
    return {
        name: (directory / name).read_text(encoding="utf-8")
        for name in exercise["starter_files"]
    }


def test_source(exercise, root=CURRICULUM):
    return (root / exercise["path"] / "test/test_solution.py").read_text(
        encoding="utf-8"
    )


def validate(root=CURRICULUM):
    manifest, exercises = load_course(root)
    expected_ids = [f"{number:03d}" for number in range(1, 101)]
    if [item["id"] for item in exercises] != expected_ids:
        raise ValueError("题库编号必须唯一、连续且按 001–100 排列")
    if len(manifest["categories"]) != 10:
        raise ValueError("课程必须包含 10 个大类")
    actual_paths = {
        path.parent.relative_to(root).as_posix()
        for path in root.glob("*/*/exercise.json")
    }
    if actual_paths != {item["path"] for item in exercises}:
        raise ValueError("存在未列入清单的题目或重复路径")
    seen = set()
    headings = [
        "学习目标",
        "前置知识",
        "先学一点",
        "任务与约定",
        "示例",
        "开始编写",
        "分层提示",
        "如何验收",
    ]
    for item in exercises:
        identifier = item["id"]
        if not item["title"] or not item["goal"]:
            raise ValueError(f"{identifier} 缺少标题或学习目标")
        if not set(item["prerequisites"]) <= seen:
            raise ValueError(f"{identifier} 前置题必须已在前文出现")
        seen.add(identifier)
        directory = root / item["path"]
        question = (directory / "README.md").read_text(encoding="utf-8")
        if (
            any(f"## {heading}" not in question for heading in headings)
            or question.count("<details>") != 2
        ):
            raise ValueError(f"{identifier} 题目说明或分层提示不完整")
        for kind in ("starter", "solution"):
            files = sources(item, kind, root)
            validate_files(files, item["entrypoint"])
            if len(item["starter_files"]) != len(files):
                raise ValueError(f"{identifier} 文件清单有重复")
            actual = {path.name for path in (directory / kind).glob("*.py")}
            if actual != set(files):
                raise ValueError(f"{identifier} {kind} 文件清单不完整")
            for name, source in files.items():
                compile(source, name, "exec")
        tree = ast.parse(test_source(item, root))
        names = [
            node.name
            for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
        ]
        if len(names) < 2 or len(names) != len(set(names)):
            raise ValueError(f"{identifier} 必须包含至少两项独立行为测试")
    return manifest, exercises


def export_bundle(root=CURRICULUM):
    manifest, exercises = validate(root)
    payloads = []
    for exercise in exercises:
        payloads.append(
            {
                **exercise,
                "question": (root / exercise["path"] / "README.md").read_text(
                    encoding="utf-8"
                ),
                "files": sources(exercise, "starter", root),
                "tests": test_source(exercise, root),
            }
        )
    return {"schema_version": 1, **manifest, "exercises": payloads}


def check(exercises):
    count = 0
    for exercise in exercises:
        identifier = exercise["id"]
        for kind in ("solution", "starter"):
            try:
                process = subprocess.run(
                    [
                        sys.executable,
                        "-m",
                        "tools.course",
                        "grade",
                        identifier,
                        "--kind",
                        kind,
                    ],
                    cwd=ROOT,
                    capture_output=True,
                    text=True,
                    timeout=15,
                )
            except subprocess.TimeoutExpired as error:
                raise ValueError(f"{identifier} {kind} 执行超过 15 秒") from error
            if process.returncode != 0:
                raise ValueError(f"{identifier} {kind} 执行失败：{process.stderr}")
            result = json.loads(process.stdout)
            if result.get("content_error") or any(
                case["status"] == "content_error" for case in result["cases"]
            ):
                raise ValueError(f"{identifier} 测试内容错误：{result}")
            if result["passed"] != (kind == "solution"):
                failures = [
                    case for case in result["cases"] if case["status"] != "passed"
                ]
                raise ValueError(
                    f"{identifier} {kind} 验收不符：{json.dumps(failures, ensure_ascii=False, indent=2)}"
                )
            if kind == "solution":
                count += result["total"]
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    subcommands = parser.add_subparsers(dest="command", required=True)
    subcommands.add_parser("validate")
    subcommands.add_parser("check")
    export_parser = subcommands.add_parser("export")
    export_parser.add_argument("output", type=Path)
    grade_parser = subcommands.add_parser("grade")
    grade_parser.add_argument("id")
    grade_parser.add_argument(
        "--kind", choices=("starter", "solution"), default="starter"
    )
    arguments = parser.parse_args()
    try:
        if arguments.command == "grade":
            _, exercises = load_course()
            exercise = next(
                (item for item in exercises if item["id"] == arguments.id), None
            )
            if exercise is None:
                raise ValueError(f"题目不存在：{arguments.id}")
            result = grade(
                sources(exercise, arguments.kind),
                test_source(exercise),
                exercise["entrypoint"],
            )
            print(json.dumps(result, ensure_ascii=False))
        elif arguments.command == "export":
            bundle = export_bundle()
            arguments.output.parent.mkdir(parents=True, exist_ok=True)
            arguments.output.write_text(
                json.dumps(bundle, ensure_ascii=False, indent=2) + "\n",
                encoding="utf-8",
            )
            print(f"已导出 {len(bundle['exercises'])} 题：{arguments.output}")
        else:
            _, exercises = validate()
            if arguments.command == "check":
                count = check(exercises)
                print(
                    f"100 题参考实现通过 {count} 项测试；100 份起始代码均未误判通过。"
                )
            else:
                print("10 类、100 题内容结构检查通过。")
    except (ValueError, OSError, SyntaxError) as error:
        parser.exit(1, f"检查失败：{error}\n")


if __name__ == "__main__":
    main()
