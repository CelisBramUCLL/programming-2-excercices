from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList


def test_creation():
    today = date(2000, 1, 1)
    calendar = CalendarStub(today)
    task_list = TaskList(calendar)
    assert 0 == len(task_list)
    assert [] == task_list.overdue_tasks
    assert [] == task_list.due_tasks
    assert [] == task_list.finished_tasks


def test_adding_task_with_due_day_in_future():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    calendar = CalendarStub(today)
    task = Task("description", tomorrow)
    task_list = TaskList(calendar)
    task_list.add_task(task)
    assert 1 == len(task_list)
    assert [] == task_list.overdue_tasks
    assert [task] == task_list.due_tasks
    assert [] == task_list.finished_tasks


def test_adding_task_with_due_day_in_past():
    today = date(2000, 1, 1)
    yesterday = date(1999, 12, 31)
    calendar = CalendarStub(today)
    task = Task("description", yesterday)
    task_list = TaskList(calendar)
    try:
        task_list.add_task(task)
        assert False
    except RuntimeError as error:
        assert "due date is in the past" == str(error)
    assert 0 == len(task_list)
    assert [] == task_list.overdue_tasks
    assert [] == task_list.due_tasks
    assert [] == task_list.finished_tasks


def test_task_becomes_finished():
    today = date(2000, 1, 1)
    tomorrow = date(2000, 1, 2)
    calendar = CalendarStub(today)
    task = Task("description", tomorrow)
    task_list = TaskList(calendar)
    task_list.add_task(task)
    task.finished = True
    assert 1 == len(task_list)
    assert [] == task_list.overdue_tasks
    assert [] == task_list.due_tasks
    assert [task] == task_list.finished_tasks
