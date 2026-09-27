from pydantic import BaseModel


# Schema for creating a new task
class TaskCreate(BaseModel):
    title: str


# Schema for updating an existing task
class TaskUpdate(BaseModel):
    title: str
    done: bool


# Schema for returning a task
class TaskResponse(BaseModel):
    id: int
    title: str
    done: bool

    class Config:
        from_attributes = True
        