from typing import Optional
from pydantic import BaseModel

class CategoryInsertPostParams(BaseModel):
    user_id: str = "123"
    category_title: str = "My Category"
    
    
class CategoryDeleteParams(BaseModel):
    user_id: str = "123"
    category_title: str = "My Category"
