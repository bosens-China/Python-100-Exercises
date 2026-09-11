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
