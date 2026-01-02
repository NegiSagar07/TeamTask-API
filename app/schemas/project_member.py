from pydantic import BaseModel
from app.schemas.user import UserResponse

class AddProjectMember(BaseModel):
    user_id: int


class ProjectMemberOut(BaseModel):
    members: list[UserResponse]

    class Config:
        from_attributes = True 