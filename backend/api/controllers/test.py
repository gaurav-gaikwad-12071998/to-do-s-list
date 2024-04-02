from fastapi import APIRouter
import json

router = APIRouter()


@router.get("/")
async def hello():
    return {"working" : True}