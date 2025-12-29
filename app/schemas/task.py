from pydantic import BaseModel
from datetime import datetime


class TaskBase(BaseModel):
    title: str
    description: str


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    is_completed: bool | None = None


class TaskResponse(TaskBase):
    id: int
    is_completed: bool
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True