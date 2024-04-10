from fastapi import APIRouter
import json

from api.__core__.api_error_response import WrongEmailOrPassword, InternalServerError
from api.controllers.auth.pydantic import loginPostObject
from todos import UserService 

auth_router = APIRouter()


user_service = UserService()

@auth_router.post("/login")
async def login(login_items: loginPostObject):
    try:
        user_email = login_items.email
        password = login_items.password
        
        return await user_service.login_user(user_email, password)
    except Exception as e:
        if "User not found." in e.args or "Wrong password." in e.args:
            return WrongEmailOrPassword()
        else:
            return InternalServerError(str(e))