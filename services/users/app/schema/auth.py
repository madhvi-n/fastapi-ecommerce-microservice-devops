from pydantic import BaseModel
from typing import Optional
from uuid import UUID
from app.models.user import UserRole
from pydantic import EmailStr


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginRequest(BaseModel):
    email: EmailStr
    password: str


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    role: Optional[UserRole] = UserRole.CUSTOMER  # optional for signup



class UserUpdate(BaseModel):
    first_name: str
    last_name: str


class UserResponse(BaseModel):
    id: int
    uuid: UUID
    first_name: str | None = None
    last_name: str | None = None
    email: EmailStr
    avatar_url: str | None = None
    role: UserRole
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True 


class PasswordUpdate(BaseModel):
    password: str
