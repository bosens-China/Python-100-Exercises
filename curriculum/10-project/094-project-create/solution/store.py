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
