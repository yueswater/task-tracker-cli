from pathlib import Path
from typing import List, Optional

from task_cli.models.task import Task, TaskStatus
from task_cli.services.list_tasks import list_tasks
from task_cli.storage.json_store import save_tasks

__all__ = ["add_task"]


def add_task(description: str, path: Optional[Path] = None) -> Task:
    tasks: List[Task] = list_tasks(path=path)
    id = 1 if not tasks else max(t.id for t in tasks) + 1
    task = Task(id=id, description=description, status=TaskStatus.TODO)

    tasks.append(task)
    save_tasks(tasks=tasks, path=path)
    return task
