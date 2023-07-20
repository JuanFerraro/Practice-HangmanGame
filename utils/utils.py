# Python
import json
from typing import Optional
from datetime import datetime, timedelta

# Passlib
from passlib.context import CryptContext

# FastAPI
from fastapi import Cookie, Depends, HTTPException, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Schema
from schemas.user import User

# JWT
import jwt
from jwt import PyJWTError

## CryptContext Object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

## Password validatios
def hash_password(password: str) -> str:
    """ HASH PASSWORD
        Function to crypt a password
    """
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """ VERIFY PASSWORD
        Function to verify a password
    """
    return pwd_context.verify(plain_password, hashed_password)

## JSON 
def read_words():
    """Read JSON Words

    Returns:
        Return a List of dictionaries
    """
    with open('words.json', 'r',encoding='utf-8') as file:
        words = json.load(file) 
    return words

## JWT Auth

## HTTPBearer instance
bearer_scheme = HTTPBearer()

SECRET_KEY = "my_secret_key_super_secret"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
