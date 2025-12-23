from pydantic import EmailStr, BaseModel

class LoginRequest(BaseModel):
    email: EmailStr
    password: str