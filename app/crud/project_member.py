from sqlalchemy import select
from sqlalchemy.orm import selectinload
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.project_member import ProjectMember
from app.models.user import User


async def add_member_to_project(db: AsyncSession, project_id: int, user_id: int):
    
    member = ProjectMember(project_id=project_id, user_id=user_id)
    db.add(member)
    await db.commit()
    await db.refresh(member)

    return member


async def get_member(db:AsyncSession, project_id: int, user_id: int) -> ProjectMember | None:
    query = select(ProjectMember).where(ProjectMember.project_id == project_id, ProjectMember.user_id == user_id)
    result = await db.execute(query)

    return result.scalar_one_or_none()


async def get_all_members(db: AsyncSession, project_id: int) -> list[User] | None:
    query = select(ProjectMember).where(ProjectMember.project_id == project_id).options(selectinload(ProjectMember.user))
    result = await db.execute(query)

    return result.scalars().all()  