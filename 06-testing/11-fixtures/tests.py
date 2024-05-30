from datetime import date

import pytest
from calendars import CalendarStub
from tasks import Task, TaskList


@pytest.fixture
def today():
    return date(2000, 1, 1)


@pytest.fixture
def tomorrow():
    return date(2000, 1, 2)


@pytest.fixture
def yesterday():
    return date(1999, 12, 31)


@pytest.fixture
def calendar(today):
    return CalendarStub(today)


@pytest.fixture
def sut(calendar):
    return TaskList(calendar)


def test_creation(sut):
    assert 0 == len(sut)
    assert [] == sut.overdue_tasks
    assert [] == sut.due_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_future(sut, tomorrow):
    task = Task("description", tomorrow)
    sut.add_task(task)
    assert 1 == len(sut)
    assert [] == sut.overdue_tasks
    assert [task] == sut.due_tasks
    assert [] == sut.finished_tasks


def test_adding_task_with_due_day_in_past(yesterday, sut):
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


def test_task_becomes_finished(tomorrow, sut):
    task = Task("description", tomorrow)
    sut.add_task(task)
    task.finished = True
    assert 1 == len(sut)
    assert [] == sut.overdue_tasks
    assert [] == sut.due_tasks
    assert [task] == sut.finished_tasks
