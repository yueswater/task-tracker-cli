from pathlib import Path

from config import FILENAME
from task_cli.models.task import Task, TaskStatus
from task_cli.services.list_tasks import list_tasks
from task_cli.storage.json_store import save_tasks


def test_list_all_tasks_empty(tmp_path: Path):
    test_file = tmp_path / FILENAME
    result = list_tasks(path=test_file)
    assert result == []


def test_list_all_tasks(tmp_path: Path):
    test_file = tmp_path / FILENAME
    tasks = [
        Task(id=1, description="a"),
        Task(id=2, description="b", status=TaskStatus.DONE),
        Task(id=2, description="c", status=TaskStatus.IN_PROGRESS),
    ]
    save_tasks(tasks=tasks, path=test_file)

    result = list_tasks(path=test_file)
    assert len(result) == 3
    assert {t.description for t in result} == {"a", "b", "c"}


def test_list_only_todo(tmp_path: Path):
    test_file = tmp_path / "tasks.json"
    tasks = [
        Task(id=1, description="a"),
        Task(id=2, description="b", status=TaskStatus.TODO),
        Task(id=3, description="c", status=TaskStatus.DONE),
    ]
    save_tasks(tasks, path=test_file)

    result = list_tasks(status=TaskStatus.TODO, path=test_file)
    assert len(result) == 2
    for task in result:
        assert task.status == TaskStatus.TODO


def test_list_only_done(tmp_path: Path):
    test_file = tmp_path / "tasks.json"
    tasks = [
        Task(id=1, description="x", status=TaskStatus.DONE),
        Task(id=2, description="y", status=TaskStatus.TODO),
    ]
    save_tasks(tasks, path=test_file)

    result = list_tasks(status=TaskStatus.DONE, path=test_file)
    assert len(result) == 1
    assert result[0].description == "x"


def test_list_only_in_progress(tmp_path: Path):
    test_file = tmp_path / "tasks.json"
    tasks = [
        Task(id=1, description="hello", status=TaskStatus.IN_PROGRESS),
        Task(id=2, description="bye", status=TaskStatus.TODO),
    ]
    save_tasks(tasks, path=test_file)

    result = list_tasks(status=TaskStatus.IN_PROGRESS, path=test_file)
    assert len(result) == 1
    assert result[0].status == TaskStatus.IN_PROGRESS
    assert result[0].description == "hello"
