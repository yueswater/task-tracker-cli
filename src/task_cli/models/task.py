from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict


class TaskStatus(Enum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


def now_utc() -> datetime:
    return datetime.now(timezone.utc)


@dataclass
class Task:
    id: int
    description: str
    status: TaskStatus = TaskStatus.TODO
    created_at: datetime = field(default_factory=now_utc)
    updated_at: datetime = field(default_factory=now_utc)

    def __post_init__(self):
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("id must be a positive integer")
        if not self.description or not self.description.strip():
            raise ValueError("description is required")

    def touch(self):
        self.updated_at = now_utc()

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Task":
        return cls(
            id=data["id"],
            description=data["description"],
            status=TaskStatus(data["status"]),
            created_at=datetime.fromisoformat(data["createdAt"]),
            updated_at=datetime.fromisoformat(data["updatedAt"]),
        )

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "createdAt": self.created_at.isoformat(),
            "updatedAt": self.updated_at.isoformat(),
        }
