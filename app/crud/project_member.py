from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.project_member import ProjectMember


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