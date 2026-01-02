from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.project import ProjectCreate
from app.models.project import Project


async def create_project(db: AsyncSession, project_in: ProjectCreate, owner_id: int) -> Project:
    project = Project(
        title = project_in.title,
        description = project_in.description,
        owner_id = owner_id,
    )
    db.add(project)
    await db.commit()
    await db.refresh(project)
    return project


async def get_my_projects(db: AsyncSession, user_id: int) -> list[Project] | None:
    query = select(Project).where(Project.owner_id == user_id)
    result = await db.execute(query)
    
    return result.scalars().all()


async def get_my_project(db: AsyncSession, user_id: int, project_id: int) -> Project | None:
    query = select(Project).where(Project.owner_id == user_id, Project.id == project_id)
    result = await db.execute(query)
    
    return result.scalar_one_or_none()