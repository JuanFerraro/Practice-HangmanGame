# Python
from datetime import date
from typing import Optional

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# User Model:
class UserBase(BaseModel):
    user_name: str = Field(min_length=3, max_length=30)
    email: EmailStr = Field()

class UserLogin(UserBase):
    password: str = Field(min_length=8, max_length=24)

class User(UserBase):
    first_name: str = Field(min_length=1, max_length=30)
    last_name: str = Field(min_length=1, max_length=30)
    birth_date: Optional[date] = Field(None)

class UserRegister(User):
    password: str = Field(min_length=8, max_length=24)