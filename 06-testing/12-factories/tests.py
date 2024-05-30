from datetime import date

import pytest
from calendars import CalendarStub
from tasks import Task, TaskList


def today():
    return date(2000, 1, 1)


def tomorrow():
    return date(2000, 1, 2)


def yesterday():
    return date(1999, 12, 31)


def create_calendar():
    return CalendarStub(today())


def create_empty_task_list(calendar=None):
    calendar = calendar or create_calendar()
    return TaskList(calendar)


def create_task(*, description="default description", due_date=None, finished=False):
    due_date = due_date or date(2000, 1, 1)
    task = Task(description, due_date)
    if finished:
        task.finished = True
    return task


def test_creation():
    sut = create_empty_task_list()
    assert 0 == len(sut)
    assert [] == sut.overdue_tasks
    assert [] == sut.due_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future():
    sut = create_empty_task_list()
    task = create_task(due_date=tomorrow())
    sut.add_task(task)
    assert 1 == len(sut)
    assert [] == sut.overdue_tasks
    assert [task] == sut.due_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_past():
    sut = create_empty_task_list()
    task = create_task(due_date=yesterday())
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
    sut = create_empty_task_list()
    task = create_task(due_date=tomorrow(), finished=True)
    sut.add_task(task)
    assert 1 == len(sut)
    assert [] == sut.overdue_tasks
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
