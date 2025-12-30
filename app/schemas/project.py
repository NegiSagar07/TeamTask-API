from pydantic import BaseModel


class ProjectCreate(BaseModel):
    title: str
    description: str


class ProjectResponse(BaseModel):
    id: int
    title: str
    description: str
    owner_id: int

    class config:
        from_attributes = True