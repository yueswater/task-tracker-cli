from pathlib import Path
from typing import Optional

from task_cli.models.task import Task, TaskStatus
from task_cli.services.list_tasks import list_tasks
from task_cli.storage.json_store import save_tasks

__all__ = ["mark_status"]


def mark_status(task_id: int, status: TaskStatus, path: Optional[Path] = None) -> Task:
    tasks = list_tasks(path=path)
    task = next((t for t in tasks if t.id == task_id), None)

    if task is None:
        raise ValueError(f"Cannot find task with id: {task_id}")

    task.touch()
    task.status = status
    save_tasks(tasks=tasks, path=path)

    return task
