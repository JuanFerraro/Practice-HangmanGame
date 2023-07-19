# Python
import json

# Passlib
from passlib.context import CryptContext

# CryptContext Object
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

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


def read_words():
    """Read JSON Words

    Returns:
        Return a List of dictionaries
    """
    with open('words.json', 'r',encoding='utf-8') as file:
        words = json.load(file) 
    return words