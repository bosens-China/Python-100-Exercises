class Task:
    def __init__(self, title):
        self.title = title
        self.done = False

    def complete(self):
        self.done = True


class TaskList:
    def __init__(self):
        pass

    def add(self, title):
        pass

    def complete(self, index):
        pass

    def pending(self):
        pass
