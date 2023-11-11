# To-Do List Application

## Introduction
This To-Do list application is a command-line tool for managing tasks. Built with SQLAlchemy and SQLite, it provides a simple yet effective way to keep track of your daily tasks. It offers features like adding tasks with deadlines, viewing tasks for today, the current week, all tasks, and missed tasks, as well as deleting tasks.

## Features
- **Add Tasks**: Add new tasks with deadlines.
- **View Tasks**: View tasks for today, the current week, or all tasks.
- **Missed Tasks**: Check tasks that are past their deadline.
- **Delete Tasks**: Remove tasks from the list.

## Installation
To use this application, you need Python installed on your system along with SQLAlchemy and SQLite. You can install SQLAlchemy using pip:

```bash
pip install sqlalchemy
```

##Usage
Run the script from the command line. The application provides a menu with options to manage your tasks:

```bash
python [script_name].py
```
- Select 1 to view today's tasks.
- Select 2 to view this week's tasks.
- Select 3 to view all tasks.
- Select 4 to view missed tasks.
- Select 5 to add a new task.
- Select 6 to delete a task.
- Select 0 to exit the application.
  
## Database
The application uses a SQLite database to store tasks. The database file is automatically created when you first run the application.
