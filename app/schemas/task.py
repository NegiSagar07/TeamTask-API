from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TaskBase(BaseModel):
    title: str
    description: str


class TaskCreate(TaskBase):
    priority: Optional[str] = None
    project_id: int
    assigned_to_id: Optional[int] = None


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    status: Optional[str] = None
    priority: Optional[str] = None
    assigned_to_id: Optional[int] = None


class TaskResponse(TaskBase):
    id: int
    status: str
    priority: str
    project_id: int
    created_by_id: int
    assigned_to_id: Optional[int] = None
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        from_attributes = True