# Task Tracker CLI

A simple command-line task tracker for managing your to-do list directly from the terminal.  
This project was built as a learning exercise following the specifications from [roadmap.sh](https://roadmap.sh/projects/task-tracker).



## Features

- Add new tasks
- List tasks by status (`todo`, `in-progress`, `done`)
- Update task descriptions
- Mark tasks as in progress or done
- Delete tasks
- All data is stored in a local `tasks.json` file



## Installation

This project uses [Poetry](https://python-poetry.org/) for dependency management.

```bash
git clone https://github.com/yueswater/task-tracker-cli.git
cd task-tracker-cli
poetry install
````



## Usage

Once installed, you can use the CLI via:

```bash
poetry run task-cli <command> [arguments]
```



### Commands

#### `add`

Add a new task:

```bash
task-cli add "Buy groceries"
```

#### `list`

List all tasks:

```bash
task-cli list
```

List only tasks of a certain status:

```bash
task-cli list todo
task-cli list done
task-cli list in-progress
```

#### `update`

Update the description of a task:

```bash
task-cli update 3 "Buy groceries and cook dinner"
```

#### `mark-done`

Mark a task as done:

```bash
task-cli mark-done 3
```

#### `mark-in-progress`

Mark a task as in progress:

```bash
task-cli mark-in-progress 3
```

#### `delete`

Delete a task:

```bash
task-cli delete 3
```



## Example Output

```bash
$ task-cli list
[1] todo         Buy groceries
[2] in-progress  Write documentation
[3] done         Submit report
```



## Project Structure

```
task-tracker-cli/
├── src/
│   └── task_cli/
│       ├── app.py
│       ├── models/
│       ├── services/
│       └── storage/
├── tests/
├── Makefile
├── pyproject.toml
├── README.md
```



## Testing

Run the full test suite with coverage:

```bash
make test
make coverage
```

All tests are located under the `tests/` directory and use `pytest` with `pytest-cov`.



## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.