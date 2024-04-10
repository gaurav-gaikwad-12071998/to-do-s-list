from fastapi import APIRouter, Depends
import json
from todos import UserService
from todos.services import user_management

user_router = APIRouter()
user_service = UserService()

# @user_router.get("/")
# async def get_all_users():
#     return {"working": True}

@user_router.get("/")
async def get_all_users():
    return await user_service.get_all_users()

