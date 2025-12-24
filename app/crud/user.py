from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from app.models.user import User

async def create_user(db: AsyncSession, email: str, hashed_password: str) -> User:
    user = User(email=email, hashed_password=hashed_password, is_active=True)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user_by_email(db: AsyncSession, email: str) -> User|None:
    query = select(User).where(User.email == email.lower())
    result = await db.execute(query)

    return result.scalar_one_or_none()


async def get_user_by_id(db: AsyncSession, id: int) -> User|None:
    query = select(User).where(User.id == id)
    result = await db.execute(query)

    return result.scalar_one_or_none()
