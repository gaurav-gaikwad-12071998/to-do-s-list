from typing import Optional
from pydantic import BaseModel

class UserEditPutParams(BaseModel):
    user_name: Optional[str] = None
    user_birthdate: Optional[str] = None
    
class UserContactEditPutParams(BaseModel):
    user_contact: str = None
    password: str = None
    
class UserEmailEditPutParams(BaseModel):
    user_email: str = None
    password: str = None


    