"""Users views"""

# FastAPI
from fastapi import APIRouter, status, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

# Schemas
from schemas.user import UserBase, UserLogin

# Utilities
from utils.utils import read_words, hash_password, verify_password

# Config
from config.database import connect_to_mongodb

# Initialization Router
users_router = APIRouter()

# Templates
templates = Jinja2Templates(directory="./public/templates")

""" Conexion BD """
@users_router.on_event("startup")
async def startup():
    users_router.mongodb_client = connect_to_mongodb()

# GET: 
@users_router.get('/sign-up/', tags = ['users'])
def user_sign_up(request: Request):
    """USER SIGN UP

    Args:
        request (Request): Necessary for templateResponse

    Returns:
        sign.up.html: Static Page with add new user form
    """
    return templates.TemplateResponse("sign-up.html", {"request": request})

# POST: Add New User
@users_router.post('/sign-up/', tags=['users'])
def sign_up(request: Request, user: UserLogin = Depends(UserLogin.user_register_as_form)):
    users_collection = users_router.mongodb_client["users"]
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="El usuario ya está registrado")
    user.password = hash_password(user.password)
    users_collection.insert_one(user.dict())
    return JSONResponse(status_code=200, content="Usuario registrado exitosamente")

    