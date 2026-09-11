"""执行题目行为测试；这是学习反馈内核，不是恶意代码安全沙箱。

只依赖 Python 标准库。浏览器宿主负责停止和超时，本内核限制每项标准输出与错误输出长度；维护 CLI
在可终止的子进程中调用。本模块修改 cwd 与导入状态，不可在线程间并发调用。
"""

import ast
import contextlib
import importlib
import io
import os
from pathlib import Path
import re
import sys
import tempfile
import traceback
import types
import unittest


class OutputLimitExceeded(RuntimeError):
    pass


class _Output(io.StringIO):
    """限制单次测试输出，避免 print 循环占满浏览器内存。"""

    def write(self, text):
        remaining = 32_000 - self.tell()
        if len(text) > remaining:
            super().write(text[:remaining])
            raise OutputLimitExceeded("输出超过 32000 个字符，请减少打印或检查循环")
        return super().write(text)


class _Assertions(ast.NodeTransformer):
    """给常见断言补充实际值与预期值，保持操作数只执行一次。"""

    def visit_Assert(self, node):
        test = node.test
        if isinstance(test, ast.Compare) and len(test.ops) == 1:
            operation = test.ops[0]
            helper = {ast.Eq: "_equal", ast.Is: "_same"}.get(type(operation))
            if helper:
                arguments = [test.left, test.comparators[0]]
                if node.msg is not None:
                    arguments.append(node.msg)
                return ast.copy_location(
                    ast.Expr(ast.Call(ast.Name(helper, ast.Load()), arguments, [])),
                    node,
                )
        return node


def validate_files(files, entrypoint="main.py"):
    if not isinstance(files, dict) or not files or entrypoint not in files:
        raise ValueError("必须提供源文件及入口文件")
    for name, source in files.items():
        if not isinstance(name, str) or not re.fullmatch(r"[a-z][a-z0-9_]*\.py", name):
            raise ValueError(f"仅支持工作区内的顶层 Python 文件：{name!r}")
        if not isinstance(source, str):
            raise ValueError(f"文件内容必须是文本：{name}")


def _equal(actual, expected, message=None):
    if actual != expected:
        raise AssertionError(
            f"预期：{expected!r}；实际：{actual!r}"
            + (f"；{message}" if message else "")
        )


def _same(actual, expected, message=None):
    if actual is not expected:
        raise AssertionError(
            f"预期：{expected!r}（同一对象）；实际：{actual!r}"
            + (f"；{message}" if message else "")
        )


def grade(files, test_source, entrypoint="main.py"):
    """接收文件名到源码的映射，返回可 JSON 序列化的逐项结果。

    每项测试在全新的临时工作区加载完整学生代码，测试文件拥有独立命名空间。
    不做源码相等判断，也不执行参考答案。非法题目测试是 content_error，不能通过。
    """
    validate_files(files, entrypoint)
    try:
        tree = ast.parse(test_source, filename="test_solution.py")
        names = [
            node.name
            for node in tree.body
            if isinstance(node, ast.FunctionDef) and node.name.startswith("test_")
        ]
        if not names or len(names) != len(set(names)):
            raise ValueError("测试必须包含名称唯一的 test_ 函数")
        test_code = compile(
            ast.fix_missing_locations(_Assertions().visit(tree)),
            "test_solution.py",
            "exec",
        )
    except (SyntaxError, ValueError) as error:
        return {
            "passed": False,
            "total": 0,
            "passed_count": 0,
            "cases": [],
            "content_error": str(error),
        }

    results = []
    module_names = {Path(name).stem for name in files} | {"student"}
    for name in names:
        output = _Output()
        errors = _Output()
        case = {"name": name, "status": "passed", "message": "", "traceback": ""}
        original_directory = Path.cwd()
        original_path = sys.path.copy()
        previous_modules = {
            key: sys.modules[key] for key in module_names if key in sys.modules
        }
        with tempfile.TemporaryDirectory(prefix="python100-") as temporary:
            directory = Path(temporary)
            phase = "setup"
            try:
                for filename, source in files.items():
                    (directory / filename).write_text(source, encoding="utf-8")
                (directory / "test_solution.py").write_text(
                    test_source, encoding="utf-8"
                )
                for key in module_names:
                    sys.modules.pop(key, None)
                sys.path.insert(0, str(directory))
                importlib.invalidate_caches()
                os.chdir(directory)
                student = types.ModuleType("student")
                student.__file__ = str(directory / entrypoint)
                sys.modules["student"] = student
                phase = "student"
                with (
                    contextlib.redirect_stdout(output),
                    contextlib.redirect_stderr(errors),
                ):
                    exec(
                        compile(files[entrypoint], entrypoint, "exec"), student.__dict__
                    )
                    namespace = {
                        "__name__": "exercise_tests",
                        "student": student,
                        "raises": unittest.TestCase().assertRaises,
                        "_equal": _equal,
                        "_same": _same,
                    }
                    phase = "tests"
                    exec(test_code, namespace)
                    phase = "case"
                    namespace[name]()
            except BaseException as error:
                # 学生代码中的 SystemExit 也不能退出维护者的整次检查。
                case["status"] = "content_error" if phase == "tests" else "failed"
                case["message"] = f"{type(error).__name__}: {error}"
                case["traceback"] = "".join(traceback.format_exception(error))
            finally:
                os.chdir(original_directory)
                sys.path[:] = original_path
                # 清除本工作区导入的模块，恢复同名宿主模块。
                for key, module in list(sys.modules.items()):
                    filename = getattr(module, "__file__", None)
                    if key in module_names or (
                        isinstance(filename, str)
                        and filename.startswith(str(directory) + os.sep)
                    ):
                        sys.modules.pop(key, None)
                sys.modules.update(previous_modules)
                sys.path_importer_cache.pop(str(directory), None)
                importlib.invalidate_caches()
        case["stdout"] = output.getvalue()
        case["stderr"] = errors.getvalue()
        results.append(case)
    passed_count = sum(case["status"] == "passed" for case in results)
    return {
        "passed": passed_count == len(results),
        "total": len(results),
        "passed_count": passed_count,
        "cases": results,
    }
