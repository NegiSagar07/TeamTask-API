from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db_session
from app.core.dependencies import get_current_user
from app.crud.project import get_my_project
from app.crud.project_member import add_member_to_project, get_member, get_all_members
from app.models.user import User
from app.schemas.project_member import AddProjectMember, ProjectMemberOut


router = APIRouter(prefix='/project', tags=['Project Member'])

@router.post("/{project_id}/members", status_code=status.HTTP_201_CREATED)
async def add_project_member(project_id: int, member_data: AddProjectMember, db: AsyncSession = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    
    owner = await get_my_project(db=db, user_id=current_user.id, project_id=project_id)
    if not owner:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are not authorized to add member in this project")
    
    db_member = await get_member(db=db, project_id=project_id, user_id=member_data.user_id)
    if db_member:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user already the part of the project")

    new_member = await add_member_to_project(db=db, project_id=project_id, user_id=member_data.user_id)
    return new_member


@router.get("/{project_id}/members",response_model=ProjectMemberOut)
async def read_members_of_project(project_id: int, db: AsyncSession = Depends(get_db_session), current_user: User = Depends(get_current_user)):
    
    owner = await get_my_project(db=db, user_id=current_user.id, project_id=project_id)
    if not owner:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="you are not authorized to read the information of this project")
    
    db_members = await get_all_members(db=db, project_id=project_id)
    users = [member.user for member in db_members]

    return {"members": users}