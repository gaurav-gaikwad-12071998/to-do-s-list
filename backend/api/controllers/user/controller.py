from fastapi import APIRouter, Depends
import json
from api.__core__.api_error_response import InternalServerError, UserNotFound
from api.controllers.user.pydantic import UserEditPutParams, UserContactEditPutParams, UserEmailEditPutParams
from todos import UserService
from todos import MESSAGES

user_router = APIRouter()
user_service = UserService()

# @user_router.get("/")
# async def get_all_users():
#     return {"working": True}

@user_router.get("/", tags=["users"])
async def get_all_users():
    return await user_service.get_all_users()

@user_router.put("/{user_id}", tags=["users"])
async def edit_user(user_id, user_edit_params: UserEditPutParams):
    try:
        return await user_service.edit_user(user_id, dict(user_edit_params))
    except Exception as e:
        if MESSAGES["USER_NOT_FOUND"] in e.args:
            return UserNotFound()
        else:
            return InternalServerError(str(e))


@user_router.put("/contact/{user_id}", tags=["users"])
async def edit_user_contact(user_id, user_contact_edit_params: UserContactEditPutParams):
    try:
        password = user_contact_edit_params.password
        user_edit_params = {
            "user_contact" : user_contact_edit_params.user_contact
        }
        
        return await user_service.edit_sensitive_data(user_id, password, user_edit_params)
    except Exception as e:
        if MESSAGES["USER_NOT_FOUND"] in e.args:
            return UserNotFound()
        else:
            return InternalServerError(str(e))
        
@user_router.put("/email/{user_id}", tags=["users"])
async def edit_user_email(user_id, user_email_edit_params: UserEmailEditPutParams):
    try:
        password = user_email_edit_params.password
        user_edit_params = {
            "user_email" : user_email_edit_params.user_email
        }
        
        return await user_service.edit_sensitive_data(user_id, password, user_edit_params)
    except Exception as e:
        if MESSAGES["USER_NOT_FOUND"] in e.args:
            return UserNotFound()
        else:
            return InternalServerError(str(e))

@user_router.delete("/{user_id}", tags=["users"])
async def delete_user(user_id):
    try:
        return await user_service.delete_user(user_id)
    except Exception as e:
        if MESSAGES["USER_NOT_FOUND"] in e.args:
            return UserNotFound()
        else:
            return InternalServerError(str(e))

