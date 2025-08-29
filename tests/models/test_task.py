from datetime import datetime

import pytest

from task_cli.models.task import Task, TaskStatus


def test_task_creation():
    task = Task(id=1, description="Write tests")
    assert task.id == 1
    assert task.description == "Write tests"
    assert task.status == TaskStatus.TODO
    assert isinstance(task.created_at, datetime)
    assert isinstance(task.updated_at, datetime)


def test_task_invalid_id():
    with pytest.raises(ValueError):
        Task(id=0, description="Invalid ID")


def test_task_empty_description():
    with pytest.raises(ValueError):
        Task(id=1, description="")


def test_task_status_update():
    task = Task(id=2, description="Change status")
    task.status = TaskStatus.DONE
    assert task.status == TaskStatus.DONE


def test_task_serialization_roundtrip():
    task = Task(id=4, description="Roundtrip")
    data = task.to_dict()
    restored = Task.from_dict(data=data)
    assert restored.id == task.id
    assert restored.description == task.description
    assert restored.status == task.status
    assert restored.created_at == task.created_at
    assert restored.updated_at == task.updated_at


def test_task_touch_updates_timestamp():
    task = Task(id=3, description="Touch me")
    old_time = task.updated_at
    task.touch()
    assert task.updated_at > old_time
