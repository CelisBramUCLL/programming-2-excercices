import datetime


class Task:
    def __init__(self, description, due_date):
        self.__description = description
        self.__due_date = due_date
        self.__finished = False

    @property
    def description(self):
        return self.__description

    @property
    def due_date(self):
        return self.__due_date

    @property
    def finished(self):
        return self.__finished

    @finished.setter
    def finished(self, value):
        self.__finished = value


class TaskList:
    def __init__(self, calendar):
        self.__calendar = calendar
        self.__tasks = []

    def add_task(self, task):
        if task.due_date < self.__calendar.today:
            raise RuntimeError("due date is in the past")
        self.__tasks.append(task)

    def __len__(self):
        return len(self.__tasks)

    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished]

    @property
    def due_tasks(self):
        return [task for task in self.__tasks if not task.finished]

    @property
    def overdue_tasks(self):
        return [
            task
            for task in self.__tasks
            if task.due_date < self.__calendar.today and not task.finished
        ]
