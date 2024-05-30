from datetime import date
from calendars import CalendarStub
from tasks import Task, TaskList


def setup_function():
    global today, tomorrow, yesterday, calendar, sut
    today = date(2000, 1, 1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)
    tomorrow = date(2000, 1, 2)
    yesterday = date(1999, 12, 31)


def test_creation():
    assert 0 == len(sut)
    assert [] == sut.overdue_tasks
    assert [] == sut.due_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future():
    task = Task("description", tomorrow)
    sut.add_task(task)
    assert 1 == len(sut)
    assert [] == sut.overdue_tasks
    assert [task] == sut.due_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_past():
    task = Task("description", yesterday)
    try:
        sut.add_task(task)
        assert False
    except RuntimeError as error:
        assert "due date is in the past" == str(error)
    assert 0 == len(sut)
    assert [] == sut.overdue_tasks
    assert [] == sut.due_tasks
    assert [] == sut.finished_tasks


def test_task_becomes_finished():
    task = Task("description", tomorrow)
    sut.add_task(task)
    task.finished = True
    assert 1 == len(sut)
    assert [] == sut.overdue_tasks
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
