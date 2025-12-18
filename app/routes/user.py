from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.db import get_db_session
from app.schemas.user import UserCreate, UserResponse
from app.models.user import User
from app.crud.user import create_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def register_user(
    payload: UserCreate,
    db: AsyncSession = Depends(get_db_session),
):
    result = await db.execute(
        select(User).where(User.email == payload.email)
    )
    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = await create_user(
        db=db,
        email=payload.email,
        hashed_password=payload.password,  # hashing comes next step
    )

    return user
