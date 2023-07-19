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

# GET: Sign Up Page
@users_router.get('/sign-up/', tags = ['users'])
def user_sign_up(request: Request):
    """USER SIGN UP

    Args:
        request (Request): Necessary for templateResponse

    Returns:
        sign.up.html: Static Page with add new user form
    """
    return templates.TemplateResponse("sign-up.html", {"request": request})

# GET: Login Page
@users_router.get('/login/', tags = ['users'])
def user_sign_up(request: Request):
    """USER LOGIN

    Args:
        request (Request): Necessary for templateResponse

    Returns:
        _templateResponse_: _Static Page with login form_
    """
    return templates.TemplateResponse("login.html", {"request": request})

# POST: Add New User
@users_router.post('/sign-up/', tags=['users'])
def sign_up(request: Request, user: UserLogin = Depends(UserLogin.user_register_as_form)):
    """USER SIGN UP

    Args:
        request (Request)
        user (UserLogin, optional): This is the user information, Defaults to Depends(UserLogin.user_register_as_form).
 

    Returns:
        _TemplateResponse_: _Returns the home page with a confirmation o problem message_
    """
    users_collection = users_router.mongodb_client["users"]
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        return templates.TemplateResponse("index.html", {"request": request, "message":"Este correo ya tiene una cuenta"})
    user.password = hash_password(user.password)
    users_collection.insert_one(user.dict())
    return templates.TemplateResponse("index.html", {"request": request, "message":"Registro Exitoso"})

    