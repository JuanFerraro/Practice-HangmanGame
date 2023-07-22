# Python
import json
from typing import Optional, List
from datetime import datetime, timedelta

# Passlib
from passlib.context import CryptContext

# FastAPI
from fastapi import Cookie, Depends, HTTPException, Body
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

# Schema
from schemas.user import User

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


## Services:

def update_max_score(users_collection, email, new_max_score):
    existing_user = users_collection.find_one({"email": email})
    if new_max_score > existing_user.get('max_score'):
        users_collection.update_one(
            {"email": email},
            {"$set": {"max_score": new_max_score}}
        )


def get_top_users(users_collection, limit=6):
    top_users = users_collection.find().sort("max_score", -1).limit(limit)
    return list(top_users)