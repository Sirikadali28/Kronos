from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    """
    Base schema for users.
    """

    full_name: str
    email: EmailStr


class UserCreate(UserBase):
    """
    Schema used when creating a new user.
    """

    password: str


class UserLogin(BaseModel):
    """
    Schema used for login.
    """

    email: EmailStr
    password: str


class UserResponse(UserBase):
    """
    Schema returned by the API.
    """

    model_config = ConfigDict(from_attributes=True)

    id: str
    role: str
    is_active: bool
    created_at: datetime


class Token(BaseModel):
    """
    JWT token response.
    """

    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    """
    Data stored inside JWT.
    """

    email: str | None = None
