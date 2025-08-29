from pathlib import Path

from config import FILENAME
from task_cli.models.task import Task, TaskStatus
from task_cli.services.mark_status import mark_status
from task_cli.storage.json_store import save_tasks


def test_mark_done(tmp_path: Path):
    test_file = tmp_path / FILENAME
    task_id = 1
    status = TaskStatus.DONE
    description = "Mark task done"

    save_tasks([Task(id=task_id, description=description)], path=test_file)

    marked_task = mark_status(task_id=task_id, status=status, path=test_file)

    assert marked_task.status == TaskStatus.DONE


def test_mark_in_progress(tmp_path: Path):
    test_file = tmp_path / FILENAME
    task_id = 1
    status = TaskStatus.IN_PROGRESS
    description = "Mark task in progress"

    save_tasks([Task(id=task_id, description=description)], path=test_file)

    marked_task = mark_status(task_id=task_id, status=status, path=test_file)

    assert marked_task.status == TaskStatus.IN_PROGRESS


def test_mark_timestamp(tmp_path: Path):
    test_file = tmp_path / FILENAME
    task_id = 1
    status = TaskStatus.DONE
    description = "Task"
    task = Task(id=task_id, description=description)

    save_tasks([task], path=test_file)

    marked_task = mark_status(task_id=task_id, status=status, path=test_file)

    assert task.updated_at < marked_task.updated_at
