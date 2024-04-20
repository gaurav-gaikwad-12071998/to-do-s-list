from fastapi import APIRouter, Depends
import json
from api.__core__.api_error_response import InternalServerError, UserNotFound
from api.controllers.category.pydantic import CategoryDeleteParams, CategoryInsertPostParams
from todos import CategoryService
from todos import MESSAGES

category_router = APIRouter()
category_service = CategoryService()

@category_router.get("/", tags=["category"])
async def get_all_category():
    return await category_service.get_all_categories()


@category_router.get("/user/{user_id}", tags=["category"])
async def get_categories_by_user(user_id:str):
    return await category_service.get_categories_by_user(user_id)

@category_router.post("/", tags=["category"])
async def insert_category_for_user(category_insert_params:CategoryInsertPostParams):
    
    user_id = category_insert_params.user_id
    category_title = category_insert_params.category_title
    
    return await category_service.create_category_for_user(user_id, category_title)

@category_router.delete("/{category_id}", tags=["category"])
async def delete_category_for_user(category_id, category_insert_params:CategoryDeleteParams):
    try:
        user_id = category_insert_params.user_id
        category_title = category_insert_params.category_title
        
        return await category_service.delete_category_for_user(user_id, category_title, category_id)
    except Exception as e:
        if MESSAGES["USER_NOT_FOUND"] in e.args:
            return UserNotFound()
        else:
            return InternalServerError(str(e))
