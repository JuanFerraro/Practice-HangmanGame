# FastAPI
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

# Config
from config.database import connect_to_mongodb

# Routers
from routers.games import games_router
from routers.users import users_router

# Initializate App
app = FastAPI()
app.title = 'Hangman Game 🎯'
app.version = '0.1'

""" Conexion BD """
""" @app.on_event("startup")
async def startup():
    app.mongodb_client = connect_to_mongodb() """

# Including Routers
app.include_router(games_router)
app.include_router(users_router)

# Static Files
app.mount("/static", StaticFiles(directory="./public/static"), name="static")
templates = Jinja2Templates(directory="./public/templates")

""" ## Home
@app.get(path='/', status_code=status.HTTP_200_OK)
def home_page():
    return JSONResponse(content={'Hello,':'world!'}) """