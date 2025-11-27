# Python Todo List Application 🐍✅

A feature-rich, object-oriented Todo List application built with Python that demonstrates core OOP principles while providing a practical task management solution.

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![OOP](https://img.shields.io/badge/Object--Oriented-Design-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features ✨

- ✅ **Object-Oriented Design** - Clean, modular code using OOP principles
- 📝 **Multiple Todo Lists** - Create and manage different todo lists
- 🎯 **Task Management** - Add, remove, complete, and update tasks
- 📊 **Priority Levels** - High, Medium, Low priority tasks
- 📈 **Progress Tracking** - View completion statistics
- 💾 **Data Persistence** - Automatic save/load to JSON file
- 🔍 **Smart Filtering** - Filter by status, priority, or category
- 🎨 **Interactive CLI** - User-friendly command-line interface

## OOP Concepts Demonstrated 🏗️

- **Encapsulation** - Data hiding with proper getters/setters
- **Abstraction** - Simplified interfaces for complex operations
- **Composition** - Building complex objects from simpler ones
- **Modularity** - Separate concerns with dedicated classes

## Project Structure 📁

```
py-todo-list/
├── todo_app.py          # Core OOP implementation
├── run_todo.py          # Interactive CLI runner
├── todo_data.json       # Auto-generated data storage
├── requirements.txt     # Project dependencies
└── README.md           # This file
```

## Class Architecture 🏛️

### `Task` Class
Represents individual tasks with properties and behaviors:
```python
class Task:
    - title: str
    - description: str  
    - priority: str
    - completed: bool
    - created_at: datetime
```

### `TodoList` Class
Manages collections of tasks:
```python
class TodoList:
    - name: str
    - tasks: List[Task]
    - categories: Dict
```

### `TodoManager` Class
Orchestrates multiple todo lists with persistence:
```python
class TodoManager:
    - todo_lists: Dict[str, TodoList]
    - file_operations
```

## Installation & Setup 🚀

### Prerequisites
- Python 3.6 or higher
- Git Bash (for Windows users)

### Quick Start
1. **Clone the repository**
   ```bash
   git clone https://github.com/reezmahanan/py-todo-list.git
   cd py-todo-list
   ```

2. **Run the application**
   ```bash
   # Method 1: Direct execution
   python todo_app.py
   
   # Method 2: Interactive mode (recommended)
   python run_todo.py
   ```

## Usage Examples 💡

### Basic Usage
```python
from todo_app import TodoManager, Task

# Create manager and todo list
manager = TodoManager()
manager.create_todo_list("Personal")

# Add tasks
task = Task("Learn Python OOP", "Complete todo list project", "High")
manager.get_todo_list("Personal").add_task(task)

# Mark as complete
manager.get_todo_list("Personal").mark_task_complete("Learn Python OOP")
```

### Interactive Features
- Create multiple todo lists (Work, Personal, Shopping)
- Add tasks with descriptions and priorities
- Mark tasks complete/incomplete
- Filter tasks by status and priority
- View completion statistics
- Automatic data persistence

## Code Examples 🧪

### Creating a Task
```python
task = Task(
    title="Buy groceries",
    description="Milk, Eggs, Bread",
    priority="High",
    due_date=datetime(2024, 1, 20)
)
```

### Managing Todo Lists
```python
# Create manager
manager = TodoManager()

# Create lists
manager.create_todo_list("Work")
manager.create_todo_list("Personal")

# Add tasks to specific list
work_list = manager.get_todo_list("Work")
work_list.add_task(Task("Prepare presentation", "Quarterly review", "High"))

# Get statistics
stats = work_list.get_statistics()
print(f"Completion: {stats['completion_rate']:.1f}%")
```

## API Reference 📚

### Task Methods
- `mark_complete()` - Mark task as done
- `mark_incomplete()` - Mark task as pending  
- `update_priority(priority)` - Change task priority
- `to_dict()` - Serialize task for storage

### TodoList Methods
- `add_task(task)` - Add new task
- `remove_task(title)` - Remove task by title
- `get_completed_tasks()` - Get all completed tasks
- `get_pending_tasks()` - Get all pending tasks
- `get_tasks_by_priority(priority)` - Filter by priority
- `get_statistics()` - Get completion metrics

### TodoManager Methods
- `create_todo_list(name)` - Create new list
- `get_todo_list(name)` - Retrieve list by name
- `save_to_file()` - Save all data to JSON
- `load_from_file()` - Load data from JSON

## Data Persistence 💾

The application automatically saves your data to `todo_data.json`:
```json
{
  "Personal": [
    {
      "title": "Buy groceries",
      "description": "Milk, Eggs, Bread",
      "priority": "High",
      "completed": true,
      "created_at": "2024-01-15 10:30:00"
    }
  ]
}
```

## Contributing 🤝

We welcome contributions! Please feel free to submit pull requests for:
- New features
- Bug fixes  
- Documentation improvements
- Code optimization

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a pull request

## Future Enhancements 🔮

- [ ] Web interface with Flask/Django
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Email notifications for due tasks
- [ ] Mobile app version
- [ ] Collaborative todo lists
- [ ] Advanced analytics and reporting

## Learning Outcomes 🎓

This project demonstrates:
- Python OOP principles in practice
- File I/O operations with JSON
- Data serialization/deserialization
- Modular code organization
- Error handling and validation
- User interface design patterns

## License 📄

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Connect with Me 📞

- GitHub: [@reezmahanan](https://github.com/reezmahanan)
- Project Link: [https://github.com/reezmahanan/py-todo-list](https://github.com/reezmahanan/py-todo-list)

---

**⭐ Star this repo if you found it helpful!**

*Built with ❤️ using Python and Object-Oriented Programming principles*
