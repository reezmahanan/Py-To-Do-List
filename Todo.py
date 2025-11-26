import json
from datetime import datetime


class Task:
    """Represents a single task in the todo list"""
    
    def __init__(self, title, description="", priority="Medium", due_date=None):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now()
    
    def mark_complete(self):
        """Mark the task as completed"""
        self.completed = True
    
    def mark_incomplete(self):
        """Mark the task as incomplete"""
        self.completed = False
    
    def update_priority(self, new_priority):
        """Update the priority of the task"""
        valid_priorities = ["Low", "Medium", "High"]
        if new_priority in valid_priorities:
            self.priority = new_priority
            return True
        return False
    
    def __str__(self):
        """String representation of the task"""
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.title} (Priority: {self.priority})"
    
    def to_dict(self):
        """Convert task to dictionary for serialization"""
        return {
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'due_date': self.due_date.strftime('%Y-%m-%d') if self.due_date else None,
            'completed': self.completed,
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S')
        }


class TodoList:
    """Manages a collection of tasks"""
    
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.categories = {}
    
    def add_task(self, task):
        """Add a new task to the todo list"""
        if isinstance(task, Task):
            self.tasks.append(task)
            return True
        return False
    
    def remove_task(self, task_title):
        """Remove a task by title"""
        for task in self.tasks:
            if task.title.lower() == task_title.lower():
                self.tasks.remove(task)
                return True
        return False
    
    def find_task(self, title):
        """Find a task by title"""
        for task in self.tasks:
            if task.title.lower() == title.lower():
                return task
        return None
    
    def get_completed_tasks(self):
        """Get all completed tasks"""
        return [task for task in self.tasks if task.completed]
    
    def get_pending_tasks(self):
        """Get all pending tasks"""
        return [task for task in self.tasks if not task.completed]
    
    def get_tasks_by_priority(self, priority):
        """Get tasks filtered by priority"""
        return [task for task in self.tasks if task.priority == priority]
    
    def mark_task_complete(self, task_title):
        """Mark a specific task as complete"""
        task = self.find_task(task_title)
        if task:
            task.mark_complete()
            return True
        return False
    
    def mark_task_incomplete(self, task_title):
        """Mark a specific task as incomplete"""
        task = self.find_task(task_title)
        if task:
            task.mark_incomplete()
            return True
        return False
    
    def display_tasks(self, task_list=None):
        """Display all tasks or a specific list of tasks"""
        tasks_to_display = task_list if task_list else self.tasks
        
        if not tasks_to_display:
            print("No tasks found!")
            return
        
        print(f"\n{'='*50}")
        print(f"TODO LIST: {self.name}")
        print(f"{'='*50}")
        
        for i, task in enumerate(tasks_to_display, 1):
            print(f"{i}. {task}")
    
    def get_statistics(self):
        """Get statistics about the todo list"""
        total_tasks = len(self.tasks)
        completed_tasks = len(self.get_completed_tasks())
        pending_tasks = len(self.get_pending_tasks())
        
        return {
            'total': total_tasks,
            'completed': completed_tasks,
            'pending': pending_tasks,
            'completion_rate': (completed_tasks / total_tasks * 100) if total_tasks > 0 else 0
        }


class TodoManager:
    """Manages multiple todo lists"""
    
    def __init__(self):
        self.todo_lists = {}
    
    def create_todo_list(self, name):
        """Create a new todo list"""
        if name not in self.todo_lists:
            self.todo_lists[name] = TodoList(name)
            return True
        return False
    
    def get_todo_list(self, name):
        """Get a todo list by name"""
        return self.todo_lists.get(name)
    
    def delete_todo_list(self, name):
        """Delete a todo list"""
        if name in self.todo_lists:
            del self.todo_lists[name]
            return True
        return False
    
    def list_all_todo_lists(self):
        """Display all todo lists"""
        if not self.todo_lists:
            print("No todo lists found!")
            return
        
        print("\nAll Todo Lists:")
        print("-" * 20)
        for name, todo_list in self.todo_lists.items():
            stats = todo_list.get_statistics()
            print(f"{name}: {stats['completed']}/{stats['total']} tasks completed")
    
    def save_to_file(self, filename="todo_data.json"):
        """Save all todo lists to a file"""
        try:
            data = {}
            for list_name, todo_list in self.todo_lists.items():
                data[list_name] = [task.to_dict() for task in todo_list.tasks]
            
            with open(filename, 'w') as f:
                json.dump(data, f, indent=2)
            print(f"Data saved to {filename}")
        except Exception as e:
            print(f"Error saving data: {e}")
    
    def load_from_file(self, filename="todo_data.json"):
        """Load todo lists from a file"""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
            
            for list_name, tasks_data in data.items():
                self.create_todo_list(list_name)
                todo_list = self.get_todo_list(list_name)
                
                for task_data in tasks_data:
                    task = Task(
                        title=task_data['title'],
                        description=task_data.get('description', ''),
                        priority=task_data.get('priority', 'Medium'),
                        due_date=datetime.strptime(task_data['due_date'], '%Y-%m-%d') if task_data.get('due_date') else None
                    )
                    if task_data.get('completed'):
                        task.mark_complete()
                    todo_list.add_task(task)
            
            print(f"Data loaded from {filename}")
        except FileNotFoundError:
            print("No saved data found.")
        except Exception as e:
            print(f"Error loading data: {e}")


# Example usage and demonstration
def main():
    # Create todo manager
    manager = TodoManager()
    
    # Create a personal todo list
    manager.create_todo_list("Personal")
    personal_list = manager.get_todo_list("Personal")
    
    # Add some tasks
    task1 = Task("Buy groceries", "Milk, Eggs, Bread", "High")
    task2 = Task("Finish Python project", "Complete the OOP todo list", "High")
    task3 = Task("Read book", "Read 50 pages", "Low")
    
    personal_list.add_task(task1)
    personal_list.add_task(task2)
    personal_list.add_task(task3)
    
    # Mark one task as complete
    personal_list.mark_task_complete("Buy groceries")
    
    # Display all tasks
    personal_list.display_tasks()
    
    # Display statistics
    stats = personal_list.get_statistics()
    print(f"\nStatistics: {stats['completed']}/{stats['total']} completed ({stats['completion_rate']:.1f}%)")
    
    # Create a work todo list
    manager.create_todo_list("Work")
    work_list = manager.get_todo_list("Work")
    
    work_task1 = Task("Prepare presentation", "Quarterly review", "High")
    work_task2 = Task("Team meeting", "Weekly sync", "Medium")
    
    work_list.add_task(work_task1)
    work_list.add_task(work_task2)
    
    # Display all todo lists
    manager.list_all_todo_lists()
    
    # Save data to file
    manager.save_to_file()
    
    # Demonstrate loading (comment out the above code and uncomment below to test loading)
    # new_manager = TodoManager()
    # new_manager.load_from_file()
    # new_manager.list_all_todo_lists()


if __name__ == "__main__":
    main()