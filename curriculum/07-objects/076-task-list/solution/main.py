class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True


class TaskList:
    def __init__(self):
        self._tasks = []

    def add(self, title):
        self._tasks.append(Task(title))
        return len(self._tasks) - 1

    def complete(self, index):
        if not 0 <= index < len(self._tasks):
            raise IndexError("任务不存在")
        self._tasks[index].complete()

    def pending(self):
        return [task.title for task in self._tasks if not task.done]
