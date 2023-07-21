"""Users views"""

# FastAPI
from fastapi import APIRouter, status, Request, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.templating import Jinja2Templates

# Schemas
from schemas.user import User, UserLogin, UserRegister
from bson.objectid import ObjectId #bson Mongo

# Utilities
from utils.utils import hash_password, verify_password, create_access_token

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

## GET: Login Page
@users_router.get('/login/', tags = ['users'])
def user_sign_up(request: Request):
    """USER LOGIN PAGE

    Args:
        request (Request): Necessary for templateResponse

    Returns:
        _templateResponse_: _Static Page with login form_
    """
    return templates.TemplateResponse("login.html", {"request": request})

## POST: User Login
@users_router.post('/login/', tags=['users'])
def user_login(request: Request, user: UserLogin = Depends(UserLogin.user_login_as_form)):
    """USER login
    
    Args:
        request (Request): Necessary for templateResponse
        user (User_Login): This is the necessary information for the user login, it contains:
                            - Email 
                            - Password 
                            It depends of user_login_as_form a @classMethod

    Returns:
        _templateResponse_: _Static Page_
    """
    users_collection = users_router.mongodb_client["users"]
    existing_user = users_collection.find_one({"email": user.email})

    if existing_user:
        user_in = User
        user_in.user_name = existing_user.get('user_name')
        user_in.max_score = existing_user.get('max_score')
        user_in.email = existing_user.get('email')
        access_token = create_access_token(data={"sub": user_in.email})
        print('TOKEN ->', access_token)

        if verify_password(user.password, existing_user.get('password')):
            """ return templates.TemplateResponse("index.html", {"request": request, 
                                                             "user": user_in
                                                             }) """
            response = templates.TemplateResponse("index.html", {"request": request, "user": user_in})
            response.set_cookie(key="access_token", value=access_token, httponly=True)
            return response
        else:
            return templates.TemplateResponse("login.html", {"request": request, "message":"Las contraseñas no coinciden"})
    return templates.TemplateResponse("login.html", {"request": request, "message":"No existe usuario con este correo"})


## GET: Sign Up Page
@users_router.get('/sign-up/', tags = ['users'])
def user_sign_up(request: Request):
    """USER SIGN UP

    Args:
        request (Request): Necessary for templateResponse

    Returns:
        sign.up.html: Static Page with add new user form
    """
    return templates.TemplateResponse("sign-up.html", {"request": request})

## POST: Add New User
@users_router.post('/sign-up/', tags=['users'])
def sign_up(request: Request, user: UserRegister = Depends(UserRegister.user_register_as_form)):
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

## POST: Update MaxScore User
@users_router.post('/game/user/', tags=['users'])
def check_user_max_score(request: Request, user: User = Depends(User.user_as_form)):
    users_collection = users_router.mongodb_client["users"]
    existing_user = users_collection.find_one({"email": user.email})
    if user.max_score > existing_user.get('max_score'):
        users_collection.update_one(
            {"email": user.email},
            {"$set": {"max_score": user.max_score}}
        )
        existing_user["max_score"] = user.max_score
    return templates.TemplateResponse("index.html", {"request": request, "user": user})
