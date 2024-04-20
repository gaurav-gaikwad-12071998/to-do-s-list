import datetime
from pydantic import BaseModel


class LoginPostObject(BaseModel):
    email: str = "abc@gmail.com"
    password: str = "password"
    
class SignUpPostObject(BaseModel):
    user_name: str = "Naruto Uzumaki"
    user_email: str = "naruto7@gmailcom" 
    user_password: str = "Hinata@123"
    confirm_password: str = "Hinata@123"
    user_contact: str = "1234567890"
    user_birthdate: str = datetime.date(year=2024, month=4, day=10)
    role: str = "editor"