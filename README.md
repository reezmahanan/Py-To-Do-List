# Py To-Do List

A small, object-oriented Python to‑do list manager with support for multiple lists, task priorities, completion tracking, and simple JSON persistence.

This repository contains a single-file implementation (Todo.py) that demonstrates the core models and operations you need to build and persist a basic to‑do app.

## Features

- Task model with title, description, priority, due date, created timestamp, and completion state
- TodoList to manage a collection of tasks
- TodoManager to manage multiple named todo lists
- Methods to add/remove/find tasks, mark complete/incomplete, filter by priority, and display tasks
- Save/load all todo lists to/from a JSON file (`todo_data.json`)
- Small example CLI-style demo in `main()` for quick experimentation

## Requirements

- Python 3.7+ (uses datetime formatting; works with any modern Python 3)
- No external dependencies

## Installation

Clone the repository:

```bash
git clone https://github.com/reezmahanan/Py-To-Do-List.git
cd Py-To-Do-List
```

## Usage

Run the example demo (this will create example lists/tasks, display them, and save to `todo_data.json`):

```bash
python Todo.py
```

Programmatic usage (import the classes in your own script):

```python
from Todo import Task, TodoList, TodoManager
from datetime import datetime

manager = TodoManager()
manager.create_todo_list("Personal")
personal = manager.get_todo_list("Personal")

t = Task("Buy groceries", "Milk, eggs, bread", priority="High", due_date=datetime(2025, 12, 01))
personal.add_task(t)
personal.mark_task_complete("Buy groceries")

manager.save_to_file("todo_data.json")
```

To load previously saved data:

```python
manager = TodoManager()
manager.load_from_file("todo_data.json")
manager.list_all_todo_lists()
```

## JSON save format

Saved file (default `todo_data.json`) is a dictionary with list names as keys and arrays of task objects as values. Example:

```json
{
  "Personal": [
    {
      "title": "Buy groceries",
      "description": "Milk, Eggs, Bread",
      "priority": "High",
      "due_date": "2025-12-01",
      "completed": true,
      "created_at": "2025-11-29 10:25:00"
    }
  ],
  "Work": [
    {
      "title": "Prepare presentation",
      "description": "Quarterly review",
      "priority": "High",
      "due_date": null,
      "completed": false,
      "created_at": "2025-11-29 10:26:00"
    }
  ]
}
```

Notes:
- `due_date` is saved as `YYYY-MM-DD` or `null` if not set.
- `created_at` is saved as `YYYY-MM-DD HH:MM:SS`.

## Extension ideas

- Add a small CLI with argparse to create lists and tasks from the command line
- Add edit/update task methods (title/description/due_date)
- Support recurring tasks and reminders
- Add sorting/filtering options (by due date, priority, created date)
- Add unit tests for core behaviors
- Add persistence with SQLite for larger datasets

## Contributing

Contributions, bug reports, and suggestions are welcome. Please open an issue or submit a pull request.

When contributing:
- Add tests for new behavior
- Keep code style consistent and add docstrings where appropriate

## License

This project is provided under the MIT License. See LICENSE for details (or add one if you plan to share publicly).

## Contact

Author: reezmahanan


