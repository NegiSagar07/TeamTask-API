from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import UserCreate, UserResponse
from sqlalchemy.ext.asyncio import AsyncSession
from app.db import get_db_session
from app.crud.user import create_user, get_user_by_email


router = APIRouter(prefix="/users", tags=["Users Register"])

@router.post("/", response_model=UserResponse)
async def register_user(user: UserCreate, db: AsyncSession = Depends(get_db_session)):
    
    email = user.email.lower()
    db_user = await get_user_by_email(db, email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="email already registered")
    
    hashed_password = "abcd-vaha-se-nikle-pandaji"

    new_user = await create_user(db, email, hashed_password)

    return new_user