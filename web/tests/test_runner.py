import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from run_tests import run_tests


def test_existing_exercise_runs_and_reports_failures():
    test_source = (Path(__file__).resolve().parents[2] / 'part_1_basics/test_exercise_001.py').read_text(encoding='utf-8')
    passed = json.loads(run_tests(1, 'def hello_world():\n    return "Hello, World!"', test_source))
    failed = json.loads(run_tests(1, 'def hello_world():\n    return None', test_source))
    assert passed == [{'name': 'test_hello_world', 'passed': True}]
    assert failed[0]['passed'] is False


def test_every_independent_exercise_is_collectable():
    root = Path(__file__).resolve().parents[2]
    for number in (*range(1, 51), 96, 97, 98):
        folder = 'part_1_basics' if number <= 20 else 'part_2_control_flow' if number <= 40 else 'part_3_functions' if number <= 50 else 'part_5_advanced_topics'
        source = (root / folder / f'exercise_{number:03d}.py').read_text(encoding='utf-8')
        tests = (root / folder / f'test_exercise_{number:03d}.py').read_text(encoding='utf-8')
        results = json.loads(run_tests(number, source, tests))
        assert results and results[0]['name'] != '加载代码', number
