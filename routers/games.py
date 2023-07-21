"""Game views"""
# Python
import random

# FastAPI
from fastapi import APIRouter, status, Request, Body, Depends
from fastapi.templating import Jinja2Templates

# Schemas
from schemas.user import User

# Utilities
from utils.utils import read_words

# Initialization Router
games_router = APIRouter()

# Templates
templates = Jinja2Templates(directory="./public/templates")


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
