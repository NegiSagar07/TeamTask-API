from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.auth import LoginRequest
from app.db import get_db_session
from app.crud.user import get_user_by_email
from app.core.security import verify_password


router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/login")
async def login(payload: LoginRequest, db: AsyncSession = Depends(get_db_session)):

    email = payload.email.lower()

    db_user = await get_user_by_email(db, email)

    if not db_user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="invalid credentials")
    
    if not verify_password(payload.password, db_user.hashed_password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="wrong password")
    
    return {"message": "login successful"}