# To-Do List Application using Tkinter

## Overview

This is a simple To-Do List application implemented in Python using the Tkinter library. The application provides a graphical user interface (GUI) for managing a list of tasks. Users can add tasks, mark them as completed, and delete tasks using the provided buttons.

## Features

- **Add Task:** Enter a task in the provided entry field and click the "Add Task" button to add it to the list.
- **Mark as Completed:** Double-click on a task in the list or click the "Mark as Completed" button to mark it as completed.
- **Delete Task:** Select a task and click the "Delete Task" button to remove it from the list.

## Usage

1. Ensure you have Python installed on your system.
2. Copy the provided code into a Python file (e.g., `todo_app.py`).
3. Run the script using the command: `python todo_app.py`.
4. The To-Do List application window will appear.

## Application Structure

The application is structured as a class named `TodoApp`, which is initialized with a Tkinter root window. The key components of the application include:

- **Task Entry:** A Tkinter Entry widget for entering new tasks.
- **Add Task Button:** A button to add tasks to the list.
- **Task Listbox:** A Tkinter Listbox widget to display the list of tasks.
- **Mark as Completed Button:** A button to mark selected tasks as completed.
- **Delete Task Button:** A button to delete selected tasks from the list.

The `add_task`, `mark_task`, and `delete_task` methods handle the logic for adding, marking, and deleting tasks, respectively.

## How to Run

```bash
python todo_app.py
```

## Dependencies

- Python 3
- Tkinter library

## License

This To-Do List Application is open-source and available under the [MIT License](LICENSE).

Feel free to customize and enhance the application according to your preferences and needs. If you encounter any issues or have suggestions for improvements, please create an issue or submit a pull request.
