# Python
from datetime import date
from typing import Optional

# FastAPI
from fastapi import Form

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# User Model:
class UserBase(BaseModel):
    email: EmailStr = Field()

class UserLogin(UserBase):
    password: str = Field(min_length=8, max_length=24)

    @classmethod
    def user_login_as_form(
        cls,
        email: str = Form(),
        password: str = Form(),
    ):
        return cls(
            email = email,
            password = password
        )

class User(UserBase):
    user_name: str = Field(min_length=3, max_length=30)
    max_score: int = Field(default=0, ge=0)

class UserRegister(User):
        password: str = Field(min_length=8, max_length=24)

        @classmethod
        def user_register_as_form(
            cls,
            user_name: str = Form(),
            email: str = Form(),
            password: str = Form(),
        ):
            return cls(
                user_name = user_name,
                email = email,
                password = password
            ) 
