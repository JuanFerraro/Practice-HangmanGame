"""Game views"""
# Python
import random

# FastAPI
from fastapi import APIRouter, status, Request, Depends
from fastapi.templating import Jinja2Templates

# Schemas
from schemas.user import User

# Utilities
from utils.utils import read_words, update_max_score, get_top_users
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
@games_router.post('/play-again/', tags=['game'])
def user_play_again(request: Request, user: User = Depends(User.user_as_form)):
    """_summary_

    Args:
        request (Request): _description_
        user (User, optional): _description_. Defaults to Depends(User.user_as_form).

    Returns:
        _type_: _description_
    """
    users_collection = games_router.mongodb_client["users"]
    update_max_score(users_collection, user.email, user.max_score)
    words = read_words()
    word = random.choice(words)
    return templates.TemplateResponse("new-game.html", {"request": request, 'word': word, "user": user})

## GET: Ranking
@games_router.get(path="/game/ranking/", tags=['game'])
def ranking(request: Request):
    users_collection = games_router.mongodb_client["users"]
    top_users = get_top_users(users_collection, limit=6)
    print(top_users)
    return templates.TemplateResponse("ranking.html", {"request": request, "top_users": top_users})