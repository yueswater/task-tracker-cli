import json
import logging
from pathlib import Path
from typing import List, Optional

from config import FILENAME
from task_cli.models.task import Task

logging.basicConfig(level=logging.DEBUG)


def get_default_path() -> Path:
    return Path.cwd() / FILENAME


def load_tasks(path: Optional[Path] = None) -> List[Task]:
    target = path or get_default_path()
    if not target.exists():
        target.write_text("[]", encoding="utf-8")
        return []

    tasks = []
    try:
        with open(target, "r", encoding="utf-8") as f:
            raw_data = json.load(f)
    except json.JSONDecodeError:
        logging.exception(f"Failed to decode json file: {target}")
        return []

    for task in raw_data:
        tasks.append(Task.from_dict(task))

    return list(tasks)


def save_tasks(tasks: List[Task], path: Optional[Path] = None) -> None:
    path = path or get_default_path()
    data = [task.to_dict() for task in tasks]

    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
