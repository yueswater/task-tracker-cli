from pathlib import Path

import pytest

from config import FILENAME
from task_cli.models.task import Task
from task_cli.services.delete_task import delete_task
from task_cli.services.list_tasks import list_tasks
from task_cli.storage.json_store import save_tasks


def test_delete_existing_task_should_remove_it(tmp_path: Path):
    test_file = tmp_path / FILENAME
    task_id = 1
    description = "Delete me"

    save_tasks([Task(id=task_id, description=description)], path=test_file)
    delete_task(task_id=task_id, path=test_file)

    remaining_tasks = list_tasks(path=test_file)
    assert all(t.id != task_id for t in remaining_tasks)
    assert len(remaining_tasks) == 0


def test_delete_should_raise_if_id_not_found(tmp_path: Path):
    test_file = tmp_path / FILENAME
    save_tasks([], path=test_file)

    with pytest.raises(ValueError) as e:
        delete_task(task_id=999, path=test_file)

    assert "id: 999" in str(e.value)


def test_delete_should_not_affect_other_tasks(tmp_path: Path):
    test_file = tmp_path / FILENAME
    tasks = [Task(id=1, description="Delete me"), Task(id=2, description="Keep me")]
    save_tasks(tasks, path=test_file)

    delete_task(task_id=1, path=test_file)
    remaining = list_tasks(path=test_file)

    assert len(remaining) == 1
    assert remaining[0].id == 2
    assert remaining[0].description == "Keep me"


def test_delete_should_persist_after_reloading(tmp_path: Path):
    test_file = tmp_path / FILENAME
    save_tasks([Task(id=1, description="A")], path=test_file)

    delete_task(task_id=1, path=test_file)
    reloaded = list_tasks(path=test_file)

    assert reloaded == []
