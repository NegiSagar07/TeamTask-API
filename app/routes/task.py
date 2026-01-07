from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.task import TaskCreate, TaskResponse, TaskUpdate
from app.db import get_db_session
from app.core.dependencies import get_current_user
from app.models.user import User
from app.crud.task import create_task, get_tasks_by_project
from app.crud.project_member import get_member
from app.crud.project import get_my_project


router = APIRouter(prefix="/tasks", tags=["Task Section"])

@router.post("/", response_model=TaskResponse)
async def create_new_task(task_in: TaskCreate, db: AsyncSession = Depends(get_db_session), current_user: User = Depends(get_current_user)):

    project_owner = await get_my_project(db=db, user_id=current_user.id, project_id=task_in.project_id)
    if not project_owner:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="You are not authorized to create the task only owner has permission to create task")

    db_member = await get_member(db=db, project_id=task_in.project_id, user_id=task_in.assigned_to_id)
    if not db_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The member is not part of the group, first add member to the project")

    task = await create_task(db=db, task_in=task_in, user_id=current_user.id)
    return task


@router.get("/", response_model=list[TaskResponse])
async def read_all_task_of_project(project_id: int, db: AsyncSession = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    
    project_owner = await get_my_project(db=db, user_id=current_user.id, project_id=project_id)
    if not project_owner:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are not authorized to read about this project")

    my_tasks = await get_tasks_by_project(db=db, project_id=project_id)
    if not my_tasks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="you do not have any tasks yet!")
    
    return my_tasks