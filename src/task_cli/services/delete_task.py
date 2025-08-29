from pathlib import Path
from typing import Optional

from task_cli.models.task import Task
from task_cli.services.list_tasks import list_tasks
from task_cli.storage.json_store import save_tasks

__all__ = ["delete_task"]


def delete_task(task_id: int, path: Optional[Path] = None) -> Task:
    tasks = list_tasks(path=path)
    task = next((t for t in tasks if t.id == task_id), None)

    if task is None:
        raise ValueError(f"Cannot find task with id: {task_id}")

    tasks.remove(task)
    save_tasks(tasks=tasks, path=path)
    return task
