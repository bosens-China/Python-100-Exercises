"""Run one existing exercise test file without depending on pytest in the browser."""

import contextlib
import inspect
import io
import json
import re
import sys
import tempfile
import traceback
import types
from pathlib import Path
from unittest import mock


class Raises:
    def __init__(self, expected, match=None):
        self.expected = expected
        self.match = match

    def __enter__(self):
        return self

    def __exit__(self, kind, value, _traceback):
        if kind is None:
            raise AssertionError(f"未抛出 {self.expected.__name__}")
        if not issubclass(kind, self.expected):
            return False
        if self.match and not re.search(self.match, str(value)):
            raise AssertionError(f"异常信息不符合预期：{value}")
        return True


class Mocker:
    Mock = mock.Mock

    def __init__(self):
        self.patches = []

    def patch(self, target, **kwargs):
        patch = mock.patch(target, **kwargs)
        self.patches.append(patch)
        return patch.start()

    def stop(self):
        for patch in reversed(self.patches):
            patch.stop()


def run_tests(number, exercise_source, test_source):
    group = ("part_1_basics" if number <= 20 else "part_2_control_flow" if number <= 40
             else "part_3_functions" if number <= 50 else "part_5_advanced_topics")
    module_name = f"{group}.exercise_{number:03d}"
    previous = {}
    for name in ("pytest", "requests", group, module_name):
        previous[name] = sys.modules.get(name)

    pytest = types.ModuleType("pytest")
    pytest.fixture = lambda function: function
    pytest.raises = Raises
    requests = types.ModuleType("requests")
    requests.exceptions = types.SimpleNamespace(RequestException=type("RequestException", (Exception,), {}))
    requests.get = mock.Mock()
    requests.post = mock.Mock()
    package = types.ModuleType(group)
    package.__path__ = []
    exercise = types.ModuleType(module_name)
    sys.modules.update({"pytest": pytest, "requests": requests, group: package, module_name: exercise})

    results = []
    try:
        with contextlib.redirect_stdout(io.StringIO()):
            exec(compile(exercise_source, module_name, "exec"), exercise.__dict__)
        namespace = {}
        exec(compile(test_source, f"test_exercise_{number:03d}.py", "exec"), namespace)
        for name, function in namespace.items():
            if not name.startswith("test_") or not callable(function):
                continue
            mocker = Mocker()
            fixtures = []
            try:
                with tempfile.TemporaryDirectory() as directory:
                    arguments = {}
                    for parameter in inspect.signature(function).parameters:
                        if parameter == "tmp_path":
                            arguments[parameter] = Path(directory)
                        elif parameter == "mocker":
                            arguments[parameter] = mocker
                        elif parameter in namespace:
                            fixture = namespace[parameter]()
                            arguments[parameter] = next(fixture)
                            fixtures.append(fixture)
                        else:
                            raise RuntimeError(f"不支持的测试参数：{parameter}")
                    function(**arguments)
                results.append({"name": name, "passed": True})
            except Exception as error:
                frames = traceback.extract_tb(error.__traceback__)
                location = next((frame for frame in reversed(frames) if frame.filename.endswith(f"test_exercise_{number:03d}.py")), None)
                results.append({"name": name, "passed": False, "message": f"{location.lineno} 行：{error}" if location else str(error) or type(error).__name__})
            finally:
                for fixture in reversed(fixtures):
                    fixture.close()
                mocker.stop()
    except Exception as error:
        results.append({"name": "加载代码", "passed": False, "message": f"{type(error).__name__}: {error}"})
    finally:
        for name, module in previous.items():
            if module is None:
                sys.modules.pop(name, None)
            else:
                sys.modules[name] = module

    return json.dumps(results, ensure_ascii=False)
