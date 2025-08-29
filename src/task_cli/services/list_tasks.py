from pathlib import Path
from typing import List, Optional

from task_cli.models.task import Task, TaskStatus
from task_cli.storage.json_store import load_tasks

__all__ = ["list_tasks"]


def list_tasks(
    status: Optional[TaskStatus] = None, path: Optional[Path] = None
) -> List[Task]:
    tasks = load_tasks(path=path)
    if status:
        tasks = [t for t in tasks if t.status == status]
    return tasks
