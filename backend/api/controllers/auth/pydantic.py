
from pydantic import BaseModel


class loginPostObject(BaseModel):
    email: str = "abc@gmail.com"
    password: str = "password"