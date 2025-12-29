from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.db import get_db_session
from app.core.dependencies import get_current_user
from app.models.user import User
from app.crud.task import create_task, get_task_by_user


router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.post("/", response_model=TaskResponse)
async def create_new_task(task_in: TaskCreate, db: AsyncSession = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    task = await create_task(db=db, task_in=task_in, user_id=current_user.id)
    return task


@router.get("/", response_model=list[TaskResponse])
async def read_my_tasks(db: AsyncSession = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    my_tasks = await get_task_by_user(db=db, user_id=current_user.id)
    return my_tasks