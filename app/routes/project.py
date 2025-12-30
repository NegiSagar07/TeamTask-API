from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db_session
from app.core.dependencies import get_current_user
from app.schemas.project import ProjectResponse, ProjectCreate
from app.models.user import User
from app.crud.project import create_project, get_my_projects


router = APIRouter(prefix="/project", tags=["Project"])

@router.post("/", response_model=ProjectResponse)
async def create_new_project(project_in: ProjectCreate, db: AsyncSession = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    
    project = await create_project(db=db, project_in=project_in, owner_id=current_user.id)
    return project


@router.get("/", response_model=list[ProjectResponse])
async def read_my_projects(db: AsyncSession = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    
    projects = await get_my_projects(db=db, user_id=current_user.id)
    return projects