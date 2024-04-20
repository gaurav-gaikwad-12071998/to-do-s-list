from fastapi import APIRouter
import json

from api.__core__.api_error_response import WrongEmailOrPassword, InternalServerError, BadCredentials
from api.controllers.auth.pydantic import LoginPostObject, SignUpPostObject
from todos import UserService 
from todos import MESSAGES

auth_router = APIRouter()

user_service = UserService()

@auth_router.post("/login", tags=["auth"])
async def login(login_items: LoginPostObject):
    try:
        user_email = login_items.email
        password = login_items.password
        
        return await user_service.login_user(user_email, password)
    except Exception as e:
        if MESSAGES["USER_NOT_FOUND"] in e.args or MESSAGES["WRONG_PASSWORD"] in e.args:
            return WrongEmailOrPassword()
        else:
            return InternalServerError(str(e))
        
@auth_router.post("/signup", tags=["auth"])
async def signup(sign_up_items: SignUpPostObject):
    try:
        user_name = sign_up_items.user_name
        user_email = sign_up_items.user_email
        user_password = sign_up_items.user_password
        confirm_password = sign_up_items.confirm_password
        user_contact = sign_up_items.user_contact
        user_birthdate = sign_up_items.user_birthdate
        role = sign_up_items.role
        
        if(user_password != confirm_password):
            return BadCredentials("Password and confirm password should be same.")
        
        return await user_service.sign_up_user( user_name, user_email, user_password, confirm_password, user_contact, user_birthdate, role)
    except Exception as e:
        if MESSAGES["USER_NOT_FOUND"] in e.args or MESSAGES["WRONG_PASSWORD"] in e.args:
            return WrongEmailOrPassword()
        else:
            return InternalServerError(str(e))
        
        

        
