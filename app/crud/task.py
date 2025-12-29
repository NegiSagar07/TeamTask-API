from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.task import TaskCreate
from app.models.task import Task

async def create_task(db: AsyncSession, task_in: TaskCreate, user_id: int) -> Task:
    task = Task(
        title = task_in.title,
        description = task_in.description,
        user_id = user_id,
    )
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_task_by_user(db: AsyncSession, user_id: int):
    query = select(Task).where(Task.user_id == user_id)
    result = await db.execute(query)

    return result.scalars().all()