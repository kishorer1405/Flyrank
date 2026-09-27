from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine
from app import models
from app.schemas import TaskCreate, TaskUpdate
from fastapi import Response

app = FastAPI(
    title="Task API",
    version="3.0"
)

# Create tables automatically
models.Base.metadata.create_all(bind=engine)


# Database Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Seed 3 tasks only if table is empty
def seed_tasks():
    db = SessionLocal()

    if db.query(models.Task).count() == 0:

        db.add_all([
            models.Task(title="Learn FastAPI", done=False),
            models.Task(title="Learn SQLite", done=False),
            models.Task(title="Complete FlyRank Assignment", done=False),
        ])

        db.commit()

    db.close()


seed_tasks()


# Home
@app.get("/")
def home():
    return {
        "message": "Task CRUD API using SQLite"
    }


# GET ALL TASKS
@app.get("/tasks")
def get_tasks(db: Session = Depends(get_db)):
    return db.query(models.Task).all()


# GET SINGLE TASK
@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task


# CREATE TASK
@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title is required"
        )

    new_task = models.Task(
        title=task.title,
        done=False
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task


# UPDATE TASK
@app.put("/tasks/{task_id}")
def update_task(
    task_id: int,
    task_update: TaskUpdate,
    db: Session = Depends(get_db)
):

    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    task.title = task_update.title
    task.done = task_update.done

    db.commit()
    db.refresh(task)

    return task


# DELETE TASK

@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(models.Task).filter(
        models.Task.id == task_id
    ).first()

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    db.delete(task)
    db.commit()

    return Response(status_code=status.HTTP_204_NO_CONTENT)