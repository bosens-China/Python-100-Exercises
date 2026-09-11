import json
from domain import new_task


class Store:
    def __init__(self):
        self._tasks = {}
        self._next_id = 1

    def add(self, title):
        task = new_task(self._next_id, title)
        self._tasks[task["id"]] = task
        self._next_id += 1
        return task.copy()

    def list(self, done=None):
        if done is not None and type(done) is not bool:
            raise ValueError("筛选条件必须是布尔值或 None")
        return [
            task.copy()
            for _, task in sorted(self._tasks.items())
            if done is None or task["done"] == done
        ]

    def complete(self, identifier):
        if type(identifier) is not int or identifier not in self._tasks:
            raise KeyError(identifier)
        self._tasks[identifier]["done"] = True
        return self._tasks[identifier].copy()

    def delete(self, identifier):
        if type(identifier) is not int or identifier not in self._tasks:
            return False
        del self._tasks[identifier]
        return True

    def export_json(self):
        return json.dumps(self.list(), ensure_ascii=False)

    def import_json(self, text):
        rows = json.loads(text)
        if not isinstance(rows, list):
            raise ValueError("必须是任务列表")
        tasks = {}
        for row in rows:
            if not isinstance(row, dict) or set(row) != {"id", "title", "done"}:
                raise ValueError("任务字段无效")
            task = new_task(row["id"], row["title"])
            if type(row["done"]) is not bool or task["id"] in tasks:
                raise ValueError("状态无效或 ID 重复")
            task["done"] = row["done"]
            tasks[task["id"]] = task
        self._tasks = tasks
        self._next_id = max(tasks, default=0) + 1
        return len(tasks)
