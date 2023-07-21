"""Game views"""
# Python
import random

# FastAPI
from fastapi import APIRouter, status, Request, Depends
from fastapi.templating import Jinja2Templates

# Schemas
from schemas.user import User

# Utilities
from utils.utils import read_words
from config.database import connect_to_mongodb

# Initialization Router
games_router = APIRouter()

# Templates
templates = Jinja2Templates(directory="./public/templates")

""" Connect DB """
games_router.mongodb_client = connect_to_mongodb()

## GET
@games_router.get(path='/', status_code=status.HTTP_200_OK, tags=['game'])
def game(request: Request):
    """GAME
    Args:
        request (Request)
    Returns:
        Returns template response with the index page.
    """
    return templates.TemplateResponse("index.html", {"request": request})

## POST
@games_router.post(path='/new-game/', status_code=status.HTTP_200_OK, tags=['game'])
def new_game(request: Request, user: User = Depends(User.user_as_form)):
    words = read_words()
    word = random.choice(words)
    print("word ->",word)
    print("user type ->",type(user))
    print("user ->",user)
    return templates.TemplateResponse("new-game.html", {"request": request, 'word': word, "user": user})

## POST: Update MaxScore User -> new-game.html
@games_router.post('/play-again/', tags=['users'])
def user_play_again(request: Request, user: User = Depends(User.user_as_form)):
    users_collection = games_router.mongodb_client["users"]
    existing_user = users_collection.find_one({"email": user.email})
    print('user.max_score', user.max_score)
    print("existing_user.get('max_score')", existing_user.get('max_score'))
    if user.max_score > existing_user.get('max_score'):
        users_collection.update_one(
            {"email": user.email},
            {"$set": {"max_score": user.max_score}}
        )
        existing_user["max_score"] = user.max_score
    words = read_words()
    word = random.choice(words)
    return templates.TemplateResponse("new-game.html", {"request": request, 'word': word, "user": user})
