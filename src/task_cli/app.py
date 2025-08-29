import argparse

import task_cli.services as services
from task_cli.models.task import TaskStatus

status_map = {
    "todo": TaskStatus.TODO,
    "done": TaskStatus.DONE,
    "in-progress": TaskStatus.IN_PROGRESS,
}


def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add new task
    add_parser = subparsers.add_parser(name="add", help="Add a new task")
    add_parser.add_argument("description", type=str, help="Task description")

    # List tasks by status (default=all)
    list_parser = subparsers.add_parser(name="list", help="List tasks")
    list_parser.add_argument(
        "status",
        nargs="?",
        choices=["todo", "done", "in-progress"],
        help="Filter by status (optional)",
    )

    # Update task by task_id
    update_parser = subparsers.add_parser(name="update", help="Update task description")
    update_parser.add_argument("id", type=int, help="ID of the task to update")
    update_parser.add_argument("description", type=str, help="New description")

    # Delete task by task_id
    delete_parser = subparsers.add_parser(name="delete", help="Delete task")
    delete_parser.add_argument("id", type=int, help="ID of the task to delete")

    # Mark task in-progress
    mark_done_parser = subparsers.add_parser(
        name="mark-in-progress", help="Mark task in-progress"
    )
    mark_done_parser.add_argument(
        "id", type=int, help="ID of the task to be marked in-progress"
    )

    # Mark task done
    mark_done_parser = subparsers.add_parser(name="mark-done", help="Mark task done")
    mark_done_parser.add_argument(
        "id", type=int, help="ID of the task to be marked done"
    )

    # Parse all arguments
    args = parser.parse_args()

    if args.command == "add":
        task = services.add_task(description=args.description)
        print(f"Task added successfully (ID: {task.id})")
    elif args.command == "list":
        status = status_map.get(args.status) if args.status else None
        tasks = services.list_tasks(status=status)
        for t in tasks:
            print(f"[{t.id}] {t.status.value:<12} {t.description}")
    elif args.command == "update":
        task = services.update_task(task_id=args.id, new_description=args.description)
        print(f"Task {task.id} updated.")
    elif args.command == "delete":
        task = services.delete_task(task_id=args.id)
    elif args.command == "mark-done":
        task = services.mark_status(task_id=args.id, status=TaskStatus.DONE)
    elif args.command == "mark-in-progress":
        task = services.mark_status(task_id=args.id, status=TaskStatus.IN_PROGRESS)
