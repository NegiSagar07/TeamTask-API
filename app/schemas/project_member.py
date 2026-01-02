from pydantic import BaseModel

class AddProjectMember(BaseModel):
    user_id: int