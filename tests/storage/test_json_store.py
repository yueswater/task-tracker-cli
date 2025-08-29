import json
from pathlib import Path

from config import FILENAME
from task_cli.models.task import Task, TaskStatus
from task_cli.storage.json_store import get_default_path, load_tasks, save_tasks


def test_get_default_path():
    path = get_default_path()
    assert isinstance(path, Path)
    assert path.name == "tasks.json"


def test_save_and_load_tasks(tmp_path: Path):
    test_file = tmp_path / FILENAME
    task1 = Task(id=1, description="Test one")
    task2 = Task(id=2, description="Test two", status=TaskStatus.DONE)

    save_tasks([task1, task2], path=test_file)

    assert test_file.exists()

    tasks = load_tasks(test_file)

    assert len(tasks) == 2
    assert tasks[0].id == 1
    assert tasks[1].status == TaskStatus.DONE


def test_load_file_if_missing(tmp_path: Path):
    test_file = tmp_path / FILENAME
    assert not test_file.exists()

    tasks = load_tasks(test_file)

    assert tasks == []
    assert test_file.exists()
    assert json.loads(test_file.read_text()) == []


def test_load_invalid_json(tmp_path: Path):
    test_file = tmp_path / FILENAME
    test_file.write_text("invalid json...", encoding="utf-8")

    tasks = load_tasks(test_file)

    assert tasks == []
