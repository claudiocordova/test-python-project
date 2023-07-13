import reminder as app
from reminder import Task

import datetime as dt
import pytest

from sys import version_info


def test_to_date():
    assert app._to_date("2022-09-01") == dt.date(2022, 9, 1)


def test_to_date_exception():
    with pytest.raises(ValueError, match="12345 is not in YYYY-MM-DD format."):
        app._to_date("12345")


def test_to_date_exception2():
    with pytest.raises(ValueError):
        app._to_date("2022-09-01A")


@pytest.fixture
def task_list():
    return [Task(name="pay rent"), Task(name="buy bread")]


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("buy bread", Task(name="buy bread")),
        ("buy banana", None),
        ("pay rent", Task(name="pay rent")),
        ("PAY RENT", Task(name="pay rent")),
    ],
)
def test_find_task(test_input, expected, task_list):
    # task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task(test_input, task_list) == expected


def test_find_task2(task_list):
    # task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task("pay rent", task_list) == Task(name="pay rent")


@pytest.mark.skip(reason="comming soon")
def test_find_task3(task_list):
    # task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task("pay rent", task_list) == Task(name="pay rent")


# @pytest.mark.skipif(version_info < ( 3, 8 ), reason="requires >= python3.9")
@pytest.mark.skipif(1 == 1, reason="requires >= python3.9")
def test_find_task4(task_list):
    # task_list = [Task(name="pay rent"), Task(name="buy bread")]
    print(version_info < (3, 8))
    print(version_info)
    print("hello")
    assert app._find_task("pay rent", task_list) == Task(name="pay rentt")


def test_find_task_none(task_list):
    # task_list = [Task(name="pay rent"), Task(name="buy bread")]
    assert app._find_task("pay banana", task_list) is None


def test_save_load_task_list(task_list):
    app._save_task_list(task_list)
    load_list = app._get_task_list()
    assert task_list == load_list
