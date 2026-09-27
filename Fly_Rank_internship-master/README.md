# FlyRank Backend Internship - Week 3 Assignment A2

## Project Overview
This project implements a Task Management REST API using FastAPI and SQLite. It replaces the in-memory task list with a persistent SQLite database while keeping the API endpoints unchanged.

## Tech Stack
- Python
- FastAPI
- SQLite
- SQLAlchemy
- Uvicorn

## Features
- Create Task
- Read All Tasks
- Read Task by ID
- Update Task
- Delete Task
- Automatic database creation
- Automatic seeding of 3 sample tasks

## Setup

### Create Virtual Environment
```bash
python -m venv venv
```

### Activate

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

## Database

SQLite database:

```
tasks.db
```

The application automatically:
- Creates the database
- Creates the tasks table
- Seeds 3 sample tasks if the table is empty

## Example SQL Query

```sql
SELECT COUNT(*) FROM tasks;
```

Result:

```
4
```

Explanation:

This query counts the total number of task records stored in the SQLite database.

## Author

Kishore R
