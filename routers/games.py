"""Game views"""

# FastAPI
from fastapi import APIRouter, status, Request
from fastapi.templating import Jinja2Templates

# Initialization Router
games_router = APIRouter()

# Templates
templates = Jinja2Templates(directory="./public/templates")

@games_router.get(path='/new-game/', status_code=status.HTTP_200_OK, tags=['game'])
def new_game(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})