from pathlib import Path

from config import FILENAME
from task_cli.models.task import Task, TaskStatus
from task_cli.services.add_task import add_task
from task_cli.services.list_tasks import list_tasks
from task_cli.storage.json_store import save_tasks


def test_add_task_successfully(tmp_path: Path):
    test_file = tmp_path / FILENAME
    description = "a"
    task = add_task(description=description, path=test_file)

    assert isinstance(task, Task)
    assert isinstance(task.id, int)
    assert not task.description == ""
    assert task.status in TaskStatus


def test_add_first_task(tmp_path: Path):
    test_file = tmp_path / FILENAME
    description = "First task"
    task = add_task(description=description, path=test_file)

    assert task.id == 1
    assert task.description
    assert task.status == TaskStatus.TODO


def test_increment_id(tmp_path: Path):
    test_file = tmp_path / FILENAME
    save_tasks([Task(id=1, description="first")], path=test_file)

    tasks = list_tasks(path=test_file)
    max_id = max(t.id for t in tasks)

    description = "a"
    task = add_task(description=description, path=test_file)

    assert task.id > max_id


def test_add_task_file_existence(tmp_path: Path):
    test_file = tmp_path / FILENAME

    description = "a"
    _ = add_task(description=description, path=test_file)

    assert test_file.exists()
