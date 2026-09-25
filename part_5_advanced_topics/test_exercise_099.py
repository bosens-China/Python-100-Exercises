from pathlib import Path
import re


def test_dependencies_are_pinned():
    lock = Path("requirements.lock")
    assert lock.is_file(), "请先生成 requirements.lock"
    lines = [line.strip() for line in lock.read_text(encoding="utf-8").splitlines()
             if line.strip() and not line.startswith("#")]
    assert lines, "requirements.lock 不能为空"
    assert all("==" in line and "://" not in line for line in lines), "依赖需要固定版本，且不能包含私人地址"
    direct = {re.split(r"[\[<=>~;]", line.strip())[0].lower() for line in Path("requirements.txt").read_text(encoding="utf-8").splitlines() if line.strip() and not line.startswith("#")}
    pinned = {line.split("==", 1)[0].lower() for line in lines}
    assert direct <= pinned, f"缺少直接依赖：{', '.join(sorted(direct - pinned))}"
