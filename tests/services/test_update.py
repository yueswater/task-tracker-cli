import pytest
from pathlib import Path

from config import FILENAME
from task_cli.models.task import Task
from task_cli.services.update_task import update_task
from task_cli.storage.json_store import save_tasks


def test_update_existing_task_description(tmp_path: Path):
    test_file = tmp_path / FILENAME
    task_id = 1
    old_description = "old"
    new_description = "new"

    old_task = Task(id=task_id, description=old_description)
    save_tasks(tasks=[old_task], path=test_file)

    new_task = update_task(
        task_id=task_id, new_description=new_description, path=test_file
    )

    assert old_task.id == new_task.id
    assert old_task.description != new_task.description
    assert old_task.updated_at < new_task.updated_at

def test_update_should_raise_if_id_not_found(tmp_path):
    with pytest.raises(ValueError, match="Cannot find task with id:"):
        update_task(task_id=999, new_description="Does not exist", path=tmp_path / FILENAME)
