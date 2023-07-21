# Python
import os

# Uvicorn
import uvicorn

# FastAPI
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Routers
from routers.games import games_router
from routers.users import users_router

# Initializate App
app = FastAPI()
app.title = 'Hangman Game 🎯'
app.version = '0.1'

# Including Routers
app.include_router(games_router)
app.include_router(users_router)

# Static Files
app.mount("/static", StaticFiles(directory="./public/static"), name="static")
templates = Jinja2Templates(directory="./public/templates")

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
                port=int(os.environ.get("PORT", 8000)))