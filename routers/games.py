"""Game views"""
# Python
import random

# FastAPI
from fastapi import APIRouter, status, Request
from fastapi.templating import Jinja2Templates

# Utilities
from utils.utils import read_words

# Initialization Router
games_router = APIRouter()

# Templates
templates = Jinja2Templates(directory="./public/templates")

@games_router.get(path='/game/', status_code=status.HTTP_200_OK, tags=['game'])
def game(request: Request):
    """GAME
    Args:
        request (Request)
    Returns:
        Returns template response with the index page.
    """
    return templates.TemplateResponse("index.html", {"request": request})

@games_router.get(path='/new-game/', status_code=status.HTTP_200_OK, tags=['game'])
def new_game(request: Request):
    words = read_words()
    word = random.choice(words)
    print(word)
    return templates.TemplateResponse("new-game.html", {"request": request, 'word': word})
