from sqlalchemy import Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from app.models.base import Base
from sqlalchemy.sql import func

class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(244), nullable=False)
    description: Mapped[str] = mapped_column(String(700), nullable=True)
    is_completed: Mapped[bool] = mapped_column(Boolean, default=False)

    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    created_at: Mapped[DateTime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[DateTime | None] = mapped_column(DateTime(timezone=True), onupdate=func.now())